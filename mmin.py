from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput



class My_wordApp(App):
    def build(self):
        self.operator = ["+","-","/","*"]
        self.last_was_oprator = None
        self.last_button = None

        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color= "black", foreground_color= "white"
                                  ,multiline = False,font_size= "50sp", halign ="right",readonly = True)
        main_layout.add_widget(self.solution)
        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            [".","0","c","+"],
        ]

        for row in buttons:
            h_layout= BoxLayout()
            for Label in row:
                button = Button(
                    text = Label, font_size=35,background_color="grey",pos_hint={"center_x": 0.5, "center_y":0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text = "=", font_size=35,background_color="grey",pos_hint={"center_x": 0.5, "center_y":0.5}
        )
        equal_button.bind(on_press=self.on_sollution)
        main_layout.add_widget(equal_button)

        return main_layout
    
    def on_button_press(self,instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'c':
            self.solution.text = ""

        else:
            if current and (
                self.last_was_oprator and button_text in self.operator):
                return
            elif current == "" and button_text in self.operator:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_oprator = self.last_button in self.operator
    def on_sollution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

        
if __name__ == "__main__":
    app = My_wordApp()
    app.run()