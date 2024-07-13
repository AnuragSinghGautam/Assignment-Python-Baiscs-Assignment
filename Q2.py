# # # Describe the role of predefined keywords in Python and provide examples of how they are used in a program

# # Answer:

Predefined keywords in Python are reserved words with special meanings that has a specified meaning to the compiler and cannot be used as variables.
Examples of predefined keywords are:
1. if,else,elif:

if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")

2.for/while/break/continue: 

for i in range (10):
    if i==2:
        break;
    print(i)
######
i=0
while(i>10):
    {
        if i==3:
        continue
        i++
    }

Some other predefined ones include:
False 	await 	else 	import 	pass
None 	break 	except 	in 	raise
True 	class 	finally 	is 	return
and 	continue 	for 	lambda 	try
as 	def 	from 	nonlocal 	while
assert 	del 	global 	not 	with
async 	elif 	if 	or 	yield