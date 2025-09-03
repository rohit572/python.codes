# TODO:1- Import and print the logo from Art.py When the program starts. 
import art
print(art.logo)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = " "
    for letter in original_text:

# TODO:2- What happens if the a way to restart the number/symbol/space?

'''The line 17 or 18 says that if the letter is not in the alphabet list, in that
case, all we're going to do is take the output text and plus equal to the current text or letter.
Then this will add whatever letter it is that we need to skip the output text as its original format.'''

        if letter not in alphabet: 
            output_text += letter        
        else:
            if encode_or_decode == "decode":
                shift_amount *= -1

            shifted_position = alphabet.index(letter) - shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

# TODO:3- Can you figure out a way to restart the cipher program?

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    restart = input("Type 'yes' if you want to go again. otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Good bye")