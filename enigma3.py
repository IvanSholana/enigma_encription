rotor_1 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_3 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

reflector = ["YRUHQSLDPXNGOKMIEBFZCWVJAT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

rotor_1Position = 0
rotor_2Position = 0
rotor_3Position = 0

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def plugboard(character):
    plug_board = [["A", "Y"], ["D", "X"]]
    for i in plug_board:
        if character in i:
            return i[1]
    return character

def rotor_encription(character):
    global rotor_1, rotor_2, rotor_3, rotor_1Position, rotor_2Position, rotor_3Position, reflector

    rotor1_char = rotor_1[1][rotor_1[0].index(character)]
    rotor2_char = rotor_2[1][rotor_2[0].index(rotor1_char)]
    rotor3_char = rotor_3[1][rotor_3[0].index(rotor2_char)]

    reflector_char = reflector[1][reflector[0].index(rotor3_char)]

    rotor3_char = rotor_3[0][rotor_3[1].index(reflector_char)]
    rotor2_char = rotor_2[0][rotor_2[1].index(rotor3_char)]
    rotor1_char = rotor_1[0][rotor_1[1].index(rotor2_char)]

    rotor_1Position += 1

    if rotor_1Position == len(alfabet):
        rotor_1Position = 0
        rotor_2Position += 1

        if rotor_2Position == len(alfabet):
            rotor_2Position = 0
            rotor_3Position += 1

            if rotor_3Position == len(alfabet):
                rotor_3Position = 0

    return rotor1_char

def encryption_process(character):
    character = plugboard(character)
    character = rotor_encription(character)
    character = plugboard(character)
    return character

pesan = input("Masukkan pesan: ").upper()
encryption = ""

for i in pesan:
    encryption += encryption_process(i)

print(encryption)
