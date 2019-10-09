def make_pizza(size,*toppings):
    """g概述要制作的披萨"""
    print('\nMaking a '+ str(size) + '-inch pizza with the following toppings:')
    for topping in toppings:
        print('-'+ topping)
		
def display_message():
    print('\nIn Chapter 8, I learned how to define and use functions with '
          'Python.')
		  