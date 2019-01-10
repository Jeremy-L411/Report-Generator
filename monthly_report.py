""" generates report for each tech every month at the
    end of the month creates a multisheet xlsx file for
    expenses and bonuses
"""

import os
import re
import readFiles
import generateReport

organized = '/Users/Desktop/TestEnviro/Sorted_Files'

name = re.compile(r"((?:[a-z]+|\s)*)")

for root, dirs, files in os.walk(organized, topdown=True):
    for folder in sorted(dirs):
        if re.match(name, folder) is not None and len(folder) > 4:
            newdir = os.path.join(root, folder)

            for subroot, subdirs, rootfiles in os.walk(newdir):

                expense = []
                bonus = []
                for subdir in sorted(subdirs):
                    if len(subdir) == 2:
                        froot = os.path.join(root, folder, subroot, subdir)

                        for fin_root, fin_dirs, subfiles in os.walk(froot):
                            for subfile in sorted(subfiles):
                                if subfile.endswith('.xlsx') or '.xls':
                                    if subfile != '.DS_Store':

                                        tmp = os.path.join(root, folder, subroot, subdir, subfile)
                                        save = os.path.join(root, folder, subroot, subdir)

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
                                                                         expense, subdir, bonus, '_Expense_Bonus_')
                                        except KeyError:
                                            pass
