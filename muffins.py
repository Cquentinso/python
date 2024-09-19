


choice=input('Do you want a muffin or a cupcake?')
muffin=10
cupcakes=10

while choice!='0':
    
    if choice=='muffin' and muffin>0:
         muffin= muffin-1
         
         if choice=='muffin' and muffin==0: 
          print('Muffins are out of stock')
        
    if choice=='cupcakes' and cupcakes>0:
         cupcakes= cupcakes-1
         
         if choice=='cupcakes' and cupcakes==0:
              print('cupcakes are out of stock')
    choice=input('Do you want a muffin or a cupcake?')
              

print ('cupcakes:',cupcakes)
print('muffins:',muffin)
