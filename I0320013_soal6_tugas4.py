x= 4
y= 11

a= x | y
print('nilai :',x,', binary:',format(x,'03b'))
print('nilai :',y,', binary:',format(y,'04b'))
print('----------------------(|)')
print('nilai :',a,', binary:',format(a,'08b'))

b= x >> 11
print('nilai :',x,', binary:',format(x,'03b'))
print('----------------------(>>)')
print('nilai :',b,', binary:',format(b,'08b'))

c= x ^ y
print('nilai :',x,', binary:',format(x,'03b'))
print('nilai :',y,', binary:',format(y,'04b'))
print('----------------------(^)')
print('nilai :',c,', binary:',format(c,'08b'))

d= ~x
print('nilai :',x,', binary:',format(x,'03b'))
print('----------------------(~)')
print('nilai :',d,', binary:',format(d,'08b'))

e= y & x
print('nilai :',y,', binary:',format(y,'03b'))
print('nilai :',x,', binary:',format(x,'04b'))
print('----------------------(&)')
print('nilai :',e,', binary:',format(e,'08b'))