# Follow the instructions for how to code this application
print("\n\t\t*** Wedding Planner ***\n")
inputtext="dummy"
guest_list=[]
while inputtext:
	inputtext=input("Enter a guest's name or type 'end' to stop.\n - ")
	if inputtext.lower()=="end":
		break
	else:
		guest_list.append(inputtext)
print("\n  Guest List:")
for guest in guest_list:
	print(" - "+guest)
guest_count=len(guest_list)
total_cost=12*guest_count
print(f"\nYou have invited {guest_count} guests at a cost of ${total_cost:.2f} for food")