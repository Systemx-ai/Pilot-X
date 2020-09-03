### Table of contents :page_facing_up:
1. [About](#About-car)
2. [Goal](#Goal-rocket)
3. [Safety](#Safety-oncoming_automobile)
4. [Open questions](#Open-questions-question)


### About :car:

We here at System-(x).ai are currently working towards perfecting level 2 autonomous driving in India.
Pilot-X is an open source Driver's assistance system (Currently under development). This organisation is being developed in good faith to be compliant with the Motor Vehicles Amendment Act(2019) under insertion of new section 2B - Promotion of innovation.

### Goal :rocket:

The goal of System-(x).ai is not different from that of comma ai or Tesla. Actually its a combination of both George Hotz and Elon Musk's idea.
Here's how we plan to do it.
We are planning to develop a brain for the car itself, the car's brain will be acting as a tertiary layer to the driver's limbic system and cortex. The functions that we are currently going to emulate from the limbic system is attention and memory. From the cortical system we are going to emulate sensory functions(visual perception) in a supervised manner. The output from our system needs to be characteristic of both the limbic and cortical system and become reliable over time. The driver will always have the option to disengage from the tertiary layer.

Now here's where George Hotz's idea comes in:- A car is like a computer. Hence, we have the option to tap into the car's internal control system through the OBD 2 port, just like a mechanic would do. We can send and receive messages back and forth from the car's control unit and also control the actuator functions. We can use the car's existing sensors without having to modify any of the internal firmware. As a result, it would become easier to implement self driving capabilities in the car you OWN. 

We plan on shipping you a self driving car kit. This kit will be the tertiary layer.
Anybody who knows how to operate a soldering iron can get the kit up and running in your car and get level 2 self driving functionality. Just like the Tesla you will receive Over the Air Software updates on the kit(as on your smartphone) as successive versions are developed. Hands should be on the wheels at all times and the driver should be ready to take back manual control at any time. And of course, before shipping such a product we are going to make sure that it is in full compliance with the industry guidelines as per the rules set by the Govt of India. 

### Safety :oncoming_automobile:

- As mentioned in the introduction, System-(x).ai is working on developing ADAS features, such as Adaptive cruice control (ACC) and Automated Lane Centering (ALC). The V-0.0.0 beta version is not compatible with any car at the moment. We are in the process of developing a version that will be tested on a vehicle.
- For the present version, we are including a driver monitoring algorithm, that will recognise the current driver state and transmit a warning signal in order to maximise attention. A fallback condition on limiting actuator functionality based on the driver's current state will be added.

- **Is the code published in this repo road legal ?**

As of August 2020, there are no specific laws in India that can effectively assess the functional safety of an ADAS software which makes it applicable to run on Indian roads. On the flip side, there are also no regulations that are currently regulating you(the viewer of this repo) or any other company who wants to build their own ADAS software, install it in their cars and test it on the streets. But, since public safety is of absolute importance, there should be zero compromise on the assessment of functional safety of said ADAS software, even while testing. So, the succeeding versions of System-(x).ai software that will be compatible with cars (in the future), will be developed following the guidelines proposed by the NHTSA. Find the pdf [here](https://www.nhtsa.gov/sites/nhtsa.dot.gov/files/documents/13498a_812_573_alcsystemreport.pdf)(that is the only one we found to be detailed and extensive). The code developed by System-(x).ai will abide by industry standards as prescribed by ISO 26262(international standard for functional safety of electrical and/or electronic systems) and also comply with industry safety standards/guidelines set forth by the Govt. of India. Unlike comma ai which has panda to make this determination, we have to figure out a new way to do it.

- Types of safety


### Open questions :question:
**Why aren't we building a car ?**

This is why :point_down:

<!-- Alignment options!!!!! -->
<img align="centre" width="400" height="300" src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iebhE23A8U.Q/v3/-1x-1.jpg">

*Picture: Bloomberg quint*

This is Zoox's self driving car. The picture is pretty much self explanatory. This is their result after raising $800 million. Good thing they got acquired by Amazon..!!

**Why is the code Open Sourced ?**

The quicker answer is that we are going to need help. You can make pull requests for the code and also later on down the road, we are going to need your help to support the  cars. We haven't begun to test the code on cars yet, it is still in the development phase. We are going to add build on top on opendbc by comma ai and add support for model ports and brand ports. We also need your help to build a better vision system which is in the plans for the year 2021. This year we are going to focus mostly on perfecting the ACC, LKAS and driver monitoring and the hardware.
