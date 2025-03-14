class Node:
    def initialize(self, ID):
        self.id = ID
        self.lat = 0
        self.lon = 0
        self.angle = 0
        self.key = 0
        self.status = 0
        self.data_packet = 0
        self.index = 0
        self.step = 0
        #self.time = datetime.now().microsecond
        self.max_speed = 13.89 #50 Km per hour in Singapore
        self.Veh_Data = []
        
    def get_node_id(self):
        return self.id   

    def set_key(self,key):
        self.key = key 
