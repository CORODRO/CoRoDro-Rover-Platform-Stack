#!/usr/bin/env python

"""Run a simple timed out-and-back motion profile.

This learning script sends open-loop velocity commands to drive forward,
rotate, and drive back. It is useful for first experiments when odometry or
move_base are not part of the exercise yet.
"""

import rospy
from geometry_msgs.msg import Twist
from math import pi

class TimedOutAndBack():
    def __init__(self):
        # Give the node a name
        rospy.init_node('out_and_back', anonymous=False)

        # Set rospy to execute a shutdown function when exiting
        rospy.on_shutdown(self.shutdown)
        
        # Publisher to control the robot's speed
        cmd_vel_topic = rospy.get_param("~cmd_vel_topic", "/cmd_vel")
        self.cmd_vel = rospy.Publisher(cmd_vel_topic, Twist, queue_size=5)
        
        # How fast will we update the robot's movement?
        rate = rospy.get_param("~rate", 10)
        
        # Set the equivalent ROS rate variable
        r = rospy.Rate(rate)
        
        # Set the forward linear speed in meters per second.
        linear_speed = rospy.get_param("~linear_speed", 1.0)
        
        # Set the travel distance in meters.
        goal_distance = rospy.get_param("~goal_distance", 3.0)
        
        # How long should it take us to get there?
        linear_duration = goal_distance / linear_speed
        
        # Set the rotation speed in radians per second.
        angular_speed = rospy.get_param("~angular_speed", 1.0)
        
        # Rotate 180 degrees between the outbound and return legs.
        goal_angle = rospy.get_param("~goal_angle", pi)
        
        # How long should it take to rotate?
        angular_duration = goal_angle / angular_speed
     
        # Loop through the outbound and return legs.
        for leg_index in range(2):
            # Initialize the movement command
            move_cmd = Twist()
            
            # Set the forward speed
            move_cmd.linear.x = linear_speed
            
            # Move forward for a time to go the desired distance
            ticks = int(linear_duration * rate)
            
            for t in range(ticks):
                self.cmd_vel.publish(move_cmd)
                r.sleep()
            
            # Stop the robot before the rotation
            move_cmd = Twist()
            self.cmd_vel.publish(move_cmd)
            rospy.sleep(1)
            
            if leg_index == 0:
                # Now rotate left roughly 180 degrees.
                move_cmd.angular.z = angular_speed

                # Rotate for the requested duration.
                ticks = int(angular_duration * rate)
                
                for t in range(ticks):
                    self.cmd_vel.publish(move_cmd)
                    r.sleep()
                
                # Stop the robot before the next leg.
                move_cmd = Twist()
                self.cmd_vel.publish(move_cmd)
                rospy.sleep(1)
            
        # Stop the robot
        self.cmd_vel.publish(Twist())
        
    def shutdown(self):
        # Always stop the robot when shutting down the node.
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)
 
if __name__ == '__main__':
    try:
        TimedOutAndBack()
    except rospy.ROSInterruptException:
        rospy.loginfo("Out-and-Back node terminated.")
