
import tkinter as tk
import time

class DigitalClock:
    def __init__(self, master):
        self.master = master
        master.title("Digital Clock")

        self.clock_label = tk.Label(master, font=('Arial', 100, 'bold italic'), bg='black', fg='aquamarine')
        self.clock_label.pack(fill='both', expand=1)

        self.start_button = tk.Button(master, text='Start', font=('Arial', 20), command=self.start_clock)
        self.start_button.pack(side='left', padx=10, pady=10)

        self.stop_button = tk.Button(master, text='Stop', font=('Arial', 20), command=self.stop_clock, state='disabled')
        self.stop_button.pack(side='left', padx=10, pady=10)

        self.reset_button = tk.Button(master, text='Reset', font=('Arial', 20), command=self.reset_clock, state='disabled')
        self.reset_button.pack(side='left', padx=10, pady=10)

        self.running = False
        self.elapsed_time = 0
        self.last_time = 0
        self.tick()

    def tick(self):
        if self.running:
            elapsed_time = time.time() - self.last_time
            self.elapsed_time += elapsed_time
            self.last_time = time.time()

        minutes, seconds = divmod(int(self.elapsed_time), 60)
        hours, minutes = divmod(minutes, 60)
        time_string = f'{hours:02d}:{minutes:02d}:{seconds:02d}'
        self.clock_label.config(text=time_string)

        self.clock_label.after(1000, self.tick)

    def start_clock(self):
        self.running = True
        self.last_time = time.time()
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')
        self.reset_button.config(state='normal')

    def stop_clock(self):
        self.running = False
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')

    def reset_clock(self):
        self.elapsed_time = 0
        self.start_button.config(state='normal')
        self.stop_button.config(state='disabled')
        self.reset_button.config(state='disabled')

root = tk.Tk()
clock = DigitalClock(root)
root.mainloop()
