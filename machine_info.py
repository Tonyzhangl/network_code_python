# -*- coding=utf-8 -*-

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print 'Host Name:{}'.format(host_name)
    print 'IP Name:{}'.format(ip_address)

if __name__ == '__main__':
    print_machine_info()
