# Trajectory Reconstruction from Raw Sensor Data of Vehicle Odometer

Given a set of raw sensor data collected by the readings of Odometer of a Vehicle containing the values of below mentioned 4 parameters

1) timestamp - Timestamps are all measured in seconds. The time between successive timestamps ( Δt ) will always be the same within a trajectory's data set (but not between data sets).

2) displacement - Displacement data from the odometer is in meters and gives the total distance traveled up to this point.

3) yaw_rate - Yaw rate is measured in radians per second with the convention that positive yaw corresponds to counter-clockwise rotation.

4) acceleration - Acceleration is measured in  m/ss  and is always in the direction of motion of the vehicle (forward).

# Raw Sensor Data Snapshot

![raw_sensor_data](https://user-images.githubusercontent.com/25223180/46579149-8b0aa280-ca29-11e8-808a-50228226a135.PNG)


After processing of the above provided Sensor data of Vehicle's Motion exact trajectory of the vehicle is reconstructed by plotting a graph of vehicle's X and Y position 


# Result achieved : Display of Vehicle's Trajectory plotted on the basis of raw sensor data provided

![vehicle trajectory](https://user-images.githubusercontent.com/25223180/46579404-88f71280-ca2e-11e8-9835-ebcd200f7b24.png)

# Inference derived from the plotted graph of vehicle trajectory

This vehicle first accelerates forwards and then turns right until it almost completes a full circle turn.
