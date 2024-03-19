# import time
# import datetime
# import subprocess

# def open_exe():
#     file_path = r'C:\Users\Administrator\Desktop\working_exe\working_exe.exe'
#     subprocess.Popen(file_path)

# def check_time():
# 	# time.sleep(3600)
# 	current = datetime.datetime.now()
# 	hour = current.hour
# 	min = current.minute
# 	print('current min: ' , hour)
# 	print('current min: ' , min)
# 	return hour

# while True:
# 	hour = check_time()
# 	t = 0
# 	if hour == 18:
# 		print('t: ', t)
# 		open_exe()
# 		break