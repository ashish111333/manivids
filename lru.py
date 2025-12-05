


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
        self.wait(1)
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
        so here's an array in memory that will be  acting as cache. max capacity is three 
        It will take objects  from your program and store  them in this array.
 
        """
        self.wait(3)
        
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
        for i,pool_item  in zip(reversed(range(len(pool))),pool):
            self.play(Indicate(pool_item,color=PINK),run_time=2)
            self.play(pool_item.animate.move_to(arr[i].get_center()),run_time=1.7)
        
        # label the array 
        indx_labels=reversed([0,1,2])
        arr_indx_labels=object_pool(indx_labels)
        arr_indx_labels.next_to(prog_grp,LEFT+LEFT*0.5)
        arr_indx_labels.set_color(PURPLE)
        arr_indx_labels.space_out_submobjects(1.48)
        arr_indx_labels.scale(0.69).shift(LEFT*0.2).space_out_submobjects(1.2).shift(DOWN*0.4)
        label_speech="""
        let's label the indexes of the array.
        """
        
        if not Path("label_speech.mp3").exists():
            create_voice_file(label_speech,"label_speech")
        
        
        self.add_sound("label_speech.mp3")
        self.play(FadeIn(arr_indx_labels),run_time=1.5)
        exp_lru="""
        Now in lru cache we always keep the most recently used item at the front of the array as you can see our cache
        is full if the program tries to add any other object in the cache the cache will have to start evicting items
        and the least recently used one will go out first. 
        """
        if not Path("exp_lru.mp3").exists():
            create_voice_file(exp_lru,"exp_lru")
        self.add_sound("exp_lru.mp3")
        self.wait(17)   
        
            
        l1=Arrow(stroke_width=0.2,start=arr[0].get_center(),end=arr[0].get_center()+LEFT*4).rotate(PI/10,about_point=arr[0].get_center())
        l1_text=Text("most recent").set_color(RED).scale(0.39)
        l1_text.next_to(l1,l1.get_unit_vector())
        l2=Arrow(stroke_width=0.2,start=arr[2].get_center(),end=arr[2].get_center()+LEFT*4).rotate(PI/10,about_point=arr[2].get_center())
        l2_text=Text("least recent").set_color(RED).scale(0.39)
        l2_text.next_to(l2,direction=l2.get_unit_vector())
        
        temp_exp1="""
        so in this case our program was only adding items,so the most recent one is the one that was 
        lastly added.
        """
        
        if not Path("temp_exp1.mp3").exists():
            create_voice_file(temp_exp1,"temp_exp1")
        self.add_sound("temp_exp1.mp3")
        self.wait(5)
        
        self.play(FadeIn(l1),FadeIn(l1_text),run_time=2)
        
        temp_exp2="""
        and the least recently used is the string object hello.
        """
        if not Path("temp_exp2.mp3").exists():
            create_voice_file(temp_exp2,"temp_exp2")
        self.add_sound("temp_exp2.mp3")
        self.wait(3)    
        
        self.play(FadeIn(l2),FadeIn(l2_text),run_time=2)
        self.wait(2)
        self.remove(l1,l1_text,l2,l2_text)
        
        temp_exp3="""
        let's forget about adding more items to the cache for a sec, let's only focus on accessing items.
        suppose your program wants  the integer object 1. ...after you access it the cache will  reorder itself to make this 
        integer as most recent.
        """
        
        if not  Path("temp_exp3.mp3").exists():
            create_voice_file(temp_exp3,"temp_exp3")
        
        self.add_sound("temp_exp3.mp3")
        self.wait(10)
        self.play(Indicate(pool[1],color=PINK,scale_factor=2),run_time=1.8)
        # move 1 to top 
        arr_1_pos=arr[1].get_center()
        arr_0_pos=arr[0].get_center()
        
        self.play(pool[1].animate.move_to(arr_0_pos),pool[2].animate.move_to(arr_1_pos),run_time=2)
        
        # move hello to top
    
        temp_exp4="""
        what if program accesses string object hello ? , again the same thing the cache will move this to top of
        the array, because it's the most recent now.
        """
        if not Path("temp_exp4.mp3").exists():
            create_voice_file(temp_exp4,"temp_exp4")
        
        self.add_sound("temp_exp4")
        self.wait(9)
        self.play(Indicate(pool[1],color=PINK,scale_factor=1.8),run_time=1.8)
        self.play()
       
        # generalized array cache            
        
        
        
        # explain why dll is better and also compare
        
            

        
            
            
      
      
        
        
        
        
        
        
          
        
        
        
        
        

    
        

