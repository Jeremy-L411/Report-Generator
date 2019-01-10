"""Moves files to created or existing sorted folder in the
sequence of Name> Year> Month
"""

import os
import fnmatch
import shutil
import readFiles

start_path = '/Users/Desktop/TestEnviro/Start_Folder'
temp_path = '/Users/Desktop/TestEnviro'
sorted_folder = '/Users/Desktop/TestEnviro/Sorted_Files'


# creates temp folders for sorting
if os.path.exists(os.path.join(temp_path, 'Sorted_Files')):
    pass
else:
    os.makedirs(os.path.join(temp_path, 'Sorted_Files'))

if os.path.exists(os.path.join(temp_path, 'Expense')):
    pass
else:
    os.makedirs(os.path.join(temp_path, 'Expense'))

if os.path.exists(os.path.join(temp_path, 'Bonus')):
    pass
else:
    os.makedirs(os.path.join(temp_path, 'Bonus'))


exp_pattern = '*Expense*'
bon_pattern = '*Bonus*'

# moves files from start folder to temp folders
for root, dirs, files in os.walk(start_path):
    for filename in fnmatch.filter(files, exp_pattern):
        fullpath = os.path.join(root, filename)
        shutil.move(fullpath, os.path.join(temp_path, 'Expense'))

for root, dirs, files in os.walk(start_path):
    for filename in fnmatch.filter(files, bon_pattern):
        fullpath = os.path.join(root, filename)
        shutil.move(fullpath, os.path.join(temp_path, 'Bonus'))

# moves from temp folders to sorted folders in
# Name > Year > Month format
for root, dirs, files in os.walk(os.path.join(temp_path, 'Bonus')):
    for filename in files:
        if filename.endswith('.xlsx') or '.xls':
            if filename != '.DS_Store':
                bname, date = readFiles.read_bonus(os.path.join(root, filename))
                bdate = date.split('-')
                byear = bdate[0]
                bmonth = bdate[1]
                bpath = os.path.join(root, filename)
                if os.path.exists(os.path.join(sorted_folder, bname, byear, bmonth)):
                    shutil.move(bpath, os.path.join(sorted_folder, bname, byear, bmonth))
                else:
                    os.makedirs(os.path.join(sorted_folder, bname, byear, bmonth))
                    shutil.move(bpath, os.path.join(sorted_folder, bname, byear, bmonth))

for root, dirs, files in os.walk(os.path.join(temp_path, 'Expense')):
    for filename in files:
        if filename.endswith('.xlsx') or '.xls':
            if filename != '.DS_Store':
                expname, expdate = readFiles.read_expense(os.path.join(root, filename))
                edate = expdate.split('-')
                expyear = edate[0]
                expmonth = edate[1]
                epath = os.path.join(root, filename)
                if os.path.exists(os.path.join(sorted_folder, expname, expyear, expmonth)):
                    shutil.move(epath, os.path.join(sorted_folder, expname, expyear, expmonth))
                else:
                    os.makedirs(os.path.join(sorted_folder, expname, expyear, expmonth))
                    shutil.move(epath, os.path.join(sorted_folder, expname, expyear, expmonth))

os.rmdir(os.path.join(temp_path, 'Expense'))
os.rmdir(os.path.join(temp_path, 'Bonus'))
