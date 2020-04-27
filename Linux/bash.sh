# rules:
  no space between =
  when use a variable, add $ ahead of it

#! /bin/bash
gnome-terminal -x bash -c "(sh ./run2.sh);exec bash;"    #打开新终端，执行run2.sh文件，打开的终端执行脚本后不关闭


# read data and echo to new file, open xterm to execute
input=“data.txt”
while IFS= read -r line
do
  echo "$line" | cut -d' ' -f1                         # echo to screen, cut (dilimiter ' ', first field)
  echo "$line" | cut -d' ' -f1 > output.txt            # echo to file
  sleep 10
  xterm -e bash -c '(./run.sh);' &                     # open new xterm and execute run.sh
done < "$input"


roslaunch ros_package launch.launch &                   # & means run in background
sleep 10
pid_1=$!                                                # get the pid of the previous process in background
kill $pid_1;exit                                        # kill the process