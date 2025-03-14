import sys
import traci
traci.start(["sumo", "-c", "osm.sumocfg"])
simulation_output = "Road_Trace_692219832_1.txt"
original_stdout = sys.stdout
sys.stdout = open(simulation_output, "w")
step = 0
vehicle = "veh0"
path=["692219832","692219832"]
print("692219832")
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
