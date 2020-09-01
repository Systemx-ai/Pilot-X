### Research

The idea is to utilise current resources to create a better localizer for the car.

Now how are we to do that ?

There are ways to create a localizer.
- Create a map. 
- search within that map.
- The car detects a stochastic environment and searches within that map.

How to search.

Ways to optimize search for a better performance.

- Using value prediction networks where the future predictions are conditional based upon discounted rewards.
- Explore the map in an on policy manner i.e, we are going to make a decision based on the current policy. 
- Have the model learn from the experience. (Also depends on, if the ground truth model of the environment is always available to the agent or not.)