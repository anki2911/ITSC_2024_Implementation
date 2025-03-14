import sys
import random
import math
from datetime import datetime

class Node:
    def __init__(self, ID):
        self.id = ID
        self.lat = 0
        self.lon = 0
        self.angle = 0
        self.key = 0
        self.status = 0
        self.data_packet = 0
        self.index = 0
        self.time = datetime.now().microsecond
        self.Veh_Data = []
        
    def get_node_id(self):
        return self.id   

    def set_key(self,key):
        self.key = key 

class Server:
    def __init__(self, ID):
        self.id = ID
        self.data_packet = 0
        self.Road_Data_List = []
        self.Vehicle_Keys = []
        self.Vehicle_Data = []
        self.Road_property = []
        self.Edge_Name = []
        self.Junction_Name = []
        self.Edge_Length = {}
        self.Node_Details = []
        self.Junction_Details = []
        self.Edge_Start_Lat = {}
        self.Edge_Start_Long = {}
        self.Edge_End_Lat = {}
        self.Edge_End_Long = {}
        self.Edge_Relation = {}
        self.Edge_Junc = []

    def initialize(self,id):
        key = random.randint(0,10000000)
        self.Vehicle_Keys.append((id,key))
        self.Vehicle_Data.append((id,0,0,0,0,0,0,0))
        return key

    def get_node_id(self):
        return self.id    

    def read_RoadData(self,f,index):
        #Read Each Road Data
        min_lat = 91
        max_lat = 0
        min_lon = 181
        max_lon = 0
        i = 0
        for lines in f:
            lines = lines.strip("\n")
            if i > 0:
                for words in lines:
                    words = lines.split(" ")
                self.Road_Data_List[index].append(words)
                if max_lat < float(words[0]):
                    max_lat = float(words[0])
                if min_lat > float(words[0]):
                    min_lat = float(words[0])
                if max_lon < float(words[1]):
                    max_lon = float(words[1])
                if min_lon > float(words[1]):
                    min_lon = float(words[1])   
            else:
                self.Edge_Name.append(lines)
            i = i + 1
        self.Road_property.append((min_lat,max_lat,min_lon,max_lon))

    def estimate_location(self):
        data = self.data_packet.split('_')
        flag_authentic = False
        id = data[0]
        i = 0
        index = -1
        found = False
        error = 1
        #find ID of the vehicle in the database
        while ((found == False) and (i < len(self.Vehicle_Data))):
            if str(self.Vehicle_Data[i][0]) == str(id):
                found = True
                index = i
            i = i + 1

        if found == True:
            cur_pos_x = float(data[1])
            cur_pos_y = float(data[2])
            cur_angle = float(data[3])
            cur_speed = float(data[4])
            cur_time = data[5]
            prev_pos_x = float(self.Vehicle_Data[index][1])
            prev_pos_y = float(self.Vehicle_Data[index][2])
            prev_angle = float(self.Vehicle_Data[index][3])
            prev_speed = float(self.Vehicle_Data[index][4])
            prev_time = self.Vehicle_Data[index][5]
            prev_road_id = self.Vehicle_Data[index][6]
            cur_road_id = self.Vehicle_Data[index][7]
        
        eligible_road = []
        #Find the road id where the vehicle belongs to
        for k in range(0,len(self.Road_property)):
            if ((float(data[1]) >= float(self.Road_property[k][0])) and (float(data[1]) <= float(self.Road_property[k][1])) and (float(data[2]) >= float(self.Road_property[k][2])) and (float(data[2]) <= float(self.Road_property[k][3]))):
                eligible_road.append(self.Edge_Name[k]) 
        
        #No eligible road
        if (len(eligible_road) == 0):
            print("No Road")
            #Current Road ID : 0, Vehicle moving inside the junction
            if (str(cur_road_id) == str(0)):
                a = float(prev_speed)*(float(cur_time) - float(prev_time)) + 0.5 * ((float(cur_speed) - float(prev_speed))/(float(cur_time) - float(prev_time)))*(float(cur_time) - float(prev_time))*(float(cur_time) - float(prev_time))
                dist = math.sqrt((abs(float(prev_pos_x) - float(cur_pos_x)))*(abs(float(prev_pos_x) - float(cur_pos_x))) + (abs(float(prev_pos_y) - float(cur_pos_y)))*(abs(float(prev_pos_y) - float(cur_pos_y))))*111139
                #print(dist)
                print(a)
                print("Inside Junction")
                #if (abs(dist - a) > prev_speed):
                #if (abs(dist - (cur_speed*(float(cur_time) - float(prev_time)))) > prev_speed):
                #if (a < prev_speed):
                if (dist > 2*a):
                    print("Error")
            else:    
                ind2 = self.Edge_Name.index(str(cur_road_id))
                f1 = False
                c1 = 0
                lc2 = -1
                while ((f1 == False) and (c1 < len(self.Road_Data_List[ind2]))):
                    if ((abs(float(self.Road_Data_List[ind2][c1][0]) - float(prev_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind2][c1][1]) - float(prev_pos_y)) <= 0.00005)):
                        # and (abs(float(self.Road_Data_List[ind2][c1][2]) - float(cur_angle)) <= 0.005)):
                        f1 = True
                        lc2 = c1
                    c1 = c1 + 1
                length = len(self.Road_Data_List[ind2])
                print("LC2 " + str(lc2))
                if (length - lc2) <= lc2:
                    rem_len = length - lc2
                else:
                    rem_len = lc2
                dist = math.sqrt((abs(float(prev_pos_x) - float(cur_pos_x)))*(abs(float(prev_pos_x) - float(cur_pos_x))) + (abs(float(prev_pos_y) - float(cur_pos_y)))*(abs(float(prev_pos_y) - float(cur_pos_y))))*111139
                #print(length)
                #print(dist)
                #print(rem_len)
                print("Transition")
                a = float(prev_speed)*(float(cur_time) - float(prev_time)) + 0.5 * ((float(cur_speed) - float(prev_speed))/(float(cur_time) - float(prev_time)))*(float(cur_time) - float(prev_time))*(float(cur_time) - float(prev_time))
                prev_road_id = cur_road_id
                cur_road_id = str(0)
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,cur_road_id) 
                #if (abs(dist - (cur_speed*(float(cur_time) - float(prev_time)))) > prev_speed):
                if (dist > 2*a): 
                    #a < prev_speed):
                    print("Error")
 
        elif len(eligible_road) == 1:
            #First Entry
            if (float(self.Vehicle_Data[index][1]) == 0) and (float(self.Vehicle_Data[index][2]) == 0) and (float(self.Vehicle_Data[index][3]) == 0):
                #flag_authentic = True
                print("FirstEntry")
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(eligible_road[0]))
            else:
                if (str(cur_road_id) == str(eligible_road[0])):
                    #print("Hello World")
                    ind1 = self.Edge_Name.index(str(eligible_road[0]))
                    f1 = False
                    c1 = 0
                    lc1 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind1]))):
                        if ((abs(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)) <= 0.00005)):
                            #and (abs(float(self.Road_Data_List[ind1][c1][2]) - float(prev_angle)) <= 0.005)):
                            f1 = True
                            lc1 = c1
                        c1 = c1 + 1
                    
                    ind2 = self.Edge_Name.index(str(cur_road_id))
                    f1 = False
                    c1 = 0
                    lc2 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind2]))):
                        if ((abs(float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y)) <= 0.00005)):
                        # and (abs(float(self.Road_Data_List[ind2][c1][2]) - float(cur_angle)) <= 0.005)):
                            f1 = True
                            lc2 = c1
                        c1 = c1 + 1
                    #a = 13.89 * (cur_time - prev_time)
                    a = float(prev_speed)*(float(cur_time) - float(prev_time)) + 0.5 * ((float(cur_speed) - float(prev_speed))/(float(cur_time) - float(prev_time)))*(float(cur_time) - float(prev_time))*(float(cur_time) - float(prev_time))
                    #print(a)
                    error = a - abs(lc1 - lc2)
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,cur_road_id,str(eligible_road[0]))
                    if (abs(error) > a):
                        flag_authentic = True
                        #print("Cur_Speed " + str(cur_speed))
                        #print("Error " + str(error))
                    else:
                        flag_authentic = False
                        print("Error")

                    prev_road_id = cur_road_id
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(eligible_road[0]))
                    print("Next Entry")

                else:
                    #Check for junctions and continue on the new edge
                    if (str(cur_road_id) == str(0)):
                        #Passed through junction
                        present_road_id = str(eligible_road[0])
                        ind1 = self.Edge_Name.index(str(eligible_road[0]))
                        f1 = False
                        c1 = 0
                        lc1 = -1
                        while ((f1 == False) and (c1 < len(self.Road_Data_List[ind1]))):
                            if ((abs(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)) <= 0.00005)):
                                #and (abs(float(self.Road_Data_List[ind1][c1][2]) - float(prev_angle)) <= 0.005)):
                                f1 = True
                                lc1 = c1
                            c1 = c1 + 1
                        length = len(self.Road_Data_List[ind1])
                        print("LC1 " + str(lc1))
                        if (length - lc1) <= lc1:
                            traveled = lc1
                        else:
                            traveled = length - lc1
                        
                        if ((self.Edge_Relation[str(prev_road_id) + "_" + str(present_road_id)] == 1) or (self.Edge_Relation[str(present_road_id) + "_" + str(prev_road_id)] == 1)):
                            found = False
                            i = 0
                            while ((i < len(self.Edge_Junc)) and (found == False)):
                                if (str(self.Edge_Junc[i][0]) == str(present_road_id)):
                                    found = True
                                    print("Hi There")
                                    j1 = self.Edge_Junc[i][1]
                                    j2 = self.Edge_Junc[i][2]
                                    j = 0
                                    while (j < len(self.Junction_Details)):
                                        if (str(self.Junction_Details[j][0]) == str(j1)):
                                            j1_x = self.Junction_Details[j][1]
                                            j1_y = self.Junction_Details[j][2]
                                        j = j + 1
                                    j = 0
                                    while (j < len(self.Junction_Details)):
                                        if (str(self.Junction_Details[j][0]) == str(j2)):
                                            j2_x = self.Junction_Details[j][1]
                                            j2_y = self.Junction_Details[j][2]
                                        j = j + 1
                                    if ((abs(float(cur_pos_x) - float(j1_x))) > (abs(float(cur_pos_x) - float(j2_x))) and (abs(float(cur_pos_y) - float(j1_y))) > (abs(float(cur_pos_y) - float(j2_y)))):
                                        junc = str(self.Edge_Junc[i][2])
                                        j_x = j2_x
                                        j_y = j2_y
                                    else:
                                        junc = str(self.Edge_Junc[i][1])
                                        j_x = j1_x
                                        j_y = j1_y
                                i = i + 1         
                            
                            if (found == False):
                                print("Error")
                            else:
                                a = float(prev_speed)*(float(cur_time) - float(prev_time)) + 0.5 * ((float(cur_speed) - float(prev_speed))/(float(cur_time) - float(prev_time)))*(float(cur_time) - float(prev_time))*(float(cur_time) - float(prev_time))
                                if (traveled > a):
                                    print("Error")
                                else:
                                    cur_road_id = present_road_id
                                    prev_road_id = cur_road_id
                                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(eligible_road[0]))
                    

    
        return error  
                
    def Edge_Junc_Rel(self,f,g):
        temp = []
        #Unique Junction Names
        for lines in f:
            lines = lines.strip("\n")
            for words in lines:
                words = lines.split(" ")
            temp.append(words)
            self.Edge_Length[str(words[0])] = str(words[3])
            if str(words[0]) in str(self.Edge_Name):
                self.Edge_Junc.append((str(words[0]),str(words[1]),str(words[2])))
                if str(words[1]) not in self.Junction_Name:
                    self.Junction_Name.append(str(words[1]))
                if str(words[2]) not in self.Junction_Name:
                    self.Junction_Name.append(str(words[2]))         
        f.close()

        #Store the details of Junction <ID and Co-Ordinates>
        for lines in g:
            lines = lines.strip("\n")
            for words in lines:
                words = lines.split(" ")
            self.Node_Details.append(words)
            self.Junction_Details.append((str(words[0]),str(words[1]),str(words[2])))

        #Range of Edges
        for i in range(0,len(temp)):
            e_id = str(temp[i][0])
            jstart = str(temp[i][1])
            jend = str(temp[i][2])
            for j in range(0,len(self.Node_Details)):
                if jstart == str(self.Node_Details[j][0]):
                    self.Edge_Start_Lat[str(e_id)] = str(self.Node_Details[j][1])
                    self.Edge_Start_Long[str(e_id)] = str(self.Node_Details[j][2])
                if jend == str(self.Node_Details[j][0]):
                    self.Edge_End_Lat[str(e_id)] = str(self.Node_Details[j][1])
                    self.Edge_End_Long[str(e_id)] = str(self.Node_Details[j][2])
            
        #Dictionary for Edges to store details of Road Connectivity
        for i in range(0,len(temp)-1):
            for j in range(i+1,len(temp)):
                if temp[i][1] == temp[j][2]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                elif temp[i][2] == temp[j][1]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                elif temp[i][1] == temp[j][1]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                elif temp[i][2] == temp[j][2]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                else:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 0


class Channel:
    def __init__(self, chan_id):
        self.chan_id = chan_id
        self.devicelist = []
        self.state = 0

    def attach_dev(self, dev_id):
        self.devicelist.append(dev_id)

    def detach_dev(self, dev_id):
        index = -1
        for i in range(0,len(self.devicelist)):
            if dev_id == self.devicelist[i]:
                index = i
        if index > -1:
            del self.devicelist[index]
            
    def display_chan(self):
        for i in range(0,len(self.devicelist)):
            print(self.devicelist[i])
    
    def check_chan_state(self):
        return self.state
    
    def set_state(self,val):
        self.state = val
    
    def send_data(self,sender,receiver): 
        print("Transmitting data " + str(sender.data_packet) + " from Node " + str(sender.id) + " to Server " + str(receiver.id))
        receiver.data_packet = sender.data_packet   


def main():
    #Initialization of Server
    Serv = Server(1000)
    Attacker = Node(-1)
    Svc_Chan = Channel(1)
    Svc_Chan.attach_dev(Serv.get_node_id())
    Svc_Chan.attach_dev(Attacker.get_node_id())

    print("Enter number of nodes")
    no = input()
    
    Nodes = []
    for i in range(0,int(no)):
        print("Enter Node ID")
        id = input()
        N = Node(id)
        Nodes.append(N)  
        key = Serv.initialize(id)
        Svc_Chan.attach_dev(Nodes[i].get_node_id())
        N.set_key(key)
    
    print("Enter the number of roads")
    num_of_edges = input()

    for i in range(0,int(num_of_edges)):
        Serv.Road_Data_List.append([])

    f1 = open("Road_Trace_114667396#0_1.txt","r")
    f2 = open("Road_Trace_169195795#2_1.txt","r")
    f3 = open("Road_Trace_169195795#0_1.txt","r")
    f4 = open("Road_Trace_1113726463_1.txt","r")
    f5 = open("Road_Trace_1077923225#0_1.txt","r")
    f6 = open("Road_Trace_1126237668#0_1.txt","r")
    f7 = open("Road_Trace_340498982#0_1.txt","r")
    f8 = open("Road_Trace_169195795#3_1.txt","r")

    #Read Each Road Data
    Serv.read_RoadData(f1,0)
    Serv.read_RoadData(f2,1)
    Serv.read_RoadData(f3,2)
    Serv.read_RoadData(f4,3)
    Serv.read_RoadData(f5,4)
    Serv.read_RoadData(f6,5)
    Serv.read_RoadData(f7,6)
    Serv.read_RoadData(f8,7)
    
    #Edge Details, Edge ID, Start Junction and End Junction, length of the road
    f = open("Edge_Details1.txt","r")
    g = open("Node1.txt","r")
    Serv.Edge_Junc_Rel(f,g)
    
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
    
    #Communication starts between cloud server and the vehicle
    simulation_time = 1000
    count = 0

    Waiting_Q = []

    while count < simulation_time:
        for i in range(0,len(Nodes)):
            if (count == 0) or ((Nodes[i].status == 0) and ((datetime.now().microsecond - Nodes[i].time) >= 100)):
                if Nodes[i] not in Waiting_Q:
                    #print(datetime.now().microsecond)
                    Waiting_Q.append(Nodes[i])
                    Nodes[i].status = 0

        #print(datetime.now().microsecond)
        #print(Waiting_Q)
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

            



            N.time = datetime.now().microsecond
            N.status = 0

        count = count + 1

if __name__ == '__main__':
        main()
