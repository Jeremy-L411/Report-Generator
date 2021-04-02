"""Makes random generated bonus and expense files to show how the report
    generation program works, receives one variable for path and returns
    none."""

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
expenses = []
bonus = []
os.chdir(path)


def get_random_date():

    year = '%02d' % random.choice(range(2000, 2018))
    month = '%02d' % random.choice(range(1, 13))
    day = '%02d' % random.choice(range(1, 29))
    return '{2}-{0}-{1}'.format(month, day, year)

for i in range(50):
    employee_tmp = [random.choice(techs), get_random_date(), round(random.uniform(0, 400), 2)]
    expenses.append(employee_tmp)

for i in range(0):
    bonus_tmp = [random.choice(techs), get_random_date(), random.randrange(0, 1250, 250),
                 random.randrange(0, 750, 150), random.randrange(0, 1250, 250)]
    bonus.append(bonus_tmp)

for i in range(len(expenses)):
    ename, edate, total = expenses[i]
    wb = xlsxwriter.Workbook('Test_Expense ' + ename + str(i) + '.xlsx')
    ws = wb.add_worksheet('Expenses')

    ws.write('B5', ename)
    ws.write('B3', edate)
    ws.write('J30', total)

    wb.close()

for i in range(len(bonus)):
    bname, bdate, travel, on_call, call_cases = bonus[i]
    wb = xlsxwriter.Workbook('Test_Bonus ' + bname + str(i) + '.xlsx')
    ws = wb.add_worksheet('Bonuses')

    ws.write('C3', bname)
    ws.write('C4', bdate)
    ws.write('B19', travel)
    ws.write('D19', on_call)
    ws.write('F19', call_cases)

    wb.close()
