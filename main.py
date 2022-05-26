import os
import shutil

# filesystem
spath = os.getcwd()
directories = os.listdir()

naughtylist = ["enhancersAdded.fasta", "newlst.lst", "main.py"]


def process_data(data):
    datasplit = data.split('\n\n')
    # print("Datasplit:")
    # print(f"{datasplit}\n")

    dct = {}
    for enhancer in datasplit:
        currentenhancer = enhancer.split('\n\n')
        print(f"\t-Current enhancer: {currentenhancer}\n")
        new_data = ''

        chunk = enhancer.split('\n')[1:]

        cn = 0
        for line in chunk:
            # print(p)
            if cn != len(chunk) - 1:
                # print("If statement has passed.")
                new_data += line + '\n'
                cn += 1
            else:
                # print("Else statement has been passed.")
                new_data += line
                dct[enhancer.split('\n')[0].strip()] = new_data
    return dct

# print("Directories:")
# print(directories)
# Get size of path
sizeOfPath = len(os.listdir(spath))
# print(f"Sets found: {sizeOfPath}\n")

# print("Assigning the sets to a path...")
# Iterates over the directory names and proceeds to look for the path with the training set name named crms.fasta,
# reads the file, and copies the contents to new_fl, aka a file that will be placed above the training set directories.
# This file contains all of the crms from every directory.
# print("Beginning a for loop that will iterate over all of the training set names such as adult midgut, or antenna.")
# print("Starting...\n")
for directory in directories:
    if directory != "main.py":
        # print('crms path:')
        data_1 = process_data(open(spath+'/'+directory+'/'+'crms.fasta', 'r').read())
        print(data_1)

        # creation of file
        new_fl = open(f'{spath}/neg.fasta', 'a')
        lk = list(data_1.keys())
        # print("printing lk[-1]")
        print(lk[-1])
        for g in data_1:
            if g == lk[-1]:
                # print("\nThe values match. Writing (g + newline + data_1[g]) to new_fl\n")
                # print("For reference, will print out each part of it.")
                # print("Printing")
                # print(g)
                # print('\n')
                # print(data_1[g])
                new_fl.write(g + '\n' + data_1[g]+'\n')
            else:
                # print(f"Since lk({lk[-1]}) is not equal to g({g}), we are going to write g + newline + data_1[g] + newlinenewline")
                new_fl.write(g + '\n' + data_1[g] + '\n\n')
        new_fl.close()

# We copy the file we created and paste it into each directory as neg.fasta
for directory in directories:
    if directory != "main.py" and directory != "neg.fasta":
        shutil.copy(f"{spath}/neg.fasta", f"{spath}/{directory}/")

# Finally, we print it out again as a sort of "receipt." It is named "enhancersAdded.fasta"
os.rename(f'{spath}/neg.fasta', 'enhancersAdded.fasta')


# search and destroy

# searchAndDestroy.py finds matches between a crms and a neg file within a training set and removes any matches from the
# neg file.

for directory in directories:
    # print('>>>Reading and processing the files...')
    #
    # print(directory)
    if "main.py" != directory and "enhancersAdded.fasta" != directory:
        data_1 = process_data(open(f'{spath}/{directory}/neg.fasta', 'r').read())
        data_2 = process_data(open(f"{spath}/{directory}/crms.fasta", 'r').read())

        temp_data_1 = []
        for key in data_1:
            if key in data_2:
                temp_data_1.append(key)

        # print(f'>>>Overlapping data found : {temp_data_1}')
        new_fl = open(f'{spath}/{directory}/neg.fasta', 'w')
        lk = list(data_1.keys())
        # print('>>>Writing new data...')
        for g in data_1:
            if g not in temp_data_1:
                if g == lk[-1]:
                    new_fl.write(g + '\n' + data_1[g])
                else:
                    new_fl.write(g + '\n' + data_1[g] + '\n\n')
        new_fl.close()

# removeDuplicates.py

def process_data(data):
    new_l = data.split('\n\n')
    dct = {}
    for h in new_l:
        tp = ''
        for y in h.split('\n')[1::]:
            tp += y + '\n'
        tp = tp[:-1]
        dct[h.split('\n')[0]] = tp
    return dct


for directory in directories:
    if directory != "main.py":
        data = process_data(open(f'{spath}/{directory}/neg.fasta', 'r').read())
        # print(data)
        new_fl = open(f'{spath}/{directory}/neg.fasta', 'w')
        lk = list(data.keys())
        lk = list(set(lk))
        # print('>>>Writing new data...')
        for g in lk:
            if len(g) > 0:
                if g == lk[-1]:
                    new_fl.write(g + '\n' + data[g])
                else:
                    new_fl.write(g + '\n' + data[g] + '\n\n')

        new_fl.close()

new_lst = open ("newlst.lst", "w")

# linking the main module with the newlst module here:

for x in os.listdir():
    # enhancersAdded.fasta created before newlst.lst, this will exclude that file
    # if x != "enhancersAdded.fasta" and x != "newlst.lst":
    if x not in naughtylist:
        new_lst.write(f"{os.getcwd()}/{x}\n")
new_lst.close()

print("A new .lst file has been created for use with SCRMSHAW.")

