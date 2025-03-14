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
