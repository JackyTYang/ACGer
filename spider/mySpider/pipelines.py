# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import os
import shutil


class MyspiderPipeline:
    def __init__(self):
        """
            删除某一目录下的所有文件或文件夹
            :param filepath: 路径
            :return:
            """
        filepath = './object'
        del_list = os.listdir(filepath)
        for f in del_list:
            file_path = os.path.join(filepath, f)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

    def create_dir(self, path):
        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")
        # 判断路径是否存在
        is_exists = os.path.exists(path)
        # 判断结果
        if not is_exists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False

    def process_item(self, item, spider):
        # 动画名字的文件夹
        tag_path = "./object/" + item['typo']
        # 动画名字的json文件
        f_name = tag_path + '/detail(1).json'
        #处理item数据
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #创建文件夹
        self.create_dir(tag_path)
        #如果没有就创建文件，如果有就打开，但什么都不做
        with open(f_name, 'a+') as file:
            file.close()
        #判断文件是否过大
        by = 1024 * 1024
        i = 1
        while os.path.getsize(f_name) > (3 * by):
            f_name = tag_path + '/detail(' + str(i) + ').json'
            i = i + 1
            with open(f_name, 'a+') as file:
                file.close()
        #打开文件，进行写操作
        with open(f_name, 'a+') as file:
            file.write(content)
        return item

     #def close_spider(self, spider):
         # self.f.close()

