from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory as F
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
import math
import os
from kivy.properties import StringProperty

Window.size=360,640

class UI(F.ScreenManager):

    prvs=StringProperty(f"{open('history.txt').read()}")
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.grd_btns=self.ids.grd_btn
        self.calculation=self.ids.clcltns

        button=[
            "CE","C","/","x",
            "7","8","9","-",
            "4","5","6","+",
            "1","2","3","(",
            ")","0","."
        ]
        for btn in button:
            btns=(MDFlatButton(
                text=btn,
                size_hint=(1,1),
                md_bg_color = (62/255,62/255,62/255,255/255),
                font_size="25dp",
                theme_text_color="Custom",
                text_color=(1,1,1,.5)
                ))
            btns.bind(on_release = self.text_input)
            self.grd_btns.add_widget(btns)
        rslt=(MDFlatButton(
            text="=",
            size_hint=(1,1),
            md_bg_color = (0/255,255/255,62/255,125/255),
            font_size="30dp",
            theme_text_color="Custom",
            text_color=(1,1,1,1),
            ))
        rslt.bind(on_release = self.result)
        self.grd_btns.add_widget(rslt)
    def drpdwn(self,btn):
        self.menu_list=[
            {
                "viewclass":"OneLineListItem",
                "text":"Scientific",
                "on_release":lambda x="Scientific":self.sci(),
            }
            ]
        self.menu=MDDropdownMenu(
             items=self.menu_list,
             width_mult=4
            )
        self.menu.caller=btn
        self.menu.open()

        
    def sci(self):
        sci_btn=[
            "sin(","cos(","tan(",
            "X^","In(","abs(",
            "log("
            ]
        if self.grd_btns.cols==4 and self.grd_btns.rows==5:
            self.grd_btns.cols=5
            self.grd_btns.rows=6

            for btn in sci_btn:
                btns=(MDFlatButton(
                    text=btn,
                    size_hint=(1,1),
                    md_bg_color=(62/255,62/255,62/255,255/255),
                    font_size="25dp",
                    theme_text_color="Custom",
                    text_color=(1,1,1,.5)
                ))
                btns.bind(on_release=self.text_input)
                self.grd_btns.add_widget(btns)
            else:
                pass
    def text_input(self,write):
        self.calculations=self.ids.clcltns
        self.calculations.text += write.text

        if write.text=="CE":
            self.calculations.text=" "
        if write.text=="C":
            self.calculations.text=self.calculations.text[:-2]
    def result(self,*args):
        self.function=str(self.calculations.text)
        self.ans=self.ids.ans
        self.history=self.ids.hst

        if "x" in self.function:
            self.function = self.function.replace("x","*")
        try:
            if "sin" in self.function or "cos" in self.function or "tan" in self.function or "abs" in self.function or "^" in self.function:
                self.function=self.function.replace("sin(","math.sin((math.pi/180)*")
                self.function=self.function.replace("cos(","math.cos((math.pi/180)*")
                self.function=self.function.replace("tan(","math.tan((math.pi/180)*")
                self.function=self.function.replace("abs(","math.fabs(")
                self.function=self.function.replace("^","**")
            
                result_ = eval(self.function)
                self.ans.text=str(result_)
            else:
                result_ = eval(self.function)
                self.ans.text=str(result_)
            if "log"in self.function or "In" in self.function:
                self.function=self.function_.replace("log(","math.log10(")
                self.function=self.function_.replace("In(","math.log(")

                result=eval(self.function)
                self.anstext=str(result_)

            else:
                result=eval(self.function)
                self.anstext=str(result_)
                
             
        except Exception:
            self.calculations.text="Error!!"

        with open("history.txt","a") as f:
            f.write(f"{self.function} \n Ans: {self.ans.text}\n\n")

        self.history.text=open("history.txt").read()
    def histry(self,root):
        root.current="history"
        root.transition.direction="left"
    def main_scrn(self,root):
        root.current="main"
        root.transition.direction="right"


        
    Builder.load_file("layout.kv")

class Main(MDApp):
    def build(self):
        return UI()
    def on_start(self):
        if os.path.isfile("./history.txt"):
            pass
        else:
            open("history.txt","w")
if __name__ == "__main__":
    Main().run()
