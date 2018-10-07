# Implementation of Kalman Filter using Python

Kalman filter implemented here takes in noisy LIDAR sensor data and smooths out the data to make more accurate predictions on a tracked vehicle's true position and velocity.

For autonomous vehicles, Kalman filters can be used in object tracking.

The Kalman filter has two steps: a prediction step and an update step.

In the prediction step, the filter uses a motion model to figure out where the object has traveled in between sensor measurements. 

The update step uses the sensor measurement to adjust the belief about where the object is.

# Results Visualization 
