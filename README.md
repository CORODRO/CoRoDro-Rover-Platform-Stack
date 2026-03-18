# LEO Rover ROS Model

`LEO_Rover_ROS_Model` is the standalone rover-platform repository used as the base for the CORODRO rover. It is the best place to understand the rover itself without the extra mission orchestration from `IGLUNA-FC-Code`.

## Why This Repo Matters

This repository separates the reusable rover platform stack from the full field-campaign code. It gives students a cleaner place to study:

- the robot description and URDF model,
- Gazebo simulation,
- hardware bringup,
- teleoperation,
- RViz visualization,
- localization and navigation.

## Added Value

- A student-friendly rover base stack that can be read independently from the full mission repository.
- A practical example of how the Leo Rover platform was extended for the CORODRO project.
- A compact ROS 1 navigation stack with well-separated packages and clear launch entry points.

## Algorithms Used

- `robot_localization` EKF for wheel odometry and IMU fusion in `leo_navigation/launch/odometry.launch`.
- Madgwick IMU filtering through `imu_filter_madgwick`.
- `slam_gmapping` for online 2D SLAM.
- `amcl` for map-based localization.
- `global_planner` with `use_dijkstra: true` for global path planning.
- `TrajectoryPlannerROS` with `dwa: true` for local motion planning.
- Differential-drive simulation in Gazebo through `leo_gazebo/src/differential_plugin.cpp`.

## Repository Map

- `leo_description/`: URDF, xacro files, meshes, and the `robot_description` launcher.
- `leo_gazebo/`: Gazebo launch files and the rover differential-drive plugin.
- `leo_bringup/`: bringup configuration for the physical rover stack.
- `leo_navigation/`: odometry fusion, SLAM, AMCL, and move_base configuration.
- `leo_teleop/`: joystick teleoperation.
- `leo_viz/`: RViz launch files and visualization profiles.
- `leo_mast_bringup/`: mast-related bringup configuration.
- `leo_tests/`: auxiliary launch files for tests and experiments.

## Suggested Learning Path

1. Start with `leo_description/launch/description.launch` to understand the robot model.
2. Move to `leo_gazebo/launch/leo_gazebo.launch` to see the rover in simulation.
3. Study `leo_navigation/launch/odometry.launch` for sensor fusion.
4. Study `leo_navigation/launch/gmapping.launch` and `leo_navigation/launch/amcl.launch` for localization.
5. Finish with `leo_navigation/launch/move_base.launch` and `leo_navigation/launch/navigation.launch` for navigation.

## Quick Start

1. Create a ROS 1 catkin workspace and place this repository in `src/`.
2. Install the ROS dependencies used by Gazebo, navigation, and teleoperation.
3. Build the workspace with `catkin_make`.
4. Launch the robot description with `roslaunch leo_description description.launch`.
5. Launch Gazebo with `roslaunch leo_gazebo leo_gazebo.launch`.
6. For navigation experiments, use the launch files in `leo_navigation/`.

## Notes For Students

- `leo_navigation` is the best package to study first if your focus is localization and path planning.
- `leo_description/old/` is historical material and should not be your default reference.
- The navigation demo nodes under `leo_navigation/nodes/` are educational examples, not the main production path.
- Some navigation demo scripts are also present in `IGLUNA-FC-Code`; treat this repository as the cleaner rover-platform source.
- The navigation parameters are tuned for this rover and sensor suite, so use them as a baseline rather than universal defaults.

## TODOs Before Retuning

- Validate `leo_navigation/config/ekf_localization_node/` against the current IMU, wheel odometry topic, and frame tree before changing fusion parameters.
- Re-tune `leo_navigation/config/slam_gmapping.yaml` only after checking the live lidar or scan source used by the rover.
- Review the `leo_navigation/config/move_base/` costmap and planner YAML files in simulation or hardware before changing navigation behavior.
- Re-validate `leo_navigation/config/amcl.yaml` on a representative map before adjusting localization thresholds or noise values.
- Keep `leo_description/old/` as archive material unless you intentionally want to recover a past rover model.
