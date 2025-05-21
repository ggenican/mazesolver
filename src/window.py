from tkinter import Tk, BOTH, Canvas



class Window():
    def __init__(self, width, heigth, title):
        self.__root = Tk()
        self.__root.title(title)
        self.canvas = Canvas(background="White", width=width, height=heigth)
        self.canvas.pack()
        self.running = False

    def __repr__(self):
        return f"WIDTH={self.width}, HEIGTH={self.heigth}"
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.running = True
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        while self.running:
            self.redraw()
            self.__root.update()
    
    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)