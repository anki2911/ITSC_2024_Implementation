import os
import sys
from pathlib import Path
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
    
    no = 2
    
    Nodes = []
    for i in range(0,int(no)):
        id = i+1
        N = Node()
        N.initialize(id)
        Nodes.append(N)  
        key = Serv.initialize(id)
        Svc_Chan.attach_dev(Nodes[i].get_node_id())
        N.set_key(key)

    num_of_edges = 8

    for i in range(0,int(num_of_edges)):
        Serv.Road_Data_List.append([])

    mypath = Path.cwd()
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    file_cnt = 1
    for fnames in onlyfiles:
        if "Road_Trace_" in fnames:
            print(fnames)
            Serv.read_RoadData(open(str(fnames),"r"),0)
            file_cnt += 1

    
    #f1 = open("Road_Trace_114667396#0_1.txt","r")
    #f2 = open("Road_Trace_169195795#2_1.txt","r")
    #f3 = open("Road_Trace_169195795#0_1.txt","r")
    #f4 = open("Road_Trace_1113726463_1.txt","r")
    #f5 = open("Road_Trace_1077923225#0_1.txt","r")
    #f6 = open("Road_Trace_1126237668#0_1.txt","r")
    #f7 = open("Road_Trace_340498982#0_1.txt","r")
    #f8 = open("Road_Trace_169195795#3_1.txt","r")

    #Read Each Road Data
    #Serv.read_RoadData(f1,0)
    #Serv.read_RoadData(f2,1)
    #Serv.read_RoadData(f3,2)
    #Serv.read_RoadData(f4,3)
    #Serv.read_RoadData(f5,4)
    #Serv.read_RoadData(f6,5)
    #Serv.read_RoadData(f7,6)
    #Serv.read_RoadData(f8,7)

    #Edge Details, Edge ID, Start Junction and End Junction, length of the road
    f = open("Edge_Details1.txt","r")
    g = open("Node1.txt","r")
    Serv.Edge_Junc_Rel(f,g)
    print("HELLO")
    Veh_Data = []

    f = open("ActualVehicleTrace.txt","r")
    #Veh_Data.append([])
    for lines in f:
        lines = lines.strip("\n")
        for words in lines:
            words = lines.split(" ")
        Nodes[0].Veh_Data.append(words)

    f = open("Driver_Trace.txt","r")
    #Veh_Data.append([])
    for lines in f:
        lines = lines.strip("\n")
        for words in lines:
            words = lines.split(" ")
        Nodes[1].Veh_Data.append(words)
    
    print("Pre-processiing Done")
    
    #Communication starts between cloud server and the vehicle
    simulation_steps = 55
    count = 0
    Waiting_Q = []

    while count < simulation_steps:
        for i in range(0,len(Nodes)):
            if (count == 0) or ((Nodes[i].status == 0) and (count - Nodes[i].step >= 4)):
                if Nodes[i] not in Waiting_Q:
                    print(Nodes[i].step)
                    Waiting_Q.append(Nodes[i])
                    Nodes[i].status = 0
        
        if len(Waiting_Q) > 0:
            print("Inside")
            r = random.randint(0,(len(Waiting_Q)-1))
            N = Waiting_Q.pop(r)
            #print(r)
            N.status = 1
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
                
                #Add Server Side Communications and Computations here


            N.steps = count
            N.status = 0


    

        count = count + 1       
            


    
if __name__ == '__main__':
    main()