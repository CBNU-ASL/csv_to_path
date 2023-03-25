#!/usr/bin/env python3
import rospy as rp
import pandas as pd
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped

class c_read_path():
    def init_variable(self):
        self.frame_id = rp.get_param('frame_id')
        self.file_path = rp.get_param('file_path')


    def init_pubsub(self):
        self.path_pub = rp.Publisher('/path', Path, queue_size=10)


    def fnc_read_csv(self, _path_name):
        _path = pd.read_csv(_path_name).to_numpy()
        rp.loginfo("Path Loaded:{}".format(_path_name))

        return _path


    def fnc_make_path(self, _path):
        t_path = Path()
        t_path.header.frame_id = self.frame_id
        for i in range(len(_path)):
            csv_path=PoseStamped()
            csv_path.pose.position.x = float(_path[i,0])
            csv_path.pose.position.y = float(_path[i,1])
            csv_path.pose.position.z = 0
            csv_path.pose.orientation.x = 0
            csv_path.pose.orientation.y = 0
            csv_path.pose.orientation.z = 0
            csv_path.pose.orientation.w = 1
            t_path.poses.append(csv_path)

        return t_path
