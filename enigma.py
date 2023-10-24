rotor_1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ" 
rotor_2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reflector_2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
reflector_3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor_1Position = 0
rotor_2Position = 0
rotor_3Position = 0

def rotor_encription(character):
    global rotor_1, rotor_2, rotor_3, rotor_1Position, rotor_2Position, rotor_3Position,reflector_1,reflector_2,reflector_3
   
    rotor1 = rotor_1[alfabet.index(character)]
    reflector1 = reflector_1.index(rotor1)
    rotor_1 = rotor_1[-1] + rotor_1[0:-1]
    reflector_1 = reflector_1[-1] + reflector_1[0:-1]
    rotor_1Position += 1

    rotor2 = rotor_2[reflector1]
    reflector2 = reflector_2.index(rotor2)
    
    if rotor_1Position > len(alfabet):
        rotor_2 = rotor_2[-1] + rotor_2[0:-1]
        rotor_1Position = 0
    rotor_2Position += 1

    rotor3 = rotor_3[reflector2]
    reflector3 = reflector_3.index(rotor3)
    if rotor_2Position > len(alfabet):
        rotor_3 = rotor_3[-1] + rotor_3[0:-1]
        rotor_2Position = 0
    rotor_3Position += 1

    if rotor_3Position > len(alfabet):
        rotor_3Position = 0
    
    return rotor3

def plugboard(character):
    pludge_board = [["A", "Y"], ["D", "X"]]
    for i in pludge_board:
        if character in i:
            return i[1]
    return character
     
def encription_process(character):
    character = plugboard(character)
    character = rotor_encription(character)
    character = rotor_encription(character)
    character = plugboard(character)
    return character

pesan = input("masukkan pesan : ").upper()
encription = ""

for i in pesan:
    encription += encription_process(i)

print(encription)
