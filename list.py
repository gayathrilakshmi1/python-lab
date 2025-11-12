
with open("file2.txt", "w") as file:
    file.write("hello world!\nwelcome to python programming\nthank you")
lines = []
with open("file2.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)
