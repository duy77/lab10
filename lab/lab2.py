wh= float(input('enter hours: '))
wr = float(input('enter rate: '))


if wh> 40:
    pay = (wh*wr)+ ((wh-40)*wr*0.5)
    print(str(pay))
else:
    pay = wh*wr
    print(str(pay))
    
    