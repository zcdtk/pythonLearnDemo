import xlrd
import os
import codecs

from properties import Properties

path = 'E:/Git_Clone/VUE_R6_FTL/@EDITOR/'
file = './uid_1150aed716a19ceb0a37c3e.xls'

path2 = 'E:/Git_Clone/VUE_R6_FTL/@EDITOR/'

# 创建视图基础文件
def createView(name, viewtype):  # 定义函数名
    targetfolder = path + name

    targetFileName = name
    if not os.path.exists(targetfolder):  # 判断目标文件夹是否存在
        os.makedirs(targetfolder)

    template = codecs.open(path + name + '\\' + 'template.properties', 'w', encoding='utf-8')
    template.write('EDITORTYPE=' + viewtype)  # 写入内容信息
    template.close()

    EDITOR_less = codecs.open(path + name + '\\' + 'EDITOR.less.ftl', 'w', encoding='utf-8')
    EDITOR_less.write('')  # 写入内容信息
    EDITOR_less.close()

    EDITOR_tsx = codecs.open(path + name + '\\' + 'EDITOR.tsx.ftl', 'w', encoding='utf-8')
    EDITOR_tsx.write('')  # 写入内容信息
    EDITOR_tsx.close()


# 读取excel
def properViews():

    data = Properties.readProperties(path2)

    # print(data)

    wb = xlrd.open_workbook(filename=file)  # 打开文件

    # print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格

    sheet2 = wb.sheet_by_name('数据')  # 通过名字获取表格

    # print(sheet1.name, sheet1.nrows, sheet1.ncols)
    row_index = 1
    while row_index < sheet1.nrows:

        # rows = sheet1.row_values(row_index)
        # 视图标识
        id = sheet2.cell(row_index, 0).value
        # 视图名称
        name = sheet2.cell(row_index, 1).value
        # 是否移动端编辑器
        ismobeditor = sheet2.cell(row_index, 6).value

        
        # 是移动端视图
        MOB = id.find('MOB') != -1
        MB = id.find('MB') != -1

        # 该视图已经被建立
        hastype = id in data

        # print(hastype, '==========',id, '==========', name, '==========', ismobeditor)
        row_index = row_index + 1
        if MOB:
            continue
        if MB:
            continue
        if ismobeditor == '是':
            continue
        if hastype:
            continue
        
        
        print(hastype, '==========',id, '==========', name, '==========', ismobeditor)
        createView(name, id)


if __name__ == '__main__':
    properViews()
