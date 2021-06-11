def maior(* num):
    max = min(num)
    
    for el in num:
        if(el>max):
            max=el
    
    print(f'O maior número é {max}')


maior(6,1,4,2,5,2)