cmake_minimum_required(VERSION 3.0.2)
project(path_pkg)

find_package(catkin_simple REQUIRED)
catkin_simple(ALL_DEPS_REQUIRED)

include_directories(include)