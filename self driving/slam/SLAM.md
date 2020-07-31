## SLAM 


### Libraries used
- sdl2 for 2d and 3d display
- cv2 for feature extraction
- numpy
- pygame


### Documentation
(Needs modification, not final)


- The goal here, is to create a feature based monocular SLAM.(Simultaneous Localization and Mapping). Definition of SLAM - In computational geometry, simultaneous localization and mapping (SLAM) is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it
- Build a feature based SLAM, instead of a dense SLAM. The reason being - the need to track images from one image to the next image.
- sdl2 :- pixels2d and pixels3d

- ORB opencv is used . ORB is basically a fusion of keypoint detector and descriptor with many modifications to enhance the performance.
- Detection -[Good features to track](https://docs.opencv.org/2.4/modules/imgproc/doc/feature_detection.html#goodfeaturestotrack) this determines the strong corners of the image.
- Extraction - cv2.Keypoints - The keypoint is characterized by the 2D position, scale (proportional to the diameter of the neighborhood that needs to be taken into account), orientation and some other parameters. The keypoint neighborhood is then analyzed by another algorithm that builds a descriptor (usually represented as a feature vector).
- Matching is done [here](https://github.com/SystemX-ai/Pilot-X/blob/master/self%20driving/slam/feature_extractor.py#L37) query descriptor index, train descriptor index, train image index, for matching keypoint descriptors

- In computer vision, the fundamental matrix ${\displaystyle \mathbf {F} }\mathbf {F}$  is a 3×3 matrix which relates corresponding points in stereo images. 
- The fundamental matrix relates corresponding points between a pair of uncalibrated images. The matrix transforms homogeneous image points in one image to epipolar lines in the other image.
- Describe why the filter is used, watch the video.