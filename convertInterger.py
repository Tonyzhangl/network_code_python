import socket

def convert_interger():
    data = 1234567890
    #32-bit
    print "Original:{} => Long host by order:{}, Network byte order:{}".format(data, socket.ntohl(data), socket.htonl(data))
    #16-bit
    print "Original:{} => Short host by order:{}, Network byte order:{}".format(data, socket.ntohs(data), socket.htons(data))

if __name__ == "__main__":
    convert_interger()
