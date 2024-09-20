from abc import ABC, abstractmethod
import re
class Price_Calculator:
    @abstractmethod
    def price_calculating(self, price):
        pass

class price_discount_class(Price_Calculator):
    def __init__(self, discount_rate):
        self.discount_rate = discount_rate
    def price_calculating(self, price):
        return price * self.discount_rate

class price_return_class(Price_Calculator):
    def __init__(self, stage, num):
        self.stage = stage
        self.num = num

    def price_calculating(self, price):
        return price - (price//self.stage) * self.num

class price_normal(Price_Calculator):
    def price_calculating(self, price):
        return price


class decision:
    def __init__(self, rule, price):
        self.rule = rule
        self.price = price
    
    def price_return(self):
        # 定义正则表达式模式
        pattern = r"满(\d+)减(\d+)"
        # 使用正则表达式查找匹配的内容
        match = re.search(pattern, self.rule)
        if match:
            # 提取匹配的数值
            full_value = int(match.group(1))
            discount_value = int(match.group(2))
            return full_value, discount_value
        else:
            return None, None

    def price_discount(self):
        # 定义正则表达式模式
        pattern = r"打(\d+)折"
        # 使用正则表达式查找匹配的内容
        match = re.search(pattern, self.rule)
        if match:
            # 提取匹配的数值
            discount_value = int(match.group(1))
            discount_value = int(discount_value) / 10
            return discount_value
        else:
            return None

    def rule_parsing(self):
        if "满" in self.rule and "减" in self.rule:
            stage, num = self.price_return()
            price = price_return_class(stage, num).price_calculating(self.price)
            return price

        elif "打" in self.rule and "折" in self.rule:
            rate = self.price_discount()
            price = price_discount_class(rate).price_calculating(self.price)
            return price

        elif self.rule == "正常收费":
            return self.price
            
        
    


