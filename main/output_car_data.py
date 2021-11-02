# -*- coding: utf-8 -*-
# @auther:	KaguraTart
# @time:	2021/10/31 14:50:27
# @version:	python3.8
# @institution:Tongji university

from typing import Counter
import  traci
import  numpy as np
import  pandas as pd
import os

def output_car_data2(step,project_path):

    position_data = pd.DataFrame(columns=['car_num','x_position','y_position'],dtype=float)

    #获取车辆ID
    all_vehicle_id = traci.vehicle.getIDList()
    # print(type(all_vehicle_id))
    n = 0
    #获取车辆位置
    for i in all_vehicle_id:
        all_vehicle_position = traci.vehicle.getPosition(i)
        position_data.loc[n] = [all_vehicle_id[n],all_vehicle_position[0],all_vehicle_position[1]]
        n +=1
    # print(position_data)
    try:
        position_data.to_csv(project_path+"/output_data/for"+str(step)+"seconds"+".csv")
    except:
        os.makedirs(project_path+"/output_data") 
        position_data.to_csv(project_path+"/output_data"+"/for"+str(step)+"seconds"+".csv")