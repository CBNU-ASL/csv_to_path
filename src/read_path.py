#!/usr/bin/env python3
import rospy as rp
from path_pkg.include.h_read_path import c_read_path

class read_path(c_read_path):
    def __init__(self):
        super(read_path, self).__init__()
        rp.init_node('Path_Node', anonymous=True)
        self.init_variable()
        self.init_pubsub()
        self.main_loop()

    def main_loop(self):
        _r = rp.Rate(100) # 100 Hz

        _path = self.fnc_read_csv(self.file_path)
        _path = self.fnc_make_path(_path)

        while not rp.is_shutdown():
            self.path_pub.publish(_path)
            _r.sleep()

if __name__ == '__main__':
    try:
        print("Read Path Node Start!")
        read_path()
        rp.spin()
    except rp.ROSInterruptException:
        pass