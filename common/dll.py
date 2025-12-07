from manim import *

def create_dll(l:int,sq_len:float):
    dll_grp=VGroup()
    for _ in range(l):
        dll_grp+=create_node(sq_len)
    
    dll_grp.arrange(direction=RIGHT,buff=1)
    return dll_grp.space_out_submobjects(0.63)    
        
        
    



def create_node(sq_side_l:float):
    
    node=Square(sq_side_l).set_color(BLUE_B)

    data=Text("data").move_to(node.get_center()).scale(0.5)
    l_arr=Arrow(start=node.get_left()-UP*0.4,end=node.get_left()-UP*0.4-1.5*RIGHT)
 
    r_arr=Arrow(start=node.get_right()+UP*0.4,end=node.get_right()+1.5*RIGHT+0.4*UP)
    grp=VGroup(node,data,l_arr,r_arr)
    return grp
    
    
    
    