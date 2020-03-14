import xlrd 
data = xlrd.open_workbook('irl2.xls')               # 打开Excel文件
table = data.sheet_by_index(0)                      # 获取第一个工作表
nrows = table.nrows                                 # 获取行数
ncols = table.ncols                                 # 获取列数
excel_list = []                                     # 定义excel_list
for row in range(1, nrows):
    for col in range(ncols):                        
        cell_value = table.cell(row, col).value     # 获取单元格数据
        excel_list.append(cell_value)               # 把数据追加到excel_list中