import sys

def caesar_cipher(text, shift):
    result = ""
    for char in text.upper():
        if 'A' <= char <= 'Z':
            shifted = (ord(char) - ord('A') + shift) % 26
            result += chr(shifted + ord('A'))
    return result

def print_blocks(cipher_text):
    # Split into blocks of 5 letters
    blocks = [cipher_text[i:i+5] for i in range(0, len(cipher_text), 5)]
    # Print 10 blocks per line
    for i in range(0, len(blocks), 10):
        print(" ".join(blocks[i:i+10]))

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <shift>")
        return
    shift = int(sys.argv[1])

    # Read input message
    input_text = ""
    for line in sys.stdin:
        input_text += line

    # Encrypt message
    encrypted = caesar_cipher(input_text, shift)

    # Print encrypted message in blocks
    print_blocks(encrypted)

if __name__ == "__main__":
    main()