# ros_robot_system

誰でも怪しい人になれるROSパッケージです。
個人情報保護のため、顔にモザイクがかかるようにしています。  
ボイスチェンジャーはiOS版「Voice Plus」を使用しています。なお、音源はYugoNishioの声です。

本パッケージは[千葉工業大学のロボットシステム学第10回講義](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)を元に作成しています。

---
### 動作環境
- CF-SV9PD9LC
- Ubuntu 18.04.6 LTS
- ROS Melodic
- OpneCV 4.5.1
- playsound 1.3.0

---
### セットアップ方法
ROS
[ロボットシステム学第10回講義](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)を参考にROSのセットアップを行ってください。環境は18.04なのでryuichiuedaさんが用意している、こちら[ros_setup_scripts_Ubuntu18.04](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server)のスクリプトを実行してください。

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
webカメラ
```  
$ sudo apt install cheese v4l-utils qv4l2
$ sudo usermod -a -G video [ユーザー名]
```  
webカメラの接続確認
```  
$ cheese
```  
パス修正  
本パッケージでは一部コードにファイル階層を指定しています。
使用する際はユーザーに合う階層を指定してください。  

音声変更  
流れる音声を変更することで、ご自由に不審者を演じることが出来ます。

---
### 使用方法
コードに変更を加えた場合は以下の操作をしてください。
```  
$ cd ~/catkin_ws/src
$ catkin_make
$ source ~/.bashrc
```  
以下のコードを端末ごとに実行します。
```  
$ roscore
$ rosrun uvc_camera uvc_camera_node
$ rosrun ros_robot_system vision.py
$ rosrun ros_robot_system pattern_1.py
```  

---
### 実際の様子
[https://studio.youtube.com/video/OapkfbCmNCY/edit]
[![サムネ](https://user-images.githubusercontent.com/71488443/149156044-728c68f0-72fb-49db-a9d0-051967aee3d7.png)](https://www.youtube.com/watch?v=OapkfbCmNCY)


---
### 参考にしたサイト
[ROSでWebカメラの画像を表示](http://joe.ash.jp/program/ros/tutorial/tutorial_camera.htm)閲覧日2022/1/11  
[Python,OpenCVで画像にモザイク処理(全面、一部、顔など)](https://note.nkmk.me/python-opencv-mosaic/)閲覧日2022/1/11  

### ライセンス
- ROS [BSD 3-Clause License](https://github.com/YugoNishio/ros_robot_system/blob/main/LICENSE)
- OpenCV [Apache License 2.0](https://github.com/opencv/opencv/blob/4.x/LICENSE)
- playsound [MIT License]
