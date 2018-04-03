a_ccount = "liangwenqi"
p_asswd = "123456"
login = input("请选择登录方式:1.qq 2.weixin 3.账号登录")
if login == "1":
    fashi = str("妲己,貂蝉")
    zhanshi = str("宫本,猴子")
    tanke = str("刘邦,程咬金")
    h_hero = input("请选择你的英雄职业1.fashi 2.zhanshi 3.tanke")
    if h_hero == "fashi":
        hero = input("请选择你的英雄:1.妲己 2.貂蝉")
        if hero == "1":
            print("请尽情吩咐妲己")
        elif hero == "2":
            print("叮叮当,叮叮当，叮当铃儿响")
    elif h_hero == "zhanshi":
        hero = input("请选择你的英雄:1.宫本 2.猴子")
        if hero == "1":
            print("无敌的我又迷路了,这也许就是无敌的忧伤")
        elif hero == "2":
            print("取金之路就在脚下")
    elif h_hero == "tanke":
        hero = input("请选择你的英雄1.刘邦 2.程咬金")
        if hero == "1":
            print("良心是什么能吃吗")
        elif hero == "2":
            print("进攻是最好的防守")
    
