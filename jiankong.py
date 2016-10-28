#!/usr/bin/python
#coding:utf-8
import os
import sys
import ConfigParser
import socket
def reader(path):
	con=os.popen("cat %s"%path)
	content=con.read()
	con.close()
	return content
def connect(cont):
	sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.connect(("192.168.43.95",8000))
	sock.send(cont)
	sock.close()

def main():
    cfg = ConfigParser.ConfigParser()
    #cfg.read("")

if __name__== "__main__":
    config_path=os.path.join(os.path.dirname(__file__),"client_config.cfg")
    cfg=ConfigParser.ConfigParser()
    cfg.read(config_path)
    path_dict=dict(cfg.items("PATH_CONFIG"))
    print(path_dict)
    read_path=path_dict["read_path"]
    path_list=path_dict["read_list"].split(",")
    print(read_path)
    print(path_list)



