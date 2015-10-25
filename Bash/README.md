### Find IP and MAC addresses of devices in the network
```bash
ifconfig | grep broadcast | arp -a
# Or
arp -na
# Or with manufacturer names
sudo nmap -sn 192.168.0.0/24
```
