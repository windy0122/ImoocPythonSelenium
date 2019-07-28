# coding=utf-8
import xlrd
import xlutils


class ExcelUtil(object):
    def __init__(self, excel_path=None, index=None):
        if excel_path == None:
            excel_path = '../config/casedata.xls'
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheets()[index]

    @property
    def get_data(self):
        result = []
        row = self.get_lines()
        if row is not None:
            for i in range(row):
                col = self.table.row_values(i)
                result.append(col)
            return result

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows
        if rows >= 1:
            return rows
        return None

    # 获取单元格数据
    def get_col_value(self, row, col):
        if self.get_lines() > row:
            data = self.table.cell(row, col).value
            return data
        return None

    # # 判断行数
    # def han_next(self):


    # 写入数据
    def write_value(self, row, value):
        read_value = self.data
        write_data = xlutils.copy(read_value)
        write_data.get_sheet(0).write(row, 7, value)
        write_data.save('../config/casedata.xls')


if __name__ == '__main__':
    ex = ExcelUtil('../config/casedata.xls')
    # ex.get_data()
    print(ex.get_col_value(1, 1))



