pos_x, pos_y, w, h = map(int, input().split())

print(min((pos_x, pos_y, h-pos_y, w-pos_x)))
