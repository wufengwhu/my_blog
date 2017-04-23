#coding=utf-8
import fileinput, re
field_pat=re.compile(r'\[(.+?)\]') #匹配中括号里的字段

scope={}

def replacement(match):
    code=match.group(1)
    try:
        #如果字段可以求值,返回它
        return str(eval(code, scope))
    except SyntaxError:
        # 否则执行相同作用域内的赋值语句
        exec code in scope
        return ''

# 将所有文本以一个字符串的形式获取
lines=[]
for line in fileinput.input():
    lines.append(line)
text=''.join(lines)

#将field模式的所有匹配项都替换掉
print field_pat.sub(replacement, text)