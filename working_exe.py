import csv
import datetime
from datetime import date

import tkinter as tk

def create_file():
	with open('leaving-history.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['staff_name', 'id', 'start_time', 'leaving_time', 'reason', 'department'])
 
def get_date():
	curr_date = date.today()
	date_str = curr_date.strftime("%d-%m-%Y")
	print(date_str)
	return date_str

def get_time():
	curr_time = datetime.datetime.now()
	hour = curr_time.hour
	minute = curr_time.minute
	if hour == 16 and (minute < 45 and minute > 15):
		hour = 16
		minute = 30
	elif hour == 19 and (minute < 45 and minute > 15):
		hour = 19
		minute = 30
	time_stamp = str(hour) + ":" + str(minute)
	print(type(hour))
	print(hour)
	print(minute)
	print(time_stamp)
	return time_stamp

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
('LÊ THÀNH TAM', '080427', 'B/T', 'RD'),
('TRƯƠNG THANH TUẤN', '101339', 'TEST REQUEST', 'RD'),
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
window = tk.Tk()
window.title("Personal Leaving History")
window.geometry("400x600")
window.configure(bg='#003039')


def on_leave_btn_click(button_text, button):
	
	staff = []
	date = get_date()
	time = get_time()
	for i in staffs_lst:
		update_staff = staff + [button_text[0], button_text[1], '16:30', time, button_text[2], button_text[3], date]
	print(update_staff)
	with open('leaving-history.csv', 'a', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(update_staff)
	# print(button_text)
	button.configure(state=tk.DISABLED, bg='gray')

for i in staffs_lst_2:
	leave_btn = tk.Button(window, text=f'{i[0]}', font=('Times new roman', 12), width=20,heigh=1, bg='white')
	leave_btn.configure(command=lambda i=i, btn=leave_btn: on_leave_btn_click(i, btn))
	leave_btn.pack()

window.mainloop()