import pandas as pd


def convert_csv_xlsx(file):
	data = pd.read_csv(file, dtype={1: str})
	data.to_excel(r'Y:\4. R&D\Report\CAR SAMPLE\Tuan Anh file\log\work-log.xlsx', index=False)
	print('Excel exported.')

convert_csv_xlsx('leaving-history.csv')