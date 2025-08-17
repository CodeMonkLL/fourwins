board = []
rows = 4
columns = 4

letters= ["A","B","C","D"]

for i in range(rows):
    row = []
    for j in range(rows):
        row.append(letters[j])
    print(row)