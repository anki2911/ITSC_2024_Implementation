        #One or multiple road ids in the eligible list
        if len(eligible_road) > 0:
            #First Entry
            if (float(self.Vehicle_Data[index][1]) == 0) and (float(self.Vehicle_Data[index][2]) == 0) and (float(self.Vehicle_Data[index][3]) == 0):
                print("FirstEntry")
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                return (0)
            
            #Later Entries
            else:
                found = 0
                d_min = 100
                index_min = -1
                min_d = 0
                u = 0   

                while (found == 0) and (u < len(eligible_road)):
                    ind = self.Edge_Name.index(str(eligible_road[u]))
                    c1 = 0
                    lc1 = -1
                    dist_list = []
                    while (c1 < len(self.Road_Data_List[ind])): 
                        d = math.sqrt((float(cur_pos_x)-float(self.Road_Data_List[ind][c1][0]))*(float(cur_pos_x)-float(self.Road_Data_List[ind][c1][0])) + (float(cur_pos_y)-float(self.Road_Data_List[ind][c1][1]))*(float(cur_pos_y)-float(self.Road_Data_List[ind][c1][1])))
                        dist_list.append(float(d))
                        c1 = c1 + 1
                    min_d = min(dist_list)
                    print(min_d)
                    
                    if (float(min_d) < float(d_min)):
                        if ((prev_road_id == -1) and (cur_road_id == -1)):
                            d_min = min_d
                            index_min = u
                            Road_Cur = str(eligible_road[u])
                        else:
                            if ((str(cur_road_id)+"_"+str(eligible_road[u])) in self.Edge_Relation.keys()) and (((self.Edge_Relation[str(cur_road_id)+"_"+str(eligible_road[u])] == 1) or (self.Edge_Relation[str(eligible_road[u])+"_"+str(cur_road_id)] == 1))):
                                d_min = min_d
                                index_min = u
                                Road_Cur = str(eligible_road[u])
                            elif ((str(prev_road_id)+"_"+str(eligible_road[u])) in self.Edge_Relation.keys()) and (((self.Edge_Relation[str(prev_road_id)+"_"+str(eligible_road[u])] == 1) or (self.Edge_Relation[str(eligible_road[u])+"_"+str(prev_road_id)] == 1))):
                                d_min = min_d
                                index_min = u
                                Road_Cur = str(eligible_road[u])
                            else:
                                if (u == len(eligible_road) - 1):
                                    eligible_road.clear()
                                    Road_Cur = "0"  
                                    

                    dist_list.clear()
                    u = u + 1

                
                #if (str(cur_road_id) != -1) and (str(eligible_road[u]) != -1) and (str(cur_road_id) in eligible_road):
                if (str(cur_road_id) != -1) and (str(cur_road_id) in eligible_road):
                    index_min = eligible_road.index(str(cur_road_id))
                    found = 1
                    Road_Cur = str(cur_road_id)
                    print("Found")        
                    if (float(min_d) < float(d_min)):                        
                        if ((prev_road_id == -1) and (cur_road_id == -1)):
                            d_min = min_d
                            index_min = u
                            Road_Cur = str(eligible_road[u])
                        else:
                            if ((str(cur_road_id)+"_"+str(eligible_road[u])) in self.Edge_Relation.keys()) and (((self.Edge_Relation[str(cur_road_id)+"_"+str(eligible_road[u])] == 1) or (self.Edge_Relation[str(eligible_road[u])+"_"+str(cur_road_id)] == 1))):
                                d_min = min_d
                                index_min = u
                                Road_Cur = str(eligible_road[u])
                            elif ((str(prev_road_id)+"_"+str(eligible_road[u])) in self.Edge_Relation.keys()) and (((self.Edge_Relation[str(prev_road_id)+"_"+str(eligible_road[u])] == 1) or (self.Edge_Relation[str(eligible_road[u])+"_"+str(prev_road_id)] == 1))):
                                d_min = min_d
                                index_min = u
                                Road_Cur = str(eligible_road[u])
                            elif (str(cur_road_id) == str(eligible_road[u])):
                                d_min = min_d
                                index_min = u
                                Road_Cur = str(eligible_road[u])
                            else:
                                if (u == len(eligible_road) - 1):
                                    eligible_road.clear()
                                    Road_Cur = "0"  
              
                    u = u + 1
                    
            print(Road_Cur)

        if len(eligible_road) > 0:   
            #First Entry
            if (float(self.Vehicle_Data[index][1]) == 0) and (float(self.Vehicle_Data[index][2]) == 0) and (float(self.Vehicle_Data[index][3]) == 0):
                print("FirstEntry")
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                return (0)
            else:
                if (str(cur_road_id) == str(Road_Cur)):
                    print("On the same road")
                    #Index on Road 1
                    ind1 = self.Edge_Name.index(str(Road_Cur))
                    ind2 = self.Edge_Name.index(str(cur_road_id))
                    c1 = 0
                    lc1 = -1
                    lc2 = -1
                    min_dist1 = 1000
                    min_dist2 = 1000

                    while (c1 < len(self.Road_Data_List[ind1])):
                        d1 = math.sqrt((float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x))*(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) + (float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y))*(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)))
                        if d1 <= min_dist1:
                            min_dist1 = d1
                            lc1 = c1

                        d2 = math.sqrt((float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x))*(float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x)) + (float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y))*(float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y)))
                        if d2 <= min_dist2:
                            min_dist2 = d2
                            lc2 = c1
                        
                        c1 = c1 + 1
                    
                    print("LC1 and LC2 " + str(lc1) + " " + str(lc2))
                    dist_travelled = abs(lc2 - lc1)
                    prev_road_id = cur_road_id
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                    print("Distance " + str(dist_travelled))
                    #print("Next Entry")

                    if dist_travelled > a:
                        print("Error")
                        flag_authentic = False
                        return (dist_travelled)
                    else:
                        print("No Error")
                        flag_authentic = True
                        return (dist_travelled)
                
                #From a road to another road
                elif (str(cur_road_id) != "0") and (str(Road_Cur) != "0") and (str(cur_road_id) != str(Road_Cur)):
                    print("From a road to another road")
                    #Index on Road 1
                    ind1 = self.Edge_Name.index(str(cur_road_id))
                    c1 = 0
                    lc1 = -1
                    min_dist1 = 1000
                    while (c1 < len(self.Road_Data_List[ind1])):
                        d1 = math.sqrt((float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x))*(float(self.Road_Data_List[ind1][c1][0]) - float(prev_pos_x)) + (float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y))*(float(self.Road_Data_List[ind1][c1][1]) - float(prev_pos_y)))
                        if d1 < min_dist1:
                            min_dist1 = d1
                            lc1 = c1
                        c1 = c1 + 1
                    
                    #Index on Road 2
                    #print("Cur_Road_ID " + str(cur_road_id))
                    ind2 = self.Edge_Name.index(str(Road_Cur))
                    c1 = 0
                    lc2 = -1
                    min_dist1 = 1000
                    while (c1 < len(self.Road_Data_List[ind2])):
                        d1 = math.sqrt((float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x))*(float(self.Road_Data_List[ind2][c1][0]) - float(cur_pos_x)) + (float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y))*(float(self.Road_Data_List[ind2][c1][1]) - float(cur_pos_y)))
                        if d1 < min_dist1:
                            min_dist1 = d1
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
                        #if (abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][0][0]))) < abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][len1-1][0])))) and (abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][0][1]))) < abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][len1-1][1])))):
                        #    r1 = lc1
                        #else:
                        #    r1 = len1 - lc1

                        #if (abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][0][0]))) < abs((float(cur_pos_x) - float(self.Road_Data_List[ind2][len2-1][0])))) and (abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][0][1]))) < abs((float(cur_pos_y) - float(self.Road_Data_List[ind2][len2-1][1])))):
                        #    r2 = lc2
                        #else:
                        #    r2 = len2 - lc2
                        
                        if (lc1) < (len1 - lc1):
                            r1 = lc1
                        else:
                            r1 = len1 - lc1
                        print(r1)
                        
                        if (lc2) < (len2 - lc2):
                            r2 = lc2
                        else:
                            r2 = len2 - lc2
                        print(r2)

                        if r1 + r2 <= a:
                            flag_authentic = True
                            print("No Error")
                            return (r1 + r2)
                        else:
                            flag_authentic = False
                            print("Error")
                            return (r1 + r2)   

                #From a junction to a road    
                elif (str(cur_road_id) == str(0)):
                    print("From a junction to a road")
                    ind1 = self.Edge_Name.index(str(Road_Cur))
                    c1 = 0
                    lc2 = -1
                    min_dist1 = 1000
                    while (c1 < len(self.Road_Data_List[ind1])):
                        d1 = math.sqrt((float(self.Road_Data_List[ind1][c1][0]) - float(cur_pos_x))*(float(self.Road_Data_List[ind1][c1][0]) - float(cur_pos_x)) + (float(self.Road_Data_List[ind1][c1][1]) - float(cur_pos_y))*(float(self.Road_Data_List[ind1][c1][1]) - float(cur_pos_y)))
                        if d1 < min_dist1:
                            min_dist1 = d1
                            lc2 = c1
                        c1 = c1 + 1
                    
                    len1 = len(self.Road_Data_List[ind1])
                    
                    #prev_road_id = cur_road_id
                    cur_road_id = str(Road_Cur)
                    prev_road_id = cur_road_id
                    self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,str(Road_Cur))
                    #print("Next Entry")       
            
                    #Find junction co-ordinate between prev_road_id and eligible_road_id
                    #Find distance lc1 from the junction
                    
                    #if (abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][0][0]))) < abs((float(prev_pos_x) - float(self.Road_Data_List[ind1][len1-1][0])))) and (abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][0][1]))) < abs((float(prev_pos_y) - float(self.Road_Data_List[ind1][len1-1][1])))):
                    #    r1 = lc1
                    #else:
                    #    r1 = len1 - lc1

                    if (lc1) < (len1 - lc1):
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

        #From a road to a junction
        elif len(eligible_road) == 0: 
            print("From a road to a junction")
            if str(cur_road_id) != str(0):
                ind2 = self.Edge_Name.index(str(cur_road_id))
                prev_road_id = cur_road_id
            else:
                #prev_road_id = cur_road_id
                cur_road_id = str(0)
                self.Vehicle_Data[index] = (id,cur_pos_x,cur_pos_y,cur_angle,cur_speed,cur_time,prev_road_id,cur_road_id)
                print("No Error")
                return (0)
            
            len2 = len(self.Road_Data_List[ind2])
            c1 = 0
            lc2 = -1
            min_dist1 = 1000
            while (c1 < len(self.Road_Data_List[ind2])):
                d1 = math.sqrt((float(self.Road_Data_List[ind2][c1][0]) - float(prev_pos_x))*(float(self.Road_Data_List[ind2][c1][0]) - float(prev_pos_x)) + (float(self.Road_Data_List[ind2][c1][1]) - float(prev_pos_y))*(float(self.Road_Data_List[ind2][c1][1]) - float(prev_pos_y)))
                if d1 < min_dist1:
                    min_dist1 = d1
                    lc2 = c1
                c1 = c1 + 1

            
            if (lc2 < (len2 - lc2)):
                r2 = lc2
            else:
                r2 = (len2 - lc2)
            #print("R2" + str(r2))
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
         


        




        return 0
        