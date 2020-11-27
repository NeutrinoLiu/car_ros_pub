# ROS Setup Instructions

OS: Ubuntu 18.04 Bionic

ROS version: Melodic

## Step 0: Docker

If you don't want to install Ubuntu, you can just use docker to run ROS

Here are the steps:
```
docker pull ubuntu:bionic
docker run -it ubuntu:bionic /bin/bash
apt update
apt install sudo vim lsb-release gnupg curl
adduser car
usermod -a -G sudo car
echo "su car" >> /root/.bashrc
```
(The last bit logs you in as user "car" when you enter the container.)

When you exit the container, it will stop. To start it:
```
docker ps -a
docker container start <CONTAINER ID>
docker exec -it <CONTAINER ID> /bin/bash
```

## Step 1: Install ROS

Instructions: [http://wiki.ros.org/melodic/Installation/Ubuntu](http://wiki.ros.org/melodic/Installation/Ubuntu)

## Step 2: Clone the git repository

```
git clone https://github.com/Autonomous-RC-Car-System/car_ros.git
```

## Step 3: Setup Catkin

```
cd /home/car/car_ros/catkin_ws
catkin_make
echo "source /home/car/car_ros/catkin_ws/devel/setup.bash" >> ~/.bashrc
```

## Step 4: Install python packages

```
sudo apt install python-pip
pip install pyyaml
```

## Step 5: Run ROS

```
roscore
rosrun autonomous localizationNode.py
```
