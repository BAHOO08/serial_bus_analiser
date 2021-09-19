#from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter import scrolledtext

class Gui:
    window = tk.Tk()
    comport_cb = Combobox()
    boud_rate_cb = Combobox()
    connect_pb = tk.Button()
    log_te = scrolledtext.ScrolledText()
    mb_table = ttk.Treeview()

    _scroll_pane_mb_table = ttk.Scrollbar()
    def gui_creation(self): 
        self.window.title("Serial bus analiser")
        self.window.geometry('800x400')
        self.init_comport_cb()
        self.init_boudrate_cb()
        self.init_connect_pb(row=0, column=2)
        self.init_log_te()
        self.init_mb_table(column=1, row=1)

    def start_app(self):
        self.window.mainloop()

    def init_mb_table(self, row: int, column: int):
        # tree headings - по умолчанию (нулевой столбец)
        self.mb_table = ttk.Treeview(self.window, show='headings')
        self.mb_table.grid(row=row, column=column)
        self.mb_table['columns'] = ['id', 'data type', 'value']
        self._scroll_pane_mb_table = ttk.Scrollbar(self.window, 
                                                   command=self.mb_table.yview)
        self.mb_table.configure(yscrollcommand=self._scroll_pane_mb_table.set)
        #self._scroll_pane_mb_table.pack(side=tk.RIGHT, fill=tk.Y)


        for header in self.mb_table['columns']:
            self.mb_table.heading(header, text=header, anchor='center')
            self.mb_table.column(header, anchor='center')

    # Инициализация комбобоксов
    def init_comport_cb(self):
        """
        Настройка combobox ком порта
        """
        self.comport_cb = Combobox(self.window)
        self.comport_cb['values'] = (1, 2, 3)
        self.comport_cb.current(1)
        self.comport_cb.grid(column=0, row=0)

    def init_boudrate_cb(self):
        """
        Настройка combobox с скоростью
        """
        self.boud_rate_cb = Combobox(self.window)
        self.boud_rate_cb['values'] = (9600, 19200)
        self.boud_rate_cb.current(1)
        self.boud_rate_cb.grid(column=1, row=0)

    # Настройка поля с логом
    def init_log_te(self):
        self.log_te = scrolledtext.ScrolledText(self.window, width=40, height=10)
        self.log_te.grid(column=0, row=1)

    def init_connect_pb(self, column: int, row: int):
        self.connect_pb = tk.Button(self.window, text='connect')
        self.connect_pb.grid(column=column, row=row)

    def update_coms(self, data: list):
        self.comport_cb['values'] = tuple(data)

    def get_choosed_com(self) -> str:
        self.comport_cb.get()
