import tkinter

class OutputWindow:
    def __init__(self):        
        self.output_window = tkinter.Tk()
        
        global allList
        
        self.textBox = tkinter.Text(self.output_window)
        self.textBox.insert(0.0, ('\n'.join('{},'.format(k[1]) for k in enumerate(allList))))
        self.textBox.pack(side="left", fill="both")
        
        self.scrollBar = tkinter.Scrollbar(self.output_window, command=self.textBox.yview)
        self.scrollBar.pack(side="right", fill="y")
        self.textBox["yscrollcommand"] = self.scrollBar.set
        
        tkinter.mainloop()

class InputWindow:
    def __init__(self):
        self.input_window = tkinter.Tk()
        
        self.main_frame = tkinter.Frame(self.input_window)
        self.main_frame.pack(side="top", fill="both", expand=True)
        
        self.top_frame = tkinter.Frame(self.main_frame)
        self.bot_frame = tkinter.Frame(self.main_frame)
        self.top_frame.pack(side="top", fill="x", expand=False)
        self.bot_frame.pack(side="bottom", fill="both", expand=True)
        
        self.top_left = tkinter.Frame(self.top_frame)
        self.top_right = tkinter.Frame(self.top_frame)
        self.top_left.pack(side="left", fill="x", expand=True)
        self.top_right.pack(side="right", fill="x", expand=True)
        
        self.bot_left = tkinter.Frame(self.bot_frame)
        self.bot_right = tkinter.Frame(self.bot_frame)
        self.bot_left.pack(side="left", fill="x", expand=True)
        self.bot_right.pack(side="right", fill="x", expand=True)
        
        
        self.len_label = tkinter.Label(self.top_left, text="Side Length:", width=20)
        self.len_input = tkinter.Entry(self.top_right, width=10)
        self.len_label.pack(side='left')
        self.len_input.pack(side='right')
        
        self.dim_label = tkinter.Label(self.bot_left, text="Block Dimensions:", width=20)
        self.dim_input = tkinter.Entry(self.bot_right, width=10)
        self.dim_label.pack(side='left')
        self.dim_input.pack(side='right')
        
        self.top_frame.pack()
                
        self.other_frame = tkinter.Frame(self.input_window)
        self.go_button = tkinter.Button(self.other_frame, text="Execute", command=self.pyramid)
        self.go_button.pack(side='left')
        self.other_frame.pack()
        
        tkinter.mainloop()
    
    def pyramid(self):
        size = int(self.len_input.get())
        dim = float(self.dim_input.get())
        
        global allList
        allList = []

        for z in range(size):
            for x in range(size - z):
                for y in range(size - z):
                    allList += [
                        [
                            float((x * dim) + ((dim / 2.0) * (z % 2)) + (z * (dim / 2.0)) - ((dim / 2.0) if (z % 2 == 1) else 0.0)),
                            float((y * dim) + ((dim / 2.0) * (z % 2)) + (z * (dim / 2.0)) - ((dim / 2.0) if (z % 2 == 1) else 0.0)),
                            float(z * dim)
                        ]
                    ]

        out_win = OutputWindow()

main_win = InputWindow()
