def remove_duplicate(numbers):                                                           
	mylist = []                                                                          
	for item in numbers:                                                                 
		if item not in mylist:                                                           
			mylist.append(item)                                                          
	return mylist                                                                        
numbers =  [22,11,3,5,5,5,5,5,5,5,5,5,5,5,55,5,5,5,5,5,5,5,5,5,55,5,5,5,5,77,44,56]      
                                                                                         
print(remove_duplicate(numbers))                                                         
