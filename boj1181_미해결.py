text_T = int(input())

text = [0 for i in range(text_T)]

for i in range(text_T) :
    text[i] = input()
    
text = list(set(text))

for a in range(text_T) :
    for b in range(1,len(text)) :
        if len(text[b-1]) > len(text[b]) :
            temp = text[b-1]
            text[b-1] = text[b]
            text[b] = text[b-1]
            
print(text)
