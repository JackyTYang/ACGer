# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:

    #整齐数据
    #全局ID
    guid = scrapy.Field()
    #条目类型
    typo = scrapy.Field()
    #原名
    primary_name = scrapy.Field()
    #中文名
    zh_name = scrapy.Field()
    #评分
    score_general = scrapy.Field()
    #打分人数
    vote_count = scrapy.Field()
    #简介
    description = scrapy.Field()
    #演员列表
    chara_list = scrapy.Field()
    #相关条目
    related_subjects = scrapy.Field()
    #条目图片url
    visuals = scrapy.Field()
    #tags
    tags = scrapy.Field()
    #吐槽箱
    comment_box = scrapy.Field()
    #吐槽数
    comment_num = scrapy.Field()
    #访问量「虚」
    visit_num = scrapy.Field()


    # 不整齐数据
    # 导演
    director = scrapy.Field()
    # 演出
    chara_list = scrapy.Field()
    # 制片人
    producer = scrapy.Field()
    # 别名
    names = scrapy.Field()
    # 总话数
    episode_count = scrapy.Field()
    # 放送开始
    start_date = scrapy.Field()
    # 音乐制作
    music_composer = scrapy.Field()
    # 动画制作
    animation_company = scrapy.Field()
    # 全局制作
    made = scrapy.Field()

    #game
    #开发公司
    developer = scrapy.Field()
    #游戏类型
    genre = scrapy.Field()
    #游戏引擎
    engine = scrapy.Field()
    #游戏平台
    platform = scrapy.Field()

    #music
    #艺术家
    singer = scrapy.Field()
    #作曲
    composer = scrapy.Field()
    #作词
    lyrics = scrapy.Field()

    #book
    #书籍类型
    book_type = scrapy.Field()
    #作者
    writer = scrapy.Field()
    #出版社
    press = scrapy.Field()

    #person && company
    #性别
    gender = scrapy.Field()
    #生日
    birthday = scrapy.Field()
    #职业
    jobs = scrapy.Field()
    #最近演出
    recently_chara = scrapy.Field()
    #最近参与
    recently_participated = scrapy.Field()

    #character
    cv = scrapy.Field()

    #extract_data
    extra_data = scrapy.Field()
    #anime
    scr_text = scrapy.Field()
    sub_mirror = scrapy.Field()
    production_staff = scrapy.Field()
    pic_staff = scrapy.Field()
    music_staff = scrapy.Field()
    paint_supervisor = scrapy.Field()
    sup_paint_supervisor = scrapy.Field()
    official_website = scrapy.Field()
    end_data = scrapy.Field()
    #book
    page_num = scrapy.Field()
    volume_num = scrapy.Field()
    word_num = scrapy.Field()
    magazine = scrapy.Field()
    #music
    music_label = scrapy.Field()
    disc_price = scrapy.Field()
    disc_num = scrapy.Field()
    recording = scrapy.Field()
    version_features = scrapy.Field()
    play_time = scrapy.Field()
    #game
    plan_maker = scrapy.Field()
    people_num = scrapy.Field()
    game_price = scrapy.Field()
    game_designer = scrapy.Field()
    #people & company
    blood_type = scrapy.Field()
    height = scrapy.Field()
    its_source = scrapy.Field()
    constellation = scrapy.Field()
    country = scrapy.Field()
    personal_status = scrapy.Field()
    twitter = scrapy.Field()
    #character
    weight = scrapy.Field()
    pass
