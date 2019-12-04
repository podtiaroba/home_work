#https://github.com/Bandydan/Python_Extended_Second/blob/master/hw04.md
#https://github.com/Bandydan/codeeval-problem-statements/tree/master/easy/174-slang-flavor

replacements = {'!':'. Awesome!', '?':', can U believe this?', '.':', yo.'}

with open('old_file.txt') as infile, open('new_file', 'w') as outfile:
    for line in infile:
        for src, target in replacements.items():
            line = line.replace(src, target)
        outfile.write(line)
print ("New file created!")
