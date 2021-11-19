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

#-----引入地址------
sumo_path = "F:\\software two\\sumo-1.8.0"
project_path =  "F:\sumo_pro\\traci_main\\test1"
# cfg_path = "F:\sumo_pro/traci_main\main\zhangshijie.sumo.cfg"
cfg_path = "F:\sumo_pro\\traci_main\\test1/zhangshijie.sumo.cfg"
#----------------------------------------#

#---------------------#
sys.path.append(sumo_path)
sys.path.append(sumo_path+"tools")
# sys.path.append(r"F:\software two\sumo-1.8.0\guangshen_pro")
#引入地址导入模块
sys.path.append(sumo_path+"/tools/xml")
import traci
from sumolib import checkBinary



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

    

#traci控制
def traci_control_env_update(step_time):
    #----开始---
    traci.start(sumoCmd)

    # 仿真延迟

    for step in range(0,step_time):

        #步长控制
        traci.simulationStep(step +1)
        time.sleep(0.05)
        
    
    traci.close(wait=True)
    return 0


if __name__ == "__main__":

    N_STATES = 120

    print('------------------------------------------------')
    a = traci_control_env_update(N_STATES)
    # try:
    #     a.to_csv(project_path+"/output_data"+"/Aoutput"+".csv")
    # except:
    #     os.makedirs(project_path+"/output_data") 
    #     a.to_csv(project_path+"/output_data"+"/Aoutput"+".csv")
    print('--------------------END----------------------------')