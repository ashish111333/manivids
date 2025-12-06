from manim import *

def create_dll(l:int,sq_len:float):
    dll_grp=VGroup()
    for _ in range(l):
        dll_grp+=create_node(sq_len)
    
    dll_grp.arrange(direction=RIGHT,buff=1)
    return dll_grp    
        
        
    



def create_node(sq_side_l:float):
    
    node=Square(sq_side_l).set_color(BLUE_B)
    l_ptr=Text("L_PTR").set_color(RED_B)
    r_ptr=Text("R_PTR").set_color(RED)
    data=Text("Data").move_to(node.get_center()+UP*0.4)
    ptr_grp=VGroup(l_ptr,r_ptr).move_to(node.get_center()-UP*0.4)
    
    l_arr=Arrow(start=node.get_left()-UP*0.4,end=node.get_left()-LEFT-DOWN*0.4)
 
    r_arr=Arrow(start=node.get_right()+UP*0.4,end=node.get_right()+RIGHT+0.4*UP)
    grp=VGroup(node,data,ptr_grp,l_arr,r_arr)
    return grp
    
    
    
    