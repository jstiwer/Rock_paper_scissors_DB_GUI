import tkinter as tk
from client.gui_app import Frame, menu_bar

def main():
    root = tk.Tk()
    root.title('Rock_paper_Scissors')
    root.minsize(800,600)
    #root.iconbitmap('img\icon.ico')
    root.resizable(0,0)
    menu_bar(root)

    app = Frame(root = root)

    app.mainloop()

if __name__ == '__main__':
    main()
