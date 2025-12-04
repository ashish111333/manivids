


from manim import *
from common.array import create_array,object_pool,rect_with_label
from voiceover import create_voice_file
from pathlib import Path

config.disable_caching=True

class LruScene(Scene):
    def construct(self):
        intro_text=Text("LRU CACHE",gradient=(BLUE,GREEN)).scale(0.4)
        if not Path("intro_text.mp3").exists():
                    create_voice_file(
                        "hi, in this video we will talk a bit about LRU cache...how it works? and how you can create one","intro_text")
            

        self.add(intro_text)
        self.add_sound("intro_text.mp3")
        self.wait(3)
        self.play(intro_text.animate.scale(4),run_time=5)
        self.remove(intro_text)
        cache_ex=["hello",1,"{name: titi}"]
        arr=create_array(1.3,3,3)
        pool=object_pool(cache_ex).scale(0.7)
        
        prog_rect=rect_with_label("program",4,3).move_to(pool.get_center())
        
        mem_rect=rect_with_label("memory",4,3).move_to(arr.get_center())
        arr.shift(DOWN*0.27)
        prog_grp=VGroup(prog_rect,pool).shift(RIGHT*2)
        mem_grp=VGroup(mem_rect,arr)
        mem_speech="""
        so here's an array in memory that will be  acting as cache.
        It will take objects  from your program and store  them in this array.
 
        """
        if not Path("prog_intro.mp3").exists():
            create_voice_file(mem_speech,"prog_intro")
            
        self.add_sound("prog_intro.mp3")    
        
        self.play(FadeIn(mem_grp),run_time=6)
        self.play(mem_grp.animate.shift(LEFT*2),run_time=1.2)
        
        prog_speech="""
        on the right, there's a program that has three objects that it wants to store.
        a string object...an integer object and a composite object. 
        """
        if not Path("prog_speech.mp3").exists():
            create_voice_file(prog_speech,"prog_speech")
        self.add_sound("prog_speech.mp3")
        self.wait(2)
        self.play(FadeIn(prog_grp),run_time=2)
        self.play(prog_grp.animate.shift(RIGHT),run_time=4.3)
        
        # push items from program to memory array
        
            
            
      
      
        
        
        
        
        
        
          
        
        
        
        
        

    
        

