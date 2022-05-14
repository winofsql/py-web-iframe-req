#!C:\app2\Python\python.exe

import cgitb
cgitb.enable()

# **************************************
# 共有メソッド
# **************************************
from settings import *
set( "base_name", __file__ )

# **************************************
# CGI 初期処理
# **************************************
cgi_init()

import view
