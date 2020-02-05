def main():
	list_items=[]
	stop = ''
	total=0
	while stop != 'done':
		item=input('Item (enter "done" when finished):')
		if (item != 'done'):
			price=int(input('Price:'))
			quantity=int(input('Quantity:'))
			list_items.append({'name':item,'price':price,'quantity':quantity})
		else:
			stop=item



	# write code here
	print('---------------\n receipt\n--------------')
	for item in list_items:
		total_item=item['price']*item['quantity']
		print (item['quantity'],item['name'],item['price']*item['quantity'],'KD')
		total+=total_item

	print('Total Price: ',total,'KD')



if __name__ == '__main__':
	main()
