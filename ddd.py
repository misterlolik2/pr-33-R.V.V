from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers import HtmlLexer



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
    def build(self):
        s=Scatter()
        fl=FloatLayout(size=(200, 200))
        s.add_widget(fl)        
        fl.add_widget(Button(text="Украина", font_size=20,
                             on_press=self.btn_press,
                             background_color=[1,1,0,1],
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(350, 280)))
        fl.add_widget(Button(text="РФ", font_size=20,
                             on_press=self.btn_press_r,
                             background_color=[0,1,2,2],                        
                             background_normal='',
                             size_hint=(.5, .25),
                             pos=(350, 220)))
        return s
  
    def btn_press(self, instance):
        instance.text='Слава Украине'
    def btn_press_r(self, instance):
        instance.text='Слава России'

if __name__=="__main__":
    myApp().run()
