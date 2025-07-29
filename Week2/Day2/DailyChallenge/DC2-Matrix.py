#Solve The Matrix

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''       

matrix = []

def analyze_matrix(message):
    matrix = message.split("\n")
    if "" in matrix:
        matrix.remove("")
    for index, item in enumerate(matrix):
        matrix[index] = [i for i in item]
    return decode_matrix(handle_2d_list(matrix))

def handle_2d_list(list_2d):
    matrix_decode = []

    for i in range (len(list_2d[0])):
        for j in range(len(list_2d)):
            matrix_decode.append(list_2d[j][i])
    return matrix_decode

def decode_matrix(matrix_string):
    decoded_string = ""
    for letter in matrix_string:
        if letter.isalpha():
            decoded_string += letter
        else:
            decoded_string += " "
#TO BE FINISHED