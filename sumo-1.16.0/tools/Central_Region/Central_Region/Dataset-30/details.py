import sys
import traci
from sumolib import checkBinary
sumo_binary = checkBinary('sumo-gui')
sumoCmd = [sumo_binary, "-c", "osm.sumocfg"]
traci.start(sumoCmd)
simulation_output = "Road_Trace_631885735-AddedOnRampEdge_1.txt"
original_stdout = sys.stdout
sys.stdout = open(simulation_output, "w")
step = 0
vehicle = "veh0"
path=["631885735-AddedOnRampEdge","631885735-AddedOnRampEdge"]
print("631885735-AddedOnRampEdge")
traci.vehicle.setMaxSpeed(vehicle, 1)
traci.vehicle.setRoute(vehicle,path)
while step <= 300:      
    traci.simulationStep()
    position = traci.vehicle.getPosition(vehicle)
    x_coord, y_coord = position
    lon, lat = traci.simulation.convertGeo(x_coord, y_coord)
    angle=traci.vehicle.getAngle(vehicle)
    print(lat,lon,angle)
sys.stdout.close()
sys.stdout = original_stdout
traci.close()
