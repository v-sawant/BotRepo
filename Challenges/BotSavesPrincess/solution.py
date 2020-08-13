#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    rownum = 0
    colnum = 0
    bot = tuple()# (0,0) #initialize
    princess = tuple()# (0,1) #initialize
    for gp in grid:
        for gpr in gp:
            if(gpr == 'm'):
                bot = (rownum, colnum%n)
            if(gpr == 'p'):
                princess = (rownum, colnum%n)
            colnum = colnum + 1
        rownum = rownum + 1
    #print("BOT POS:", bot)
    #print("Princess POS:", princess)
    
    while bot != princess:
        if(bot[0] > princess[0]):
            print("LEFT")
            bot = bot[0] - 1, bot[1]
        if(bot[0] < princess[0]):
            print("RIGHT")
            bot = bot[0] + 1, bot[1]
        if(bot[1] < princess[1]):
            print("DOWN")
            bot = bot[0], bot[1] + 1
        if(bot[1] > princess[1]):
            print("UP")
            bot = bot[0], bot[1] - 1
            
        #if bot[0] == princess[0] and bot[1] == princess[1]:
         #   break
        #continue

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)