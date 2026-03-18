# leo_gazebo

This package provides the Gazebo simulation layer for the rover.

## What Is Here

- `launch/leo_gazebo.launch`: starts Gazebo and spawns the rover.
- `launch/spawn_robot.launch`: inserts the rover model into the simulator.
- `launch/spawn_model.launch` and `launch/spawn_controllers.launch`: helper launch files for model and controller setup.
- `src/differential_plugin.cpp`: differential-drive plugin used by the simulated rover.

## Best Starting Point

Use `leo_gazebo.launch` as the main simulation entry point.

## Why Students Use This Package

Use this package when you want to test rover behavior in simulation before touching hardware or the full mission stack.
