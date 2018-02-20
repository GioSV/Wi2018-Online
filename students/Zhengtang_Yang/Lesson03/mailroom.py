from cursesmenu import SelectionMenu

def first_selection(res):
	response = input("Enter a Full Name or 'list' to see donor\n")
	while response == 'list':
		for item in res.keys():
			print(item)
		print('\n')
		response = input("Enter a Full Name or 'list' to see donor\n")
	else:
		if response in res:
			d_amount = input("Enter a donation amount\n")
			res[response].append(int(d_amount))
			print(response + ', thank you for your donation.')
			input("Press Enter to continue...")
		else:
			d_amount = input("Enter a donation amount\n")
			res[response] = [int(d_amount)]
			print(response + ', thank you for your donation.')
			input("Press Enter to continue...")
	return res

def second_selection(res):
	header = ('Donor Name','Total Given','Num Gifts','Average Gift')
	row_format, row_format0 = '{:<14}','{:<14}'
	for item in header[1:]:
		row_format += f' | {{:>{len(item)}}}'
		row_format0 += f'  {{}}{{:>{len(item)}}}'
	print(row_format.format(*header))
	print('-'*len(row_format.format(*header)))
	for item in res.keys():
		print(row_format0.format(item,'$',sum(res[item]),' ',len(res[item]),'$',round(sum(res[item])/len(res[item]),1)))
	input("Press Enter to continue...") 

if __name__ == "__main__":
	donors = {'Batman':[100,50,30],'Ironman':[70,80],'Hulk':[10],'Spiderman':[40,20],'Superman':[40,60,10]}
	a_list = ['Send a Thank You','Create a Report']
	while True: 
		selection = SelectionMenu.get_selection(a_list)
		if selection == 0:
			donors = first_selection(donors)
		elif selection == 1:
			second_selection(donors)
		else:
			break
