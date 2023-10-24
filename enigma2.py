rotor_1 = ["BDFHJLCPRTXVZNYEIWGAKMUSQO","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_2 = ["AJDKSIRUXBLHWTMCQGZNPYFVOE","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
rotor_3 = ["EKMFLGDQVZNTOWYHXUSPAIBRCJ","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

reflector = ["YRUHQSLDPXNGOKMIEBFZCWVJAT","ABCDEFGHIJKLMNOPQRSTUVWXYZ"]

rotor_1Position = 0
rotor_2Position = 0
rotor_3Position = 0

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def plugboard(character):
    pludge_board = [["A","X"],["C","D"]]
    for i in pludge_board:
        if character in i[0]:
            return i[1]
        elif character in i[1]:
            return i[0]
    return character

def rotor_encription(character):
    global rotor_1,rotor_2,rotor_3,rotor_1Position,rotor_2Position,rotor_3Position,reflector
    
    # ROTOR 1
    rotor_1 = [rotor_1[0][1:] + rotor_1[0][0], rotor_1[1][1:] + rotor_1[1][0]]
    rotor1 = rotor_1[1].index(rotor_1[0][alfabet.index(character)])
    rotor_1Position += 1
    # ROTOR 2
    if rotor_1Position > len(alfabet):
        rotor_1Position = 0
        rotor_2 = [rotor_2[0][1:] + rotor_2[0][0], rotor_2[1][1:] + rotor_2[1][0]]
        rotor_2Position += 1
    rotor2 = rotor_2[1].index(rotor_2[0][rotor1])

    # ROTOR 3
    if rotor_2Position > len(alfabet):
        rotor_2Position = 0
        rotor_3 = [rotor_3[0][1:] + rotor_3[0][0], rotor_3[1][1:] + rotor_3[1][0]]
    rotor3 = rotor_3[1].index(rotor_3[0][rotor2])  
    
    if rotor_3Position > len(alfabet):
        rotor_3Position = 0
    # REFLECTOR
    reflector_1 = reflector[1].index(reflector[0][rotor3])
    reflector_1 = rotor_3[0].index(rotor_3[1][reflector_1])
    reflector_1 = rotor_2[0].index(rotor_2[1][reflector_1])
    return  alfabet[rotor_1[0].index(rotor_1[0][rotor_1[0].index(rotor_1[1][reflector_1])])]
  
    
def encription_process(character):
    character = plugboard(character)
    character = rotor_encription(character)
    character = plugboard(character)
    return character

pesan = input("masukkan pesan : ").upper()
encription = ""

for i in pesan:
    encription += encription_process(i)

print(encription)

    

