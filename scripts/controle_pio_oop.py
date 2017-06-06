#!/usr/bin/env python
import rospy
import roslib
#import sys

from sensor_msgs.msg import Joy
from pioneer_sumo.msg import *
#from pioneer_sumo.msg import arma
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class PioControlJoy():

	#Metodo criador da classe
	def __init__(self,num_robo):
		
		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		rospy.Subscriber('joy', Joy, self.joy_callback)
		rospy.spin()


	#Funcao de callback do topico do joystick
	def joy_callback(self,data):

		#Recebe o valor do topico e salva em variaveis
		eixo_x = -1*data.axes[0]
		eixo_y = data.axes[1]

		#Cria e adequa a variavel que vai ser enviada no topico
		resp=motores()
		resp.motEsquerdo=eixo_y
		resp.motDireito=eixo_y

		#Publica o valor no topico de controle do motor
		self.pub.publish(resp)



#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('controla_pio', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = PioControlJoy(1)
	except rospy.ROSInterruptException: pass