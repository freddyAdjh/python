#-*- coding: utf-8 -*-

import random,json,time
GivenLetters = []
alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

with open("list.json",'r') as file:
    fichier = json.load(file)

    b = True

    s =  set()
    g = set()
    SetFinal = set()
    # print(type(g))
    lenWord = int(input("Entrer la longueur de votre mot: "))

    numLetters = 12
    
    for i in range(numLetters):
        e = input("Entrer une des  lettres: ")
        g.add(e)
        GivenLetters.append(e.lower())
    # print(g)
    start = time.time()
    for k in GivenLetters:
        for l in fichier:
            if k == l:
                for j in fichier[k]:
                    if len(j) == lenWord:
                        # j.replace("é","e")
                        # j.replace("è","e")
                        # j.replace("ë","e")
                        # j.replace("ê","e")
                        # j.replace("â","a")
                        # j.replace("ä","a")
                        # j.replace("ö","o")
                        # j.replace("ô","o")
                        # j.replace("ô","o")
                        # j.replace("î","i")
                        # j.replace("ï","i")
                        # j.replace("ù","u")
                        # j.replace("ü","u")
                        # j.replace("û","u")
                        s.add(j)
    
    # print(s)

    i=0
    
    
    for e in s:
        for k in e:
            if k in g:
                i+=1
        
        if i==lenWord:
            SetFinal.add(e)
        i=0
    print(f'{SetFinal,len(SetFinal)}')
    end = time.time()
    print(f'{end-start}')
    


        
        
    



    
