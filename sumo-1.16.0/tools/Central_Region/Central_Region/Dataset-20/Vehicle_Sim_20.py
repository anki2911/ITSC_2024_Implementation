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
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/Central_Region/Central_Region/Dataset-20/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_206.txt","w")

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['479786270','479788160','37583816','479789545','479789547-AddedOnRampEdge','479789547'])
#Successful Route_2
#traci.vehicle.setRoute('veh0',['628449302','628449302-AddedOffRampEdge','785815075'])
#Successful Route_3
#traci.vehicle.setRoute('veh0',['628449302','628449302-AddedOffRampEdge','74896358','479789547-AddedOnRampEdge','479789547'])
#Successful Route_4
#traci.vehicle.setRoute('veh0',['635161211','635161211-AddedOffRampEdge','720094147','74896359','477930417'])
#Successful Route_5
#traci.vehicle.setRoute('veh0',['635161211','635161211-AddedOffRampEdge','37583811','37583812','692895634','720101856','720101855','75616386'])
#Successful Route_6
#traci.vehicle.setRoute('veh0',['477785969','477930416','22789070','680527351','680527352','74896359','477930417'])
#Successful Route_7
#traci.vehicle.setRoute('veh0',['477785969','477930416','75616377','656751248','659826322','633590154'])


step = 0
while step < 400:
    traci.simulationStep()
    sampling_time = traci.simulation.getTime()
    print(sampling_time)

    vehicles = traci.vehicle.getIDList()  
    if step%1 == 0:
        for i in range(0, len(vehicles)):
            traci.vehicle.setSpeed(vehicles[i],5) 
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
