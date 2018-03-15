xs = [25, 25, 25, 25, 25, 25, 25, 50, 50, 50, 100, 100, 100, 100]

def ii(p):
    gg = []
    
    for i in p:
        if i > 50:
            gg.append("大于50")
        elif i < 50:
            gg.append("小于50")
        else:
            gg.append("等于50")
    return gg

x = ii(xs)
print(x)  

