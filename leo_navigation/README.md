# leo_navigation

This package contains the rover localization and navigation stack.

## Algorithms Used

- `robot_localization` EKF for wheel odometry and IMU fusion.
- Madgwick IMU filtering through `imu_filter_madgwick`.
- `slam_gmapping` for online 2D SLAM.
- `amcl` for map-based localization.
- `global_planner` with Dijkstra search for global path planning.
- `TrajectoryPlannerROS` with `dwa: true` for local planning.
- `twist_mux` for velocity-command arbitration.

## Main Entry Points

- `launch/odometry.launch`: filtered odometry and optional 3D IMU processing.
- `launch/gmapping.launch`: online SLAM.
- `launch/amcl.launch`: map-based localization.
- `launch/move_base.launch`: global and local planning stack.
- `launch/navigation.launch`: convenience launcher that starts `twist_mux` and `move_base`.

## Key Config Files

- `config/ekf_localization_node/ekf_2d.yaml`
- `config/ekf_localization_node/ekf_3d.yaml`
- `config/slam_gmapping.yaml`
- `config/amcl.yaml`
- `config/move_base/planners/global_planner.yaml`
- `config/move_base/planners/local_planner.yaml`

## Demo Scripts

The Python nodes in `nodes/` such as `odom_out_and_back.py` and `move_base_square.py` are useful learning examples for beginner ROS navigation work. They are not the main navigation stack itself.

## Best Way To Learn This Package

1. Read `odometry.launch`.
2. Check the EKF and IMU configs.
3. Read `move_base.launch` and its planner YAML files.
4. Only then move to the example nodes in `nodes/`.

## TODOs Before Changing Tuned Configs

- Validate the EKF YAML files in `config/ekf_localization_node/` on the actual rover or a faithful simulator before retuning covariances.
- Treat `config/amcl.yaml` and `config/slam_gmapping.yaml` as tuned mission defaults, not generic templates.
- Re-test `config/move_base/`, including `costmaps/` and `planners/`, before changing obstacle inflation, planner scoring, or velocity limits.
