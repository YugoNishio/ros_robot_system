#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32
from playsound import playsound

rospy.init_node('Q&A')

n = 1

def cb(message):
    global n
    #print(message)
    if message.data == 1 and n == 1:
        print('\033[42m' + "こんにちは。すみません。ちょっといいですかね。" + '\033[0m')
        playsound("/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/sound/aisatu.wav")
        print('\033[42m' + "危ないものないと思うんですが一応持ち物確認させてください。" + '\033[0m')
        playsound("/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/sound/syoudaku.wav")
        print('\033[42m' + "ここ失礼しますね。" + '\033[0m')
        playsound("/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/sound/mate.wav")
        print('\033[42m' + "これは何ですかね。お兄さんわかるでしょ" + '\033[0m')
        playsound("/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/sound/wakaran.wav")
        print('\033[42m' + "これお兄さんのだよね？" + '\033[0m')
        playsound("/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/sound/tigau.wav")
        print("終了....")
        n = 0

if n == 1:
    sub = rospy.Subscriber('answer_1', Int32, cb)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
#    pub.publish(n)
    rate.sleep()
    rospy.spin()