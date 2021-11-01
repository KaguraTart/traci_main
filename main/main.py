# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8

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


#-----引入地址------
sumo_path = "F:\\software two\\sumo-1.8.0"
project_path =  "F:\sumo_pro\main"
cfg_path = "F:\sumo_pro\main\zhangshijie.sumo.cfg"
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
H_0_meanspeed_list =[]
H_1_meanspeed_list =[]
H_2_meanspeed_list =[]
H_3_meanspeed_list =[]
H_4_meanspeed_list =[]
get_OOC0_list = []
get_OOC1_list = []
get_OOC2_list = []
get_OOC3_list = []
get_OOC4_list = []
get_OOCall_list = []
H_0_car_speed = 0
H_1_car_speed = 0
H_2_car_speed = 0
H_3_car_speed = 0
H_4_car_speed = 0



    

#traci控制
def traci_control_env_update(step_time):
    #----开始---
    traci.start(sumoCmd)

    # 仿真延迟
    
    # ----设置限速-----
    for i in range(0,5):
        traci.lane.setMaxSpeed('H_'+str(i),27.78)
    # traci.lane.setMaxSpeed('H_0',20)
    # traci.lane.setMaxSpeed('H_1',20)
    # traci.lane.setMaxSpeed('H_2',20)
    # traci.lane.setMaxSpeed('H_3',20)
    # traci.lane.setMaxSpeed('H_4',20)
    for step in range(0,step_time):


        # H_0_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_0')*3.6)
        # H_1_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_1')*3.6)
        # H_2_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_2')*3.6)
        # H_3_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_3')*3.6)
        # H_4_meanspeed_list.append(traci.lane.getLastStepMeanSpeed('H_4')*3.6)
        # H_12_meanspeed =(traci.lane.getLastStepMeanSpeed('H_1')*3.6+traci.lane.getLastStepMeanSpeed('H_2')*3.6)/2
        # get_OOC0_list.append(traci.lane.getLastStepOccupancy('H_0')*100)
        # get_OOC1_list.append(traci.lane.getLastStepOccupancy('H_1')*100)
        # get_OOC2_list.append(traci.lane.getLastStepOccupancy('H_2')*100)
        # get_OOC3_list.append(traci.lane.getLastStepOccupancy('H_3')*100)
        # get_OOC4_list.append(traci.lane.getLastStepOccupancy('H_4')*100)
        # get_OOCall_list.append((traci.lane.getLastStepOccupancy('H_0')+traci.lane.getLastStepOccupancy('H_1')+
        # traci.lane.getLastStepOccupancy('H_2')+traci.lane.getLastStepOccupancy('H_3')+traci.lane.getLastStepOccupancy('H_4'))/4*100)

    
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
        ocd.output_car_data2(step,project_path)

        try :# 获取截屏方法
            pass
            # 获取截屏
            # traci.gui.screenshot('View #0',r'F:\software two\sumo-1.8.0/guangshen_pro/img/img{}.jpg'.format(step),-1,-1)
        except :
            pass
        # print(H_0_meanspeed_list)

        #步长控制
        traci.simulationStep(step +1)
        # time.sleep(0.08)

    traci.close(wait=True)
    return 0


if __name__ == "__main__":
 #运行sumo
    MAX_EPISODES= 1
    N_STATES = 1200
    # traci.gui.setSchema('View #0','cus')  #改变GUI为真实车辆
    for episode in range(MAX_EPISODES):
        H_0_meanspeed_list =[]
        H_1_meanspeed_list =[]
        H_2_meanspeed_list =[]
        H_3_meanspeed_list =[]
        H_4_meanspeed_list =[]
        get_OOC0_list = []
        get_OOC1_list = []
        get_OOC2_list = []
        get_OOC3_list = []
        get_OOC4_list = []
        get_OOCall_list = []
        q_table_train = traci_control_env_update(N_STATES)
        # if episode % 20 == 0:
        #     q_table_train.to_excel(r'F:\software two\sumo-1.8.0/file1/doc2/'+'qtable'+str(episode)+'.xlsx',index=False)
        # episode +=1

        print('------------------------------------------------')