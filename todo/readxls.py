import xlrd


def sheets(t):
    rowlist = []
    data = xlrd.open_workbook('step02.xls')
    sheet = data.sheet_by_index(t)
    nrows = sheet.nrows
    for row in range(nrows):
        #print(sheet.row_values(row))
        rowlist.append(sheet.row_values(row))
    return rowlist


if __name__ == '__main__':
    t = sheets(1)
    print(t)
    print(t[0])

    print(t[0][0])









