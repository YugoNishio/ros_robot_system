# ros_robot_system

誰でも怪しい人になれるROSパッケージです。
個人情報保護のため、モザイクとボイスチェンジャーを使用しています。

---
### 動作環境
- CF-SV9PD9LC
- Ubuntu 18.04.6 LTS
- ROS Melodic
- OpneCV 4.5.1

---
### セットアップ方法
本パッケージ
``` 
$ cd ~/catkin_ws/src
$ git clone https://github.com/YugoNishio/ros_robot_system.git
$ catkin_make
$ source ~/.bashrc
``` 
OpenCV
```  
$ cd ~/
$ wget --no-check-certificate https://raw.githubusercontent.com/milq/milq/master/scripts/bash/install-opencv.sh  
$ chmod +x install-opencv.sh
$ ./install-opencv.sh
$ sudo apt-get install ros-melodic-cv-bridge
```  
playsound
```  
$ sudo apt install python-pip python3-pip
$ pip install playsound
```  

---
### 使用方法
以下のコードを端末ごとに実行します。
```  
roscore
rosrun uvc_camera uvc_camera_node
```  
`rqt_image_view`か`rosrun ros_robot_system --.py`

`pip install playsound`
