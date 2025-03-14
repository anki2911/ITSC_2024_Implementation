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
sumoCmd = [sumoBinary, "-c", "C:/Users/Ankita/Desktop/sumo-1.16.0/tools/Central_Region/Central_Region/Dataset-1/osm.sumocfg"]

traci.start(sumoCmd)

past_lat = 0
past_long = 0
lat = 0
lon = 0

f = open("Trace_13.txt","w")

#Successful Route_1
#traci.vehicle.setRoute('veh0',['161106358','-161106358','655225813'])
#Successful Route_2
#traci.vehicle.setRoute('veh0',['786098710-AddedOffRampEdge','176204416'])
#Successful Route_3
traci.vehicle.setRoute('veh0',['260573531','75351787','176204413-AddedOnRampEdge','176204413'])
#Successful Route_4
#traci.vehicle.setRoute('veh0',['651015378','480453198','639683704','175840049#0','75351814','709885027','709885029#0','630413854','652552910#1','652552908','652552907','652552902','652552901','652552898'])
#Successful Route_5
#traci.vehicle.setRoute('veh0',['656719985','723230939','785034103','655213521','633809077','633809078','778420264','75351811','176204459','176204464','651934674','639683703','655225813'])
#Successful Route_6
#traci.vehicle.setRoute('veh0',['786098710-AddedOffRampEdge','22823199','786099316','22823200','176204464','651934674','639683703','655225813'])
#Successful Route_7
#traci.vehicle.setRoute('veh0',['651015378','480453198','639683704','22823195','175840092','478879828'])
#Successful Route_8
#traci.vehicle.setRoute('veh0',['260573531','22823196','785028884','22823197','652552910#1','652552908','652552907','652552902','652552901','652552898'])



step = 0
while step < 199:
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
