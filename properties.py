import os
import codecs
import glob

# 获取配置信息类
class Properties(object):

    # 读取配置文件
    def readProperties(folder):
        
        properties = []
        files = glob.glob(folder + '*\*.properties')
        
        for file in files:
            if not os.path.isdir(file):
                f = codecs.open(file)
                content = f.read()
                if content.strip() != '':
                    arr = content.split('=')
                    properties.append(arr[1])
                f.close()
        
        return properties