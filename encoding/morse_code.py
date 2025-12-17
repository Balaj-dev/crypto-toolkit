# MORSE_CODE_DICT maps uppercase characters to Morse (dot = '.', dash = '-')
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',
    'E': '.',     'F': '..-.',  'G': '--.',   'H': '....',
    'I': '..',    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',   'P': '.--.',
    'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.',  '(': '-.--.',  ')': '-.--.-',
    '&': '.-...',  ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.',  '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.'
}

# reversed dictionary for decoding: Morse -> character
MORSE_TO_CHAR = {morse: char for char, morse in MORSE_CODE_DICT.items()}

def encode_to_morse(text, letter_sep=' ', word_sep=' / '):

    words = text.upper().split()
    encoded_words = []
    for w in words:
        encoded_letters = []
        for ch in w:
            if ch in MORSE_CODE_DICT:
                encoded_letters.append(MORSE_CODE_DICT[ch])
            # else: ignore unknown characters (or you could append '?')
        encoded_words.append(letter_sep.join(encoded_letters))
    return word_sep.join(encoded_words)

def decode_from_morse(morse_code, letter_sep=' ', word_sep=' / '):
    """
    Decode Morse code to plain text.
    - letter_sep: separator between letters in the morse input
    - word_sep: separator between words in the morse input
    Unknown morse sequences are replaced with '?'
    """
    words = morse_code.strip().split(word_sep)
    decoded_words = []
    for w in words:
        letters = w.strip().split(letter_sep)
        decoded_letters = []
        for s in letters:
            if s == '':
                continue
            decoded_letters.append(MORSE_TO_CHAR.get(s, '?'))
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)


