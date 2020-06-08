def func_test(H, blocks=0):
    print(H)
    if(len(H)<=1):
        return 1

    top = H[0]
    aux = []

    for h in H:
        print("h: {}, top: {}, aux: {}, block:{}".format(h, top, aux, blocks))
        if(h==top):
            continue
        if(h > top):
            aux.append(h) 
        else:
            blocks = blocks + func_test(aux, blocks)
            aux=[]
            top = h
            
    if(len(aux)!=0):
        blocks = blocks + func_test(aux, blocks)
    print("")
    print("")
    
    return blocks

H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
func_test(H)