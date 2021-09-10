#The comments in this quiz (the lines that begin with #) have instructions for creating and modifying variables. After each comment write a line of code that implements the instruction.

#Note that this code uses scientific notation to define large numbers. 4.445e8 is equal to 4.445 * 10 ** 8 which is equal to 444500000.0.



# The current volume of a water reservoir (in cubic metres)
reservoir_volume= 4.445 * 10**8
# The current volume of a water reservoir (in cubic metres)
rainfall=5e6

# decrease the rainfall variable by 10% to account for runoff
precentage=5*(10**5)
decrease=rainfall-precentage
print('required answer is:',decrease)

# add the rainfall variable to the reservoir_volume variable
total=rainfall+reservoir_volume
print('needed answer is',total)

# increase reservoir_volume by 5% to account for stormwater that flows
percent=(5/100)*reservoir_volume
reservoir_volume+=percent
print('ans required',reservoir_volume)

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume-=percent

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume-=(2.5 * (10**5))

# print the new value of the reservoir_volume variable
print('new value of reservoir_volume is',reservoir_volume)