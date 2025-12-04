


from manim import *
from common.array import create_array,object_pool,rect_with_label


class LruScene(Scene):
    def construct(self):
        intro_text=Text("LRU CACHE",gradient=(BLUE,GREEN)).scale(0.4)
        self.add(intro_text)
        self.play(intro_text.animate.scale(4),run_time=1.5)
        self.remove(intro_text)
        cache_ex=["hello",1,"{name: titi}"]
        arr=create_array(1.3,3,3)
        pool=object_pool(cache_ex).scale(0.7)
        
        prog_rect=rect_with_label("program",4,3).move_to(pool.get_center())
        
        mem_rect=rect_with_label("memory",4,3).move_to(arr.get_center())
        arr.shift(DOWN*0.27)
        prog_grp=VGroup(prog_rect,pool).shift(RIGHT*2)
        mem_grp=VGroup(mem_rect,arr)
        
        self.play(FadeIn(mem_grp),run_time=2)
        self.play(mem_grp.animate.shift(LEFT*2),run_time=1.2)
        self.play(FadeIn(prog_grp),run_time=2)
        self.play(prog_grp.animate.shift(RIGHT),run_time=1.3)
        
      
      
        
        
        
        
        
        
          
        
        
        
        
        

    
        

