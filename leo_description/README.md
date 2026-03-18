# leo_description

This package contains the rover robot model.

## What Is Here

- `urdf/leo.urdf.xacro`: the main xacro description of the rover.
- `urdf/leo.gazebo.xacro`: Gazebo-specific additions for simulation.
- `launch/description.launch`: loads the `robot_description` parameter.
- `old/`: historical material that should not be your default reference.

## Best Starting Point

Launch `description.launch` first if you want to understand how the rover model is assembled and published into ROS.

## Why Students Use This Package

Use this package to study the rover frame tree, sensors, and physical layout before moving on to Gazebo or navigation.
