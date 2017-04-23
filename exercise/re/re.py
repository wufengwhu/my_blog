# (pattern)* 允许模式重复0次或多次
# (pattern)+ 允许模式重复1次或多次
# (pattern){m, n} 允许模式重复m~n次
# group组的序号取决于它左侧的括号数
# group() start(), end(), span()
# this regular expression finds the non-word (numbers) between parentheses
grps = re.search("\((\w+)\)", raw)

emphasis_pattern=r'\* (.+)\*'  #