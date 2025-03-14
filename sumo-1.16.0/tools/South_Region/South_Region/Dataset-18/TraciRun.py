import os
import sys
import traci
import traci.constants as tc
import math
import sumolib

#net = sumolib.net.readNet('./2023-06-15-20-27-12/osm.net.xml')
#net = sumolib.net.readNet('./2023-09-27-03-32-07/osm.net.xml')
#net = sumolib.net.readNet('./2023-04-04-16-16-26/osm.net.xml')
#net = sumolib.net.readNet('./2023-09-26-13-57-27/osm.net.xml')
net = sumolib.net.readNet('./osm.net.xml')


if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")


sumoBinary = "C:/Users/Ankita/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/South_Region/South_Region/Dataset-18/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Road_Trace_74729033.txt","w")
f.write("74729033" + "\n")
#x,y = net.getNode('10189040386').getCoord()
#lon, lat = traci.simulation.convertGeo(x, y)
#print(lon)
#print(lat)

#Valid Routes
#traci.vehicle.setRoute('veh0',['23924500'])
#traci.vehicle.setRoute('veh0',['-23924500'])
#traci.vehicle.setRoute('veh0',['74527432#0'])
#traci.vehicle.setRoute('veh0',['174281658'])
#traci.vehicle.setRoute('veh0',['284167586'])
#traci.vehicle.setRoute('veh0',['464199169'])
#traci.vehicle.setRoute('veh0',['464204346'])
#traci.vehicle.setRoute('veh0',['464204347'])
#traci.vehicle.setRoute('veh0',['473393249'])
#traci.vehicle.setRoute('veh0',['473393252'])
#traci.vehicle.setRoute('veh0',['473393255'])
#traci.vehicle.setRoute('veh0',['473888861'])
#traci.vehicle.setRoute('veh0',['474471903'])
#traci.vehicle.setRoute('veh0',['477792528'])
#traci.vehicle.setRoute('veh0',['478162426'])
#traci.vehicle.setRoute('veh0',['539603100'])
#traci.vehicle.setRoute('veh0',['539603102#0'])
#traci.vehicle.setRoute('veh0',['585984922'])
#traci.vehicle.setRoute('veh0',['585984925'])
#traci.vehicle.setRoute('veh0',['585984926'])
#traci.vehicle.setRoute('veh0',['585984928#0'])
#traci.vehicle.setRoute('veh0',['585984929'])
#traci.vehicle.setRoute('veh0',['636908812'])
#traci.vehicle.setRoute('veh0',['637713639'])
#traci.vehicle.setRoute('veh0',['639419044'])
#traci.vehicle.setRoute('veh0',['641096149'])
traci.vehicle.setRoute('veh0',['74729033'])


#Successful Route_1
#traci.vehicle.setRoute('veh0',['641096149','585984929','464204346'])

#Successful Route_2
#traci.vehicle.setRoute('veh0',['477792528','474471903','464199169','174281658'])

#Successful Route_3
#traci.vehicle.setRoute('veh0',['477792528','474471903','473393255','74527432#0'])

#Successful Route_4
#traci.vehicle.setRoute('veh0',['473393252','637713639','473393249','585984922','478162426'])

#Successful Route_5
#traci.vehicle.setRoute('veh0',['473393252','637713639','464204347','585984925','639419044'])

#Successful Route_6
#traci.vehicle.setRoute('veh0',['473393252','637713639','464204347','585984925','23924500'])

#Successful Route_7
#traci.vehicle.setRoute('veh0',['473888861','636908812','284167586','478162426'])


#f = open('Road_Trace_169195795#0_1.txt','w')
#f.write("169195795#0" + "\n")

#traci.vehicle.setRoute('veh0',['1126237668#0','340498982#0'])
#traci.vehicle.setRoute('veh0',['169195795#0','169195795#2','114667396#0'])
#traci.vehicle.setRoute('veh0',['169195795#0','169195795#2','114667396#0'])

#traci.vehicle.setRoute('veh0',['169195795#0'])
#traci.vehicle.setRoute('veh0',['340498982#0'])

#traci.vehicle.setRoute('veh0',['169195795#0'])

#f = open("ActualVehicleTrace.txt","w")

step = 0
while step < 100:
    traci.simulationStep()
    sampling_time = traci.simulation.getTime()
    print(sampling_time)

    vehicles = traci.vehicle.getIDList()  
    #if step <=100:
    for i in range(0, len(vehicles)):
        traci.vehicle.setSpeed(vehicles[i], 10) 
        print(traci.vehicle.getSpeed(vehicles[i]))
        speed = traci.vehicle.getSpeed(vehicles[i])
        print("Speed of the ", vehicles[i], "is : ", traci.vehicle.getSpeed(vehicles[i]))
        past_lat = lat
        past_long = lon
        #print("Position",traci.vehicle.getPosition(vehicles[i]))
        angle = traci.vehicle.getAngle(vehicles[i])
        print("Angle",angle)
        x, y = traci.vehicle.getPosition(vehicles[i])
        lon, lat = traci.simulation.convertGeo(x, y)
        print(lon,lat)
        dist = math.sqrt((past_lat-lat)*(past_lat-lat) + (past_long-lon)*(past_long-lon))
        #print(dist)
        #print(traci.simulation.getTime())
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        f.write(str(lat) + " " + str(lon) + " " + str(angle) + "\n")

    #if step == 80:
    #    traci.vehicle.moveToXY('veh0','169195795#0','169195795#0_0',224.18,43.25,angle=85,keepRoute=1,matchThreshold=100)
    
    step += 1



#f.close()

traci.close()
