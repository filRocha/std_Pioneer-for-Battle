/* ============= NÓ DE CONTROLE DO ROBO PIONEER ==========================
 *
 * Instituto Tecnológico Vale - Mineração
 * Ouro Preto - Minas Gerais
 *
 * Setembro de 2016
 *
 *
 */

#include "ros/ros.h"
//#include "std_msgs/Float32.h"
#include "sensor_msgs/Joy.h"
#include "pioneer_sumo/motores.h"
#include "pioneer_sumo/sensores_proximidade.h"



class vrepSimControleSumo{

	private:

                     // Program defines
        float MaxSpeed;

		ros::NodeHandle n;
		ros::Publisher pub;
		ros::Subscriber sub;

		pioneer_sumo::motores set_Motores;
		pioneer_sumo::sensores_proximidade val_sensores;
		//vrep_common::EspeleoSpeedSet espSpeed;
        //float locomocaoHorizontal, locomocaoVertical;
        //float vel_l, vel_r;

	public:

		//-----Metodo construtor------------
		vrepSimControleSumo(){

             //MaxSpeed = 19;

			pub = n.advertise<vrep_common::EspeleoSpeedSet>("/robo1/motores",1);
			sub = n.subscribe("/robo1/sensores", 1, &vrepSimControleSumo::sensorCallback, this);

		}

		//----Callback de quando uma mensagem do sensor é recebida --------------
		void sensorCallback(const pioneer_sumo::sensores_proximidade& msg){

			int i;

			//Guarda os valores dos sensores de presença em uma variável
			for(i=0;i<16;i++){
				val_sensores[i] = msg.distancia[i];
			}

			//--------Publishes the values
			//pub.publish(espSpeed);

		}//Fim do callback

}; //Fim da declaracao da classe

//======================================================================



// =========================Função main ===============================
int main(int argc, char **argv){

	ros::init(argc, argv, "joy2espeleo");

	vrepSimEspMotPublisher vrepSimEspMotPublisherOBJ;

	ROS_INFO("vrepEspeleoCommand_6rodas node running");
	ros::spin();

	return 0;
}
