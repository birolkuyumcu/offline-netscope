# -*- coding: utf-8 -*-
"""
"A web-based - offline - tool for visualizing neural network topologies.
It currently supports UC Berkeley's Caffe framework."
github.com/ethereon/netscope
@author: bluekid70@gmail.com
"""


from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *
import sys
import os
import SimpleHTTPServer
import SocketServer
import threading
import time

PORT = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)

def worker():
    print "A web-based - offline - tool for visualizing neural network topologies.\n It currently supports UC Berkeley's Caffe framework.", PORT
    httpd.serve_forever()

w = threading.Thread(name= "Worker,",  target=worker)

def my_service():
    app = QApplication(sys.argv)
    webView = QWebView()
    webView.load(QUrl('http://127.1.1.1:8000'))
    webView.show()
    app.exec_()
    httpd.shutdown()
    os.exit(0)

s = threading.Thread(name= "Servis", target=my_service)

w.start()
time.sleep(1)
s.start()
