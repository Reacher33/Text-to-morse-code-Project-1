import time

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}


def text_to_morse(msg):
    message = " "
    for word in msg:
        if word in morse_code_dict:
            message += morse_code_dict[word] + " "
        elif word not in morse_code_dict:
            message += word
    return message


def morse_to_text(msg):
    reversed_dict = {value: key for key, value in morse_code_dict.items()}
    message = [reversed_dict[word] + "" for word in msg.split(" ") if word in reversed_dict]
    out_put = ""
    for words in message:
        out_put += words
    return out_put


translating = True
while translating:
    pick = input("Reply 'M' for morse to text or 'T' for text to morse code or 'Q' to quit:\n").upper()
    if pick == "M":
        morse_code = input("Enter Morse code:\n")
        output = morse_to_text(morse_code)
        print(output.title())
    elif pick == "T":
        text = input("Enter Text: \n").upper()
        output = text_to_morse(text)
        print(output)
    elif pick == "Q":
        print("Bye....😊")
        translating = False
    elif pick != "M" or pick != "T" or pick != "Q":
        print("Sorry i dont understand")
        time.sleep(2)
