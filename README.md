# LEO Rover ROS Model

ROS 1 packages for simulating, launching, visualizing, and navigating the Leo Rover platform used as the CORODRO rover base.

## Why This Repo Matters

If you want a cleaner entry point than the full mission repository, this is it. The packages here are closer to a reusable rover platform stack:

- description files,
- Gazebo simulation,
- bringup,
- teleoperation,
- visualization,
- navigation.

## Added Value

- A student-friendly rover base stack that can be studied independently from the full mission code.
- A practical example of how a research project extends a commercial/open rover platform.
- A compact ROS 1 navigation stack with well-separated packages.

## Algorithms Used

- `robot_localization` EKF for wheel odometry and IMU fusion.
- Madgwick IMU filtering through `imu_filter_madgwick`.
- gmapping for online 2D SLAM.
- AMCL for map-based localization.
- `global_planner` in Dijkstra mode for global path planning.
- `TrajectoryPlannerROS` with `dwa: true` for local planning.

## Repository Map

- `leo_description/`: URDF, meshes, and robot description launch files.
- `leo_gazebo/`: Gazebo model spawn and differential-drive plugin.
- `leo_bringup/`: hardware/software bringup configuration.
- `leo_navigation/`: localization and navigation launch/configuration.
- `leo_teleop/`: joystick teleoperation.
- `leo_viz/`: RViz configurations.
- `leo_mast_bringup/`: mast-related configuration.

## Quick Start

1. Create a ROS 1 catkin workspace.
2. Add this repository to `src/`.
3. Install the dependencies used by the navigation and Gazebo packages.
4. Build with `catkin_make`.
5. Start with `leo_description` or `leo_gazebo`, then move to `leo_navigation`.

## Notes For Students

- `leo_navigation` is the best package to study if your interest is localization and path planning.
- `leo_description/old/` is historical material and should not be your default reference.
- The navigation parameters are tuned for this rover and sensor suite; treat them as a baseline, not universal values.
