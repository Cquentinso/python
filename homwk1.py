import math

members= 4
Pizza= 8

num_slice= int(input('Enter the number of slices'))
total_slice= num_slice*members

pizza_total= math.ceil(total_slice/Pizza)
left_overs=total_slice%Pizza

print ('you need', pizza_total, 'pizzas with', left_overs, 'slice left over')
