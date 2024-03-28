wh= float(input('enter hours: '))
wr = float(input('enter rate: '))

def compupay(hours,rate):
    if hours> 40:
        pay = (hours* rate)+ ((hours-40)*rate*0.5)
        print(str(pay))
    else:
        pay = hours*rate
    return pay
xp = compupay(wh,wr)

print('pay', xp)