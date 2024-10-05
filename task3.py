word = "testingpo"

if len(word) % 2 == 0:
	print(f'{word[len(word)//2 - 1] + word[len(word)//2]}')
else:
	print(f'{word[len(word)//2]}')
