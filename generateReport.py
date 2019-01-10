""" Generates a multisheet xlsx file from expense and bonus files"""


import os
import xlsxwriter
from xlsxwriter.utility import xl_range


def create_report(path, name, elist, date, blist, report_name):
    os.chdir(path)
    wb = xlsxwriter.Workbook(name + report_name + date + '.xlsx')
    we = wb.add_worksheet('Expense')
    money = wb.add_format({'num_format': '$#,###.#0'})
    we.set_column(0, 0, 11)
    cell_format = wb.add_format({'num_format': '$#,###.#0', 'font_color': 'red'})

    row = 0
    col = 0
    we.write(row, col, 'Date')
    we.write(row, col + 1, 'Total')
    row += 1
    for edate, total in elist:
        we.write(row, col, edate)
        we.write(row, col + 1, total, money)
        row += 1
    we.write(row, 0, 'Total:')
    e_cell_range = xlsxwriter.utility.xl_range(1, 1, row - 1, 1)
    e_formula = '=SUM(%s)' % e_cell_range
    we.write(row, 1, e_formula, cell_format)

    row = 0
    wbo = wb.add_worksheet('Bonus')
    wbo.set_column(0, 0, 11)

    wbo.write(row, col, 'Date')
    wbo.write(row, col + 1, 'Travel')
    wbo.write(row, col + 2, 'On Call')
    wbo.write(row, col + 3, 'Call Cases')
    row += 1

    for bdate, travel, on_call, call_cases in blist:
        wbo.write(row, col, bdate)
        wbo.write(row, col + 1, travel, money)
        wbo.write(row, col + 2, on_call, money)
        wbo.write(row, col + 3, call_cases, money)
        row += 1
    wbo.write(row, 0, 'Total:')
    t_cell_range = xlsxwriter.utility.xl_range(1, 1, row - 1, 1)
    t_formula = '=SUM(%s)' % t_cell_range
    wbo.write(row, 1, t_formula, cell_format)

    o_cell_range = xlsxwriter.utility.xl_range(1, 2, row - 1, 2)
    o_formula = '=SUM(%s)' % o_cell_range
    wbo.write(row, 2, o_formula, cell_format)

    c_cell_range = xlsxwriter.utility.xl_range(1, 3, row - 1, 3)
    c_formula = '=SUM(%s)' % c_cell_range
    wbo.write(row, 3, c_formula, cell_format)

    wb.close()
