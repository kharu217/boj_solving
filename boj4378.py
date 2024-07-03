while True :
    try :
        m = input()
        n=m.maketrans("WERTYUIOP[]\\","QWERTYUIOP[]")
        m=m.translate(n)

        n=m.maketrans("SDFGHJKL;\'","ASDFGHJKL;")
        m=m.translate(n)

        n=m.maketrans("XCVBNM,./","ZXCVBNM,.")
        m=m.translate(n)

        n=m.maketrans("1234567890-=","`1234567890-")
        m=m.translate(n)
        print(m)
    except :
        break