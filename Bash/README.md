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

##
```bash

```

##
```bash

```
