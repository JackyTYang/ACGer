from imp import reload

import scrapy
from mySpider.items import MyspiderItem
import re
# 查找表
translateTable1 = {
    #anime
    "简体中文名":{
        'name': "zh_name",
        'list': False,
    },
    "中文名":{
        'name': "zh_name",
        'list': False,
    },
    "导演": {
        'name': "director",
        'list': True,
    },
    "话数": {
        'name': "episode_count",
        'list': False,
    },
    "放送开始": {
        'name': "start_date",
        'list': False,
    },
    "开始": {
        'name': "start_date",
        'list': False,
    },
    "制片人": {
        'name': "producer",
        'list': True,
    },
    "音乐制作": {
        'name': "music_composer",
        'list': True,
    },
    "动画制作": {
        'name': "animation_company",
        'list': True,
    },
    "别名": {
        'name': "names",
        'list': True,
    },
    "制作": {
        'name': "made",
        'list': True,
    },
    #game
    "开发": {
        'name': "developer",
        'list': True,
    },
    "游戏类型": {
        'name': "genre",
        'list': False,
    },
    "游戏引擎": {
        'name': "engine",
        'list': False,
    },
    "平台": {
        'name': "platform",
        'list': True,
    },

    #music
    "艺术家": {
        'name': "singer",
        'list': True,
    },
    "作曲": {
        'name': "composer",
        'list': True,
    },
    "作词": {
        'name': "lyrics",
        'list': True,
    },

    #book
    "作者": {
        'name': "writer",
        'list': True,
    },
    "出版社": {
        'name': "press",
        'list': True,
    },

    # # extra_data
    # # anime
    # "脚本": {
    #     'name': "scr_text",
    #     'list': True,
    # },
    # "分镜": {
    #     'name': "sub_mirror",
    #     'list': True,
    # },
    # "演出": {
    #     'name': "production_staff",
    #     'list': True,
    # },
    # "原画": {
    #     'name': "pic_staff",
    #     'list': True,
    # },
    # "音乐": {
    #     'name': "music_staff",
    #     'list': True,
    # },
    # "作画监督": {
    #     'name': "paint_supervisor",
    #     'list': True,
    # },
    #
    # "总作画监督": {
    #     'name': "sup_paint_supervisor",
    #     'list': True,
    # },
    # "官方网站": {
    #     'name': "official_website",
    #     'list': False,
    # },
    # "播放结束": {
    #     'name': "end_data",
    #     'list': False,
    # },
    # #book
    "发售日": {
        'name': "start_date",
        'list': False,
    },
    # "页数": {
    #     'name': "page_num",
    #     'list': False,
    # },
    # "册数": {
    #     'name': "volume_num",
    #     'list': False,
    # },
    # "话数": {
    #     'name': "word_num",
    #     'list': False,
    # },
    # "连载杂志": {
    #     'name': "magazine",
    #     'list': True,
    # },
    # "结束": {
    #     'name': "end_data",
    #     'list': False,
    # },
    # #music
    #
    # "厂牌": {
    #     'name': "music_label",
    #     'list': False,
    # },
    # "价格": {
    #     'name': "disc_price",
    #     'list': False,
    # },
    # "碟片数量": {
    #     'name': "disc_num",
    #     'list': False,
    # },
    # "录音": {
    #     'name': "recording",
    #     'list': False,
    # },
    # "版本特性": {
    #     'name': "version_features",
    #     'list': False,
    # },
    "发售日期": {
        'name': "start_date",
        'list': False,
    },
    # "播放时长": {
    #     'name': "play_time",
    #     'list': False,
    # },
    # "剧本": {
    #     'name': "scr_text",
    #     'list': True,
    # },
    # "企画": {
    #     'name': "plan_maker",
    #     'list': True,
    # },
    # "游玩人数": {
    #     'name': "people_num",
    #     'list': False,
    # },
    "发行日期": {
        'name': "start_date",
        'list': False,
    },
    # "售价": {
    #     'name': "game_price",
    #     'list': False,
    # },
    "总监": {
        'name': "director",
        'list': True,
    },
    # "游戏设计师": {
    #     'name': "game_designer",
    #     'list': True,
    # },

}
translateTable2 = {
    #person & company
    "简体中文名":{
        'name': "zh_name",
        'list': False,
    },
    "中文名": {
        'name': "zh_name",
        'list': False,
    },
    "性别": {
        'name': "gender",
        'list': False,
    },
    "生日": {
        'name': "birthday",
        'list': False,
    },
    "别名": {
        'name': "names",
        'list': True,
    },
    # #extra date
    # "血型": {
    #     'name': "blood_type",
    #     'list': False,
    # },
    # "身高": {
    #     'name': "height",
    #     'list': False,
    # },
    # "引用来源": {
    #     'name': "its_source",
    #     'list': False,
    # },
    # "星座": {
    #     'name': "constellation",
    #     'list': False,
    # },
    # "出身地区": {
    #     'name': "country",
    #     'list': False,
    # },
    # "个人状态": {
    #     'name': "personal_status",
    #     'list': False,
    # },
    # "官网": {
    #     'name': "official_website",
    #     'list': False,
    # },
    # "Twitter": {
    #     'name': "twitter",
    #     'list': False,
    # },
}
translateTable3 = {
    #character
    "简体中文名":{
        'name': "zh_name",
        'list': False,
    },
    "中文名": {
        'name': "zh_name",
        'list': False,
    },
    "性别": {
        'name': "gender",
        'list': False,
    },
    "生日": {
        'name': "birthday",
        'list': False,
    },
    "别名": {
        'name': "names",
        'list': True,
    },
    "cv": {
        'name': "CV",
        'list': False,
    },
    # "血型": {
    #     'name': "blood_type",
    #     'list': False,
    # },
    # "身高": {
    #     'name': "height",
    #     'list': False,
    # },
    # "体重": {
    #     'name': "weight",
    #     'list': False,
    # },
}

class BangumiSpider(scrapy.Spider):
    name = 'bangumi'

    def start_requests(self):
        urls = []
        # for i in range(8, 9):
        #     urls.append('https://bangumi.tv/subject/'+str(i))
        # for i in range(1, 2):
        #     urls.append('https://bangumi.tv/person/'+str(i))
        for i in range(1, 2):
            urls.append('https://bangumi.tv/character/'+str(i))
        for url in urls:
            judge_url = url[url.index('tv/')+3:url.rindex('/')]
            if judge_url == 'subject':
                yield scrapy.Request(url=url, callback=self.parse1)
            elif judge_url == 'person':
                yield scrapy.Request(url=url, callback=self.parse2)
            else:
                yield scrapy.Request(url=url, callback=self.parse3)


    def parse1(self, response):
        #提取数据
        def valueof(response, path, default = [' ']):
            content = response.xpath(path).extract()
            if len(content) == 0 or content[0] == '、':
                return default
            else:
                return content

        item = MyspiderItem()
        # 提取全局ID
        guid = int(re.sub("\D", "", str(response.url)))
        #提取条目类型
        typelist = ["anime", "book", "music", "game", "anime", "person"]
        for i in range(1, 7):
            check = response.xpath('//*[@id="navMenuNeue"]/li[' + str(i) + ']/a').extract()
            if "focus" in check[0]:
                break;
        typo = [typelist[i - 1]]
        #提取原名
        pr_name = valueof(response, '//*[@id="headerSubject"]/h1/a/text()')
        #提取描述
        try:
            des = response.xpath('//*[@id="subject_summary"]').extract()
            if len(des) == 0:
                description = [" "]
            else:
                description = [des[0][des[0].index(">") + 1:des[0].rindex("<") - 1]]
            description = description[0].strip(' ')
        except(Exception):
            description = ' '
        # 演员列表
        # 初始化全体
        try:
            chara_list = []
            node_list = response.xpath('//*[@id="browserItemList"]//li')
            #初始化guid的gap
            gap = 400000
            # 对每个节点进行操作
            for node in node_list:
                # 初始化元祖
                character = {
                    'guid': 0,
                }
                #//*[@id="browserItemList"]/li[1]/div/strong/a

                chara_name = valueof(node, 'div/strong/a')
                # 取值 赋值
                character['guid'] = gap + int(chara_name[0][chara_name[0].index('/character/') + 11:chara_name[0].index('" title')])
                name_list = chara_name[0][chara_name[0].index('title=') + 7:chara_name[0].index('class')-2]
                name_list = name_list.split('/')
                name_list = name_list[0].strip()
                character['primary_name'] = name_list
                #中文名
                chara_zh_name = valueof(node, 'div/div/span/span')
                if chara_zh_name != [' ']:
                    chara_zh_name = [chara_zh_name[0][chara_zh_name[0].index('>')+1:chara_zh_name[0].rindex('<')]]
                else:
                    chara_zh_name = name_list
                character['zh_name'] = chara_zh_name[0]
                # 初始化cv列表。赋值
                cv = []
                little_node_list = node.xpath('div/div/span//a')
                for little_node in little_node_list:
                    content = little_node.extract()
                    cv.append(content[content.index('>') + 1:content.rindex('<')])
                character['cv'] = cv
                chara_urls = valueof(node, 'div/strong/a/span/span')
                chara_url = chara_urls[0][chara_urls[0].index("url('") + 5:chara_urls[0].rindex(')') - 1]
                chara_url = 'https:' + chara_url
                character['visuals'] = chara_url
                chara_list.append(character)
        except(Exception):
            chara_list = [' ']
        # 关联条目
        # 初始化全体
        try:
            related_subjects = []
            big_type = ''
            node_list = response.xpath('//*[@id="columnSubjectHomeB"]/div[3]/div[2]/ul//li')
            # 对每个节点进行操作
            for node in node_list:
                # 初始化元祖
                subject = {
                    'guid': 0,
                }
                subject_name = valueof(node, 'a[2]')
                # 取值 赋值
                subject['guid'] = int(
                    subject_name[0][subject_name[0].index('/subject/') + 9:subject_name[0].index('" class')])
                subject['primary_name'] = subject_name[0][
                                          subject_name[0].index('title">') + 7:subject_name[0].rindex('<')]
                little_types = valueof(node, 'span')
                little_type = little_types[0][little_types[0].index('>') + 1:little_types[0].rindex('<')]
                #获取type
                if little_type == '':
                    little_type = big_type
                else:
                        big_type = little_type
                subject['type'] = little_type
                #//*[@id="columnSubjectHomeB"]/div[3]/div[2]/ul/li[1]/a[1]/span
                img_urls = valueof(node, 'a[1]/span')
                img_url = img_urls[0][img_urls[0].index("url('")+5:img_urls[0].rindex(')')-1]
                img_url = 'https:'+img_url
                subject['visuals'] = img_url
                # 赋值
                related_subjects.append(subject)
        except(Exception):
            related_subjects = [' ']
        #提取评分 //*[@id="panelInterestWrapper"]/div[1]/div/div[1]/div[2]/span[1]
        try:
            scores = valueof(response, '//*[@id="panelInterestWrapper"]/div[1]/div/div[1]/div[2]/span[1]')
            score = [scores[0][scores[0].index('>')+1:scores[0].rindex('<')]]
        except(Exception):
            score = ['0']
        #提取打分人数 //*[@id="ChartWarpper"]/div/small/span
        try:
            vote_counts = valueof(response, '//*[@id="ChartWarpper"]/div/small/span')
            vote_count = [vote_counts[0][vote_counts[0].index('>')+1:vote_counts[0].rindex('<')]]
        except(Exception):
            vote_count = ['0']
        #提取条目图片url
        try:
            visual = valueof(response, '//*[@id="bangumiInfo"]/div/div/a/img')
            if visual[0] != ' ':
                visuals = ['https:' + visual[0][visual[0].index("=") + 2:visual[0].rindex("class") - 1]]
            else:
                visuals = [' ']
        except(Exception):
            visuals = [' ']
        #提取tags
        tags = []
        #//*[@id="subject_detail"]/div[2]/div/a[1]/span
        node_list = valueof(response, '//*[@id="subject_detail"]/div[1]/div//a')
        try:
            if not node_list[0].__contains__('/tag/'):
                node_list = valueof(response, '//*[@id="subject_detail"]/div[2]/div//a')
                if not node_list[0].__contains__('tag'):
                    node_list = valueof(response, '//*[@id="subject_detail"]/div[3]/div//a')
            for node in node_list:
                node = node[node.index("<span>") + 6:node.index("</span>")]
                tags.append(node)
        except(Exception):
            tags = [' ']
        #提取书籍类型
        try:
            book_types = valueof(response, '//*[@id="headerSubject"]/h1/small[1]')
            if book_types != [' ']:
                book_type = book_types[0][book_types[0].index('>') + 1:book_types[0].rindex('<')]
                item['book_type'] = book_type
        except(Exception):
            print("HERE booktype ERROR")
        ###
        # 吐槽箱
        comment_box = []
        # 初始化评论数
        comment_num = 0
        #//*[@id="columnSubjectHomeB"]/div[7]/h2
        #//*[@id="comment_box"]/div[1]/div/div/p
        #//*[@id="comment_box"]/div[2]/div/div/a 评论人id
        #//*[@id="comment_box"]/div[2]/a/span  评论人头像
        #//*[@id="comment_box"]/div[2]/div/div/p 评论内容
        #//*[@id="comment_box"]/div[5]/div/div/small 评论时间
        path = '//*[@id="comment_box"]//div'
        comment_list = response.xpath(path)
        set_floor = 1
        try:
            for comment in comment_list:
                box = {
                    'floor_num': '',
                }
                # 读取评论人id
                comment_name = valueof(comment, 'div/div/a')
                if comment_name == [' ']:
                    continue
                comment_name = comment_name[0][comment_name[0].index('>') + 1:comment_name[0].rindex('<')]
                # 提取评论楼层
                comment_floor = set_floor
                set_floor = set_floor + 1
                # 提取评论内容
                comment_texts = valueof(comment, 'div/div/p')
                comment_texts = comment_texts[0][comment_texts[0].index('>')+1:comment_texts[0].rindex('<')]
                # 提取评论人头像url
                comment_img = valueof(comment, 'a/span')
                part_url = comment_img[0][comment_img[0].index('url') + 5:comment_img[0].rindex('<') - 4]
                comment_img = 'https:' + part_url
                # 提取评论时间
                comment_time = valueof(comment, 'div/div/small')
                comment_time = comment_time[0][comment_time[0].index('@') + 2:comment_time[0].rindex('<')]

                box['commenter_name'] = comment_name
                box['floor_num'] = comment_floor
                comment_num = comment_floor
                box['comment_texts'] = comment_texts
                box['comment_visuals'] = comment_img
                box['comment_time'] = comment_time
                comment_box.append(box)
        except(Exception):
            comment_box = [' ']
        #整齐数据保存结果为json文件
        item['guid'] = guid
        item['typo'] = typo[0]
        item['primary_name'] = pr_name[0]
        item['zh_name'] = ''
        item['description'] = description
        item['comment_box'] = comment_box
        item['comment_num'] = comment_num
        item['visit_num'] = 0
        item['chara_list'] = chara_list
        item['related_subjects'] = related_subjects
        item['score_general'] = float(score[0])
        item['vote_count'] = int(vote_count[0])
        item['visuals'] = visuals[0]
        item['tags'] = tags
        #查找不整齐数据并保存
        # 获取node_list,node_list下有很多li
        node_list = response.xpath('//*[@id="infobox"]//li')
        # 计数
        k = 1
        # 针对无跳转链接：创建默认值
        #别名
        item['names'] = ['']
        #平台
        item['platform'] = ['']
        #extra_data
        item['extra_data'] = {}
        extra_data = {}
        # node是node_list下的子li，对li查找关键字，在translateTable中寻找对应
        for node in node_list:
            texts = valueof(node, 'span')
            text = [texts[0][texts[0].index('">') + 2:texts[0].rindex(':')]]
            # print(valueof(node, 'a'))
            # 创建空list 保存可能有的数据
            empty_list = []
            # 找到对应li
            if translateTable1.__contains__(text[0]):
                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                #针对无跳转链接且分li[]储存的项目：别名、平台
                if text[0] == '别名' or text[0] == '平台':
                    #一定是list，不作判断
                    if item[translateTable1[text[0]]['name']] == ['']:
                        content[0] = content[0].strip('、')
                        item[translateTable1[text[0]]['name']] = content[0].split('、')
                    else:
                        item[translateTable1[text[0]]['name']].append(content[0])
                else:
                    # 针对无跳转链接：
                    # 此处作的判断：如果是无跳转链接的数据，直接content就有数据了，而有跳转链接的项，需要进一步取数据，故为空
                    if content != [' ']:
                        # 判断是否需要保存为列表形式
                        if translateTable1[text[0]]['list']:
                            content[0] = content[0].strip('、')
                            item[translateTable1[text[0]]['name']] = content[0].split('、')
                        else:
                            item[translateTable1[text[0]]['name']] = content[0]

                        # 包含 常规情况（有跳转）
                        content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                        if content != [' ']:
                            nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                            # 把a中的关键数据提取，保存到empty_list中
                            for nodes in nodes_list:
                                member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                                item[translateTable1[text[0]]['name']].append(member)

                    # 常规情况：找到li下的所有子a
                    else:
                        nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                        # 把a中的关键数据提取，保存到empty_list中
                        for nodes in nodes_list:
                            member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                            empty_list.append(member)
                        # 若存在寻找的条目，写入数据
                        # 判断是否为列表保存
                        if translateTable1[text[0]]['list']:
                            item[translateTable1[text[0]]['name']] = empty_list
                        else:
                            item[translateTable1[text[0]]['name']] = empty_list[0]
            else:

                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                # 针对无跳转链接：
                # 此处作的判断：如果是无跳转链接的数据，直接content就有数据了，而有跳转链接的项，需要进一步取数据，故为空
                empty_li = []
                if content != [' ']:
                    # # 判断是否需要保存为列表形式
                    # if translateTable1[text[0]]['list']:
                    content[0] = content[0].strip('、')
                    extra_data[text[0]] = content[0].split('、')
                    # else:
                    # extra_data[text[0]] = content[0]
                    # 包含 常规情况（有跳转）
                    content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                    if content != [' ']:
                        nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                        # 把a中的关键数据提取，保存到empty_list中
                        for nodes in nodes_list:
                            member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                            extra_data[text[0]].append(member)
                # 常规情况：找到li下的所有子a
                else:
                    nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                    # 把a中的关键数据提取，保存到empty_list中
                    for nodes in nodes_list:
                        member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                        empty_li.append(member)
                    # 若存在寻找的条目，写入数据
                    # 判断是否为列表保存
                    # if translateTable1[text[0]]['list']:
                    extra_data[text[0]] = empty_li
                    # else:
                    #     item[translateTable1[text[0]]['name']] = empty_li[0]

            item['extra_data'] = extra_data
            k = k + 1
        if item['zh_name'] == '':
            item['zh_name'] = item['primary_name']

        #退出当前url
        yield item

        pass

    def parse2(self, response):

        #提取数据
        def valueof(response, path, default = [' ']):
            content = response.xpath(path).extract()
            if len(content) == 0 or content[0] == '、':
                return default
            else:
                return content

        item = MyspiderItem()
        # 提取全局ID
        try:
            gap = 350000
            guid = gap + int(re.sub("\D", "", str(response.url)))
        except(Exception):
            guid = 0
        #提取原名
        try:
            pr_name = valueof(response, '//*[@id="headerSubject"]/h1/a/text()')
        except(Exception):
            pr_name = [' ']
        # 提取中文名 若为空则与原名相同
        try:
            zh_name = valueof(response, '//*[@id="headerSubject"]/h1/small', pr_name)
            if zh_name != pr_name:
                zh_name = [zh_name[0][zh_name[0].index('>') + 1:zh_name[0].rindex('<')]]
        except(Exception):
            zh_name = [' ']
        #提取描述//*[@id="columnCrtB"]/div[2]
        try:
            des = response.xpath('//*[@id="columnCrtB"]/div[2]').extract()
            if len(des) == 0:
                description = [" "]
            else:
                description = [des[0][des[0].index(">") + 1:des[0].rindex("<") - 1]]
        except(Exception):
            description = [' ']
        #提取图片
        try:
            visual = valueof(response, '//*[@id="columnCrtA"]/div[1]/div/a/img')
            if visual[0] != ' ':
                visuals = ['https:' + visual[0][visual[0].index("=") + 2:visual[0].rindex("class") - 2]]
            else:
                visuals = ['']
        except(Exception):
            visuals = [' ']
        # 提取职业
        try:
            contents = valueof(response, '//*[@id="columnCrtB"]/div[1]/h2')
            content = contents[0][contents[0].index(':') + 1:contents[0].rindex('<')]
            jobs = content.split()
        except(Exception):
            jobs = [' ']
        # 最近参与
        # 初始化全体
        recently_participated = []
        # 初始化可能有的 最近演出角色
        recently_chara = []
        #//*[@id="columnCrtB"]/h2[1]
        #//*[@id="columnCrtB"]/h2[2]
        judge = valueof(response, '//*[@id="columnCrtB"]/h2[1]')
        path = '//*[@id="columnCrtB"]/ul[1]'
        # 如果此条包含最近'演出'角色，说明定义路径不对，更改
        try:
            if judge[0].__contains__('演出'):
                #顺便处理 最近演出角色
                #顺便处理 最近演出角色
                chara_nodes = response.xpath('//*[@id="columnCrtB"]/ul[1]//li')
                for node in chara_nodes:
                    chara = {
                        'guid': 0,
                    }
                    # //*[@id="columnCrtB"]/ul[1]/li[2]/div/a
                    #//*[@id="columnCrtB"]/ul[1]/li[1]/div/a
                    #//*[@id="columnCrtB"]/ul[1]/li[1]/div/div/h3/a
                    gap = 400000
                    guids = valueof(node, 'div/a')
                    if guids == [' ']:
                        continue
                    chara['guid'] = gap + int(guids[0][guids[0].index('character') + 10:guids[0].index('title') - 2])
                    img_urls = valueof(node, 'div/a/img')
                    part_url = img_urls[0][img_urls[0].index('src=') + 5:img_urls[0].index('height') - 2]
                    chara['visuals'] = 'https:' + part_url
                    chara['primary_name'] = img_urls[0][img_urls[0].index('alt') + 5:img_urls[0].index('class') - 2]
                    #//*[@id="columnCrtB"]/ul[1]/li[1]/div/div/h3/p
                    zh_names = valueof(node, 'div/div/h3/p')
                    if zh_names == [' ']:
                        chara['zh_name'] = chara['primary_name']
                    else:
                        chara['zh_name'] = zh_names[0][zh_names[0].index('>') + 1:zh_names[0].rindex('<')]

                    badge_jobs = valueof(node, 'ul/li/div/span')
                    chara['badge_job'] = badge_jobs[0][badge_jobs[0].index('>') + 1:badge_jobs[0].rindex('<')]
                    #对应条目属性
                    #guid //*[@id="columnCrtB"]/ul[1]/li[1]/ul/li/a
                    sub_guids = valueof(node, 'ul/li/a')
                    chara['sub_guid'] = int(sub_guids[0][sub_guids[0].index('subject') + 8:sub_guids[0].index('title') - 2])
                    #//*[@id="columnCrtB"]/ul[1]/li[1]/ul/li/a/img
                    sub_img_urls = valueof(node, 'ul/li/a/img')
                    part_url = img_urls[0][img_urls[0].index('src=') + 5:img_urls[0].index('height') - 2]
                    chara['sub_visuals'] = 'https:' + part_url
                    p_name = sub_img_urls[0][sub_img_urls[0].index('alt') + 5:sub_img_urls[0].index('class') - 2]
                    p_name = p_name.split('/')
                    chara['sub_primary_name'] = p_name[0].strip()
                    name_lists = valueof(node, 'ul/li/div/small')
                    if name_lists == [' ']:
                        chara['sub_zh_name'] = p_name
                    else:
                        chara['sub_zh_name'] = name_lists[0][name_lists[0].index('>') + 1:name_lists[0].rindex('<')]
                    #赋值
                    recently_chara.append(chara)
                path = '//*[@id="columnCrtB"]/ul[2]'
            # 遍历
            node_list = response.xpath(path + '//li')
            for node in node_list:
                subject = {
                    'guid': 0,
                }
                # //*[@id="columnCrtB"]/ul[2]/li[1]/div/a
                guids = valueof(node, 'div/a')
                chara_guid = int(guids[0][guids[0].index('subject') + 8:guids[0].index('title') - 2])
                pri_name = guids[0][guids[0].index('title') + 7:guids[0].index('class') - 2]
                # //*[@id="columnCrtB"]/ul[2]/li[1]/div/a/img
                img_urls = valueof(node, 'div/a/img')
                part_url = img_urls[0][img_urls[0].index('src=') + 5:img_urls[0].rindex('g') + 1]
                img_url = 'https:' + part_url
                # //*[@id="columnCrtB"]/ul[2]/li[1]/div/div/span
                badge_job = valueof(node, 'div/div/span')
                job = badge_job[0][badge_job[0].index('>') + 1:badge_job[0].rindex('<')]
                subject['guid'] = chara_guid
                subject['pri_name'] = pri_name
                subject['visuals'] = img_url
                subject['badge_job'] = job
                recently_participated.append(subject)
        except(Exception):
            recently_participated = []
            # 初始化可能有的 最近演出角色
            recently_chara = []
        #吐槽箱
        comment_box = []
        c = 1
        comment_check = valueof(response, '//*[@id="columnCrtB"]/div['+str(c)+']/h2')
        try:
            while not comment_check[0].__contains__('吐槽箱'):
                c = c+1
                comment_check = valueof(response, '//*[@id="columnCrtB"]/div[' + str(c) + ']/h2')
            path = '/html/body/div[1]/div[4]/div[1]/div[2]/div[' + str(c) + ']/div//div'
            comment_list = response.xpath(path)
            #初始化评论数
            comment_num = 0
            for comment in comment_list:
                box = {
                    'floor_num': '',
                }
                #读取评论人id
                comment_name = valueof(comment, 'div[2]/strong/a')
                if comment_name == [' ']:
                    continue
                comment_name = comment_name[0][comment_name[0].index('>')+1:comment_name[0].rindex('<')]
                # 提取评论楼层
                comment_floor = valueof(comment, 'div[1]/small/a')
                comment_floor = comment_floor[0][comment_floor[0].rindex('#') + 1:comment_floor[0].rindex('<')]
                #不读评论的子评论
                if comment_floor.__contains__('-'):
                    continue
                #提取评论内容
                comment_texts = valueof(comment, 'div[2]/div/div/text()')
                comment_texts = comment_texts[0].strip('\n')
                comment_texts = comment_texts.strip()
                comment_texts = comment_texts.strip('\t')
                comment_texts = comment_texts.strip('\n')
                comment_texts = comment_texts.strip()
                comment_texts = comment_texts.strip('\t')
                #提取评论人头像url
                comment_img = valueof(comment, 'a/span')
                part_url = comment_img[0][comment_img[0].index('url') + 5:comment_img[0].rindex('<')-4]
                comment_img = 'https:' + part_url
                #提取评论时间
                comment_time = valueof(comment, 'div[1]/small/text()')
                comment_time = comment_time[0][comment_time[0].index('-') + 2:]

                box['commenter_name'] = comment_name
                box['floor_num'] = comment_floor
                #读取评论数
                comment_num = comment_floor
                box['comment_texts'] = comment_texts
                box['comment_visuals'] = comment_img
                box['comment_time'] = comment_time
                comment_box.append(box)
        except(Exception):
            comment_box = [' ']
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[6]/div/div[69]/div[2]/div/div/text()
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[6]/div/div[1]/div[2]/div/div[1]/text()
        # /html/body/div[1]/div[4]/div[1]/div[2]/div[5]/div/div[2]  /div[2]/strong/a 评论人
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/div/div[1]  /div[2]/div/div/text() 评论内容
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/div/div[2]  /a/span 评论人头像
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/div/div[3]  /div[1]/small/a 评论楼层
        #/html/body/div[1]/div[4]/div[1]/div[2]/div[5]/div/div[3]  /div[1]/small/text() 评论时间

        #####
        #整齐数据保存结果为json文件
        item['guid'] = guid
        item['primary_name'] = pr_name[0]
        item['zh_name'] = zh_name[0]
        item['jobs'] = jobs
        item['description'] = description[0]
        item['recently_chara'] = recently_chara
        item['recently_participated'] = recently_participated
        item['visuals'] = visuals[0]
        item['comment_box'] = comment_box
        item['comment_num'] = comment_num
        item['visit_num'] = 0
        #查找不整齐数据并保存
        # 获取node_list,node_list下有很多li
        node_list = response.xpath('//*[@id="infobox"]//li')
        # 计数
        k = 1
        # 针对无跳转链接：创建默认值
        item['gender'] = ['']
        item['names'] = ['']
        #extra_data
        item['extra_data'] = {}
        extra_data = {}
        # node是node_list下的子li，对li查找关键字，在translateTable中寻找对应
        for node in node_list:
            texts = valueof(node, 'span')
            text = [texts[0][texts[0].index('">') + 2:texts[0].rindex(':')]]
            # 创建空list 保存可能有的数据
            empty_list = []
            # 找到对应li
            if translateTable2.__contains__(text[0]):
                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                # 针对无跳转链接且分li[]储存的项目：别名、平台
                if text[0] == '别名':
                    # 一定是list，不作判断
                    if item[translateTable2[text[0]]['name']] == ['']:
                        content[0] = content[0].strip('、')
                        item[translateTable2[text[0]]['name']] = content[0].split('、')
                    else:
                        item[translateTable2[text[0]]['name']].append(content[0])
                else:
                    # 针对无跳转链接：
                    if content != [' ']:
                        # 判断是否需要保存为列表形式
                        if translateTable2[text[0]]['list']:
                            content[0] = content[0].strip('、')
                            item[translateTable2[text[0]]['name']] = content[0].split('、')
                        else:
                            item[translateTable2[text[0]]['name']] = content[0]
                        # 包含 常规情况（有跳转）
                        content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                        if content != [' ']:
                            nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                            # 把a中的关键数据提取，保存到empty_list中
                            for nodes in nodes_list:
                                member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                                item[translateTable2[text[0]]['name']].append(member)
                    # 常规情况：找到li下的所有子a
                    else:
                        pass
            else:

                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                # 针对无跳转链接：
                # 此处作的判断：如果是无跳转链接的数据，直接content就有数据了，而有跳转链接的项，需要进一步取数据，故为空
                empty_li = []
                if content != [' ']:
                    # # 判断是否需要保存为列表形式
                    # if translateTable1[text[0]]['list']:
                    content[0] = content[0].strip('、')
                    extra_data[text[0]] = content[0].split('、')
                    # else:
                    # extra_data[text[0]] = content[0]
                    # 包含 常规情况（有跳转）
                    content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                    if content != [' ']:
                        nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                        # 把a中的关键数据提取，保存到empty_list中
                        for nodes in nodes_list:
                            member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                            extra_data[text[0]].append(member)
                # 常规情况：找到li下的所有子a
                else:
                    nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                    # 把a中的关键数据提取，保存到empty_list中
                    for nodes in nodes_list:
                        member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                        empty_li.append(member)
                    # 若存在寻找的条目，写入数据
                    # 判断是否为列表保存
                    # if translateTable1[text[0]]['list']:
                    extra_data[text[0]] = empty_li
                    # else:
                    #     item[translateTable1[text[0]]['name']] = empty_li[0]

            item['extra_data'] = extra_data
            k = k + 1
        #最后判断是person还是company
        if item['gender'] == ['']:
            item['typo'] = 'company'
        else:
            item['typo'] = 'real_person'
        # #退出当前url
        yield item
        pass

    def parse3(self, response):

        # 提取数据
        def valueof(response, path, default=[' ']):
            content = response.xpath(path).extract()
            if len(content) == 0 or content[0] == '、':
                return default
            else:
                return content

        item = MyspiderItem()
        # 提取全局ID
        try:
            gap = 400000
            guid = gap + int(re.sub("\D", "", str(response.url)))
        except(Exception):
            guid = 0
        # 提取原名
        try:
            pr_name = valueof(response, '//*[@id="headerSubject"]/h1/a/text()')
        except(Exception):
            pr_name = [' ']
        # 提取中文名 若为空则与原名相同
        # //*[@id="headerSubject"]/h1/small
        try:
            zh_name = valueof(response, '//*[@id="headerSubject"]/h1/small', pr_name)
            if zh_name != pr_name:
                zh_name = [zh_name[0][zh_name[0].index('>')+1:zh_name[0].rindex('<')]]
        except(Exception):
            zh_name = [' ']
        # 提取描述//*[@id="columnCrtB"]/div[2]
        try:
            des = response.xpath('//*[@id="columnCrtB"]/div[2]').extract()
            if len(des) == 0:
                description = [" "]
            else:
                description = [des[0][des[0].index(">") + 1:des[0].rindex("<") - 1]]
        except(Exception):
            description = [' ']
        # 提取图片
        try:
            visual = valueof(response, '//*[@id="columnCrtA"]/div[1]/div/a/img')
            if visual[0] != ' ':
                visuals = ['https:' + visual[0][visual[0].index("=") + 2:visual[0].rindex("class") - 2]]
            else:
                visuals = ['']
        except(Exception):
            visuals = [' ']
        # 最近参与
        # 初始化全体
        recently_participated = []
        try:
            node_list = response.xpath('//*[@id="columnCrtB"]/ul//li')
            for node in node_list:
                subject = {
                    'guid': 0,
                }
                guids = valueof(node, 'div/a')
                # 该character类别下需要作如下判断，以跳过空项
                if guids == [' ']:
                    continue
                else:
                    chara_guid = int(guids[0][guids[0].index('subject') + 8:guids[0].index('title') - 2])
                # //*[@id="columnCrtB"]/ul[2]/li[1]/div/a/img
                #//*[@id="columnCrtB"]/ul/li[1]/div/a/img
                img_urls = valueof(node, 'div/a/img')
                part_url = img_urls[0][img_urls[0].index('src') + 5:img_urls[0].index('alt') - 2]
                pri_name = img_urls[0][img_urls[0].index('alt') + 5:img_urls[0].index('class') - 2]
                img_url = 'https:' + part_url
                # //*[@id="columnCrtB"]/ul[2]/li[1]/div/div/span
                # //*[@id="columnCrtB"]/ul/li[2]/div/div/span
                badge_job = valueof(node, 'div/div/span')
                job = badge_job[0][badge_job[0].index('>') + 1:badge_job[0].rindex('<')]

                subject['guid'] = chara_guid
                subject['pri_name'] = pri_name
                subject['visuals'] = img_url
                subject['badge_job'] = job
                recently_participated.append(subject)
        except(Exception):
            recently_participated = [' ']
        ###
        # 吐槽箱
        comment_box = []
        c = 1
        comment_check = valueof(response, '//*[@id="columnCrtB"]/div[' + str(c) + ']/h2')
        try:
            while not comment_check[0].__contains__('吐槽箱'):
                c = c + 1
                comment_check = valueof(response, '//*[@id="columnCrtB"]/div[' + str(c) + ']/h2')
            path = '/html/body/div[1]/div[4]/div[1]/div[2]/div[' + str(c) + ']/div//div'
            comment_list = response.xpath(path)
            # 初始化评论数
            comment_num = 0
            for comment in comment_list:
                box = {
                    'floor_num': '',
                }
                # 读取评论人id
                comment_name = valueof(comment, 'div[2]/strong/a')
                if comment_name == [' ']:
                    continue
                comment_name = comment_name[0][comment_name[0].index('>') + 1:comment_name[0].rindex('<')]
                # 提取评论楼层
                comment_floor = valueof(comment, 'div[1]/small/a')
                comment_floor = comment_floor[0][comment_floor[0].rindex('#') + 1:comment_floor[0].rindex('<')]
                # 不读评论的子评论
                if comment_floor.__contains__('-'):
                    continue
                # 提取评论内容
                comment_texts = valueof(comment, 'div[2]/div/div/text()')
                comment_texts = comment_texts[0].strip('\n')
                comment_texts = comment_texts.strip()
                comment_texts = comment_texts.strip('\t')
                comment_texts = comment_texts.strip('\n')
                comment_texts = comment_texts.strip()
                comment_texts = comment_texts.strip('\t')
                # 提取评论人头像url
                #//*[@id="post_20"]/a/span
                #//*[@id="post_86200"]/a/span
                #/html/body/div[1]/div[4]/div[1]/div[2]/div[6]/div/div[100]/a/span
                comment_img = valueof(comment, 'a/span')
                part_url = comment_img[0][comment_img[0].index('url') + 5:comment_img[0].rindex('<') - 4]
                comment_img = 'https:' + part_url
                # 提取评论时间
                comment_time = valueof(comment, 'div[1]/small/text()')
                comment_time = comment_time[0][comment_time[0].index('-') + 2:]

                box['commenter_name'] = comment_name
                box['floor_num'] = comment_floor
                # 读取评论数
                comment_num = comment_floor
                box['comment_texts'] = comment_texts
                box['comment_visuals'] = comment_img
                box['comment_time'] = comment_time
                comment_box.append(box)
        except(Exception):
            comment_box = [' ']
        # 整齐数据保存结果为json文件
        item['guid'] = guid
        item['typo'] = 'character'
        item['primary_name'] = pr_name[0]
        item['zh_name'] = zh_name[0]
        item['description'] = description[0]
        item['recently_participated'] = recently_participated
        item['comment_box'] = comment_box
        item['comment_num'] = comment_num
        item['visit_num'] = 0
        item['visuals'] = visuals[0]
        # 查找不整齐数据并保存
        # 获取node_list,node_list下有很多li
        node_list = response.xpath('//*[@id="infobox"]//li')
        # 计数
        k = 1
        # 针对无跳转链接：创建默认值
        item['names'] = ['']
        #extra_data
        item['extra_data'] = {}
        extra_data = {}
        # node是node_list下的子li，对li查找关键字，在translateTable中寻找对应
        for node in node_list:
            texts = valueof(node, 'span')
            text = [texts[0][texts[0].index('">') + 2:texts[0].rindex(':')]]
            # 创建空list 保存可能有的数据
            empty_list = []
            # 找到对应li
            if translateTable3.__contains__(text[0]):
                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                # 针对无跳转链接且分li[]储存的项目：别名
                if text[0] == '别名':
                    # 一定是list，不作判断

                    if item[translateTable3[text[0]]['name']] == ['']:
                        content[0] = content[0].strip('、')
                        item[translateTable3[text[0]]['name']] = content[0].split('、')
                    else:
                        item[translateTable3[text[0]]['name']].append(content[0])
                else:
                    # 针对无跳转链接：
                    if content != [' ']:
                        # 判断是否需要保存为列表形式
                        if translateTable3[text[0]]['list']:
                            content[0] = content[0].strip('、')
                            item[translateTable3[text[0]]['name']] = content[0].split('、')
                        else:
                            item[translateTable3[text[0]]['name']] = content[0]
                        # 包含 常规情况（有跳转）
                        content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                        if content != [' ']:
                            nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                            # 把a中的关键数据提取，保存到empty_list中
                            for nodes in nodes_list:
                                member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                                item[translateTable3[text[0]]['name']].append(member)
                        else:
                            pass
                    # 常规情况：找到li下的所有子a
                    else:
                        pass
            else:
                content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/text()')
                # 针对无跳转链接：
                # 此处作的判断：如果是无跳转链接的数据，直接content就有数据了，而有跳转链接的项，需要进一步取数据，故为空
                empty_li = []
                if content != [' ']:
                    # # 判断是否需要保存为列表形式
                    # if translateTable1[text[0]]['list']:
                    content[0] = content[0].strip('、')
                    extra_data[text[0]] = content[0].split('、')
                    # else:
                    # extra_data[text[0]] = content[0]
                    # 包含 常规情况（有跳转）
                    content = valueof(response, '//*[@id="infobox"]/li[' + str(k) + ']/a')
                    if content != [' ']:
                        nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                        # 把a中的关键数据提取，保存到empty_list中
                        for nodes in nodes_list:
                            member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                            extra_data[text[0]].append(member)
                # 常规情况：找到li下的所有子a
                else:
                    nodes_list = response.xpath('//*[@id="infobox"]/li[' + str(k) + ']//a')
                    # 把a中的关键数据提取，保存到empty_list中
                    for nodes in nodes_list:
                        member = nodes.extract()[nodes.extract().index('>') + 1:nodes.extract().rindex('<')]
                        empty_li.append(member)
                    # 若存在寻找的条目，写入数据
                    # 判断是否为列表保存
                    # if translateTable1[text[0]]['list']:
                    extra_data[text[0]] = empty_li
                    # else:
                    #     item[translateTable1[text[0]]['name']] = empty_li[0]

            item['extra_data'] = extra_data
            k = k + 1
        # #退出当前url
        yield item
        pass
