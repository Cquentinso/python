muffin=10
cupcakes=10
i=0

for i in range(10):
    choice=input(str('Do you want a muffin or a cupcake?'))
    if choice=='muffin':
        muffin= muffin-1
    elif choice=='cupcakes':
        cupcakes= cupcakes-1
i=i+1
if cupcakes==0 and muffin==0:
    print('out of stock')

finish=input('press 0 to finish ')
print ('cupcakes:',cupcakes)
print('muffins:',muffin)
