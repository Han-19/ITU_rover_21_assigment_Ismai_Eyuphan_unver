import numpy as np
import rospy 
from std_msgs.msg import String



class my_generator():
    def __init__(self):
    
        rospy.init_node("encoder_sub_node")
        self.last_data =0
        self.pub_16 = rospy.Publisher('/position/drive', String, queue_size = 10)
        self.pub_24 = rospy.Publisher('/position/robotic_arm', String, queue_size = 10)


        self.generator_and_listener()



    def data_read(self,data,last_data):
    	if self.last_data != data:
			if data.startswith('A') and data.endswith('B'):
				data= data[1:-1]
				if len(data)==16:
					new_data= (((data[0]),(data[1:4])),
							((data[4]),(data[5:8])),
							((data[8]),(data[9:12])),
							((data[12]),(data[13:])))
					
				else:
					new_data= (((data[0]),(data[1:4])),
							((data[4]),(data[5:8])),
							((data[8]),(data[9:12])),
							((data[12]),(data[13:16])),
							((data[16]),(data[17:20])),
							((data[20]),(data[21:])))
				return new_data
			else:
				
				return "CORRUPTED DATA !!!  " #not publishing any corrupted or duplicated data
                
    	else:
            return 'duplicate'
            

    def publisher(self,data):
        my_data = self.data_read(data.data,self.last_data)
        if my_data !='duplicate' and my_data !='CORRUPTED DATA !!!  ':
            if len(my_data)==4:
    			MY_DATA = "{} {:03} {} {:03} {} {:03} {} {:03}".format(my_data[0][0],self.limiter(my_data[0][1]),
												my_data[1][0],self.limiter(my_data[1][1]),
												my_data[2][0],self.limiter(my_data[2][1]),
												my_data[3][0],self.limiter(my_data[3][1]))
    			self.pub_16.publish(MY_DATA)

            elif len(my_data)==6:
			    MY_DATA = "{} {:03} {} {:03} {} {:03} {} {:03} {} {:03} {} {:03}".format(my_data[0][0],self.limiter(my_data[0][1]),
														                                 my_data[1][0],self.limiter(my_data[1][1]),
														                                 my_data[2][0],self.limiter(my_data[2][1]),
														                                 my_data[3][0],self.limiter(my_data[3][1]),
														                                 my_data[4][0],self.limiter(my_data[4][1]),
														                                 my_data[5][0],self.limiter(my_data[5][1]))  			
            if len(MY_DATA)== 23:
                self.pub_16.publish(MY_DATA)
            elif len(MY_DATA)== 35:
                self.pub_24.publish(MY_DATA)
            self.last_data = data.data

    def limiter(self,number):
        number = int(number)
    	if number > 255:
		    number =255
    	elif number < -255:
			number = -255
    	return number
		

    def generator_and_listener(self):
        rate = rospy.Rate(2)
    	while not rospy.is_shutdown():
			rospy.Subscriber("/serial/drive", String, self.publisher,queue_size=3)
			rospy.Subscriber("/serial/robotic_arm", String, self.publisher,queue_size=3)
			rate.sleep()

        rospy.spin()
my_generator()
