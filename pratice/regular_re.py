import re

txt='geekforgeeks a computer science portal for geeks'
match=re.search(r'portal',txt)

if match:
    print(match.group())
    print("start:", match.start(), "End",match.end())
else:
    print("no match")