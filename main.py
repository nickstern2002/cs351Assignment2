
def main():
    ciphertext = input("Enter Ciphertext: ").upper()

    print("\nStep 1: Frequency Analysis")
    freq = run_frequency_block(ciphertext)  # reuse computed freq later

    print("\nStep 2: Automated Partial Decryption")
    partial_text = automated_partial_decrypt(ciphertext, freq)

    print("\nStep 3: Manual Replacement Phase")
    print("You can now make manual letter replacements to refine your decryption.")
    run_manual_replace_block(partial_text)

def run_frequency_block(ciphertext):
    freq = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0,
            "K": 0, "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0,
            "U": 0, "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

    k = []
    k.append(ciphertext)

    for word in k:
        print(f"Checking letter in '{word}':")
        for letter in word:
            if letter in freq:
                freq[letter] += 1

    print(freq)
    return freq



def automated_partial_decrypt(ciphertext, charFrequency):
    # Frequency list pulled from Cornell:
    # https://pi.math.cornell.edu/~mec/2003-2004/cryptography/subs/frequencies.html
    LETTER_FREQUENCY = "ETAOINSRHDLUCMFYWGPBVKXQJZ"

    present_letters = []
    for ch, count in charFrequency.items():
        if count > 0:
            present_letters.append(ch)

    sorted_letters = []
    temp_freq = charFrequency.copy()

    while temp_freq:
        max_letter = None
        max_count = -1
        for letter, count in temp_freq.items():
            if count > max_count:
                max_count = count
                max_letter = letter

        sorted_letters.append(max_letter)

        del temp_freq[max_letter]

        if len(sorted_letters) == len(present_letters):
            break

    mapping = {}
    for i in range(len(sorted_letters)):
        if i < len(LETTER_FREQUENCY):
            mapping[sorted_letters[i]] = LETTER_FREQUENCY[i]

    partial_text = ""
    for ch in ciphertext:
        if ch.isalpha():
            partial_text += mapping.get(ch, ch)
        else:
            partial_text += ch

    print("Letter Mapping:", mapping)
    print("\nPartially Deciphered Text:\n")
    print(partial_text)

    return partial_text

def run_manual_replace_block(partial_text):
    original_text = partial_text

    current_chars = list(partial_text)

    print("Original text:", "".join(current_chars))

    while True:
        choice = input("Do you want to change a letter? (yes/no): ").strip().lower()

        if choice in ("yes", "y"):
            changet = input("What letter you want to change: ").strip().upper()
            changett = input("What letter would you replace it with: ").strip().upper()

            for idx, ch in enumerate(original_text):
                if ch.upper() == changet:
                    current_chars[idx] = changett

            print(f"Replaced '{changet}' with '{changett}'")
            print("Changed text:", "".join(current_chars))

        elif choice in ("no", "n"):
            final_text = "".join(current_chars)
            print("Final text:", final_text)
            break
        else:
            print("Please enter yes or no.")



if __name__ == "__main__":
    main()
