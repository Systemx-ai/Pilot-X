### How to approach the control problem 


Firstly, there is the whole vehicle control system. We need to divide the control system into a few parts.

- Controller
- Plant/car
- Input
- System
- Output

- There's the input, then the system, then the compute and then output.
Designing the control problem 

- So, given a bunch of actions, you have to predict the desired action and you optimize the process along the way to reach that desired action. How do you do that.

Let's say that you want to reach a desired action k, given the previous states ranging from 1 to k-1. You have to keep optimizing the process to reach the desired action.

p(action(k)) <- p(action[(1 - (k-1))])

Now, coming to the control problemm itself. 
If we consider the vehicle model as a 2d problem. There are two outputs. 
- Longitudinal control
- lateral control

Long control consists of controlling gas and breaks, output of which is acceleration , ego vehicle velocity
Lateral control consists of controlling steering angle.

Perception - > path planning -> output.

Let's break down each of these.
- Perception:- Visual perception is required for a better understanding of the driving scene. Cars move, trees and buildings don't and we can device the categories accordingly. You train seg nets. Based on the ground truthing of the frames, we can create a better localizer. 
  - Inputs:- Camera images (dimensions x RGB X temporal)
  - Loss function:- the loss function that is commonly used in seg nets is pixel wise cross entropy loss. This loss function examines each pixel indiviually. log loss summed over all possible classes.
  - Outputs -> probability from seg nets. Outputs can range from obj detection, trajectory generation, driving scene etc.

- Path Planning
  - Understnding the physics behind the trajectory planning, the physics behind lateral offset, curvature, lookahead distance from the geometric vehicle mo0del. We are taking the weighted average of the lane width,  both left and right.
  - Inputs:- Camera images , desired set points. A way to do that is either by Model Predictive control - fine tuning the closed loop feedback system at each timestep.
  - Ouputs:- optimize and steer to the desired point. Use a PI or a PID controller. You can also use an LQR as a backup. The output is the desired steering angle, lookahead distance, optimum trajectory. 

  For long control -> input driver state, output -> gas, brakes, throttle. Kinematics

Path planning idea:

A couple of assumptions:- let's assume that we have the probabilities from the seg net that can determine where the drivable area is. It is within that drivable area that we need to search exactly where the lead car is. 

A few ways in which it can be done is as follows:- 
1) map representations: we are already assuming that the car is aware of its location within the map and is able to localize itself and avoid obstacles along the way. There are A* and other path planning algorithms.
2) Another way is without the map. The car needs to determine where the lead car is and then using the lane widths , it can locate its own position / guess its own position and using these positions, the car needs to guess the desired path that it should follow.
3) Assign weights to both left and right lanes. Compute their probability w r t centre lane. from location calculate the desired path.

Lateral control
  
