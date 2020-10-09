class TIME:
    def __init__(self,seconds):
        self.seconds = seconds
        self.hours = int(self.seconds/3600)
        self.minutes = int((self.seconds-(self.hours*3600))/60)
        self.seconds = self.seconds-(self.hours*3600)-(self.minutes*60)
    
    def print_details(self):
        print("{} : {} : {}".format(self.hours,self.minutes,self.seconds))
        
    def add_object(self,obj):
       new_secs = obj.seconds+self.seconds
       new_mins = obj.minutes+self.minutes
       new_hours = obj.hours+self.hours
       new_mins+= int(new_secs/60)
       new_hours+= int(new_mins/60)
       new_secs = new_secs%60
       new_mins = new_mins%60
       print("answer is {} : {} : {}".format(new_hours , new_mins , new_secs))

sec = int(input())
my_time = TIME(sec)      
my_time.print_details()
my_time2 = TIME(sec)
my_time2.print_details()
my_time2.add_object(my_time)
