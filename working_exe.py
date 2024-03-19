import csv
import datetime
from datetime import date
import pandas as pd

import tkinter as tk

def create_file():
	with open('leaving-history.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['staff_name', 'id', 'start_time', 'leaving_time', 'reason', 'department', 'date'])

def convert_csv_xlsx(file):
	data = pd.read_csv(file, dtype={1: str})
	print(data)
	data.to_excel('work-log.xlsx', index=False)
	print('Excel exported.')

def get_date():
	curr_date = date.today()
	date_str = curr_date.strftime("%d-%m-%Y")
	print(date_str)
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
	print(type(hour))
	print(hour)
	print(minute)
	print(time_stamp)
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
	for i in staffs_lst_2:
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
	print(button_text)
	button.configure(state=tk.DISABLED, bg='gray')
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
			else: print("Item not found in the list.")

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

	
	


staffs_lst = [
('LE PHUONG', '070032', 'TEST REQUEST', 'R-D'),
('TRUONG TU XUAN', '080262', 'TEST REQUEST', 'R-D'),
('TRUONG THANH TAM', '080427', 'B/T', 'R-D'),
('LE THANH TUAN', '101339', 'TEST REQUEST', 'R-D'),
('PHAM THI HUONG', '172684', 'TEST REQUEST', 'R-D'),
('NGUYEN HOANG VIET', '172759', 'TEST REQUEST', 'R-D'),
('NGUYEN THI HONG YEN', '172824', 'TEST REQUEST', 'R-D'),
('BUI DINH PHUC', '193273', 'TEST REQUEST', 'R-D'),
('TTRUONG VAN MINH', '203591', 'TEST REQUEST', 'R-D'),
('NGUYEN QUANG QUI', '203638', 'TEST REQUEST', 'R-D'),
('NGUYEN THI DIEM MY', '213714', 'TEST REQUEST', 'R-D'),
('LE MINH THANG', '223906', 'TEST REQUEST', 'R-D'),
('LE QUOC TRUNG', '224016', 'B/T', 'R-D'),
('NGUYEN TUAN ANH', '224057', 'TEST REQUEST', 'R-D'),
('TRAN VAN LUU', '234102', 'TEST REQUEST', 'R-D'),
('LE HUYNH ANH KHOA', '234168', 'B/T', 'R-D'),
('NGUYEN MAI PHUONG', '234170', 'TEST REQUEST', 'R-D'),
('PHAM NG NGOC TUYET', '234172', 'TEST REQUEST', 'R-D'),

]

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


root = tk.Tk()
root.title("Personal Leaving History")
root.geometry("400x700")
root.configure(bg='#003039')

export_btn = tk.Button(root, text='Export excel file', fg='#a52a2a', font='Arial', command=lambda: convert_csv_xlsx('leaving-history.csv'))
export_btn.pack()


for i in staffs_lst_2:
	leave_btn = tk.Button(root, text=f'{i[0]}', font=('Times new roman', 12), width=20,heigh=1, bg='white')
	leave_btn.configure(command=lambda i=i, btn=leave_btn: on_leave_btn_click(i, btn))
	leave_btn.pack()



open_subwindow = tk.Button(root, text='Chỉnh sửa (xoá mục)', command=open_list_recent_added, fg='white', bg='red' )
open_subwindow.pack()

root.mainloop()