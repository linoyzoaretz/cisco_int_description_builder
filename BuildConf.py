switchport = 1
wall_port = 25

# switch int range 1-48
# every third port is VoIP - VLAN 130 
# if the port is not third that it just get a description :) 

for switchport in range(1,48):
    if(switchport % 3 == 0):
       print("default interface G1/0/"+ str(switchport))
       print("interface G1/0/"+ str(switchport))
       print("description Wall_" + str(wall_port))
       print("switchport mode access")
       print("switchport access vlan 130")
       print("!")
       switchport += 1
       wall_port += 1
    
    else:
        print("interface G1/0/"+ str(switchport))
        print("description Wall_" + str(wall_port))
        print("!")
        switchport += 1
        wall_port += 1
    
    
    