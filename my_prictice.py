#https://github.com/zenoswang/String-practice/blob/main/my_prictice.py
###
###有一个不定长度的String，其中前面是字母，后边是数字,例如："abcd123.456", 
###要求写一个方法得到其中的数字以String的形式返回,数字保留小数点后两位， 不四舍五入，截去多余小数,
###例如："abcd123.456"，得到"123.45" 如果数字没有小数点,要得到两位为0的小数，例如："abcd123"，得到"123.00".

import re

def extract_and_format_number1(s):
    # 匹配字符串中的数字部分，包括可能的小数点和后面的数字
    match = re.search(r'(\d+)\.?(\d*)', s)
    if match:
        integer_part = match.group(1)
        decimal_part = match.group(2)
        # 如果小数部分存在，保留两位；如果不存在，添加"00"
        formatted_decimal = (decimal_part + '00')[:2]
        return f"{integer_part}.{formatted_decimal}"
    else:
        # 如果没有找到数字，理论上不应该发生，因为题目假设字符串包含数字
        return "No number found"

def extract_and_format_number2(s):
    # 使用正则表达式匹配字符串中的数字部分
    match = re.search(r'(\d+)\.?(\d*)', s)
    if match:
        # 提取整数部分和小数部分
        integer_part = match.group(1)
        decimal_part = match.group(2)
        # 格式化小数部分，确保小数点后有两位数字
        formatted_number = f"{integer_part}." + (decimal_part + "00")[:2]
        return formatted_number
    else:
        # 如果没有找到匹配的数字部分，返回原字符串
        return s


# 测试代码
test_strings = ["abcd123.456", "abcd123", "abcd123.", "abcd123.1", "abcd12.34", "abcd"]
print("test1===========================")
for test in test_strings:
    print(f"{test} -> {extract_and_format_number1(test)}")
print("test2===========================")
for test in test_strings:
    print(f"{test} -> {extract_and_format_number2(test)}")
