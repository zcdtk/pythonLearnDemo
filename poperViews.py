import xlrd
import os
import codecs

from properties import Properties

path = './template/'
file = './uid_157390d616a0fbf9b0873c5.xls'

path2 = 'E:/Git_Clone/VUE_R4_STYLE01/@VIEW/'

# 创建视图基础文件
def createView(name, viewtype):  # 定义函数名
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
def properViews():

    data = Properties.readProperties(path2)

    # print(data)

    wb = xlrd.open_workbook(filename=file)  # 打开文件

    # print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格

    sheet2 = wb.sheet_by_name('数据')  # 通过名字获取表格

    # print(sheet1.name, sheet1.nrows, sheet1.ncols)
    row_index = 0
    while row_index < sheet1.nrows:

        # rows = sheet1.row_values(row_index)
        # 视图标识
        viewid = sheet2.cell(row_index, 0).value
        # 视图名称
        viewname = sheet2.cell(row_index, 1).value
        # 是否实体视图
        isentityview = sheet2.cell(row_index, 5).value

        if isentityview == '是':
            viewid = 'APP' +  viewid
        
        # 是移动端视图
        MOB = viewid.find('MOB') != -1
        # 是动态视图
        DYNA = viewid.find('DYNA') != -1
        # 该视图已经被建立
        hastype = viewid in data

        # print(hastype, '==========',viewid, '==========', viewid, '==========', isentityview)
        row_index = row_index + 1
        if MOB:
            continue
        if DYNA:
            continue
        if hastype:
            continue

        createView(viewname, viewid)


if __name__ == '__main__':
    properViews()
