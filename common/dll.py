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
    l_arr=Arrow()
    r_arr=Arrow()    
    grp=VGroup(node,data,ptr_grp)
    return grp
    
    
    
    