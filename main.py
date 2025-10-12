'''
Nick S. & Steven R. CS351 Homework 3
'''

#Define Main for functions and user input
def main():
    
    #Ask user for cipher input text
    #Assumption: input is expected to be upper case only so this is forced
    ciphertext = input("Enter Ciphertext: ").upper()

	#Print statement before setting the freq.
    print("\nStep 1: Frequency Analysis")


	#Set freq. variable to the function of the run freq. block with
	#the cipher text as the parameter 
    freq = run_frequency_block(ciphertext)

	#Print statement before printing the partial decryption
    print("\nStep 2: Automated Partial Decryption")
    partial_text = automated_partial_decrypt(ciphertext, freq)

	#Print statement before printing the decryption with the user inputed changed character
    print("\nStep 3: Manual Replacement Phase")
    print("You can now make manual letter replacements to refine your decryption.")
    
    #Use function to replace letter with user input 
    run_manual_replace_block(partial_text)

#Define function to decrypt cipher text with the frequencies
def run_frequency_block(ciphertext):

    #Create dictionary for each letter in the alphabet and set the count to 0 
    freq = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
            "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
            "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

    #Create list to store the count of each letter
    fcount = []

    #append the ciphertext onto the stored list
    fcount.append(ciphertext)

    #Loop through each word in the stored list
    for word in fcount:
        
        #Loop through each letter in the word
        for letter in word:
            
            #Checks for the letter in the freq. dictionary
            if letter in freq:
	    
                #Increment the letter in the freq. by 1
                freq[letter] += 1
    
    #print the frequencies
    print_frequency(freq)
    
    #return the freq. dictionary in this function
    return freq

#Define function to decrypt cipher text with the frequencies
def automated_partial_decrypt(ciphertext, charFrequency):
    
    '''
    Frequency list pulled from Cornell:
    https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    '''
    LETTER_FREQUENCY = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

    '''
    present_letters is used to track each letter present in the ciphertext
    Letters that are not present in the text are not included
    This is later used for created a list of letters sorted by their frequency
    From most common to the least common
    '''    
    present_letters = []
    for ch, count in charFrequency.items():
        if count > 0:
            present_letters.append(ch)

    '''
    The next 17 lines handle the creation of `sorted_letters`
    This is list of letters present in cipher text in order
    from most common to least common
    '''    
    sorted_letters = []
    charFrequencyCopy = charFrequency.copy()

    while charFrequencyCopy:
        max_letter = None
        max_count = -1
        for letter, count in charFrequencyCopy.items():
            if count > max_count:
                max_count = count
                max_letter = letter

        sorted_letters.append(max_letter)

        del charFrequencyCopy[max_letter]

        if len(sorted_letters) == len(present_letters):
            break

    '''
    This code block constructs a map, mapping letters in the cipher text
    to the letter they are automatically replaced with
    The replacement letter is determined by the LETTER_FREQUENCY list
    sourced from Cornell, saved at the top of the function
    '''    
    mapping = {}
    for i in range(len(sorted_letters)):
        if i < len(LETTER_FREQUENCY):
            mapping[sorted_letters[i]] = LETTER_FREQUENCY[i]

    '''
    This block handles the creation of the partially decrypted cipher text
    Iterates through the original ciphertext replacing letter by letter based
    on the mapping setup before
    '''    
    partial_text = ""
    for ch in ciphertext:
        if ch.isalpha():
            partial_text += mapping.get(ch, ch)
        else:
            partial_text += ch

    #printing for the letter mapping and the partially decrypted text
    print_letter_map(mapping)
    
    #Print statement before partially decrypted text
    print("\nPartially Deciphered Text:\n")
    
    #Print partially decrypted text
    print(partial_text)

    #Return the partial text
    return partial_text

#Define function for replacing letter with user input
#from the decrypted partial text
def run_manual_replace_block(partial_text):
    
    #Create variable to hold the partial text
    original_text = partial_text

    #Create variable to keep the current chars from the partial text
    current_chars = list(partial_text)

    #While loop till user says no
    while True:
        
        #Ask for user input , remove leading and trailing chars. and make them lowercase
        choice = input("Do you want to change a letter? (yes/no): ").strip().lower()

        #If the user chooses “yes” or “y”
        if choice in ("yes", "y"):
            
            ''' 
            Ask user what letter they want to change and what they would want to replace the letter with while 
            stripping all leading and trailing characters.
            Assumption: Ciphertext is only upper so letters to change are forced to be upper case for easy use.            
            '''            
            changet = input("What letter you want to change: ").strip().upper()
            changett = input("What letter would you replace it with: ").strip().upper()

            '''
            The index of the characters to replace is pulled from the original unedited text(`original_text`)
            While the actual replacement is done on the modified `current_chars`
            This is done to prevent a cascading replace bug
            i.e. if an s->t swap was done, then t->v we only want the characters that were originally t to be swapped to v            
            '''            
            for idx, ch in enumerate(original_text):
                if ch.upper() == changet:
                    current_chars[idx] = changett
                    
            #print the change text with joining the current char change 
			print("Changed text:", "".join(current_chars))

        #Else if choice is no 
        elif choice in ("no", "n"):

            '''
            Join the current characters to the final text,
			print the final changed text and break the loop          
			'''
            final_text = "".join(current_chars)
            print("Final text:", final_text)
            break
        
        #Else ask the user to enter yes or no
        else:
            print("Please enter yes or no.")

'''
Define function to print out table
for each cipher letter mapped to its
plain text letter
'''
def print_letter_map(mapping):
    
    '''
    Format printing to split the cipher
    letters and the plain text letters
    onto a table
    '''
    print("\nLetter Mapping Table:")
    print("----------------------")
    print("Cipher | Plain")
    print("-------|------")
    
    #for loop through the cipher and plain text
    #in the mapping dictionary 
    for cipher, plain in sorted(mapping.items()):
        
        #Print out the cipher letter followed by
        #plain text letter
        print(f"   {cipher}   ==>   {plain}")

#Define function to print the frequncies 
def print_frequency(freq):
    
    #Print statement before showing the frequncies
    print("\nLetter Frequency Table:")
    print("-----------------------")
    
    '''
    The key field expects a func so lambda is used to define a func inline
    rather than create separate logic just to sort by the value instead of the key
    '''   
    for letter, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
        
		#bar is used to add a visual count of letter frequency, just makes it look nicer
        bar = "|" * count
        
        #print the letter, count , followed by the bar tallies
        print(f"{letter}: {count}   {bar}")

#if file is directed to main
if __name__ == "__main__":
    
    #call main function
    main()
