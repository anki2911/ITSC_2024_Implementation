import os
import sys
import traci
import traci.constants as tc
import math
import xml.etree.ElementTree as ET 
import sumolib

net = sumolib.net.readNet('./2023-06-15-20-27-12/osm.net.xml')

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))

sumoBinary = "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/tools/2023-06-15-20-27-12/osm.sumocfg"]

#Road Data based on edge IDs
f1 = open("Road_Trace_114667396#0_1.txt","r")
f2 = open("Road_Trace_169195795#2_1.txt","r")
f3 = open("Road_Trace_169195795#0_1.txt","r")
f4 = open("Road_Trace_1113726463_1.txt","r")
f5 = open("Road_Trace_1077923225#0_1.txt","r")
f6 = open("Road_Trace_1126237668#0_1.txt","r")
f7 = open("Road_Trace_340498982#0_1.txt","r")
f8 = open("Road_Trace_169195795#3_1.txt","r")

#Actual Driver data
F_veh = open("ActualVehicleTrace.txt","r")

Road_Data_List = []
Road_property = []
Edge_Name = []
Junction_Name = []

Edge_Relation = {}

Edge_Length = {}
Edge_Start_Lat = {}
Edge_End_Lat = {}
Edge_Start_Long = {}
Edge_End_Long = {}

#Data Structure to store list of Road Data
for i in range(0,8):
    Road_Data_List.append([])

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f1:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[0].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1])   
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f2:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[1].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1])   
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f3:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[2].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f4:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[3].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f5:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[4].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f6:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[5].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f7:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[6].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)
        
    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Read Each Road Data
min_lat = 91
max_lat = 0
min_lon = 181
max_lon = 0
i = 0
for lines in f8:
    lines = lines.strip("\n")
    if i > 0:
        for words in lines:
            words = lines.split(" ")
        Road_Data_List[7].append(words)
        if max_lat < float(words[0]):
            max_lat = float(words[0])
        if min_lat > float(words[0]):
            min_lat = float(words[0])
        if max_lon < float(words[1]):
            max_lon = float(words[1])
        if min_lon > float(words[1]):
            min_lon = float(words[1]) 
    else:
        Edge_Name.append(lines)

    i = i + 1
Road_property.append((min_lat,max_lat,min_lon,max_lon))

#Edge Details, Edge ID, Start Junction and End Junction, length of the road
f = open("Edge_Details.txt","r")

temp = []

#Unique Junction Names
for lines in f:
    lines = lines.strip("\n")
    for words in lines:
        words = lines.split(" ")
    temp.append(words)
    Edge_Length[str(words[0])] = str(words[3])
    if str(words[0]) in Edge_Name:
        if str(words[1]) not in Junction_Name:
            Junction_Name.append(str(words[1]))
        if str(words[2]) not in Junction_Name:
            Junction_Name.append(str(words[2]))         
f.close()

#Store the details of Junction <ID and Co-Ordinates>
Node_Details = []
Junction_Details = []
f = open("Node.txt","r")
for lines in f:
    lines = lines.strip("\n")
    for words in lines:
        words = lines.split(" ")
    Node_Details.append(words)
    Junction_Details.append((str(words[0]),str(words[1]),str(words[2])))

#Connect Edges and Junctions
for i in range(0,len(temp)):
    e_id = str(temp[i][0])
    jstart = str(temp[i][1])
    jend = str(temp[i][2])
    for j in range(0,len(Node_Details)):
        if jstart == str(Node_Details[j][0]):
            Edge_Start_Lat[str(e_id)] = str(Node_Details[j][1])
            Edge_Start_Long[str(e_id)] = str(Node_Details[j][2])
        if jend == str(Node_Details[j][0]):
            Edge_End_Lat[str(e_id)] = str(Node_Details[j][1])
            Edge_End_Long[str(e_id)] = str(Node_Details[j][2])
            
#Adjacency List for Edges to store details of Road Connectivity
for i in range(0,len(temp)-1):
    for j in range(i+1,len(temp)):
        if temp[i][1] == temp[j][2]:
            Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
        elif temp[i][2] == temp[j][1]:
            Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
        elif temp[i][1] == temp[j][1]:
            Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
        elif temp[i][2] == temp[j][2]:
            Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
        else:
            Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 0

#Algorithm Predict Next Step
Eligible_List = []
Actual_Veh_Data = []

#Get Simulation Time depending on length of offline data
simtime = 0
for lines in F_veh:
    lines = lines.strip("\n")
    simtime += 1
    for words in lines:
        words = lines.split(" ")
    Actual_Veh_Data.append(words)
#print(Actual_Veh_Data)    

prev_x = 0
prev_y= 0

timer = 0
prev_pos_x = float(Actual_Veh_Data[timer][0])
prev_pos_y = float(Actual_Veh_Data[timer][1])
prev_angle = float(Actual_Veh_Data[timer][2])
prev_speed = float(Actual_Veh_Data[timer][3])
timer += 1

while(timer < simtime):
    cur_pos_x = float(Actual_Veh_Data[timer][0])
    cur_pos_y = float(Actual_Veh_Data[timer][1])
    cur_angle = float(Actual_Veh_Data[timer][2])
    cur_speed = float(Actual_Veh_Data[timer][3])
    
    eligible_road1 = []
    eligible_road2 = []
    for i in range(0,len(Road_property)):
        if cur_pos_x > Road_property[i][0] and cur_pos_x < Road_property[i][1] and cur_pos_y > Road_property[i][2] and cur_pos_y < Road_property[i][3]:
            eligible_road1.append(Edge_Name[i])
            e_id = Edge_Name[i]
    #print(eligible_road1)

    if len(eligible_road1) > 0:
        for j in range(0,len(eligible_road1)):
            total_len = Edge_Length[str(eligible_road1[j])]
            index = Edge_Name.index(str(eligible_road1[j]))
            start_lat = Edge_Start_Lat[str(eligible_road1[j])]
            end_lat = Edge_End_Lat[str(eligible_road1[j])]
            start_long = Edge_Start_Long[str(eligible_road1[j])]
            end_long = Edge_End_Long[str(eligible_road1[j])]

            if prev_x == 0 and prev_y == 0:
                count = 0
            found = 0
            last_count = count
            while ((found == 0) and (count < len(Road_Data_List[index]))):
                if ((abs(float(Road_Data_List[index][count][0]) - float(cur_pos_x)) <= 0.00005) and (abs(float(Road_Data_List[index][count][1]) - float(cur_pos_y)) <= 0.00005) and (abs(float(Road_Data_List[index][count][2]) - float(cur_angle)) <= 0.005)):
                    found = 1
                    prev_x = 1
                    prev_y = 1
                    print(count - last_count)
                    print(prev_speed)
                    print(cur_speed)
                    #print(count)
                else:
                    count += 1
            if found == 0 and count < len(Road_Data_List[index]):
                print("Unmatch")

            if count >= len(Road_Data_List[index]):
                count = 0
                prev_x = 0
                prev_y = 0   
    else:
        e1 = Edge_End_Lat[str(e_id)]  
        e2 = Edge_End_Long[str(e_id)]
        if (abs(float(e1) - float(cur_pos_x)) <= 0.0002) and (abs(float(e2) - float(cur_pos_y)) <= 0.0002):
            print("Passing through junction")
            print(count - last_count)
            print(prev_speed)
            print(cur_speed)
            #print(count)
        else:
            print("Unmatch")

    prev_pos_x = cur_pos_x
    prev_pos_y = cur_pos_y
    prev_speed = cur_speed
    prev_angle = cur_angle

 
    timer += 1




