import re

def extract_number(s):
    # 使用正则表达式匹配字符串中的数字部分
    match = re.search(r'\d+(?:\.\d+)?', s)
    if match:
        number_str = match.group()
        # 如果数字部分包含小数点，则截取小数点后两位
        if '.' in number_str:
            return number_str.rstrip('0').rstrip('.')
        else:
            # 如果没有小数点，则添加两位0
            return f"{number_str}.00"
    return ""

# 测试代码
test_strings = ["abcd123.456", "abcd123", "abcd123.", "abcd123.1", "abcd12.34", "abcd"]
for test in test_strings:
    print(f"{test} -> {extract_number(test)}")
