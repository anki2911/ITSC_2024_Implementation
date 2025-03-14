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
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/East_Region/East_Region/Dataset-7/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_78.txt","w")

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['651135161','696946493'])
#Successful Route_2
#traci.vehicle.setRoute('veh0',['696946492','15775495','74535469'])
#Successful Route_3
#traci.vehicle.setRoute('veh0',['166741193','717446237','74535469'])
#Successful Route_4
#traci.vehicle.setRoute('veh0',['481949081'])
#Successful Route_5
#traci.vehicle.setRoute('veh0',['74662604','633576832','34403109','34760645','638069333','717446236'])
#Successful Route_6
#traci.vehicle.setRoute('veh0',['700998527','934406421','62272692','34403107','631931875'])
#Successful Route_7
#traci.vehicle.setRoute('veh0',['655688364','655688725','655688603','655688982','655689130','655689131','522398498','652289910','506882383','696949302','506882382'])
#Successful Route_8
#traci.vehicle.setRoute('veh0',['546182226','750425972','546182224','481949082','655687093','655687569','750425969','652289910','506882383','696949302','506882382'])


step = 0
while step < 200:
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
