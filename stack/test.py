#!/usr/bin/python3
from netfilterqueue import NetfilterQueue

import os
import argparse

#cmd1 = "iptables -A INPUT -p udp --dport 8443 -j NFQUEUE --queue-num 1"
#cmd2 = "iptables -A OUTPUT --dest 10.10.10.10 -p udp --dport 8443 -j NFQUEUE --queue-num 1"
#os.system(cmd1)
#os.system(cmd2)

def DroporAccept(pkt):
    if(pkt.id == int(results.packet)):
        print("Packet is",pkt)
        pkt.drop()
        raise SystemExit
    else:
        pkt.accept()
        print("Accepting")

def  main():
    print("THERE")
    global results
    results = 0
    parser = argparse.ArgumentParser(description="Arg parser")
    parser.add_argument('-pkt', action='store', dest='packet',default='',
                    help='Drop packet')
    parser.add_argument('-p', action='store', dest='port',default='8443',
                    help='Port number')
    parser.add_argument('-pr', action='store', dest='protocol',default='udp',
                    help='Protocol')
    parser.add_argument('-dip', action='store', dest='destip',default='',
                    help='Destination IP addresss')
    parser.add_argument('-dp', action='store', dest='dport',default='',
                    help='Destination Port')
    parser.add_argument('-sp', action='store', dest='sport',default='',
                    help='Source Port')
    parser.add_argument('-indir', action='store', dest='direction_in',default='',
                    help='INPUT')
    parser.add_argument('-outdir', action='store', dest='direction_out',default='',
                    help='OUTPUT')
    results = parser.parse_args()
    print("Adding the IPTABLE Rules")
    iptables = ["iptables -A " + results.direction_in + " -p " + results.protocol + " --dport " + results.port + " -j NFQUEUE --queue-num 1", "iptables -A " + results.direction_out + " --dest " + results.destip + " -p " + results.protocol + " --sport " + results.port + " -j NFQUEUE --queue-num 1"]
    #iptables = ['iptables -A INPUT -p udp --dport 8443 -j NFQUEUE --queue-num 1', 'iptables -A OUTPUT --dest 172.16.77.1 -p udp --sport 8443 -j NFQUEUE --queue-num 1']
    for line in iptables:
        print(line)
        os.system(line)
    print("Adding IPTABLE rules done")
    print ("packet to be dropped     =", results.packet)
    nfqueue = NetfilterQueue()
    nfqueue.bind(1,DroporAccept)
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        print("Flushing iptables.")
        # This flushes everything, you might wanna be careful
        os.system('iptables -F')
        os.system('iptables -X')
        os.system('ip6tables -F')
        os.system('ip6tables -X')
        nfqueue.unbind()
if __name__ == "__main__":
    main()

