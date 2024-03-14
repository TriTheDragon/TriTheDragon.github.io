import os

names = {"A": "00", "B": "01", "C": "02", "D": "03", "E": "04", "F": "05", "G": "06", "H": "07", "I": "08", 
         "J": "09", "K": "0A", "L": "0B", "M": "0C", "N": "0D", "O": "0E", "P": "0F", "Q": "10", "R": "11",
         "S": "12", "T": "13", "U": "14", "V": "15", "W": "16", "X": "17", "Y": "18", "Z": "19", "1": "1A",
         "2": "1B", "3": "1C", "4": "1D", "5": "1E", "6": "1F", "7": "20", "8": "21", "9": "22"}
directory = './'
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.png'):
            fName = os.path.join(dirpath, filename)

            oldName = os.path.splitext(filename)[0]
            if oldName in names:
                print(os.path.splitext(filename)[0])
                print(fName)
                print(dirpath + "/" + names[oldName] + ".png")
                os.rename(fName, dirpath + "/" + names[oldName] + ".png")