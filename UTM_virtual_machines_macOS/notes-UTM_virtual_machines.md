# Purpose

Document using UTM to create virtual machines on MacOS Apple Silicon CPUs. On my 2021 MacBook Pro M1 Max I found that VMWare Fusion did not work to get a running Ubuntu VM that I need to set up Openfoam. I'm therefore trying UTM.

# Steps

- Install [UTM](https://mac.getutm.app/).
- Install [Ubuntu 20.05 for UTM](https://mac.getutm.app/gallery/ubuntu-20-04). I had to follow Step 2 in **Cannot boot into installer**, i.e., hit ESC right after rebooting to enter shell and choose `ubuntu` option for booting. Not sure why it doesn't just boot right into Ubuntu when starting the VM.

To check the OS version:

    $ cat /etc/os-release
    
