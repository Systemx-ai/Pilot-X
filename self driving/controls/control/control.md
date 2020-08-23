### How to approach the control problem 

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
  - Inputs:- Camera images , desired set points. A way to do that is either by Model Predictive control or by fine tuning the closed loop feedback system at each timestep.
  - Ouputs:- optimize and steer to the desired point. Use a PI or a PID controller. You can also use an LQR as a backup. The output is the desired steering angle, lookahead distance, optimum trajectory. 

- Output
  
