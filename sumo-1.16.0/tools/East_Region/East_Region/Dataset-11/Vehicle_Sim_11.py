import os
import sys
import traci
import traci.constants as tc
import math
import sumolib

net = sumolib.net.readNet('./osm.net.xml')


if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")


sumoBinary = "C:/Users/Ankita/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/East_Region/East_Region/Dataset-11/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_117.txt","w")

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['718972473','718972473-AddedOffRampEdge','626073789','924526184','626075660','32839192','311265151','652238209','633145351','445716781-AddedOnRampEdge','445716781'])

#Successful Route_2
#traci.vehicle.setRoute('veh0',['718972473','718972473-AddedOffRampEdge','635098148','736721782','635098149','700500973','33176817#1-AddedOnRampEdge','33176817#1'])

#Successful Route_3
#traci.vehicle.setRoute('veh0',['718972473','718972473-AddedOffRampEdge','635098148','736721782','635098149','993071477','711901303','635098150#0','635098150#1-AddedOnRampEdge','635098150#1'])

#Successful Route_4
#traci.vehicle.setRoute('veh0',['715627057','646117453#1','648721689','654572674','32921891','483100679','626072444'])

#Successful Route_5
#traci.vehicle.setRoute('veh0',['715627057','700595302','652189113','33176817#1-AddedOnRampEdge','33176817#1'])

#Successful Route_6
#traci.vehicle.setRoute('veh0',['715627057','646117453#1','648721689','654572674','32921891','483100679','626072444'])

#Successful Route_7
#traci.vehicle.setRoute('veh0',['715627057','646117453#1','646117454','311265513#0','311265513#1','445716781-AddedOnRampEdge','445716781'])





step = 0
while step < 300:
    traci.simulationStep()
    sampling_time = traci.simulation.getTime()
    print(sampling_time)

    vehicles = traci.vehicle.getIDList()  
    if step%1 == 0:
        for i in range(0, len(vehicles)):
            traci.vehicle.setSpeed(vehicles[i],10) 
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
            f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        #print(dist)
        #print(traci.simulation.getTime())
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + " " + str(speed) + " " + str(traci.simulation.getTime()) + "\n")
        #f.write(str(lat) + " " + str(lon) + " " + str(angle) + "\n")

    #if step == 80:
    #    traci.vehicle.moveToXY('veh0','169195795#0','169195795#0_0',224.18,43.25,angle=85,keepRoute=1,matchThreshold=100)
    
    step += 1


f.close()

traci.close()
