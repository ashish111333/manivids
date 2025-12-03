


from manim import *
from common.array import create_array,object_pool,rect_with_label


class LruScene(Scene):
    def construct(self):
        intro_text=Text("LRU CACHE",gradient=(BLUE,GREEN)).scale(0.4)
        self.add(intro_text)
        self.play(intro_text.animate.scale(4),run_time=1.5)
        self.remove(intro_text)
        cache_ex=["hello",1,"{name: titi}"]
        arr=create_array(3,3).scale(0.4)
        pool=object_pool(cache_ex).scale(0.7)
        elps=Ellipse(3,4).set_color(GREEN)
        pool.move_to(elps.get_center())
        arr.move_to(LEFT)
        
        self.play(FadeIn(arr))
        
        
        
        
          
        
        
        
        
        

    
        

