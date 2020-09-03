### Research

The idea is to utilise current resources to create a better localizer for the car.

Now how are we to do that ?

There are ways to create a localizer.
- Create a map. 
- search within that map.
- The driving agent detects a stochastic environment and searches within that map.

How to search.

Ways to optimize search for a better performance.

- Using value prediction networks where the future predictions are conditional based upon discounted rewards.
- Explore the map in an on policy manner i.e, we are going to make a decision based on the current policy. 
- Have the model learn from the experience. (Also depends on, if the ground truth model of the environment is always available to the agent or not)
- A model based method can be used.

### Questions

### TO DO: 

	- Maximise the experience from the random stochastic model.
	- Make use of uncertainty as a potential experience
	- eliminate biases that can make the model behave suboptimally in the real life environments.


One of the ways that we can do it is by maximising attention. for eg:- in a language model, a transformer network uses attention mechanisms, like hard attention, soft attention, self attention and multi head attention  mechanisms, to pay attention to parts of the input. 

We can have the driving agent memorise particular uncertainties that occur with a higher frequency and in different representations. 

- Then we can use attention mechanisms and make a connection between the target action and the source action. 
- The attention vector/context vector is going to look for clues in the input env that can help to encode these uncertainties.

-We can create a score function which can deliver the aggregate of these interactions. 
 
The goal is to do it with less data.

- [Model predictive policy learning](https://arxiv.org/pdf/1901.02705.pdf). A ppaer by Lecun worthy of looking into. Here, we can have the uncertainity regularized.
- Use Hierarchial memory networks to pay soft attention
- learn those representations using episodic memory. 


