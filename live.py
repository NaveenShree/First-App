from kaki.app import App
from kivy.factory import Factory as F
import os

class Live(App):
    CLASSES ={
        "UI":"main"
        }
    KV_FILES={
        os.path.join(os.getcwd(),"layout.kv")
        }
    AUTORELOADER_PATHS=[
        (".",{"recursive":True}),
        ]
    def build_app(App):
        return F.UI()
    def on_start(self):
        if os.path.isfile("./history.txt"):
            pass
        else:
            open("history.txt","w")

Live().run()
