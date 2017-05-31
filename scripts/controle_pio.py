#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Joy
from pioneer_sumo.msg import arma
from pioneer_sumo.msg import motores
from pioneer_sumo.msg import sensores_chao
from pioneer_sumo.msg import sensores_dist


pub=rospy.Publisher('vrep_ros_interface/robo1/motores', motores, queue_size=1)

def joy_callback(msg):
	eixo_x = -1*msg.axes[0]
	eixo_y = msg.axes[1]

	#rospy.loginfo("Eixo x:" + str(eixo_x) + "  eixo y:" + str(eixo_y))

	resp=motores()
	resp.motEsquerdo=eixo_y
	resp.motDireito=eixo_y

	pub.publish(resp)


def controle_pio():
	
	rospy.init_node('controle_pio', anonymous=True)
	rospy.Subscriber('joy', Joy, joy_callback)
	rospy.spin()

if __name__ == '__main__':
    controle_pio()