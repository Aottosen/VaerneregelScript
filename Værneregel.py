import pandas as pd

see = pd.read_csv(r"C:\Users\asott\Desktop\Timeopgørelse\VærneregelFinalTest.csv")

i = len(see.index)

print("i= " + str(i))

Prev = see['Total Undervisning'][0]

PrevPrev = see['Total Undervisning'][1]


def værneregel(current, prev, prevPrev):

    savecurrent = see['Total Undervisning'][current]

    z = see['Total Undervisning'][current] + prev + prevPrev - 70.5

    global PrevPrev
    PrevPrev = prev

    global Prev
    Prev = savecurrent

    return z


for x in range(2, i):
    if see['Navn'][x] != see['Navn'][x - 2]:

        savecurrent = see['Total Undervisning'][x]

        see['Total Undervisning'][x] = 0

        PrevPrev = Prev

        Prev = savecurrent

    if see['Navn'][x] == see['Navn'][x - 2]:
        see['Total Undervisning'][x] = værneregel(x, Prev, PrevPrev)
        print(see['Navn'][x] + " " + str(see['Year-week'][x]) + " " + str(see['Total Undervisning'][x]))
    if x==2:
        PrevPrev = see['Total Undervisning'][1]

for x in range(2, i):
    if see['Navn'][x]==see['Navn'][x-2]:
        if see['Total Undervisning'][x] > 0 and (see['Total Undervisning'][x-1] > 0 or see['Total Undervisning'][x-2] > 0):

            if see['Total Undervisning'][x-1] > 0 and see['Total Undervisning'][x-2] > 0:
                see['Total Undervisning'][x] = see['Total Undervisning'][x]-(see['Total Undervisning'][x-1]+see['Total Undervisning'][x-2])
                print("test" + see['Navn'][x] + " " + str(see['Year-week'][x]) + " " + str(see['Total Undervisning'][x]))

            elif see['Total Undervisning'][x-1] > 0:
                see['Total Undervisning'][x] = see['Total Undervisning'][x] - see['Total Undervisning'][x-1]
                print("test" + see['Navn'][x] + " " + str(see['Year-week'][x]) + " " + str(see['Total Undervisning'][x]))

            elif see['Total Undervisning'][x-2] > 0:
                see['Total Undervisning'][x] = see['Total Undervisning'][x] - see['Total Undervisning'][x-2]
                print("test" + see['Navn'][x] + " " + str(see['Year-week'][x]) + " " + str(see['Total Undervisning'][x]))

for x in range(2, i):
    if see['Navn'][x]!=see['Navn'][x-2]:
        see['Total Undervisning'][x] = 0

see['Total Undervisning'][0] = 0

see['Total Undervisning'][1] = 0

see.to_csv("C:\\Users\\asott\\Desktop\\Timeopgørelse\\Værneregeltest.csv")