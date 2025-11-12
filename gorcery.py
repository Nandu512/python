rice=45;
sugar=40;
oil=130;
riceq=3;
sugarq=2.5;
oilq=1.8;
tpr=rice*riceq
tps=sugar*sugarq
tpo=oil*oilq
sugarq=int(sugarq)
oilq=int(oilq)
print('total price of rice is',tpr)
print('total price of sugar is',tps)
print('total price of oil is',tpo)
totalprice=tpr+tps+tpo
print('total bill is',int(totalprice))
import random
k=random.randrange(5,10)
print('delivery charge is',k)
finalbill=totalprice+k
print('total bill after delivery charge is',finalbill)


