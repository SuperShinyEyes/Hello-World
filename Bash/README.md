### Find IP and MAC addresses of devices in the network
```bash
ifconfig | grep broadcast | arp -a
# Or
arp -na
# Or with manufacturer names
sudo nmap -sn 192.168.0.0/24
```

## Get Wifi information
```bash
# Mac
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport -I en1

# Linux
iwlist wlan0 scan | grep 'Address\|Signal'
```

## [SSHFS](https://medium.com/dev-tricks/mount-a-remote-filesystem-with-sshfs-8a37e85b39ee#.gwcy0bex5)
```bash
mkdir remote_home
# $user@$host:$remote_path $local_dir
sshfs me@www.myhost.com:/home/me/ remote_home
ls -l remote_home/

umount remote_home
```

```bash
brew install sshfs 
```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```

##
```bash

```
