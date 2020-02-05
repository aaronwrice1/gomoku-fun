from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import random

num_rows = 19
num_cols = 19


class TestApp(App):

    turn = 0
    buttons = []

    def build(self):

        layout = GridLayout(cols=num_cols)

        for i in range(num_rows):
            for j in range(num_cols):
                btn = Button()
                btn.bind(on_press=callback)
                self.buttons.append(btn)
                layout.add_widget(btn)

        return layout


def callback(instance):

    if app.turn == 0:
        instance.text = "x"

        # ai turn
        ai_turn()

    # for two player
        # app.turn = 1

    # else:
    #     instance.text = "o"
    #     app.turn = 0

    print('The button <%s> is being pressed' % instance.text)


def ai_turn():
    valid_options = [b for b in app.buttons if b.text == ""]
    random_choice = random.randint(0, len(valid_options) - 1)
    valid_options[random_choice].text = "o"


app = TestApp()
app.run()
