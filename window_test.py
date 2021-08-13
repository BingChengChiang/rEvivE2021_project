import tkinter as tk
from tkinter import ttk

nameList = ['石門水庫', '翡翠水庫', '寶山第二水庫', '永和山水庫', '明德水庫', '鯉魚潭水庫', '德基水庫', '石岡壩', '霧社水庫', '日月潭水庫', '集集攔河堰', '湖山水庫', '仁義潭水庫', '白河水庫', '烏山頭水庫', '曾文水庫', '南化水庫', '阿公店水庫', '高屏溪攔河堰', '牡丹水庫']
dayList = [i + 1 for i in range(31)]
monthList = [i + 1 for i in range(12)]
yearList = [i for i in range(2022,1969,-1)]
unitList = ["毫米","萬立方公尺","萬立方公尺","公尺","公尺","萬立方公尺","%"]
titleList = ["集水區降雨量","進水量","出水量","與昨日水位差","水位","有效蓄水量","蓄水量百分比"]

class Window:

    def __init__(self, title='Water Reservoir Crawling System', geometry='320x320'):
        # open a window
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(geometry)

        tk.Label(self.root, text = "Select Water Reservoir Name").pack()
        # name list
        self.nameBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.nameBox["values"] = nameList
        self.nameBox.current(3)
        self.nameBox.pack()

        tk.Label(self.root, text = "Select Plot Variable").pack()
        # choice list
        self.choiceBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.choiceBox["values"] =  [a +'（'+ b +'）' for a, b in zip(titleList, unitList)]
        self.choiceBox.current(6)
        self.choiceBox.pack()

        tk.Label(self.root, text = "Select Start Date").pack()
        # start year list
        self.startYearBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.startYearBox["values"] = yearList
        self.startYearBox.current(1)
        self.startYearBox.pack()
        # start month list
        self.startMonthBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.startMonthBox["values"] = monthList
        self.startMonthBox.current(6)
        self.startMonthBox.pack()
        # start day list
        self.startDayBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.startDayBox["values"] = dayList
        self.startDayBox.current(0)
        self.startDayBox.pack()

        tk.Label(self.root, text = "Select End Date").pack()
        # end year list
        self.endYearBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.endYearBox["values"] = yearList
        self.endYearBox.current(1)
        self.endYearBox.pack()
        # end month list
        self.endMonthBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.endMonthBox["values"] = monthList
        self.endMonthBox.current(7)
        self.endMonthBox.pack()
        # end day list
        self.endDayBox=ttk.Combobox(self.root,textvariable=tk.StringVar()) 
        self.endDayBox["values"] = dayList
        self.endDayBox.current(0)
        self.endDayBox.pack()

        # close the window
        self.search_button = tk.Button(self.root, text = 'Search', command=self.quit)
        self.search_button.pack()

        self.root.mainloop()

    def quit(self):
        self.name = self.nameBox.get()
        self.startDate = (int(self.startYearBox.get()), int(self.startMonthBox.get()), int(self.startDayBox.get()))
        self.endDate = (int(self.endYearBox.get()), int(self.endMonthBox.get()), int(self.endDayBox.get())) 
        self.choice = self.choiceBox.current()
        self.root.destroy()