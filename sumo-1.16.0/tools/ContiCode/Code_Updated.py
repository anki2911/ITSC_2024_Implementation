import os
import sys
import time

from os import listdir
from os.path import isfile, join
import random
import math
from datetime import datetime
from Car import Node
from Frequency import Channel
from CloudServer import Server

def main():
    #Initialization of Server
    Serv = Server(1000)
    Attacker = Node()
    Attacker.initialize(-1)
    Svc_Chan = Channel(1)
    Svc_Chan.attach_dev(Serv.get_node_id())
    Svc_Chan.attach_dev(Attacker.get_node_id())
    
    no = 1
    
    Nodes = []
    for i in range(0,int(no)):
        id = i+1
        N = Node()
        N.initialize(id)
        Nodes.append(N)  
        key = Serv.initialize(id)
        Svc_Chan.attach_dev(Nodes[i].get_node_id())
        N.set_key(key)

    num_of_edges = 0
    cwd = "../West_Region/West_Region/Dataset-7/"
    list_roads = []
    list_of_files = os.listdir(cwd) 
    for each_file in list_of_files:
        if each_file.startswith('Road'):  
            num_of_edges = num_of_edges + 1
            list_roads.append(str(cwd) + str(each_file))
            #print(each_file)

    for i in range(0,int(num_of_edges)):
        Serv.Road_Data_List.append([])
    
    for i in range(len(list_roads)):
        #print(list[i])
        f = open(list_roads[i],"r")
        Serv.read_RoadData(f,i)
    
    #Edge Details, Edge ID, Start Junction and End Junction, length of the road
    f = open(str(cwd) + "Edge_Details.txt","r")
    g = open(str(cwd) + "Node.txt","r")
    Serv.Edge_Junc_Rel(f,g)
    
    Veh_Data = []

    f = open(str(cwd) + "TraceAttack_72.txt","r")
    out_file = open(str(cwd) + "ResultsAttack_7_2.txt","w")
    
    #f = open(str(cwd) + "Trace_Test_error_1.txt","r")
    #out_file = open(str(cwd) + "Results_30_301_error.txt","w")

    #Veh_Data.append([])
    for lines in f:
        lines = lines.strip("\n")
        for words in lines:
            words = lines.split(" ")
        Nodes[0].Veh_Data.append(words)

    print("Pre-processiing Done")
    
    #Communication starts between cloud server and the vehicle
    simulation_steps = len(Nodes[0].Veh_Data)
    #simulation_steps = 40
    #print(simulation_steps)
    count = 0
    Waiting_Q = []

    while count < simulation_steps:
        #for i in range(0,len(Nodes)):
        #    if (count == 0) or ((Nodes[i].status == 0) and (count - Nodes[i].step >= 4)):
        #        if Nodes[i] not in Waiting_Q:
        #            print(Nodes[i].step)
        #            Waiting_Q.append(Nodes[i])
        #            Nodes[i].status = 0
        
        #if len(Waiting_Q) > 0:
        #    print("Inside")
        #    r = random.randint(0,(len(Waiting_Q)-1))
        #    N = Waiting_Q.pop(r)
            #print(r)
        #    N.status = 1
        if Svc_Chan.check_chan_state() == 0:
            id = N.id
            print(N.index)
            lat = N.Veh_Data[N.index][0]
            lon = N.Veh_Data[N.index][1]
            bear = N.Veh_Data[N.index][2]
            speed = N.Veh_Data[N.index][3]
            t = N.Veh_Data[N.index][4]
            N.data_packet = str(id) + "_" + str(lat) + "_" + str(lon) + "_" + str(bear) + "_" + str(speed) + "_" + str(t)
            N.index = N.index + 1
        
            if Svc_Chan.check_chan_state() == 0:
                Svc_Chan.set_state(1)
                Svc_Chan.send_data(N,Serv)
                Svc_Chan.set_state(0)
                error = Serv.estimate_location()
                out_file.write(str(error) + "\n")
                start = time.perf_counter()
                if error >= 100: 
                    msg_digest = Serv.attack_prevent(N.get_node_id(),N.get_key())
                    print(N.data_packet)
                    print(sys.getsizeof(N.data_packet))
                    N.data_packet = str(msg_digest) + "$" + N.data_packet
                    print(N.data_packet)
                    print(sys.getsizeof(N.data_packet))
                end = time.perf_counter()
                elapsed_time = end - start
                print(f"Elapsed time: {elapsed_time:.6f} seconds")
                    
                
                #Add Server Side Communications and Computations here


            N.steps = count
            N.status = 0

        count = count + 1       
    

    
if __name__ == '__main__':
    main()