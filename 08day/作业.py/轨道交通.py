p_ath = int(input("输入路程"))
if p_ath <= 6:
    money = 3
elif p_ath > 6 and p_ath <=12:
    money = 4
elif p_ath > 12 and p_ath <= 22:
    money = 5
elif p_ath > 22 and p_ath <= 32:
    money = 6
elif p_ath >32:
    money = int((p_ath - 32)/20) + 7
    if money <= 100:
        print(money)
    elif money > 100 and money <= 150:
        m_money = (money - 100)*0.8 + 100
    elif money > 150 and money <= 400:
        m_money = 100 + 50*0.8+250*0.5
    elif money > 400:
        m_money = money
        
    
