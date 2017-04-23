#coding=utf-8
fields = (line.split() for line in open("portfolio.txt"))
portfolio = [ { 'name': f[0],
                'shares':int(f[1]),
                'price' : float(f[2])}
                for f in fields]
msft = [ s for s in portfolio if s['name'] == 'MSFT']
large_holdings = [s for s in portfolio if s['shares']*s['price'] >= 1000]
print(sum(float(f[1]) * float(f[2]) for f in fields))