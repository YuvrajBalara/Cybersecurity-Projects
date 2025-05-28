
from scapy.all import 
interface= 'wlano' 
probeReqs = []

def sniffproves (p):
    if p.haslayer (Dot11ProbeReq):
        netName= p.getlayer (Dot11ProbeReq).info
        if netName not in probeReqs:
            probeReqs.append(netName)
            print('[+] Detected New Probe Request: + netName)
                  
sniff(iface=interface, prn=sniffProves)