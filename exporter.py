import os
import glob
import csv
from xlsxwriter.workbook import Workbook
import json


def save_to_csv(jobs):
    with open('vacancy.csv', 'w', encoding = 'UTF-8') as file:
        file.writelines(['name', 'company', 'location', 'link']) 
        for job in jobs:
            vacancy = (list(job.values()))
            file.writelines(f'{vacancy}\n')

    with open('vacancy.csv', 'r', encoding = 'UTF-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
    with open('vacancy.json', 'w', encoding = 'UTF-8') as file:
        json.dump(rows, file)
    
    for csvfile in glob.glob(os.path.join('.', 'vacancy.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()    