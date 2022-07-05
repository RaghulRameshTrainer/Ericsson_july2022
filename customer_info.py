import sys

# To get the command line argument collected
# To exit the program based on conditions

if len(sys.argv) != 3:
    print("USAGE : {} {},  {}".format(sys.argv[0], "customer name","acct no"))
    print("Please rerun the prog with valid arguments.")
    print("Exiting....")
    sys.exit(0)
    
print("The program name :", sys.argv[0])
print("Customer name :" , sys.argv[1])
print("Account number :", sys.argv[2])
