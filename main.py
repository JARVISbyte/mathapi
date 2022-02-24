# a python main file
import pyglet as p

print("Hello World!")


class MainWindow(p.window.Window):
    def __init__(self):
        super().__init__()
        self.set_size(960, 540)
        self.set_caption("a 3d render")

if __name__ == "__main__":
    window = MainWindow()
    p.app.run()
