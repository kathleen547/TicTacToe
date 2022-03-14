#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:12:34 2022

@author: katoshee
"""
# %%

def printBoard(A):
    x=0
    print('  0 1 2')
    for i in A:
        print(x,end=(" "))
        for j in i:
            print(j, end=(" "))
        x+=1
        print("")
        
def changePlayer(x):
    if x=='X':
        return '0'
    else:
        return 'X'
    
def checkWinner(z):
    if (p[0][0]==z and p[0][1]==z and p[0][2]==z) or (p[1][0]==z and p[1][1]==z \
        and p[1][2]==z)or (p[2][0]==z and p[2][1]==z and p[2][2]==z):
        return True
    elif (p[0][0]==z and p[1][0]==z and p[2][0]==z) or(p[0][1]==z and p[1][1]==z \
        and p[2][1]==z) or (p[0][2]==z and p[1][2]==z and p[2][2]==z):
        return True
    elif (p[0][0]==z and p[1][1]==z and p[2][2]==z) or (p[0][2]==z and p[1][1]==z \
        and p[2][0]==z):
        return True
    else:
        return False
    
p=[['_','_','_'],
   ['_','_','_'],
   ['_','_','_']]

sign='X'
moves=0

while True:
    print('Your move '+ sign)
    printBoard(p)
    print('Enter coordinates:')
    a=input('row: ')
    if not a.isdigit():
        continue
    a=int(a)
    if a<0 or a>2:
        print('Invalid number of row. Try again')
        continue
    b=input('column: ')
    if not b.isdigit():
        continue
    b=int(b)
    if b<0 or b>2:
        print('Invalid number of colum. Try again')
        continue
    if p[a][b]=='_':
        p[a][b] = sign
        moves+=1
    else:
        print('Invalid move!! Try again')
        continue
    winner=checkWinner(sign)
    if winner:
        print('Congratulations!! You won:'+ sign)   
        break
    if moves==9:
        print('Tie!!')
        break
    sign=changePlayer(sign)
    
