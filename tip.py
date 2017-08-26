# if time permits see if you can do a while loop so it starts over
bill = float(raw_input("What's your total? "))
service = raw_input("Was your service good, fair or bad? ")

if service.lower() == "good":
    print "Your tip should be $%.2f or more." % (bill * 0.20)
elif service.lower() == "fair":
    print "Your tip should be $%.2f or more." % (bill * 0.15)
elif service.lower() == "bad":
    print "Your tip should be $%.2f or more." % (bill * 0.10)
else:
    print "Please tell us whether your service was good, fair or bad."
