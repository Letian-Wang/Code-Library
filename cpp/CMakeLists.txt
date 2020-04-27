CMAKE_MINIMUM_REQUIRED( VERSION 3.0)
PROJECT(hello)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_LIST_DIR}/include)          # where to find head file
LINK_DIRECTORIES("lib")                                         # where to find libraries
AUX_SOURCE_DIRECTORY(. DIR_SRCS)                                # give source file to variable
ADD_EXECUTABLE(hello ${DIR_SRCS})                               # generate excutable file
TARGET_LINK_LIBRARIES(main Test)                                # link libraries to executable file


# In subdirectory
AUX_SOURCE_DIRECTORY(. DIR_TEST_SRCS)
ADD_LIBRARY(Test ${DIR_TEST_SRCS})

# add all source file
file(GLOB_RECURSE cpp_list ./*.cpp)

CMAKELIST 4 个模块：
纳入所有源文件： file()或者aux_source_directory()，ADD_EXECUTABLE()
哪找头文件: INCLUDE_DIRECTORIES()
哪找库文件: LINK_DIRECTORIES()
链接库文件：TARGET_LINK_LIBRARIES()

创建库文件: ADD_LIBRARY()
查找库文件：find_package()
