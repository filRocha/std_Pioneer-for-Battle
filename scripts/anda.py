#!/usr/bin/env python
import rospy
import roslib
#import sys

#imports de mensagens
from pioneer_sumo.msg import *
#from pioneer_sumo.msg import arma
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class ControleRobo():

	#Metodo criador da classe
	def __init__(self,num_robo):
		
		#definindo variaveis
		self.sensorTras1 = 0
		self.sensorFrente1 = 0
		self.sensorTras2 = 0
		self.sensorFrente2 = 0

		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		#rospy.Subscriber('joy', Joy, self.joy_callback)
		rospy.Subscriber('/vrep_ros_interface/robo'+str(num_robo)+'/sensoresChao',sensores_chao,self.sensorChaoCallback)
		#rospy.spin()

		#Iniciio do comando do robo
		comando=motores()
		while not rospy.is_shutdown():

			if self.sensorFrente1 > 0.08 or self.sensorFrente2 > 0.08:
				comando.motEsquerdo=1
				comando.motDireito=1
			else:
				comando.motEsquerdo=-1
				comando.motDireito=-1

			self.pub.publish(comando)

	#Funcao que le o sensor do chao
	def sensorChaoCallback(self,data):
		self.sensorTras1 = data.dist_tras1
		self.sensorFrente1 = data.dist_frente1
		self.sensorTras2 = data.dist_tras2
		self.sensorFrente2 = data.dist_frente2




#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('anda', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(1)
	except rospy.ROSInterruptException: pass
