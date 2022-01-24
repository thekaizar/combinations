import random
theList = [1,2,3,'c','d']
#debug#print(theList[0:1])
#debug#print(theList[1:2])

def yourPassword(aList):
	selected = []
	for a in range(0,len(aList)):	
		##print('the length of a list is: ',len(aList))
		##print('the length of the list is: ',len(theList))
		#print('iteration: ',a)
		currentRandom = random.randint(0,a)
		selected.append(aList[currentRandom])
		#print('list length: ',len(aList))
		#aList.pop(currentRandom)
		#print(aList)
	print('Winning Ticket: ',selected)
	return selected

winningTicket = yourPassword(theList)

def swap(eins,zwei,drei):

	c = eins[zwei]
	eins[zwei] = eins[drei]
	eins[drei] = c

def combination(eins, d, zwei):

	if zwei == d:
		for e in d:
			print(e)
	else:
		for e in d:
			swap(eins, zwei, e)
			combination(eins, d, e+1)
			swap(eins, zwei, e)

def CainAndAbel(aList,winningTicket):
	print('length of winningTicket: ',len(winningTicket))
	print('the length of the list is: ',len(aList))

	eins = []

	for i in 4:
		print(i)


#	for c in range(0,len(aList)):
		#debug#print('c iteration is: ',c)
		#print(aList[c])

#		if aList[c] == winningTicket:
#			print('aMatch')

#		for d in range(0, len(aList)):    
			#debug#print('d iteration is: ',d)
			#debug#print(c,d)
			#debug#print(aList[c],aList[d])
#			print(aList[c:d+1])
			#print('the number of variables is: ',len(aList[c:d+1]) )
 
			#for e in range(0,


CainAndAbel(theList,winningTicket)