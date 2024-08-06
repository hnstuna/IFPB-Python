s = float(input())

if s <= 280:
    print("%.2f" % round(s))
    print("20")
    print("%.2f" % round(s*0.20))
    print("%.2f" % round(s*0.20+s))

elif 280 < s < 700:
    print("%.2f" % round(s))
    print("15")
    print("%.2f" % round(s * 0.15))
    print("%.2f" % round(s * 0.15 + s))

elif 700 < s < 1500:
    print("%.2f" % round(s))
    print("10")
    print("%.2f" % round(s * 0.10))
    print("%.2f" % round(s * 0.10 + s))

elif s > 1500:
    print("%.2f" % round(s))
    print("5")
    print("%.2f" % round(s * 0.05))
    print("%.2f" % round(s * 0.05 + s))

