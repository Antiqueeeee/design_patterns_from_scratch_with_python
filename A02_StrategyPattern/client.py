from component import decision

input_data = [(300,8,"打8折"),(300,8,"满10减1"),(300,8,"正常收费")]
for data in input_data:
    price, num , rule = data
    dec = decision(rule=rule,price=price * num)
    print(f"应收费：{dec.rule_parsing()}")
