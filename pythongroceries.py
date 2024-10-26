prices = {'apple': 0.40, 'banana': 0.50, 'kiwi': 0.29,}
my_purchase = {
    'apple': 13,  #the amount of fruit I bought
    'banana': 6, # the amout of fruit I bought
    'kiwi':20} # the amount of fruit I bought
grocery_bill = sum(prices[fruit] * my_purchase[fruit]
                   for fruit in my_purchase)
print ('I owe the grocery store $%.2f' % grocery_bill)