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
rows = 10
cols = 20

a = [
    "      * * * * *      ",
    "     *          *       ",
    "   *              *       ",
    "* * * * * * * * * * * * *",
    "*                       *",
    "* * * * * * * * * * * * *",
    "   *   *       *   *   ",
    "     *           *    "
]

for i in range(rows):
    if i < len(a):
        print(a[i])
    else:
           print()