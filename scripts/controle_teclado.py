#!/usr/bin/env python
import rospy
import roslib
#import sys

#imports de mensagens
from pioneer_sumo.msg import *
from keyboard.msg import Key
#from pioneer_sumo.msg import arma
#from pioneer_sumo.msg import motores
#from pioneer_sumo.msg import sensores_chao
#from pioneer_sumo.msg import sensores_dist


#Cria a classe do noo para publicar no motor
class ControleRobo():

	#Metodo criador da classe
	def __init__(self,num_robo):
		
		#definindo variaveis
		self.keyUp=0 #273
		self.keyDown=0 #274
		self.keyLeft=0 #276
		self.keyRight=0 #275


		rospy.loginfo("Num Robo "+ str(num_robo))

		self.pub = rospy.Publisher('vrep_ros_interface/robo'+str(num_robo)+'/motores', motores, queue_size=1)
		
		rospy.Subscriber('/keyboard/keydown',Key,self.keyDownCallback)
		rospy.Subscriber('/keyboard/keyup',Key,self.keyUpCallback)

		#rospy.spin()

		#Iniciio do comando do robo
		comando=motores()
		while not rospy.is_shutdown():

			if self.keyUp==1 and self.keyLeft==0 and self.keyRight==0:
				comando.motEsquerdo=1
				comando.motDireito=1
			elif self.keyDown==1 and self.keyLeft==0 and self.keyRight==0:
				comando.motEsquerdo=-1
				comando.motDireito=-1
			elif self.keyUp==1 and self.keyLeft==0 and self.keyRight==1:
				comando.motEsquerdo=1
				comando.motDireito=0.6
			elif self.keyUp==1 and self.keyLeft==1 and self.keyRight==0:
				comando.motEsquerdo=0.6
				comando.motDireito=1
			elif self.keyUp==0 and self.keyLeft==0 and self.keyRight==0:
				comando.motEsquerdo=0
				comando.motDireito=0
			elif self.keyDown==1 and self.keyLeft==0 and self.keyRight==1:
				comando.motEsquerdo=-1
				comando.motDireito=-0.6
			elif self.keyDown==1 and self.keyLeft==1 and self.keyRight==0:
				comando.motEsquerdo=-0.6
				comando.motDireito=-1
			elif self.keyDown==0 and self.keyUp==0 and self.keyLeft==0 and self.keyRight==1:
				comando.motEsquerdo=1
				comando.motDireito=-1
			elif self.keyDown==0 and self.keyUp==0 and self.keyLeft==1 and self.keyRight==0:
				comando.motEsquerdo=-1
				comando.motDireito=1


			self.pub.publish(comando)

	#Funcao que recebe o topico key down
	def keyDownCallback(self,data):
		print(data.code)

		if data.code==273 and self.keyUp==0:
			self.keyUp=1

		if data.code==274 and self.keyDown==0:
			self.keyDown=1

		if data.code==275 and self.keyRight==0:
			self.keyRight=1

		if data.code==276 and self.keyLeft==0:
			self.keyLeft=1


	#Funcao que recebe o topico do key up
	def keyUpCallback(self,data):
		print(data.code)

		if data.code==273 and self.keyUp==1:
			self.keyUp=0

		if data.code==274 and self.keyDown==1:
			self.keyDown=0

		if data.code==275 and self.keyRight==1:
			self.keyRight=0

		if data.code==276 and self.keyLeft==1:
			self.keyLeft=0



#Funcao main que chama a classe criada
if __name__ == '__main__':

	#Inicializa o nosso no com o nome
	rospy.init_node('controle_teclado', anonymous=True)

	#Instancia a classe e entra em um regime de tratamento de eventuais erros
	try:
		obj_no = ControleRobo(1)
	except rospy.ROSInterruptException: pass
