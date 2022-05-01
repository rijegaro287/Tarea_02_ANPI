cmake_minimum_required(VERSION 3.22)
project(Parte_3)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -larmadillo")

add_executable(Parte_3 parte3_p1.cpp parte3.h parte3_p2.cpp)