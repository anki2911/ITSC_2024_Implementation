import os
import sys
import traci
import traci.constants as tc
import math
import xml.etree.ElementTree as ET 
import sumolib

net = sumolib.net.readNet('./2023-06-15-20-27-12/osm.net.xml')

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))

sumoBinary = "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/tools/2023-06-15-20-27-12/osm.sumocfg"]

traci.start(sumoCmd)

# Pass the path of the xml document 
tree = ET.parse('./2023-06-15-20-27-12/osm.net.xml') 

# get the parent tag 
root = tree.getroot() 

print("Edge")

f = open("Edge_Details1.txt","w")
Edge = []

for e in root.iter('edge'):
    e_id = e.get('id')
    e_from = e.get('from')
    e_to = e.get('to')
    l = traci.lane.getLength(str(e_id)+"_0")
    print(str(e_id) + " from " + str(e_from) + " to " + str(e_to))
    #if str(e_from) == 'None' and str(e_to) == 'None':
    #    f.write(str(e_id) + " " + str(-100) + " " + str(-100) + " " + str(l) + "\n")
    #    print(str(e_id) + " from " + str(e_from) + " to " + str(e_to))
    if str(e_from) == 'None' and str(e_to) != 'None':
        f.write(str(e_id) + " " + str(-100) + " " + str(e_to) + " " + str(l) + "\n")
        print(str(e_id) + " from " + str(e_from) + " to " + str(e_to))
        Edge.append(e_id)
    elif str(e_to) != 'None' and str(e_from) == 'None':
        f.write(str(e_id) + " " + str(e_from) + " " + str(-100) + " " + str(l) + "\n")
        print(str(e_id) + " from " + str(e_from) + " to " + str(e_to))
        Edge.append(e_id)
    elif str(e_to) != 'None' and str(e_from) != 'None':
        f.write(str(e_id) + " " + str(e_from) + " " + str(e_to) + " " + str(l) + "\n")
        print(str(e_id) + " from " + str(e_from) + " to " + str(e_to))
        Edge.append(e_id)
        
f.close()

print(Edge)

for i in range(0,len(Edge)):
    st = 'veh_' + str(i)
    type = 'v_type_' + str(i)
    traci.vehicle.add(st,[str(Edge[i])],type)


#vehicles = traci.vehicle.getIDList()  
#for i in range(0, len(Edge)):
#    traci.vehicle.setSpeed(vehicles[i], 10) 
#    g = open(str(Edge[i]) + ".txt", "w")
#    g.write(str(Edge[i]) + "\n")
#    step = 0
#    while (step < 100):
#        traci.simulationStep()
#        sampling_time = traci.simulation.getTime()
#        print(sampling_time)
#	angle = traci.vehicle.getAngle(vehicles[i])
#        x, y = traci.vehicle.getPosition(vehicles[i])
#        lon, lat = traci.simulation.convertGeo(x, y)
#        g.write(str(lat) + " " + str(lon) + " " + str(angle) + "\n")    
#        step += 1
#    g.close()


print("Junction")

g = open("Node1.txt","w")

for junc in root.iter('junction'):
    j_id = junc.get('id')

    x = float(junc.get("x"))
    y = float(junc.get("y"))

    lon, lat = traci.simulation.convertGeo(x, y)

    g.write(str(j_id) + " " + str(lat) + " " + str(lon) + "\n")
    print("Junction id " + str(j_id) + " X " + str(lat) + " Y " + str(lon))

g.close()

traci.close()
