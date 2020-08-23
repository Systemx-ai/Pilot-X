# code needs to be fixed. Not Final
# do the library
# calculate the curvature, the distance, limits to acceleration, deceleration, calculate stopping distance.
# ACC will be built on top of this library.

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
    lead_gap = 1
    offset_distance = 4  # vertical distance from the initial tangent to a point on the curve
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

def calculate_deceleration(ego_velocity, lead_gap, lead_velocity):

    critical_acceleration = -max(0.0, ((ego_velocity **2) + (lead_velocity**2))) // (max(2 * (distance)))
    #constant deceleration
    return critical_acceleration

class CruiseControl(object):
    def __init(self):
        self.critical_acceleration = 0.0
        self.reset()

    def reset(self):
        self.distance = 0.0

    def update(ego_velocity, curr_steering_angle, Car_Parametres):

        #host to lead vehicle distance as a function of speed
        host_to_lead_distance= calculate_distance(ego_velocity, lead_velocity)
        self.calculate_deceleration = calculate_deceleration(ego_velocity, lead_velocity,host_to_lead_distance)
        self.compute_acceleration_limits = compute_acceleration_limits(ego_velocity, total_breakpoint_max, host_to_lead_disatnce, 
                                                                    total_acceleration_max, total_breakpoint_max, total_acceleration_min,
                                                                     total_breakpoint_min)

     
        final_acceleartion = np.clip(critical_acceleration, -max_acceleration, max_acceleration)
        return final_acceleartion, host_to_lead_distance
        
# Not final. Code needs to be cleaned up. add calculate stopping distance and update stopping distance
# https://korkortonline.se/en/theory/reaction-braking-stopping/#:~:text=Formula%3A%20Remove%20the%20zero%20from,researchers%20measuring%20the%20braking%20distance.
