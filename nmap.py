from operator import iadd
import nmap

scanner = nmap.PortScanner() #variable used to port scanner class

print("Welcome, this is a simple nmap automation tool")
print("<------------------------------------------------------->")

ip_addr = input ("Please enter the ip address you want ot scan: ") #prompt the user to enterthe ip address
print("The ip you entered is :", ip_addr)
type(ip_addr)

resp = input("""\nPlease entere the type of scan you want to run 
                1)SYN ACK Scan
                2)UDP Scan
                3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

if resp =='1':
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-2000', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())# show ip status
    print(scanner[ip_addr].all.protocols()) #print all the protocols
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys()) #display the open port
elif resp == '2': 
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-2000', '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())# show ip status
    print(scanner[ip_addr].all.protocols()) #print all the protocols
    print("Open Ports: ", scanner[ip_addr]['udp'].keys()) #display the open port   
elif resp == '3': 
    print('Nmap Version: ', scanner.nmap_version())
    scanner.scan(ip_addr, '1-2000', '-v -sS -sV -sC -A -O')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())# show ip status
    print(scanner[ip_addr].all.protocols()) #print all the protocols
    print("Open Ports: ", scanner[ip_addr]['udp'].keys()) #display the open port   
elif resp >= '4':
    print("Please neter the valid option")