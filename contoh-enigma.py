# Define the rotor settings for the Enigma machine
rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ" # Rotor 1 mapping
rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE" # Rotor 2 mapping
rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO" # Rotor 3 mapping
reflector = "YRUHQSLDPXNGOKMIEBFZCWVJAT" # Reflector mapping

# Define the starting position for each rotor
rotor1_start = 0 # Starting position for rotor 1
rotor2_start = 0 # Starting position for rotor 2
rotor3_start = 0 # Starting position for rotor 3

# Define the plugboard settings for the Enigma machine
plugboard = {"A": "B", "C": "D", "E": "F", "G": "H", "I": "J", "K": "L", "M": "N", "O": "P", "Q": "R", "S": "T",
             "U": "V", "W": "X", "Y": "Z"} # Plugboard mappings

# Define the Enigma machine's encryption function
def enigma(text):
    global rotor1_start, rotor2_start, rotor3_start # Access global variables inside function
    # Convert the input text to uppercase and remove any spaces
    text = text.upper().replace(" ", "")

    # Initialize an empty list to store the encrypted text
    encrypted_text = []

    # Loop over each character in the input text
    for char in text:
        # Apply the plugboard settings to the current character
        char = plugboard.get(char, char)

        # Increment the starting position of the first rotor
        rotor1_start = (rotor1_start + 1) % 26

        # Check if the first rotor has completed a full revolution and increment the second rotor if so
        if rotor1_start == 0:
            rotor2_start = (rotor2_start + 1) % 26

            # Check if the second rotor has completed a full revolution and increment the third rotor if so
            if rotor2_start == 0:
                rotor3_start = (rotor3_start + 1) % 26

        # Map the current character through the first rotor
        char = rotor1[(ord(char) - 65 + rotor1_start) % 26]

        # Map the current character through the second rotor
        char = rotor2[(ord(char) - 65 + rotor2_start) % 26]

        # Map the current character through the third rotor
        char = rotor3[(ord(char) - 65 + rotor3_start) % 26]

        # Map the current character through the reflector
        char = reflector[(ord(char) - 65) % 26]

        # Map the current character back through the third rotor in reverse
        char = chr((rotor3.index(char) - rotor3_start + 26) % 26 + 65)

        # Map the current character back through the second rotor in reverse
        char = chr((rotor2.index(char) - rotor2_start + 26) % 26 + 65)

        # Map the current character back through the first rotor in reverse
        char = chr((rotor1.index(char) - rotor1_start + 26) % 26 + 65)

        # Apply the plugboard settings to the final encrypted character
        char = plugboard.get(char, char)

        # Add the final encrypted character to the encrypted text list
        encrypted_text.append(char)

    # Join the encrypted text list into a single string
    encrypted_text_str = "".join(encrypted_text)

    # Return the encrypted text
    return encrypted_text_str

# Apply the Enigma machine's encryption function
encrypted = enigma(input("enter the text : "))
# Print the generated encrypted text
print("Encrypted Text:", encrypted)