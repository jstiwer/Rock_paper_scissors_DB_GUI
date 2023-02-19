import tkinter as tk

def menu_bar(root):
    menu_bar = tk.Menu(root)
    root.config(menu = menu_bar, width=300, height=300)

    start_bar = tk.Menu(menu_bar, tearoff = 0)
    menu_bar.add_cascade(label='Start', menu=start_bar)
    start_bar.add_command(label='Play')
    start_bar.add_command(label='Statistics')
    start_bar.add_command(label='Exit', command=root.destroy)

    help_bar =  tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label='Help', menu=help_bar)
    help_bar.add_command(label='Github' )
  



class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, )
        self.root = root
        self.pack()
        self.config(width=780, height=590, background='#233142')