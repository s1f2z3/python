bored = [
	[0,0,0],
	[0,0,0],
	[0,0,0],
]

ai = [
	[0,0,0],
	[0,0,0],
	[0,0,0],
]

winner = 0
def winCheck(play = 1, bored = bored):
	global winner
	for line in bored:
		if line[0]!=0:
			if all(x == line[0] for x in line):
				if play ==1:
					#print('end')
					if line[0] == '1':
						winner = 1
					else:
						winner = 2
				return 1
	for i in range(len(bored[0])):
		if bored[0][i] != 0:
			if all(row[i] == bored[0][i] for row in bored):
				if play == 1:
					#print('End')
					if bored[0][i] == '1':
						winner = 1
					else:
						winner = 2
				return 1
	
	if bored[0][0] != 0:
		if all(bored[i][i] == bored[0][0] for i in range(len(bored[0]))):
			if play == 1:
				#print('EEEnd')
				if bored[0][0] == '1':
					winner = 1
				else:
					winner = 2
			return 1
	if bored[0][len(bored[0])-1] != 0:
		if all(bored[i][len(bored[0])-1-i] == bored[0][len(bored[0])-1] for i in range(len(bored[0]))):
			if play == 1:
				#print('Ennnnnnd')
				if bored[0][0] == '1':
					winner = 1
				else:
					winner = 2
			return 1
	return 0

def draw(bored=bored):
	print()
	j = 0
	for line in bored:
		i = 0
		for cell in line:
			if cell == 0:
				print(f' {i+j*len(line)+1} ',end='')
			elif cell == 1:
				print(' 0 ',end='')
			else:
				print(' X ',end='')
			if len(line)-1 != i:
				print('|',end='')
			i += 1
		print()
		if j != len(bored)-1:
			for cell in line:
				print('____',end='')
			print()
		j += 1	
	print()
	winCheck()



def aiPlayer():
	global ai
	for i in range(len(ai)):
		for j in range(len(ai[i])):
			if ai[i][j] == 0:
				ai[i][j] =1	
	#draw(ai)	
	return 6


def player(typ):
	if winner == 0:
		j = 0
		for line in bored:
			for cell in line:
				if cell == 0:
					break
				j += 1	
		if j == len(bored)*len(bored[0]):
			return 1
		try:
			if typ == 2:
				while (True):
					play = int(input('choose a place to play: '))
					if bored[int((play-1)/len(bored[0]))][(play-1)%len(bored[0])] == 0:
						break
					else:
						draw()
						print('chose an empty space')
						
				bored[int((play-1)/len(bored[0]))][(play-1)%len(bored[0])] = typ
				ai[int((play-1)/len(bored[0]))][(play-1)%len(bored[0])] = typ
			else:
				play = aiPlayer()
				bored[int((play-1)/len(bored[0]))][(play-1)%len(bored[0])] = typ
				ai[int((play-1)/len(bored[0]))][(play-1)%len(bored[0])] = typ
			return 0
		except:
			print('Wrong Input')
			return -1
	return 1
			
def main():
	#print('hello world')
	
	draw()
	while( player(2) != 1 ):
		draw()
		player(1)
		draw()
	
	if winner == 0:
		print('Draw')
	elif winner == 1:
		print('O won')
	else:
		print('X won')


if __name__ == '__main__':
	main()
