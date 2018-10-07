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

Kalman filters can give insights into variables that cannot be directly measured. 

Although lidar does not directly give velocity information, the Kalman filter can infer velocity from the lidar measurements.

# Visualization Results of Kalman filter velocity estimation versus the Ground Truth

![kalman_filter_velocity_estimation_graph](https://user-images.githubusercontent.com/25223180/46580511-98cd2180-ca43-11e8-949d-82406027687d.png)

The motion model used in this Kalman filter assumes that velocity is constant and that acceleration a random noise.
This motion model might be too simplistic because the Kalman filter has trouble predicting velocity as the object decelerates.
