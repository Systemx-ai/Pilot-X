### Table of contents :page_facing_up:
1. [About](#About)
2. [Goal](#Goal)
3. [Safety](#Safety)
4. [Open questions](#Open-questions)


### About :car:

We here at System-X are currently working towards perfecting level 2 autonomous driving in India.
Pilot-X is an open source Driver's assistance system (Currently under development). This organisation is being developed in good faith to be compliant with the Motor Vehicles Amendment Act(2019) under insertion of new section 2B - Promotion of innovation.

### Goal :rocket:

The goal of System-X is not different from that of comma ai. System-X plans on shipping a cost effective self driving car kit, complete with the necessary hardware. Anybody who knows how to operate a soldering iron can get the kit up and running in your car and receive level 2 self driving functionality. Just like the Tesla you will receive Over the Air Software updates on the kit(as on your smartphone) as successive versions are developed. Hands should be on the wheels at all times and the driver should be ready to take back manual control at any time. And of course, before shipping such a product we are going to make sure that it is in full compliance with the industry guidelines as per the rules set by the Govt of India. 

### Safety :oncoming_automobile:

- As mentioned in the introduction, System-X is working on developing ADAS features, such as Adaptive cruice control (ACC) and Automated Lane Centering (ALC). The V-0.0.0 beta version is not compatible with any car at the moment. We are in the process of developing a version that will be tested on a vehicle.
- For the present version, we are including a driver monitoring algorithm, that will recognise the current driver state and transmit a warning signal in order to maximise attention. A fallback condition on limiting actuator functionality based on the driver's current state will be added.

- **Is the code published in this repo road legal ?**

As of August 2020, there are no specific laws in India that can effectively assess the functional safety of an ADAS software which makes it applicable to run on Indian roads. On the flip side, there are also no regulations that are currently regulating you(the viewer of this repo) or any other company who wants to build their own ADAS software, install it in their cars and test it on the streets. But, since public safety is of absolute importance, there should be zero compromise on the assessment of functional safety of said ADAS software, even while testing. So, the succeeding versions of System-X software that will be compatible with cars (in the future), will be developed following the guidelines proposed by the NHTSA. (that is the only one we found to be detailed and extensive). The code developed by System-X will abide by industry standards as prescribed by ISO 26262(international standard for functional safety of electrical and/or electronic systems) and also comply with industry safety standards/guidelines set forth by the Govt. of India.

 - If you (indiviual or company) decide to use the code pertaining to Pilot-X to build your own ADAS , please make sure that your use case is in full compliance with the local laws of your state/country and meets the automotive industry standards. If not, then you need to modify the code/build on top of Pilot-X.


### Open questions :question:
**Why aren't we building a car ?**

This is why :point_down:

<!-- Alignment options!!!!! -->
<img align="centre" width="400" height="300" src="https://assets.bwbx.io/images/users/iqjWHBFdfxIU/iebhE23A8U.Q/v3/-1x-1.jpg">

*Picture: Bloomberg quint*

This is Zoox's self driving car. The picture is pretty much self explanatory. This is their result after raising $800 million. Good thing they got acquired by Amazon..!!

**Why is the code Open Sourced ?**
