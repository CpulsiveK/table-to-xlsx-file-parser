from tkinter import Button


class Widget:
    def __init__(self) -> None:
        self.button = None


class BuilderInterface:
    def button(self):
        pass


class Builder:
    def __init__(self) -> None:
        self.widget = Widget()

    def button(self, main_window, text, command, height, width, highlightbackground, highlightthickness):
        self.widget.button = Button(
            main_window,
            text=text,
            command=command,
            height=height,
            width=width,
            highlightbackground=highlightbackground,
            highlightthickness=highlightthickness
        ).grid()

        return self

    def build(self):
        return self.widget
