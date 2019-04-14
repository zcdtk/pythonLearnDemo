import xlrd
import os
import codecs

path = './template/'
file = './uid_157390d616a0fbf9b0873c5.xls'

# 创建文件夹及文件
def txt(name, viewtype):  # 定义函数名
    targetfolder = path + name

    targetFileName = name
    if not os.path.exists(targetfolder):  # 判断目标文件夹是否存在
        os.makedirs(targetfolder)

    template = codecs.open(path + name + '\\' + 'template.properties', 'w', encoding='utf-8')
    template.write('VIEWTYPE=' + viewtype)  # 写入内容信息
    template.close()

    VIEW_less = codecs.open(path + name + '\\' + 'VIEW.less.ftl', 'w', encoding='utf-8')
    VIEW_less.write('${P.getLayoutCode().code}')  # 写入内容信息
    VIEW_less.close()

    VIEW_tsx = codecs.open(path + name + '\\' + 'VIEW.tsx.ftl', 'w', encoding='utf-8')
    VIEW_tsx.write('<#ibizinclude>\n../@MACRO/VIEW.tsx.ftl\n</#ibizinclude>')  # 写入内容信息
    VIEW_tsx.close()


# 读取excel
def read_excel():

    wb = xlrd.open_workbook(filename=file)  # 打开文件

    print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格

    sheet2 = wb.sheet_by_name('数据')  # 通过名字获取表格

    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    row_index = 0
    while row_index < sheet1.nrows:

        rows = sheet1.row_values(row_index)
        cell1 = sheet2.cell(row_index, 0).value
        cell2 = sheet2.cell(row_index, 1).value

        # 去掉移动端视图与动态视图
        MOB = cell1.find('MOB') != -1
        DYNA = cell1.find('DYNA') != -1

        row_index = row_index + 1
        # if MOB:
        #     continue
        # if DYNA:
        #     continue
        txt(cell2, cell1)


if __name__ == '__main__':
    read_excel()
