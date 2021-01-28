
Assumes OpenSSH client.

# Best practice

Based on my recent experience and learning from the online articles linked to in the Information section, here is my take on the best practice use of ssh on my mac laptop.

- Either have 1 or only a limited number of key pairs, all of which go in `~/.ssh`.
	- 1 key: `id_rsa` and `id_rsa.pub` (private and public keys, respectively)
	- 2 keys: Something like `key-home` & `key-home.pub` and `key-work`& `key-work.pub`.
- When I want to set up using a key to ssh into some other linux/macos machine, execute the following command to copy the public key to the other machine: `ssh-copy-id -i ~/.ssh/<key_name>.pub user@somehost`
- Add the new server to `~/.ssh/config` with an entry like the following:

        Host <alias name>
            Hostname <host name>
            IdentitiesOnly yes
            User <username>
            IdentityFile ~/.ssh/<key_name>
- To ssh into the server, now all you need to do is execute `ssh <alias name>`


# Information

[The Ultimate Guide to SSH - Setting Up SSH Keys](https://www.freecodecamp.org/news/the-ultimate-guide-to-ssh-setting-up-ssh-keys/) - excellent, and while it doesn't say so, the file organization is for MacOS.


# ssh Config file

[Use SSH Config File to Manage SSH Connections to Various Remote Servers](https://linuxhandbook.com/ssh-config-file/) - Using SSH profiles can help you in cases where you regularly connect to various servers. No need to remember the IP address and other such details for SSH connection.

[Using the SSH Config File](https://linuxize.com/post/using-the-ssh-config-file/)

>The SSH config file is also read by other programs such as scp , sftp , and rsync.

[SSH Config File](https://www.ssh.com/ssh/config/) - full documentation