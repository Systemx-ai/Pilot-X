## TO DO



![alt_text](https://www.scielo.br/img/revistas/lajss/v11n14/a02fig02.jpg)





### The basic idea

The Lateral block implements a look ahead control model to generate normalized steering commands that track a lateral reference displacement. The normalized steering commands can vary between -1 to 1. To model the dynamics, the block uses a linear single track (bicycle) model. Use the Lateral Driver block to:

Close the loop between a predefined path and actual vehicle motion using a PI controller.

Generate steering commands that track predefined paths. 




### Lateral path tracking

The model represents driver steering control behavior during path-following and obstacle avoidance maneuvers. Drivers preview (look ahead) to follow a predefined path.


### External Actions

Use External Actions parameters to create input  for signals that can disable, hold, or override the closed-loop steering command. The block uses this priority order for the input commands: disable (highest), hold, override. 


input --> system --> output


### Method

1. Calculate the curve - parametres
2. Calculate the Lookahead - parametres
3. calculate the actual offset
4. External actions w.r.t  car parametres
5. Close the loop using the PI controller
6. Update

Input commands - current position, current steering command fromm CAN bus, ego velocity.
Output:- lookahead distance, use that distance to calculate the lookahead position,  generated steering command, distance and steering command correlation. 

External actions to be taken within the PI Loop

### External action

Steer override and a fallback condition.
