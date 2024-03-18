import datetime
# from datetime import date
# from datetime import datetime
import csv
import pandas as pd

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

def create_file():
	with open('leaving-history.csv', 'w', encoding='utf-8', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['staff_name', 'id', 'start_time', 'leaving_time', 'reason', 'department', 'date'])

create_file()