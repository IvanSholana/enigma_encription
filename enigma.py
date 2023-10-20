rotor_1 = "RBJTMVAQCXHKSYNGPLWIFDOUEZ"
rotor_2 = "LUCQGWVRFDHJSZBXPKNIYOAEMT"
rotor_3 = "TABDMKWJOIPXNLVFCQZGEYSRUH"

alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rotor_1Position = 0
rotor_2Position = 0
rotor_3Position = 0

def rotor_encription(character):
    global rotor_1, rotor_2, rotor_3, rotor_1Position, rotor_2Position, rotor_3Position
   
    rotor1 = rotor_1[alfabet.index(character)]
    rotor_1 = rotor_1[-1] + rotor_1[0:len(rotor_1)-2]
    rotor_1Position += 1

    rotor2 = rotor_2[alfabet.index(rotor1)]
    if rotor_1Position > len(alfabet):
        rotor_2 = rotor_2[-1] + rotor_2[0:len(rotor_2)-2]
        rotor_2Position += 1
        rotor_1Position = 0

    rotor3 = rotor_3[alfabet.index(rotor2)]
    if rotor_2Position > len(alfabet):
        rotor_3 = rotor_3[-1] + rotor_3[0:len(rotor_3)-2]
        rotor_2Position = 0
    
    return rotor3

def switch_pludge(character):
    pludge_board = [["A", "Y"], ["D", "X"]]
    for i in pludge_board:
        if character in i:
            return i[1]
        return character
     
def encription_process(character):
    character = switch_pludge(character)
    character = rotor_encription(character)
    character = rotor_encription(character)
    character = switch_pludge(character)
    return character

pesan = input("masukkan pesan : ").upper()
encription = ""

for i in pesan:
    encription += encription_process(i)

print(encription)
