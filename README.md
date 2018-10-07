# Implementation of Kalman Filter using Python

Kalman filter implemented here takes in noisy LIDAR sensor data and smooths out the data to make more accurate predictions on a tracked vehicle's true position and velocity.

For autonomous vehicles, Kalman filters can be used in object tracking.

The Kalman filter has two steps: a prediction step and an update step.

In the prediction step, the filter uses a motion model to figure out where the object has traveled in between sensor measurements. 

The update step uses the sensor measurement to adjust the belief about where the object is.

# Results Visualization 

![graph](https://user-images.githubusercontent.com/25223180/46580459-c5346e00-ca42-11e8-9760-034e255f8564.png)

The chart contains ground turth, the lidar measurements, and the Kalman filter belief.

The Kalman filter tends to smooth out the information obtained from the lidar measurement.

