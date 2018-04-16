# Let's say we have 5 monkeys and a whole lot of peaches on a beach.
# The first monkey consumed 1 peach, and splited the rest of the peaches into 5 equal piles, took his pile, and left the rest on the beach.
# The second monkey consumed 1 peach, and splited the rest of the peaches into 5 equal piles, took his pile, and left the rest on the beach.
# The second monkey did so probably because he didn't realize the first monkey had already took his pile.
# The thrid monkey, fourth monkey, and the fifth monkey all did the same.

# Question:  How many peaches at lesat were on the beach? And how many peaches were left at each stage?

monkey=5

def resultprint(monkey, peach):
    if(monkey==0):
        return peach
    next = resultprint(monkey-1, peach)
    if (next % 4 ==0):
        print('peaches:'+ str(int(next*5/4+1)) + 'monkies:' + str(monkey))
        return next*5/4+1
    else:
        return -1;

def monkeypeach(monkey, peach):
    if(monkey==0):
        return peach
    next = monkeypeach(monkey-1, peach)
    if (next % 4 ==0):
        return next*5/4+1
    else:
        return -1;
	
	
		
def peachfinder(peach):
    while monkeypeach(monkey, peach) <0:
        peach=peach+1
    return resultprint(monkey,peach);		


if __name__ == "__main__":
    peachfinder(0);