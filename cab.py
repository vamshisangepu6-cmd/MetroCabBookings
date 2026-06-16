fromstation=input("Enter the From_station: ")
tostation=input("Enter the To_station: ")
ticket=int(input("Enter the number of tickets: "))
if fromstation==tostation:
    print("Please enter correct station names") 
else:
    print(f"Selected :{fromstation}")
    print("To")
    print(f"{tostation}")   
    metrobill=ticket*50
    op=int(input("""Do you need a cab?
    1.Yes
    2.No"""))
    if op==1:
        dest=input("Enter the destination: ")
        print(f"cab from :{tostation} to {dest} ")
        cabbill=100
        totalbill=metrobill+cabbill
        print(f"Total bill is : {totalbill}")
    elif op==2:
        print(f"Total bill is : {metrobill}")
    else:
        print("Invalid option")
        