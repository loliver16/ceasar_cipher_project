import sys

"""
Applies caesar cipher to inputed text using given shift. First converts
text to uppercase then adds shifts. 

Parameters:
text - text to be coded
shift - number of characters in alphabet to shift each letter
"""
def caesar_cipher(text, shift):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))
    return result

"""
Prints ciphered text in blocks of 5 letters, with 10 blocks per line. 

Parameters:
cipher_text - ciphered text to be printed
"""
def print_blocks(cipher_text):
    # Split into blocks of 5 letters
    blocks = [cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)]
    # Print 10 blocks per line
    for i in range(0, len(blocks), 10):
        print(" ".join(blocks[i:i+10]))

"""
Runs caesar cipher by reading stdin, calling previous functions, 
and printing the resulting ciphered message. 
"""
def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <shift>")
        return
    try:
        shift = int(sys.argv[1])
    except ValueError:
        print("Error: The shift value must be an integer.")
        return

    # Read input message
    input_text = sys.stdin.read()

    # Encrypt message
    encrypted = caesar_cipher(input_text, shift)

    # Print encrypted message in blocks
    print_blocks(encrypted)

if __name__ == "__main__":
    main()