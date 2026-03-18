cmake_minimum_required(VERSION 2.8.3)
project(leo_navigation)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY launch/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
    PATTERN ".svn" EXCLUDE)

install(DIRECTORY config/
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config)

catkin_install_python(PROGRAMS
    scripts/message_filter
    nodes/move_base_square.py
    nodes/nav_square.py
    nodes/odom_out_and_back.py
    nodes/time_out_and_back.py
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
