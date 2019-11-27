content = "Ultimate testing. Good Luck :)"
filename = str(filename_cleaner(seq))
if op == 1:
    f = open(input_folder + filename + ".txt", "w")
else:
    f = open(output_folder + filename + ".txt", "w")
f.write(content)
f.close()
size = len(content)
print("Successfully write {} sizes at {}!".format(filename, size))