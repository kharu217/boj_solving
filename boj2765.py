num = 0
while True:
    num += 1
    r_inch, spinT, s_time = map(float, input().split())
    if spinT == 0:
        break
    
    r_feat = r_inch/12
    r_mile = r_feat/5280

    m_time = s_time/60
    h_time = m_time/ 60
    
    l = 3.1415927*r_mile
    d = spinT*l
    v = d/h_time
    
    print("Trip #{}: {:.2f} {:.2f}".format(num, round(d, 2), round(v, 2)))

