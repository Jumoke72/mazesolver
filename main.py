from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        super().__init__()
        self.__root = Tk()
        self.__root.title = "My Maze Solver"
        self.canvas = Canvas(self.__root, {"bg": "white"}) 
        self.canvas.pack()
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)


    #redraw all the graphics in the window
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update() #update_idletasks()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
            
def main():
    win = Window(800, 600)
    win.wait_for_close()

main()
