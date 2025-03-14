import sys
import traci
from sumolib import checkBinary                   #start traci
sumo_binary = checkBinary('sumo-gui')
sumoCmd = [sumo_binary, "-c", "osm.sumocfg"]
traci.start(sumoCmd)
