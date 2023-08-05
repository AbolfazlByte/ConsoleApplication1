''' Encoded string '''
coded_string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"

''' Decode function '''
def Decoder(code):
    code_list = code.split()
    plain_code = 'x' * len(code_list)
    for c in code_list:
        index = int(c[1:])
        value_to_insert = c[0]
        plain_code = plain_code[:index] + value_to_insert + plain_code[index+1:]
    
    return plain_code




print(Decoder(coded_string))
