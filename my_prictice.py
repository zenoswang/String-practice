import re

def extract_and_format_number(s):
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

# 测试代码
test_strings = ["abcd123.456", "abcd123", "abcd123.", "abcd123.1", "abcd12.34", "abcd"]
for test in test_strings:
    print(f"{test} -> {extract_and_format_number(test)}")
