from tkinter import Button, Frame


class Widget:
    def __init__(self) -> None:
        self.button = None


class BuilderInterface:
    def button(self):
        pass


class Builder(BuilderInterface):
    def __init__(self) -> None:
        self.widget = Widget()

    def button(
            self, main_window: Frame, text: str, command, height: int, width: int, highlightbackground: str, highlightthickness: int):
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
