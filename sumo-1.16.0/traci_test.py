import os, sys
import traci

if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


sumoBinary = "./bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "./tools/2023-04-04-16-19-12/osm.sumocfg"]

traci.start(sumoCmd)
step = 0
while step < 100:
    traci.simulationStep()
    #if traci.inductionloop.getLastStepVehicleNumber("0") > 0:
    #    traci.trafficlight.setRedYellowGreenState("0", "GrGr")
    step += 1

traci.close()