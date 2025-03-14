import random
import math

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
        #Read Each Road Data, min and max latitude and longitude
        min_lat = 91
        max_lat = 0
        min_lon = 181
        max_lon = 0
        i = 0
        for lines in f:
            lines = lines.strip("\n")
            #print(lines)
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
                    self.Edge_Relation[str(temp[j][0])+"_"+str(temp[i][0])] = 1
                elif temp[i][2] == temp[j][1]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                    self.Edge_Relation[str(temp[j][0])+"_"+str(temp[i][0])] = 1
                elif temp[i][1] == temp[j][1]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                    self.Edge_Relation[str(temp[j][0])+"_"+str(temp[i][0])] = 1
                elif temp[i][2] == temp[j][2]:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 1
                    self.Edge_Relation[str(temp[j][0])+"_"+str(temp[i][0])] = 1
                else:
                    self.Edge_Relation[str(temp[i][0])+"_"+str(temp[j][0])] = 0
                    self.Edge_Relation[str(temp[j][0])+"_"+str(temp[i][0])] = 0
    
    
    def estimate_location(self):
        data = self.data_packet.split('_')
        flag_authentic = False
        id = data[0]
        i = 0
        index = -1
        found = False
        error = 0
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
        else:
            print("Not Found")
            return 0
        
        print("Previous Road ID " + str(prev_road_id))
        print("Current Road ID " + str(cur_road_id))

        a = 34 * (float(cur_time) - float(prev_time))
        eligible_road = []
        c1 = 0
        lc1 = -1

        #Find the road id where the vehicle belongs to
        for k in range(0,len(self.Road_property)):
            if ((float(data[1]) >= float(self.Road_property[k][0])) and (float(data[1]) <= float(self.Road_property[k][1])) and (float(data[2]) >= float(self.Road_property[k][2])) and (float(data[2]) <= float(self.Road_property[k][3]))):
                eligible_road.append(self.Edge_Name[k]) 
                f1 = False
                c1 = 0
                lc1 = -1
        Road_Cur = "0"
        print(eligible_road)
        #Currently on a road
        if len(eligible_road) > 0:
            if len(eligible_road) == 1:
                Road_Cur = str(eligible_road[0])
            elif len(eligible_road) > 1:
                #print(eligible_road)
                #if str(cur_road_id) == '0':
                found = 0
                for u in range(len(eligible_road)):
                    if str(eligible_road[u]) != str(prev_road_id):
                        if str(prev_road_id) != '0':
                            if ((self.Edge_Relation[str(eligible_road[u])+"_"+str(prev_road_id)] == 1) or (self.Edge_Relation[str(prev_road_id)+"_"+str(eligible_road[u])] == 1)):
                                Road_Cur = str(eligible_road[u])
                                found = 1
                if found == 0:
                    d_min = 100
                    x_min = 0
                    y_min = 0
                    index_min = u
                    for u in range(len(eligible_road)):
                        d1 = math.sqrt((cur_pos_x - float(self.Edge_Start_Lat[str(eligible_road[u])]))*(cur_pos_x - float(self.Edge_Start_Lat[str(eligible_road[u])])) + (cur_pos_y - float(self.Edge_Start_Long[str(eligible_road[u])]))*(cur_pos_y - float(self.Edge_Start_Long[str(eligible_road[u])])))
                        d2 = math.sqrt((cur_pos_x - float(self.Edge_End_Lat[str(eligible_road[u])]))*(cur_pos_x - float(self.Edge_End_Lat[str(eligible_road[u])])) + (cur_pos_y - float(self.Edge_Start_Long[str(eligible_road[u])]))*(cur_pos_y - float(self.Edge_Start_Long[str(eligible_road[u])])))
                        if d1 < d2:
                            t1 = d1
                            if d_min > d1:
                                d_min = d1
                                x_min = self.Edge_Start_Lat[str(eligible_road[u])]
                                y_min = self.Edge_Start_Long[str(eligible_road[u])]
                                index_min = u
                                Road_Cur = eligible_road[u]
                        else:
                            t1 = d2
                            if d_min > d2:
                                d_min = d2
                                x_min = self.Edge_End_Lat[str(eligible_road[u])]
                                y_min = self.Edge_End_Long[str(eligible_road[u])]
                                index_min = u
                                Road_Cur = eligible_road[u]
                    
                #else:    
                #    Road_Cur = str(cur_road_id)
            
            print(Road_Cur)
        
        #elif len(eligible_road) == 1:
            #First Entry
            if (float(self.Vehicle_Data[index][1]) == 0) and (float(self.Vehicle_Data[index][2]) == 0) and (float(self.Vehicle_Data[index][3]) == 0):
                print("FirstEntry")
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                return (0)
            else:
                #On the same road
                if (str(cur_road_id) == str(Road_Cur)):
                    print("On the same road")
                    #Index on Road 1
                    ind1 = self.Edge_Name.index(str(Road_Cur))
                    f1 = False
                    c1 = 0
                    lc1 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind1]))):    
                        if ((abs(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) <= 0.00001) and (abs(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)) <= 0.00001)):
                            f1 = True
                            lc1 = c1
                        c1 = c1 + 1
                    #print(lc1)
                    #Index on Road 2
                    ind2 = self.Edge_Name.index(str(cur_road_id))
                    f1 = False
                    c1 = 0
                    lc2 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind2]))):
                        if ((abs(float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x)) <= 0.00001) and (abs(float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y)) <= 0.00001)):
                            f1 = True
                            lc2 = c1
                        c1 = c1 + 1
                    #print(lc2)
                    dist_travelled = abs(lc2 - lc1)
                    #print(dist_travelled)
                    prev_road_id = cur_road_id
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                    #print("Next Entry")

                    if dist_travelled > a:
                        print("Error")
                        flag_authentic = False
                        return (dist_travelled)
                    else:
                        print("No Error")
                        flag_authentic = True
                        return (dist_travelled)

                #From a junction to a road    
                elif (str(cur_road_id) == str(0)):
                    print("From a junction to a road")
                    ind1 = self.Edge_Name.index(str(Road_Cur))
                    f1 = False
                    c1 = 0
                    lc1 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind1]))):    
                        if ((abs(float(self.Road_Data_List[ind1][c1][0]) - float(cur_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind1][c1][1]) - float(cur_pos_y)) <= 0.00005)):
                            f1 = True
                            lc1 = c1
                        c1 = c1 + 1
                    len1 = len(self.Road_Data_List[ind1])
                    
                    prev_road_id = cur_road_id
                    #cur_road_id = str(Road_Cur)
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                    #print("Next Entry")       
            
                    #Find junction co-ordinate between prev_road_id and eligible_road_id
                    #Find distance lc1 from the junction
                    if (abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][0][0]))) < abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][len1-1][0])))) and (abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][0][1]))) < abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][len1-1][1])))):
                        r1 = lc1
                    else:
                        r1 = len1 - lc1
                    
                    #if (lc1 < (len1 - lc1)):
                    #    r1 = lc1
                    #else:
                    #    r1 = (len1 - lc1)

                    if (r1 <= a):
                        flag_authentic = True
                        print("No Error")
                        return (r1)
                    else:
                        flag_authentic = False
                        print("Error")
                        return (r1)
            

                #From a road to another road
                elif (str(cur_road_id) != str(Road_Cur)):
                    print("From a road to another road")
                    #Index on Road 1
                    ind1 = self.Edge_Name.index(str(Road_Cur))
                    f1 = False
                    c1 = 0
                    lc1 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind1]))):    
                        if ((abs(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)) <= 0.00005)):
                            f1 = True
                            lc1 = c1
                        c1 = c1 + 1
                
                    #Index on Road 2
                    #print("Cur_Road_ID " + str(cur_road_id))
                    ind2 = self.Edge_Name.index(str(cur_road_id))
                    f1 = False
                    c1 = 0
                    lc2 = -1
                    while ((f1 == False) and (c1 < len(self.Road_Data_List[ind2]))):
                        if ((abs(float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y)) <= 0.00005)):
                            f1 = True
                            lc2 = c1
                        c1 = c1 + 1

                    len1 = len(self.Road_Data_List[ind1])
                    len2 = len(self.Road_Data_List[ind2])

                    prev_road_id = cur_road_id
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                    #print("Next Entry")
                
                    #Find distance between lc1 and end point and lc2 and end point
                    #Sum them and check if its less than a
                    if ((self.Edge_Relation[str(cur_road_id)+"_"+str(Road_Cur)] == 1) or (self.Edge_Relation[str(Road_Cur)+"_"+str(cur_road_id)] == 1)):
                        if (abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][0][0]))) < abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][len1-1][0])))) and (abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][0][1]))) < abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][len1-1][1])))):
                            r1 = lc1
                        else:
                            r1 = len1 - lc1

                        if (abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][0][0]))) < abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][len2-1][0])))) and (abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][0][1]))) < abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][len2-1][1])))):
                            r2 = lc2
                        else:
                            r2 = len2 - lc2
                        
                        if r1 + r2 <= a:
                            flag_authentic = True
                            print("No Error")
                            return (r1 + r2)
                        else:
                            flag_authentic = False
                            print("Error")
                            return (r1 + r2)      

                
                    #if ((self.Edge_Relation[str(cur_road_id)+"_"+str(Road_Cur)] == 1) or (self.Edge_Relation[str(Road_Cur)+"_"+str(cur_road_id)] == 1)):
                    #    if (lc1 < (len1 - lc1)):
                    #        r1 = lc1
                    #    else:
                    #        r1 = len1 - lc1
                    #    if (lc2 < (len2 - lc2)):
                    #        r2 = lc2
                    #    else:
                    #        r2 = (len2 - lc2)

                        
        #From a road to a junction
        elif len(eligible_road) == 0: 
            print("From a road to a junction")
            if str(cur_road_id) != str(0):
                ind2 = self.Edge_Name.index(str(cur_road_id))
            else:
                #prev_road_id = cur_road_id
                cur_road_id = str(0)
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,cur_road_id)
                print("No Error")
                return (0)
            
            len2 = len(self.Road_Data_List[ind2])
            f1 = False
            c1 = 0
            lc2 = -1
            while ((f1 == False) and (c1 < len(self.Road_Data_List[ind2]))):
                if ((abs(float(self.Road_Data_List[ind2][c1][0]) - float(prev_pos_x)) <= 0.00005) and (abs(float(self.Road_Data_List[ind2][c1][1]) - float(prev_pos_y)) <= 0.00005)):
                    f1 = True
                    lc2 = c1
                c1 = c1 + 1

            #Find co-ordinate of the end point and check the distance between lc1 and end point
            if (abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][0][0]))) < abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][len2-1][0])))) and (abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][0][1]))) < abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][len2-1][1])))):
                r2 = lc2
            else:
                r2 = len2 - lc2
            #print("R2 " + str(r2))

            #if (lc2 < (len2 - lc2)):
            #    r2 = lc2
            #else:
            #    r2 = (len2 - lc2)

            found = 0
            for i in range(0,len(self.Edge_Junc)):
                if (str(self.Edge_Junc[i][0]) == str(cur_road_id)) and (found == 0):
                    found = 1
                    end_1 = self.Edge_Junc[i][1]
                    for j in range(0,len(self.Junction_Details)):
                        if str(self.Junction_Details[j][0]) == str(end_1):
                            x1 = self.Junction_Details[j][1]
                            y1 = self.Junction_Details[j][2]
                    end_2 = self.Edge_Junc[i][2]
                    for j in range(0,len(self.Junction_Details)):
                        if str(self.Junction_Details[j][0]) == str(end_2):
                            x2 = self.Junction_Details[j][1]
                            y2 = self.Junction_Details[j][2]
                    
                    if (abs(float(cur_pos_x) - float(x1)) < abs(float(cur_pos_x) - float(x2))) and (abs(float(cur_pos_y) - float(y1)) < abs(float(cur_pos_y) - float(y2))):
                        cur_junc = end_1
                    else:
                        cur_junc = end_2

            #print(prev_road_id)
            #prev_road_id = cur_road_id
            cur_road_id = str(0)
            self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,cur_road_id)
            #print("Next Entry")

            if ((found == 1) and (r2 <= a)):
                flag_authentic = True
                print("No Error")
                return (r2)
            else:
                flag_authentic = False
                print("Error")
                return (r2)
            
            