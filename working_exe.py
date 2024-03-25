"""
MyApp - A Professional Technology Application
Author: Tuan Anh
Date: 03/25/2024

This application is the property of Tuan Anh. All rights reserved.
"""
import csv
import datetime
from datetime import date
import pandas as pd
import sys
import tkinter as tk
import os


staffs_lst_2 = [
('LÊ PHƯƠNG', '070032', 'TEST REQUEST', 'RD'),
('TRƯƠNG TƯ XUÂN', '080262', 'TEST REQUEST', 'RD'),
('TRƯƠNG THÀNH TAM', '080427', 'B/T', 'RD'),
('LÊ THANH TUẤN', '101339', 'TEST REQUEST', 'RD'),
('PHẠM THỊ PHƯƠNG', '172684', 'TEST REQUEST', 'RD'),
('NGUYỄN HOÀNG VIỆT', '172759', 'TEST REQUEST', 'RD'),
('NGUYỄN THỊ HỒNG YẾN', '172824', 'TEST REQUEST', 'RD'),
('BÙI ĐÌNH HỒNG PHÚC', '193273', 'TEST REQUEST', 'RD'),
('TRƯƠNG VĂN MINH', '203591', 'TEST REQUEST', 'RD'),
('NGUYỄN QUANG QUÍ', '203638', 'TEST REQUEST', 'RD'),
('NGUYỄN THỊ DIỄM MY', '213714', 'TEST REQUEST', 'RD'),
('LÊ MINH THẮNG', '223906', 'TEST REQUEST', 'RD'),
('LÊ QUỐC TRUNG', '224016', 'B/T', 'RD'),
('NGUYỄN TUẤN ANH', '224057', 'TEST REQUEST', 'RD'),
('TRẦN VĂN LƯU', '234102', 'TEST REQUEST', 'RD'),
('LÊ HUỲNH ANH KHOA', '234168', 'B/T', 'RD'),
('NGUYỄN MAI PHƯƠNG', '234170', 'TEST REQUEST', 'RD'),
('PHẠM NG NGỌC TUYẾT', '234172', 'TEST REQUEST', 'RD'),
]

def create_file():
	with open('leaving-history.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['staff_name', 'id', 'start_time', 'leaving_time', 'reason', 'department', 'date'])

def convert_csv_xlsx(file):
	data = pd.read_csv(file, dtype={1: str})
	# data.to_excel('work-log.xlsx', index=False)
	storage_path = 'Y:/4. R&D/Report/CAR SAMPLE/CHECK-IN/overtime-log.xlsx'
	if os.path.exists(storage_path):
		data.to_excel(r'Y:/4. R&D/Report/CAR SAMPLE/CHECK-IN/overtime-log.xlsx', index=False)
		print("Excel exported to'Y:/4. R&D/Report/CAR SAMPLE/CHECK-IN/overtime-log.xlsx'")
	else:
		print('Storage destination unavailable, excel file changed save to root folder.')
		data.to_excel('overtime-log.xlsx', index=False)

def open_export_folder():
	export_path = 'Y:/4. R&D/Report/CAR SAMPLE/CHECK-IN'
	os.startfile(export_path)

def get_date():
	curr_date = date.today()
	date_str = curr_date.strftime("%d-%m-%Y")
	return date_str

def get_time():
	curr_time = datetime.datetime.now()
	hour = curr_time.hour
	minute = curr_time.minute
	if hour == 16 and (minute < 45 and minute > 10):
		hour = 16
		minute = 30
	elif hour == 19 and (minute < 45 and minute > 10):
		hour = 19
		minute = 30
	time_stamp = str(hour) + ":" + str(minute)
	# print(time_stamp)
	return time_stamp

def get_name_of_weekday():
	import datetime
	current_date = datetime.datetime.now()
	week_day = current_date.weekday()
	# week_day = 6
	# week_day_name = datetime.datetime.strftime(current_date, '%A')
	return week_day

def on_leave_btn_click(button_text, button):
	staff = []
	date = get_date()
	time = get_time()
	start_time = None
	weekday = get_name_of_weekday()
	if weekday == 6:
		start_time = '7:30'
	else: start_time = '16:30'
	update_staff = staff + [button_text[0], button_text[1], start_time, time, button_text[2], button_text[3], date]
	print(update_staff)
	with open('leaving-history.csv', 'a', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(update_staff)
	button.configure(state=tk.DISABLED, bg='gray')
	# display.write(f"{update_staff[0]} [{update_staff[1]}] {time}\n")
	# if button['background'] == 'white':
	# 	button['background'] = 'grey'
	# else:
	# 	button['background'] = 'white'

def open_list_recent_added():
	subwindow = tk.Toplevel(root)
	subwindow.title("Recent added")
	subwindow.geometry("500x700")

	def toggle_button(line, btn):
		btn.configure(state=tk.DISABLED, bg='grey')
		lines = []
		with open('leaving-history.csv', 'r', encoding='utf-8', newline='') as file:
			reader = csv.reader(file)
			for row in reader:
				lines.append(row)
		for i in lines:
			if line == i:
				lines.remove(line)
				print('Item removed successfully.')

		with open('leaving-history.csv', 'w', encoding='utf-8', newline='') as file:
			writer = csv.writer(file)
			for row in lines:
				writer.writerow(row)

	with open('leaving-history.csv', 'r', encoding='utf-8') as file:
		reader = csv.reader(file)
		lines = list(reader)

	last_20_lines = lines[-20:]
	for line in last_20_lines:
		item_lst = tk.Button(subwindow, text=line, width=700, bg='white')
		item_lst.configure(command=lambda i=line, btn=item_lst: toggle_button(i, btn))
		item_lst.pack()

class ConsoleOutput(tk.Text):

	def write(self, message):
		self.insert(tk.END, message)
		self.see(tk.END)


def set_normal_state_btn():
	for btn in btn_container_1.winfo_children():
		btn.configure(state=tk.NORMAL)
		btn.configure(bg='white')
	for btn in btn_container_2.winfo_children():
		btn.configure(state=tk.NORMAL)
		btn.configure(bg='white')


convert_csv_xlsx('leaving-history.csv')
root = tk.Tk()
root.title("Personal Leaving History")
root.geometry("380x600")
root.configure(bg='#003039')

# display = ConsoleOutput(root, bg='black',fg='#55f210', height=10, width=47)
# display.place(x=0, y=0)
# sys.stdout = display

btn_container_1 = tk.Frame(root)
btn_container_1.place(x=0, y=250)
for i in staffs_lst_2[:9]:
	leave_btn = tk.Button(btn_container_1, text=f'{i[0]}', font=('Times new roman', 12), width=20,heigh=1)
	leave_btn.configure(command=lambda i=i, btn=leave_btn: on_leave_btn_click(i, btn))
	leave_btn.pack()
btn_container_2 = tk.Frame(root)
btn_container_2.place(x=190, y=250)
for i in staffs_lst_2[9:]:
	leave_btn = tk.Button(btn_container_2, text=f'{i[0]}', font=('Times new roman', 12), width=20,heigh=1)
	leave_btn.configure(command=lambda i=i, btn=leave_btn: on_leave_btn_click(i, btn))
	leave_btn.pack()

edit_btn = tk.Button(root, text='Chỉnh sửa (xoá mục)', command=open_list_recent_added, fg='#a52a2a', width=15, height=1 )
edit_btn.place(x=102, y=205)

tools_container = tk.Frame(root)
tools_container.place(x=0, y=200)
export_btn = tk.Button(root, text='Export excel file', width=13, fg='#a52a2a', command=lambda: convert_csv_xlsx('leaving-history.csv'))
export_btn.place(x=0, y=170)

open_folder_btn = tk.Button(root, text='Open file location...', command=lambda: open_export_folder())
open_folder_btn.place(x=102, y=170)

refesh_btn = tk.Button(root, text='Refesh all button', width=13, command=lambda: set_normal_state_btn())
refesh_btn.place(x=0, y=205)

excel_directory = tk.Label(root, text='Check-in tool - Author: Tuan Anh - Date: 03-25-2024-All rights reserved', fg='#55f210', bg='black')
excel_directory.place(x=0, y=580)




root.mainloop()
convert_csv_xlsx('leaving-history.csv')
