# check env
    env
    printevn

# check certain env variable
    printenv HOME
    echo $HOME

    printevn PATH
    echo $PATH

# add evn
    DOWNLOAD = /home/letian/download
    export DOWNLOAD

    export PATH = /home/letian/anaconda2:$PATH
    export PATH = $PATH:/hone/letian/anaconda2

# delete path
    unset DOWNLOAD


/etc/profile                All user, when log in
/etc/environment            All user, when log in, second file
~/.profile                  Current user, 
~/.bashrc                   Current user, when bash is open, executed by .profile