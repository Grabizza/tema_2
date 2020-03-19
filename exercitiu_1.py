# The problem: replace that text from `string` between start and end with the text from `patches`

# patches modificat pentru:
string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# //[start, end, patch]
patches = [[4, 14, "Conquistador"], [27, 33, "King"], [42, 49, "Palace"]]

string1 = string[:int(patches[0][0])] + str(patches[0][2]) + string[int(patches[0][1]):]
string2 = string1[:int(patches[1][0])] + str(patches[1][2]) + string1[int(patches[1][1]):]
string3 = string2[:int(patches[2][0])] + str(patches[2][2]) + string2[int(patches[2][1]):]
print(string3)

### or patches nemodificat

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# //[start, end, patch]
patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]

string = string[:int(patches[0][0])] + str(patches[0][2]) + string[int(patches[0][1]):int(patches[1][0])] + str(patches[1][2]) + string[int(patches[1][1]):int(patches[2][0])] + str(patches[2][2]) + string[int(patches[2][1]):]
print(string)

### or patches modificat pentru acuratete

string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
patches = [[4, 14, "Conquistador"], [25, 31, "King"], [42, 49, "Palace"]]
string = string[:int(patches[0][0])] + str(patches[0][2]) + string[int(patches[0][1]):int(patches[1][0])] + str(patches[1][2]) + string[int(patches[1][1]):int(patches[2][0])] + str(patches[2][2]) + string[int(patches[2][1]):]
print(string)
