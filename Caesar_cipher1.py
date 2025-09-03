"""CAESAR CIPHER is the way of encrypting text by shifting each letter a fixed number of places down the 
alphabet. FOR EXAMPLE : - with 'a' shift of 3 , A becomes D , B becomes F etc.
it's a simple way to encode messages , easily decoded by reversing the shift."""

# Description-We are going to build an encryption and decryption program using the caesar cipher.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called encrypt() that takes original_text and shift_amount as 2 inputs.
# TODO-2: Inside the 'encrypt' Function, shift each letter of the original_text forwards in the alphabet by the shift_amount and
#  print the encrytpted text. 

def encrypt(original_text, shift_amount):
    cipher_text = "" # to accumulated it we need to haev some sort of empty string, which will call ciphertext.

    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount # we take index and we add ahift amount to it. 
        
        # we save this shifted position into a variable so that we can use it.

# TODO-4: what happens if you try to shift z forwards by 9? Can you fix the code?

        # we shifted position modulo equals the length of the alphabet is going to make sure that we always in the range of 0 to 25. 
        shifted_position %= len(alphabet) 

        cipher_text += alphabet[shifted_position] # we turn index into the actual letter.

    # Now we want to print it out. 
    print(f"Here is the encode result: {cipher_text}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrpt a message.
encrypt(original_text=text, shift_amount=shift)