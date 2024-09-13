speedlimit= float(input( 'what is the speed limit in miles per hour? '))
speed=float(input( 'what is your speed in miles per hour ')) 
distance= float(input( 'what distance are you travelling? '))
savedtime=0

time= distance/speedlimit
speedtime= distance/speed

minutes= 60
time1= minutes*time
time2=minutes*speedtime

if speed > speedlimit:
    savedtime=time1-time2
else:
    print('you do not save any time')

print(f'time taken at speed limit {time1:.2f}')
print(f'time taken when speeding {time2:.2f}')
print(f'time saved {savedtime:.2f}')
