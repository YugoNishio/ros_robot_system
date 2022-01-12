#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Int32

class ImageConvert(object):
    def __init__(self):
        self.bridge = CvBridge()
        self.subscribed_image_color = rospy.Subscriber("image_raw", Image, self.color_callback_and_convert)
        self.publisher_answer_1 = rospy.Publisher("answer_1", Int32, queue_size=10)

    def main(self):
        try:
            rospy.spin()
        except KeyboardInterrupt:
            print("end")
            cv2.destroyAllWindows()
    
    def color_callback_and_convert(self, topic):
        try:
            cv_image_color = self.bridge.imgmsg_to_cv2(topic, "bgr8")
        except CvBridgeError as e:
            print(e)

        cascade_path = "/home/yugonishio/catkin_ws/src/ros_robot_system/scripts/haarcascade_frontalface_default.xml"        
        image_gray = cv2.cvtColor(cv_image_color, cv2.COLOR_BGR2GRAY)
        cascade = cv2.CascadeClassifier(cascade_path)
        facerect = cascade.detectMultiScale(image_gray, scaleFactor=1.1, minNeighbors=2, minSize=(30, 30))
        color = (255, 255, 255)
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(cv_image_color, tuple(rect[0:2]),tuple(rect[0:2]+rect[2:4]), color, thickness=2)
        
        print("x:",rect[0]," y:", rect[1], " width: ",rect[2], " height:",rect[3])
        dst_area = self.mosaic_area(cv_image_color, rect[0], rect[1], rect[2], rect[3])

        self.publisher_answer_1.publish(1)
        
        cv2.imshow("image", dst_area)
        cv2.waitKey(3)

    def mosaic(self, src, ratio):
        small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
        return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

    def mosaic_area(self, src, x, y, width, height, ratio=0.05):
        dst = src.copy()
        dst[y:y + height, x:x + width] = self.mosaic(dst[y:y + height, x:x + width], ratio)
        return dst

if __name__ == "__main__":
    rospy.init_node("vision")
    image_convert = ImageConvert()
    image_convert.main()