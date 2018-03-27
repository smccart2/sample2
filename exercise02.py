# -*- coding: utf-8 -*-
print "\n run by Shayna"
print 


while True:
    price = raw_input("Enter the price as cents, a multiple of five cents, or 'done' (without quotes) if you are finished: ")
    if price == "done":
        print "Good-bye!"
        break
    else:
        if price.isdigit() == False:
           print "Your input is not a number"

        if int(price) % 5 == 0:
            print "You entered", price, "cents."
        
        else:
            print "Your price is not a multiple of five cents"
            continue
