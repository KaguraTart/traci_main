# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

#引入包
# from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
# from dateutil.relativedelta import relativedelta
from datetime import datetime, date
import os, sys
import  time
import tqdm

#-----引入地址------
sumo_path = "F:\\software two\\sumo-1.10.0"
project_path =  "F:\sumo_pro\\traci_main\guangshen\guangshen"
# cfg_path = "F:\sumo_pro/traci_main\main\zhangshijie.sumo.cfg"
cfg_path = "F:\sumo_pro/traci_main\guangshen\guangshen\guangshen_ALL.sumo.cfg"
#----------------------------------------#



#---------------------#
sys.path.append(sumo_path)
sys.path.append(sumo_path+"tools")
# sys.path.append(r"F:\software two\sumo-1.8.0\guangshen_pro")
#引入地址导入模块
sys.path.append(sumo_path+"/tools/xml")
import traci
from sumolib import checkBinary
# import xml2csv

#------导入自己写的包-------
import output_car_data2 as ocd2
import output_car_data as ocd

#绘图图式
plt.rcParams['figure.figsize']=(30,10)
plt.style.use('ggplot')

#--------引入SUMO环境变量-----------------
# if 'SUMO_HOME' in os.environ:
#      tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
#      sys.path.append(tools)
# else:
#      sys.exit("please declare environment variable 'SUMO_HOME'")


#--------traci提供实时交互接口--------


#是否打开gui True为打开 False为关闭
gui = True
if gui == 1: 
    sumoBinary = sumo_path+"/bin/sumo-gui"
else:
    sumoBinary = sumo_path+"/bin/sumo"

#-----配置文件cfg打开以及输出xml格式统计数据
sumoCmd = [sumoBinary, "-c", cfg_path ,'--tripinfo-output',project_path+"/tripinfo2_TEST.xml",'--duration-log.statistics']

#仿真时间
simulation_time =1200
#-----画图全局变量--------


# output_data1 = pd.DataFrame()
    

#traci控制
def traci_control_env_update(step_time):
    #----开始---
    traci.start(sumoCmd)

    # 仿真延迟
    
    # ----设置限速-----
    # for i in range(0,5):
    #     traci.lane.setMaxSpeed('H_'+str(i),27.78)


    for step in range(0,step_time):


    
        #交通信号灯控制
        # traci.trafficlight.setRedYellowGreenState(traci.trafficlight.getIDList()[0], choose_action(step, q_table)+'G')  #trafficlight_control(step)  trafficlight_control2(step)

        # simulation_current_time = traci.simulation.getTime()

        #目前时间
        # print('simulation time is:',simulation_current_time)

        # #获取车辆ID
        # all_vehicle_id = traci.vehicle.getIDList()
        # print(all_vehicle_id)
        # #获取车辆位置
        # # all_vehicle_position = traci.vehicle.getPosition(step)
        #获取车辆是否经过车线

        #---按照帧率输出车辆位置信息---#
        # print(ocd2.output_car_data2(step,project_path))
        # out_data = ocd2.output_car_data2(step,project_path)
        
        # if step ==0:
        #     output_data1 = out_data
        # else:
        #     output_data1 = pd.concat([output_data1,out_data],axis=0,ignore_index=True)
        
        # out_data = ocd2.output_car_data2(step,project_path)
        # output_data1 = 0
        # if step ==0:
        #     output_data1 = ocd2.output_car_data2(step,project_path)
        # else:
        #     output_data1 = pd.concat([output_data1,ocd2.output_car_data2(step,project_path)],axis=0,ignore_index=True)

        # ocd.output_car_data2(step,project_path)
        # print(output_data1)
        try :# 获取截屏方法
            pass
            # 获取截屏
            # traci.gui.screenshot('View #0',r'F:\software two\sumo-1.8.0/guangshen_pro/img/img{}.jpg'.format(step),-1,-1)
        except :
            pass
        # print(H_0_meanspeed_list)

        #步长控制
        traci.simulationStep(step +1)
        # time.sleep(0.005)
    
    traci.close(wait=True)
    return output_data12
    # return 0


if __name__ == "__main__":
 #运行sumo
    # output_data1 = pd.DataFrame(columns=['car_num','x_position','y_position','x_acce(m^2/s)','y_acce(m^2/s)','length(m)','speed(m/s)','LateralSpeed(m/s)','accelaration(m^2/s)','angel(du)','roadID','LaneID','Lane_index','lane_position'],dtype=float)

    N_STATES = 12000
    # traci.gui.setSchema('View #0','cus')  #改变GUI为真实车辆

    # q_table_train = traci_control_env_update(N_STATES)
        # if episode % 20 == 0:
        #     q_table_train.to_excel(r'F:\software two\sumo-1.8.0/file1/doc2/'+'qtable'+str(episode)+'.xlsx',index=False)
        # episode +=1
    print('------------------------------------------------')
    a = traci_control_env_update(N_STATES)
    try:
        a.to_csv(project_path+"/output_data"+"/Aoutput5"+".csv")
    except:
        os.makedirs(project_path+"/output_data") 
        a.to_csv(project_path+"/output_data"+"/Aoutput5"+".csv")
    print('--------------------END----------------------------')