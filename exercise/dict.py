stock = {
    "name" : "GOOG",
    "shares": 100,
    "price":490.10
}

name  = stock["name"]

# empty dict
prices  = {}
if "SCOX" in prices:
    p = prices["SCOX"]
else:
    p = 0.0

p = prices.get("SCOX", 0.0)
syms = list(stock)
for key in stock:
    print key , stock[key]

print stock
print syms
del stock["price"]
print stock
values=range(1,11)+'Jack Queen King'.split()   
suits='diamonds clubs hearts spades'.split()
deck=['%s of %s' %(v, s) for v in values for s in suits]
print deck



