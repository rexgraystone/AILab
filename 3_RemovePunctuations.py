# 3. Write a Python program to remove punctuations, count the number of spaces, or replace a punctuation mark with a character from a given string.

import string

with open("Datasets/3_Paragraph.txt", "r") as file:
	content = file.readlines()
	text = ""
	for element in content:
		text += element
	file.close()
	
print(f"The original contents of the file are:\n {text}")

punctuations = string.punctuation

count_punc, count_spaces, count_replace = 0, 0, 0

repeat = True

while repeat: 
	choice = int(input("1. Remove Punctuation marks from the text\n2. Count the number of spaces in the text\n3. Replace a punctuation mark with a specific Character.\nEnter your choice: "))

	match choice:
		case 1:
			for element in text:
				if element in punctuations:
					text = text.replace(element, "")
					count_punc += 1
			print(f"\nThe contents of the file after filtering the punctuations are:\n {text}")
			print(f"The number of punctuation marks in the text are:\n\t{count_punc}")
		case 2:
			for element in text:
				if element == " ":
					count_spaces += 1
			print(f"The number of spaces in the text are:\n\t{count_spaces}")
		case 3: 
			punc = input("\nEnter the punctuation character: ")
			replace = input("\nEnter the replacement character: ")
			if punc in punctuations:
				for element in text:
					if element == punc:
						text = text.replace(punc, replace)
						count_replace += 1
				print(f"\nThe contents of the file after replacing \'{punc}\' with \'{replace}\' are:\n {text}")
				print(f"\nThe number of characters replaced are:\n\t{count_replace}")
			else:
				print("Please enter a valid punctuation mark.")
	repeat = int(input("\nWould you like to repeat? \t1. Yes 0. No\n"))