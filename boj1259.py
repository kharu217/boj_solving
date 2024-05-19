def is_falindrom(input_text):
    if len(input_text) == 1 :
        return True
    elif input_text == input_text[::-1] :
        return True
    else :
        return False
    
while True :
    text = input()
    
    check_text = is_falindrom(text)
    
    if int(text) == 0 :
        break
    elif check_text == True :
        print("yes")
    elif check_text == False:
        print("no")