CMAKE_MINIMUM_REQUIRED( VERSION 3.0)
PROJECT(hello)
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_LIST_DIR}/include)          # where to find head file
LINK_DIRECTORIES("lib")                                         # where to find libraries
LINK_DIRECTORIES(${CMAKE_CURRENT_LIST_DIR}/lib)                 # where to find libraries
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

库：
自己的库 (add_library, add_subdirectory) (自己最好就别搞库了, 用file全搞定)
别人的库 (find_package)

CMakeLists:
Basics IBM: https://www.ibm.com/developerworks/cn/linux/l-cn-cmake/index.html
Common command: https://elloop.github.io/tools/2016-04-10/learning-cmake-2-commands
更多变量： https://blog.csdn.net/netnote/article/details/4051620
file command and function : https://elloop.github.io/tools/2016-04-11/learning-cmake-3-function-macro
find package: https://blog.csdn.net/haluoluo211/article/details/80559341
			  https://blog.csdn.net/bytxl/article/details/50637277
use third-party library: https://cloud.tencent.com/developer/article/1446788
use self-created library: https://juejin.im/post/5a6f3cda6fb9a01c9d32231c
构建链接库： https://blog.csdn.net/wks19891215/article/details/51002615
查找链接库： http://www.yeolar.com/note/2014/12/16/cmake-how-to-find-libraries/
ADD_SUBDIRECTORY :https://blog.csdn.net/xierhacker/article/details/80945449
