
def compressfile(file_location):
    data = open(file_location, "r")
    lines = data.readlines()
    compressed_data = []
    for item in lines:
        words = item.split()
        if words:
            compressed_data.append(words)
            compressed_data.append("\n")
    new_data = open(file_location, "w")
    for items in compressed_data:
        for item in items:
            new_data.write(item)
            if item != "\n":
                new_data.write(" ")

compressfile("../opdracht8.txt")