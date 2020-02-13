#function that present a random item from a list. 
#import random!!!


def random_list(the_list):
  stop = len(the_list)-1
  random_number = random.randint(0,stop)
  print(the_list[random_number])
