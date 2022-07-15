
import requests
import time
from pinpong.board import Board,Pin
from pinpong.extension.unihiker import *
from unihiker import GUI

IP="10.1.2.3"
PORT="8000"

u_gui=GUI()
u_gui.draw_text(text="访问结果：",x=10,y=10)
tx_status=u_gui.draw_text(text="",x=10,y=50)
u_gui.draw_text(text="数据：",x=10,y=100)
tx_value=u_gui.draw_text(text="",x=10,y=150)

Board().begin()
p_p29_analog=Pin(Pin.P29, Pin.ANALOG) #P29 光线传感器


while True:
    val = p_p29_analog.read_analog()
    tx_value.config(text=str(val))
    try:
        resp = requests.get("http://"+IP+":"+PORT+"/input?id=1&val=" + str(val) )
        if resp.status_code == 200:
            tx_status.config(text="访问成功")
        else:
            tx_status.config(text="访问错误")
    except Exception:
        print("服务器未开启")
    time.sleep(1)