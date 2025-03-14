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
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/Central_Region/Central_Region/Dataset-27/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_276.txt","w")

#Succesful Route_1
#traci.vehicle.setRoute('veh0',['481883082','481874105','481883083','641552501','661082739','540284047','74558013','629329896','481883084','629331530','93841769','464804345'])
#Successful Route_2
#traci.vehicle.setRoute('veh0',['37553312','481874105','481883083','641552501','661082739','528461142','37553426','74558014'])
#Successful Route_3
#traci.vehicle.setRoute('veh0',['628467246','628505878','628505877','497372799','628499130','74558013','629329896','481883084','629331530','93841769','464804345'])
#Successful Route_4
#traci.vehicle.setRoute('veh0',['482089304','482089305','37553427#0','630802882'])
#Successful Route_5
#traci.vehicle.setRoute('veh0',['482089304','482089305','74981331','540284048','535018514','628467247'])
#Successful Route_6
traci.vehicle.setRoute('veh0',['117055160','546438772','1167733851','175959439-AddedOnRampEdge','175959439','22298435','74558014'])


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
