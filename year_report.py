"""For each name in the sorted directory it creates a yearly summary of
    expenses and bonuses in a multisheet xlsx file"""


import os
import re
import generateReport
import readFiles

organized = '/Users/Desktop/TestEnviro/Sorted_Files'

year = re.compile(r"\d\d\d\d")
name = re.compile(r"((?:[a-z]+|\s)*)")

for root, dirs, files in os.walk(organized, topdown=True):
    for folder in sorted(dirs):
        if re.match(name, folder) is not None:
            newdir = os.path.join(root, folder)

            for subroot, subdirs, subfiles in os.walk(newdir):
                for subdir in sorted(subdirs):
                    if re.match(year, subdir):
                        fdir = os.path.join(root, folder, subdir)
                        expense = []
                        bonus = []
                        save = os.path.join(root, folder, subdir)

                        for froot, fdrirs, ffiles in os.walk(fdir):
                            for file in sorted(ffiles):
                                if file != '.DS_Store':
                                    if '_Expense_Bonus_' not in file:
                                        tmp = os.path.join(root, folder, subdir, froot, file)

                                        try:
                                            edate, etotal = readFiles.expense_variables(tmp)
                                            expense.append([edate, etotal])
                                        except KeyError:
                                            pass

                                        try:
                                            bdate, btravel, bon_call, bcall_cases = readFiles.bonus_variables(tmp)
                                            bonus.append([bdate, btravel, bon_call, bcall_cases])
                                        except KeyError:
                                            pass
                                        try:
                                            generateReport.create_report(save, folder,
                                                                         expense, subdir, bonus, '_Year_End_')
                                        except KeyError:
                                            pass
