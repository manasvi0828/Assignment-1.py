import re
test_str = "wow, what a wonderful day!!!;"
print("The original string is : " + test_str)
res = re.sub(r'[^\w\s]', '', test_str)

print("The string after punctuation filter : " + res)