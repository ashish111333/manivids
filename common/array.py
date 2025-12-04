from manim import *
from typing import  List,Tuple


def create_array(length: float,width: float,l:int):
    
    arr=VGroup()
    for i in range(l):
        arr+=Rectangle(height=length,width=width).scale(1).set_color(GREEN)
    arr.arrange(DOWN,buff=0.01)
    return arr

def object_pool(objs: List):
    objs_pool=VGroup()
    for obj in objs:
        o=Text(f"{obj}").set_color(YELLOW)
        objs_pool+=o
    objs_pool.arrange(DOWN,buff=0.7)
    return objs_pool
    
    
def rect_with_label(label: str,h:int,w:int):
    header_rect=Rectangle(height=0.5,width=w)
    header_txt=Text(label).scale(0.4).move_to(header_rect.get_center())
    container_rect=Rectangle(height=h,width=w)
    vg=VGroup(VGroup(header_rect,header_txt),container_rect).arrange(DOWN,buff=0.01)
    return vg
    
    
    
    