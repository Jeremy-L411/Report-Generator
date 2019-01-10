"""Generates a specific number of fake files per random individual from
    techs list. same as make_random_fake_files with specific expense and
    bonus's per name"""

import xlsxwriter
import random
import os


techs = ["Bob Dole", "Marilyn Monroe", "Abraham Lincon", "Nelson Mandela",
         "Winston Churchill", "Donald Trump", "Bill Gates",
         "Margaret Thatcher", "Christopher Columbus", "Muhammad Ali",
         "Charles Darwin", "Paul McCartney", "Albert Einstein", "Elvis Presley",
         "Ludwig Beetoven", "Lyndon Johnson", "Rosa Parks",
         "George Orwell", "Dalai Lama", "Walt Disney", "Neil Armstrong"]

path = '/Users/Desktop/TestEnviro/Start_Folder'
os.makedirs(path)
expenses = []
bonus = []
os.chdir(path)


def get_random_date():
    
    year = '%02d' % random.choice(range(2017, 2018))
    month = '%02d' % random.choice(range(1, 13))
    day = '%02d' % random.choice(range(1, 29))
    return '{2}-{0}-{1}'.format(month, day, year)


for i in range(3):
    rtech = random.choice(techs)
    for j in range(10):
        etmp = [rtech, get_random_date(), round(random.uniform(0, 400), 2)]
        expenses.append(etmp)

    for k in range(10):
        btemp = [rtech, get_random_date(), random.randrange(0, 1250, 250),
                 random.randrange(0, 750, 150), random.randrange(0, 1250, 250)]
        bonus.append(btemp)

    for l in range(len(expenses)):
        ename, edate, total = expenses[l]
        wb = xlsxwriter.Workbook('Test_Expense ' + ename + str(l) + '.xlsx')
        ws = wb.add_worksheet('Expenses')

        ws.write('B5', ename)
        ws.write('B3', edate)
        ws.write('J30', total)

        wb.close()

    for m in range(len(bonus)):
        bname, bdate, travel, on_call, call_cases = bonus[m]
        wb = xlsxwriter.Workbook('Test_Bonus ' + bname + str(m) + '.xlsx')
        ws = wb.add_worksheet('Bonuses')

        ws.write('C3', bname)
        ws.write('C4', bdate)
        ws.write('B19', travel)
        ws.write('D19', on_call)
        ws.write('F19', call_cases)

        wb.close()
