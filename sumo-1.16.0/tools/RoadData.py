import os
import sys
import traci
import traci.constants as tc
import math
import xml.etree.ElementTree as ET 

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))

sumoBinary = "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/bin/sumo-gui"
sumoCmd = [sumoBinary, "-c", "C:/Users/ankita.samaddar/Desktop/sumo-1.16.0/tools/2023-06-15-20-27-12/osm.sumocfg"]

#traci.start(sumoCmd)
f1 = open("Road_Trace_114667396#0_1.txt","r")
f2 = open("Road_Trace_169195795#2_1.txt","r")
f3 = open("Road_Trace_169195795#0_1.txt","r")
f4 = open("Road_Trace_1113726463_1.txt","r")
f5 = open("Road_Trace_1077923225#0_1.txt","r")
f6 = open("Road_Trace_1126237668#0_1.txt","r")
f7 = open("Road_Trace_340498982#0_1.txt","r")
f8 = open("Road_Trace_169195795#3_1.txt","r")

Road_Data_List = []
Road_property = []
Edge_Name = []
Junction_Name = []

Edge_Relation = {}

for i in range(0,8):
    Road_Data_List.append([])

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

f = open("Edge_Details.txt","r")

temp = []

for lines in f:
    lines = lines.strip("\n")
    for words in lines:
        words = lines.split(" ")
    temp.append(words)
    if str(words[0]) in Edge_Name:
        if str(words[1]) not in Junction_Name:
            Junction_Name.append(str(words[1]))
        if str(words[2]) not in Junction_Name:
            Junction_Name.append(str(words[2]))           
f.close()

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

print(Road_property)







    


