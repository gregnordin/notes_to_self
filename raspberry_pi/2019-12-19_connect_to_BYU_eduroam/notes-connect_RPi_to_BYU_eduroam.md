# 12/19/19

## Problem

To ssh into a Raspberry Pi (RPi) connected to a BYU wifi network, we used to use the BYU-Secure wifi network. Use of BYU-Guest (which is now BYU-Wifi) does not permit ssh'ing from a computer to an RPi because port 22 is closed. As of now, BYU-Secure is being shutdown across campus in favor of using eduroam. The problem is connecting an RPi to eduroam because Raspian does not support eduroam out of the box. 

## Solution

### Starting point

- Raspberry Pi 4B with 4GB RAM
- Fresh install of Raspbian Buster with desktop, Version: September 2019, Release date: 2019-09-26 on 16 GB microSD card

### References

[BYU Connecting to Eduroam for Linux (Ubuntu)](https://it.byu.edu/it?id=kb_article&sys_id=b952edc9db527bc0eb8d2f625b96192f)  
[Connecting Raspberry Pi to Eduroam Wifi](https://yasoob.me/posts/raspberry-pi-eduroam-wifi/)    
[How can you connect “eduroam” Wi-Fi with Raspberry Pi ?](https://medium.com/@celikemirhan/how-can-you-connect-eduroam-wi-fi-with-raspberry-pi-8f704e6fa7f6)  
[Pi 4 Raspbian Buster PEAP connection failed](https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=244731&p=1565601&hilit=eduroam#p1565601)  
[Fix wireless driver problem with nl80211](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=253567&p=1572347&hilit=eduroam#p1572347)  

### Steps

#### Edit `/etc/wpa_supplicant/wpa_supplicant.conf`

	$ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

Add the following:

    network={
        ssid="eduroam"
        scan_ssid=1
        key_mgmt=WPA-EAP
        eap=PEAP
        identity="<BYU netid>@byu.edu"
        password="xxxxxxxxxxx"
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
    }
    
Note: I originally also had the following line in my network definition:

		ca_cert="/etc/ssl/certs/ca-certificates.crt"

as per [BYU Connecting to Eduroam for Linux (Ubuntu)](https://it.byu.edu/it?id=kb_article&sys_id=b952edc9db527bc0eb8d2f625b96192f). After rebooting, it looks like this line was deleted from `wpa_supplicant.conf`.

#### Edit `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant`

	$ sudo nano /lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant

Follow [Fix wireless driver problem with nl80211](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=253567&p=1572347&hilit=eduroam#p1572347). Line 58 is originally:

	wpa_supplicant_driver="${wpa_supplicant_driver:-nl80211,wext}"

Change it to

	wpa_supplicant_driver="${wpa_supplicant_driver:-wext}"

#### Reboot

Now everything should work.


### Final version of `/etc/wpa_supplicant/wpa_supplicant.conf`

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US

    network={
        ssid="eduroam"
        scan_ssid=1
        key_mgmt=WPA-EAP
        eap=PEAP
        identity="<BYU netid>@byu.edu"
        password="xxxxxxxxxxx"
        phase1="peaplabel=0"
        phase2="auth=MSCHAPV2"
    }

### Final version of `/lib/dhcpcd/dhcpcd-hooks/10-wpa_supplicant`

    # Start, reconfigure and stop wpa_supplicant per wireless interface.
    # This is needed because wpa_supplicant lacks hotplugging of any kind
    # and the user should not be expected to have to wire it into their system
    # if the base system doesn't do this itself.

    if [ -z "$wpa_supplicant_conf" ]; then
        for x in \
            /etc/wpa_supplicant/wpa_supplicant-"$interface".conf \
            /etc/wpa_supplicant/wpa_supplicant.conf \
            /etc/wpa_supplicant-"$interface".conf \
            /etc/wpa_supplicant.conf \
        ; do
            if [ -s "$x" ]; then
                wpa_supplicant_conf="$x"
                break
            fi
        done
    fi
    : ${wpa_supplicant_conf:=/etc/wpa_supplicant.conf}

    wpa_supplicant_ctrldir()
    {
        dir=$(key_get_value "[[:space:]]*ctrl_interface=" \
            "$wpa_supplicant_conf")
        dir=$(trim "$dir")
        case "$dir" in
        DIR=*)
            dir=${dir##DIR=}
            dir=${dir%%[[:space:]]GROUP=*}
            dir=$(trim "$dir")
            ;;
        esac
        printf %s "$dir"
    }

    wpa_supplicant_start()
    {
        # If the carrier is up, don't bother checking anything
        [ "$ifcarrier" = "up" ] && return 0

        # Pre flight checks
        if [ ! -s "$wpa_supplicant_conf" ]; then
            syslog warn \
                "$wpa_supplicant_conf does not exist"
            syslog warn "not interacting with wpa_supplicant(8)"
            return 1
        fi
        dir=$(wpa_supplicant_ctrldir)
        if [ -z "$dir" ]; then
            syslog warn \
                "ctrl_interface not defined in $wpa_supplicant_conf"
            syslog warn "not interacting with wpa_supplicant(8)"
            return 1
        fi

        wpa_cli -p "$dir" -i "$interface" status >/dev/null 2>&1 && return 0
        syslog info "starting wpa_supplicant"
        wpa_supplicant_driver="${wpa_supplicant_driver:-wext}"
        driver=${wpa_supplicant_driver:+-D}$wpa_supplicant_driver
        err=$(wpa_supplicant -B -c"$wpa_supplicant_conf" -i"$interface" \
            "$driver" 2>&1)
        errn=$?
        if [ $errn != 0 ]; then
            syslog err "failed to start wpa_supplicant"
            syslog err "$err"
        fi
        return $errn
    }

    wpa_supplicant_reconfigure()
    {
        dir=$(wpa_supplicant_ctrldir)
        [ -z "$dir" ] && return 1
        if ! wpa_cli -p "$dir" -i "$interface" status >/dev/null 2>&1; then
            wpa_supplicant_start
            return $?
        fi
        syslog info "reconfiguring wpa_supplicant"
        err=$(wpa_cli -p "$dir" -i "$interface" reconfigure 2>&1)
        errn=$?
        if [ $errn != 0 ]; then
            syslog err "failed to reconfigure wpa_supplicant"
            syslog err "$err"
        fi
        return $errn
    }

    wpa_supplicant_stop()
    {
        dir=$(wpa_supplicant_ctrldir)
        [ -z "$dir" ] && return 1
        wpa_cli -p "$dir" -i "$interface" status >/dev/null 2>&1 || return 0
        syslog info "stopping wpa_supplicant"
        err=$(wpa_cli -i"$interface" terminate 2>&1)
        errn=$?
        if [ $errn != 0 ]; then
            syslog err "failed to start wpa_supplicant"
            syslog err "$err"
        fi
        return $errn
    }

    if [ "$ifwireless" = "1" ] && \
        type wpa_supplicant >/dev/null 2>&1 && \
        type wpa_cli >/dev/null 2>&1
    then
        case "$reason" in
        PREINIT)	wpa_supplicant_start;;
        RECONFIGURE)	wpa_supplicant_reconfigure;;
        DEPARTED)	wpa_supplicant_stop;;
        esac
    fi

