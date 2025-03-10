# for loop
#a=[1,5,6,8]
#for a in a:
#    print(a*2)


# Range in for loop
#for a in range(2,20,2):
 #   print(a)

# Nested for loop 
#p=['a','b','c']
#q=['x','y','z']
#for s in p:
#    for t in q:
#        print(s,t)


# print Rightangle triangle
#p=['*','* *','* * *','* * * *','* * * * *']
#for i in p:
#    print(i)

# print a car pattern 
# rows = 10


# a = [
#     "      * * * * *      ",
#     "     *          *       ",
#     "   *              *       ",
#     "* * * * * * * * * * * * *",
#     "*                       *",
#     "* * * * * * * * * * * * *",
#     "   *   *       *   *   ",
#     "     *           *    "
# ]

# for i in range(rows):
#     if i < len(a):
#         print(a[i])
#     else:
#            print()

#for loop car print
# for row in range(10):
#     for col in range(20):
#         if(row==0 and (col>4 and col<10)
#            or (row==1 and (col==4 or col==10))):
            
#             print('*',end=' ')
        
#         else:
#              print(' ',end=' ')
#     print()

#function in python
# def abc():
#     a=10
#     b=20
#     c=a+b
#     print(c)
# def add(a,b):
#     c=a+b
#     print(c)
# p=20
# q=40
# add(p,q)

# rows = 10
# cols = 20

# for row in range(rows):
#     for col in range(cols):
#         if (row == 0 and 6 <= col <= 10) or (row == 1 and (col == 5 or col == 11)) or \
#            (row == 2 and (col == 3 or col == 13)) or (row == 3) or \
#            (row == 4 and (col == 0 or col == cols - 1)) or (row == 5) or \
#            (row == 6 and (col == 3 or col == 6 or col == 13 or col == 16)) or \
#            (row == 7 and (col == 5 or col == 14)):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()  # Move to the next line

#display a car take an input from usre
def carA():
    row=102
    col=300
    for row in range(row):
        for col in range(col):
            if(row==0 and (col>=6 and col<=16)
                or (row==1 and (col==5 or col==17))
                or (row==2 and (col==4 or col==18))
                or (row==3 and (col==3 or col==19))
                or (row==4 and (col>=0 and col<=2))
                or (row==4 and (col>=20 and col<=22))
                or (row==5 and (col==0 or col==22))
                or (row==6 and (col==0 or col==22))
                or (row==7 and (col==0 or col==22))
                or (row==7 and (col>=2 and col<=3))
                or (row==7 and (col>=7 and col<=8))
                or (row==7 and (col>=12 and col<=13))
                or (row==7 and (col>=17 and col<=18))
                or (row==7 and (col>=20 and col<=22))
                or (row==8 and (col>=1 and col<=4))
                or (row==8 and (col>=6 and col<=9))
                or (row==8 and (col>=11 and col<=14))
                or (row==8 and (col>=16 and col<=19))
                or (row==9 and (col>=2 and col<=3))
                or (row==9 and (col>=7 and col<=8))
                or (row==9 and (col>=12 and col<=13))
                or (row==9 and (col>=17 and col<=18))
                ):
                
                print('*',end=' ')
            
            else:
                print(' ',end=' ')
        print()

    print("--------------- CAR A ----------------------- ")

def carB():
    row=12
    col=30
    for row in range(row):
        for col in range(col):
            if(row==0 and (col>=3 and col<=16)
                or (row==1 and (col>=2 and col<=13))
                or (row==1 and col==17)
                or (row==2 and (col>=1 and col<=13))
                or (row==2 and col==18)
                or (row==3 and (col>=0 and col<=13))
                or (row==3 and col==19)
                or (row==4 and (col>=0 and col<=13))
                or (row==4 and (col>=20 and col<=22))
                or (row==5 and (col==0 or col==22))
                or (row==6 and (col==0 or col==22))
                or (row==7 and (col>=2 and col<=3))
                or (row==7 and col==0)
                or (row==7 and (col>=7 and col<=8))
                or (row==7 and (col>=12 and col<=13))
                or (row==7 and (col>=17 and col<=18))
                or (row==7 and (col>=20 and col<=22))
                or (row==8 and (col>=1 and col<=4))
                or (row==8 and (col>=6 and col<=9))
                or (row==8 and (col>=11 and col<=14))
                or (row==8 and (col>=16 and col<=19))
                or (row==9 and (col>=2 and col<=3))
                or (row==9 and (col>=7 and col<=8))
                or (row==9 and (col>=12 and col<=13))
                or (row==9 and (col>=17 and col<=18))
                ):
                
                print('*',end=' ')
                
            
            else:
                print(' ',end=' ')
        print()
    print("--------------- CAR B ----------------------- ")


def weel2():
    row=12
    col=30
    for row in range(row):
        for col in range(col):
             if( (row==6 and (col==0 or col==22))
                or (row==6 and (col>=5 and col<=6))
                or (row==6 and (col>=15 and col<=16))
                or (row==7 and (col==0 or col==22))
                or (row==7 and (col>=4 and col<=7))
                or (row==7 and (col>=14 and col<=17))
                or (row==8 and (col>=0 and col<=2))
                or (row==8 and (col>=4 and col<=7))
                or (row==8 and (col>=9 and col<=12))
                or (row==8 and (col>=14 and col<=17))
                or (row==8 and (col>=19 and col<=22))
                or (row==9 and (col>=5 and col<=6))
                or (row==9 and (col>=15 and col<=16))
                ):
                
                print('*',end=' ')
             else:
                print(' ',end=' ')
        print()

def weel4():
    row=12
    col=30
    for row in range(row):
        for col in range(col):
             if( 
                (row==6 and (col==0 or col==22))
                or (row==7 and (col==0 or col==22))
                or (row==7 and (col>=2 and col<=3))
                or (row==7 and (col>=7 and col<=8))
                or (row==7 and (col>=12 and col<=13))
                or (row==7 and (col>=17 and col<=18))
                or (row==7 and (col>=20 and col<=22))
                or (row==8 and (col>=1 and col<=4))
                or (row==8 and (col>=6 and col<=9))
                or (row==8 and (col>=11 and col<=14))
                or (row==8 and (col>=16 and col<=19))
                or (row==9 and (col>=2 and col<=3))
                or (row==9 and (col>=7 and col<=8))
                or (row==9 and (col>=12 and col<=13))
                or (row==9 and (col>=17 and col<=18))
                ):
                
                print('*',end=' ')
             else:
                print(' ',end=' ')
        print()

def choice():
    print("Choose a car \n CAR A : 1 \n CAR B : 2 ")
    x=int(input("Enter Your Choice :"))
    print(f"Choose weels for car {x} \n 1 : Two weels \n 2 : Four weels ")
    y=int(input("Enter Your Choice :"))
    if (x==1 and y==1):
         row=12
         col=30
         for row in range(row):
                for col in range(col):
                    if( row==0 and (col>=6 and col<=16)
                        or (row==1 and (col==5 or col==17))
                        or (row==2 and (col==4 or col==18))
                        or (row==3 and (col==3 or col==19))
                        or (row==4 and (col>=0 and col<=2))
                        or (row==4 and (col>=20 and col<=22))
                        or (row==5 and (col==0 or col==22))
                        or (row==6 and (col==0 or col==22))
                        or (row==6 and (col>=5 and col<=6))
                        or (row==6 and (col>=15 and col<=16))
                        or (row==7 and (col==0 or col==22))
                        or (row==7 and (col>=4 and col<=7))
                        or (row==7 and (col>=14 and col<=17))
                        or (row==8 and (col>=0 and col<=2))
                        or (row==8 and (col>=4 and col<=7))
                        or (row==8 and (col>=9 and col<=12))
                        or (row==8 and (col>=14 and col<=17))
                        or (row==8 and (col>=19 and col<=22))
                        or (row==9 and (col>=5 and col<=6))
                        or (row==9 and (col>=15 and col<=16))
                        ):
                        
                        print('*',end=' ')
                    else:
                        print(' ',end=' ')
                print()
    elif(x==1 and y==2):
        row=12
        col=30
        for row in range(row):
                for col in range(col):
                    if( row==0 and (col>=6 and col<=16)
                        or (row==1 and (col==5 or col==17))
                        or (row==2 and (col==4 or col==18))
                        or (row==3 and (col==3 or col==19))
                        or (row==4 and (col>=0 and col<=2))
                        or (row==4 and (col>=20 and col<=22))
                        or (row==5 and (col==0 or col==22))
                        or (row==6 and (col==0 or col==22))
                        or (row==7 and (col==0 or col==22))
                        or (row==7 and (col>=2 and col<=3))
                        or (row==7 and (col>=7 and col<=8))
                        or (row==7 and (col>=12 and col<=13))
                        or (row==7 and (col>=17 and col<=18))
                        or (row==7 and (col>=20 and col<=22))
                        or (row==8 and (col>=1 and col<=4))
                        or (row==8 and (col>=6 and col<=9))
                        or (row==8 and (col>=11 and col<=14))
                        or (row==8 and (col>=16 and col<=19))
                        or (row==9 and (col>=2 and col<=3))
                        or (row==9 and (col>=7 and col<=8))
                        or (row==9 and (col>=12 and col<=13))
                        or (row==9 and (col>=17 and col<=18))
                        ):
                        
                        print('*',end=' ')
                    else:
                        print(' ',end=' ')
                print()
    elif(x==2 and y==1):
        row=12
        col=30
        for row in range(row):
                for col in range(col):
                    if( row==0 and (col>=3 and col<=16)
                        or (row==1 and (col>=2 and col<=13))
                        or (row==1 and col==17)
                        or (row==2 and (col>=1 and col<=13))
                        or (row==2 and col==18)
                        or (row==3 and (col>=0 and col<=13))
                        or (row==3 and col==19)
                        or (row==4 and (col>=0 and col<=13))
                        or (row==4 and (col>=20 and col<=22))
                        or (row==5 and (col==0 or col==22))
                        or (row==6 and (col==0 or col==22)) 
                        or (row==6 and (col>=5 and col<=6))
                        or (row==6 and (col>=15 and col<=16))
                        or (row==7 and (col==0 or col==22))
                        or (row==7 and (col>=4 and col<=7))
                        or (row==7 and (col>=14 and col<=17))
                        or (row==8 and (col>=0 and col<=2))
                        or (row==8 and (col>=4 and col<=7))
                        or (row==8 and (col>=9 and col<=12))
                        or (row==8 and (col>=14 and col<=17))
                        or (row==8 and (col>=19 and col<=22))
                        or (row==9 and (col>=5 and col<=6))
                        or (row==9 and (col>=15 and col<=16))
                        ):
                        
                        print('*',end=' ')
                    else:
                        print(' ',end=' ')
                print()
    elif(x==2  and y ==2):
                   carB()
        
 
    else:print(" invalid input \n -----------------!!ERROR!!---------------------")



    


    


         
# carA()
# carB()
# weel4()
# weel2()        
#from Python_clock import *samay()
choice()  