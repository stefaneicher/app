cmake_minimum_required(VERSION 3.10)

project(app VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

include_directories(src)

add_executable(app src/main.cpp)

target_link_libraries(app CONAN_PKG::Calculator)



