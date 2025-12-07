


from manim import *
from common.array import create_array,object_pool,rect_with_label
from voiceover import create_voice_file
from pathlib import Path
from typing import List
from common.dll import create_dll

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
        
        
        if not Path("prog_intro.mp3").exists():
            create_voice_file(mem_speech,"prog_intro")
            
        self.add_sound("prog_intro.mp3")    
        self.wait(1)
        self.play(FadeIn(mem_grp),run_time=6)
        self.play(mem_grp.animate.shift(LEFT*2),run_time=1.2)
        self.wait(1.5)
        
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
        self.wait(2)
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
        self.play(Indicate(pool[0],color=PINK,scale_factor=1.8),run_time=1.5)
        
        
        # move 0 to 1
        vgrp12=VGroup(pool[1],pool[2])
        pool0pos=pool[1].get_center()
        self.play(vgrp12.animate.shift(DOWN*1.3),pool[0].animate.move_to(pool0pos),run_time=3.8)
        
        temp_exp5="""
        so if you noticed ...shifting the string object hello, which was the last item in the cache aka the least recent item 
        it tooks us three shifts in this array. can you guess how much it would take for an array of size n ? 
        ...before I explain it ... let's look at what happens when our program wants to add more items to cache.

        """
        if not Path("temp_exp5.mp3").exists():
            create_voice_file(temp_exp5,"temp_exp5")
        self.add_sound("temp_exp5.mp3")
        self.wait(19)
        
        
        pool_item=Text("5").set_color(YELLOW).scale(0.8)
        pool_item.move_to(prog_rect.get_center())
        self.play(FadeIn(pool_item),run_time=2)
        
        temp_exp6="""
        so let's say now your program wants to add this integer item 5 to the cache.
        but the cache is full so it will evict the least recently  used item to make room for this 
        integer item.
        """
        if not Path("temp_exp6.mp3").exists():
            create_voice_file(temp_exp6,"temp_exp6")

        self.add_sound("temp_exp6.mp3")
        self.wait(14)
        
        # evict lru item
        vgrp012=VGroup(pool[0],pool[1],pool[2])
        self.play(vgrp012.animate.shift(DOWN*1.3),FadeOut(pool[2]),run_time=2)
        self.play(pool_item.animate.move_to(arr[0].get_center()),run_time=3)

        self.clear()
        # show generalized array cache with time complexity
        arr=create_array(0.6,1.2,10)
        
        arr_indx_labels_part1=[0,1,2,3,4,5]
        arr_indx_labels_grp=VGroup()
        for i,j in zip(arr[0:6],range(6)):
            arr_indx_labels_grp+=Text(str(j)).move_to(i.get_center()+LEFT*0.8).scale(0.5)
            
        arr_index_labels_part2:List[Mobject]=[Dot(0.01),Dot(0.01),Dot(0.01),Text("n")]  
        arr_index_labels_grp2=VGroup()
        for i,j in zip(arr[6:10],arr_index_labels_part2):
            arr_index_labels_grp2+=j.move_to(i.get_center()+LEFT*0.8).scale(0.5)
        final_grp=arr_indx_labels_grp+arr_index_labels_grp2
        
        
        
        temp_exp7="""
        an array perfectly tracks the most recent items added to it over a period of time ,
        but there's one problem, if we use array as a cache store sometimes cache would  need to push the last item
        to the very front to make it most recent. let's see how ... here's an array of max capacity n acting as cache. 
        
        """ 
        if not Path("temp_exp7.mp3").exists():
            create_voice_file(temp_exp7,"temp_exp7")
        self.add_sound("temp_exp7.mp3")
        self.wait(2.5)
        self.play(Create(arr),run_time=7)
        self.play(Create(final_grp),run_time=5)
        self.wait(3.9)

        temp_exp8="""
        now if you want to move the least recent item to the end of the array you would have to do 
        n operations can you see that ? 
        """
        if not Path("temp_exp8.mp3").exists():
            create_voice_file(temp_exp8,"temp_exp8")
        self.add_sound("temp_exp8.mp3")
        self.wait(7)
        
        temp_exp9="""
        this will move to the end of the array. that's one operation
        """
        if not Path("temp_exp9.mp3").exists():
        
            create_voice_file(temp_exp9,"temp_exp9")
        self.add_sound("temp_exp9")
        self.wait(1.3)
        self.play(Indicate(arr[0],scale_factor=1.08),run_time=2)
        brc=Brace(arr-arr[0],direction=RIGHT)
        brc_txt=Text("n-1").next_to(brc,direction=RIGHT)
        temp_exp10="""
        and the remaining n minus 1 items need to be moved one Up each so that will be n minus 1 operations.
        """
        if not Path("temp_exp10.mp3").exists():
            create_voice_file(temp_exp10,"temp_exp10")
        
        self.add_sound("temp_exp10.mp3")
        self.wait(2.8)
        self.play(Indicate(arr-arr[0],scale_factor=1.08),run_time=1.5)
        self.play(Create(brc),Create(brc_txt),run_time=1)
        grp=VGroup(arr,final_grp,brc,brc_txt)
        self.play(grp.animate.shift(LEFT*2),run_time=1)
        self.wait(1.8)
        temp_exp11="""
        so total operations will be n, so time complexity for array cache will be O of n.
        """
        if not Path("temp_exp11.mp3").exists():
            create_voice_file(temp_exp11,"temp_exp11")
        
        self.add_sound("temp_exp11")
        self.wait(2)
        txt=Text("Total operations  ").shift(RIGHT*1.2)
        txt1=MathTex(r"= n - 1 + 1 ").next_to(txt,direction=RIGHT*0.1)
        txt2=MathTex(r"= n").next_to(txt1,direction=RIGHT*0.1)
        self.wait(1.5)
        tc_txt=MathTex(r"O(n)").shift(RIGHT*1.2+DOWN*1.2)
        
        grp=VGroup(txt,txt1,txt2,tc_txt)
        grp.scale(0.8).shift(RIGHT+UP)
        
        self.play(Write(grp),run_time=3)
        self.wait(3)
         
        # explain why dll is better and also compare
        temp_exp12="""
        there's a better data structure to help us here, that is a doubly linked list.

        """
        if not Path("temp_exp12.mp3").exists():
            create_voice_file(temp_exp12,"temp_exp12")
        self.add_sound("temp_exp12")
        self.clear()  
        dll=create_dll(4,1.4)
        self.play(Create(dll),run_time=3)
        
        
        most_recent=Text("most recent").scale(0.5).set_color(RED)
        least_recent=Text("least recent").scale(0.5).set_color(RED)
        arrow_lst_recent=Arrow(start=dll[0].get_center()+UP*2,end=dll[0].get_center()+UP*0.8,stroke_width=0.5)
        arrow_mst_recent=Arrow(start=dll[3].get_center()+UP*2,end=dll[3].get_center()+UP*0.8,stroke_width=0.5)
        most_recent.next_to(arrow_mst_recent,direction=UP)
        least_recent.next_to(arrow_lst_recent,direction=UP)

        self.wait(2)
        
        temp_exp13="""
        so in an  actual LRU cache implemenation we use a linked list instead of an array to store items,
        simply because shifting the the least recently  used item to end is an O Of 1 operation.
        """
        if not Path("temo_exp13").exists():
            create_voice_file(temp_exp13,"temp_exp13")
        self.add_sound("temp_exp13.mp3")
        self.wait(12)
        temp_exp14="""
        so the first Node is least recent as it was added first.
        """
        if not Path("temp_exp14.mp3").exists():
            create_voice_file(temp_exp13,"temp_exp14")
        self.add_sound("temp_exp14.mp3")
        self.wait(3)    
        self.play(Indicate(dll[0]),run_time=1.5)
        self.play(Create(arrow_lst_recent),run_time=2)
        self.play(Create(least_recent),run_tim3=2)
        
        
        temp_exp15="""
        and the last node is the Most recent one.
        """
        if not Path("temp_exp15.mp3").exists():
            create_voice_file(temp_exp14,"temp_exp15")
        self.add_sound("temp_exp15.mp3")
        self.wait(2)
        self.play(Indicate(dll[3]),run_time=1.5)
        self.play(Create(arrow_mst_recent),run_time=2)
        self.play(Create(most_recent),run_time=1.5)
        self.wait(3)
        self.clear()
        
        end_tx="""
        That's it for this video if you enjoyed this make sure to give a thumbs up,
        make sure to check the description for LRU cache source code using linked list.
        ...  your feedback will help me make better videos. also tell me if you like these 
        animated videos or you prefer more manual face to face way of explaining concepts.
        Let me know.
        """
        if not Path("end_tx.mp3").exists():
            create_voice_file(end_tx,"end_tx")
            
        self.add_sound("end_tx.mp3")
        tx=Text("Thank you").scale(3).set_color_by_gradient(BLUE,GREEN)
        self.play(Create(tx),run_time=4)
        self.wait(3)
              
        # add an image of code maybe ?? :()
        
        
        
        

