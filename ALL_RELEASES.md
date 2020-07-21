### V- 0.0.0 Beta

Currently the V-0.0.0 Beta version consists of self driving controls algorithm. Not to be used for testing. 
The detailed list of the work that has been currently done on V-0.0.0 Beta are as follows:
- The base steering model from the paper "End-to-end Multi-Modal Multi-Task Vehicle Control
for Self-Driving Cars with Visual Perceptions" has been implemented. Driving data was used from Driving in Downtown Chicago video by J_Utah.
-  A localizer comprising of EKF has been used for vehicle localization by using the vehicle dynamics bicycle model as a baseline. 
-  An adaptive Cruise control has been developed from scratch.
-  Geometric lateral control has been developed using a PI control along with anti-integral windup protection that steers to a position. (Also using the bicycle model as a potential baseline)
-  For Research - A VAE has been used to learn the hidden representations of a video frame. Instead of using end to end learning in everything, this is an alternative method.    Unlike a traditional autoencoder, a VAE maps the input data into the parameters of a probability distribution, such as the mean and variance of a Gaussian. Next thing to do is to train a RNN with hidden representations (latent vectors) of video frames as inputs . This way the RNN will learn temporal patterns of frames.

- A driver alert system is on the way, along with the path planner to follow the trajectory.
- Opendbc. Using Opendbc (all thanks to comma ai), we can use their preprocessor to create DBC files from a brand DBC file and a model specific DBC file.
  - Model Port:- the car’s brand is already supported, but the specific model, model year or trim isn’t.
  - Brand Port:- Either the car’s brand isn’t supported or the specific car model is substantially different from any currently supported cars.
