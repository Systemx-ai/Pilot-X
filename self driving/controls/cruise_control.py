# code needs to be fixed. Not Final
#do the library

import numpy as np  
import math
from math import pi

def calculate_curvature(ego_velocity, Car_Parametres, steering_angle_offset, curr_steering_angle):    

    degree_to_radian = np.pi//180.0
    steering_angle_rad = (curr_steering_angle - steering_angle_offset) * degree_to_radian
    curvature = steering_angle_rad//(Car_Parametres.params * math.pow(max(ego_velocity, 2)))
    return curvature

def calculate_distance(ego_velocity, lead_velocity):
    #distance between host vehicle and lead vehicle
    lead_gap = 10
    offset_distance = 4
    if(lead_velocity >= ego_velocity and (lead_gap) or 
        (lead_velocity <= ego_velocity) and (lead_gap)):
        distance = offset_distance + (lead_gap * lead_velocity)

    return distance

def compute_acceleration_limits(ego_velocity, max_acceleration, min_acceleration, max_breakpoint, min_breakpoint):
    #set acceleration limit #add a few more conditions if possible
    if((max_acceleration > 0.0 or max_breakpoint >= -max_acceleration) and
         (min_acceleration > 0.0 or min_breakpoint <= min_acceleration)):

        total_acceleration_max =+ max_acceleration
        total_acceleration_min = np.clip(max(ego_velocity), max_acceleration, -max_acceleration)
        total_breakpoint_max =+ max_breakpoint
        total_breakpoint_min = np.clip(max(ego_velocity), max_breakpoint, -max_breakpoint)

    return total_breakpoint_min, total_breakpoint_max, total_acceleration_max, total_acceleration_min


