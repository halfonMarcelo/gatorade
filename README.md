# gatorade

Welcome to the gatorade python script README. This is a very simple program to use.


DIRECTIONS:
After running SCRMshaw, the output will have to be analyzed. This script needs to be placed in the directory above all of the training sets to be analyzed. For example: 

main.py
|
fly_brain 
|
neg.fasta crms.fasta

The script will ignore any files written into it's "naughtylist" found on line 8. 

PURPOSE:

This script will analyze the neg.fasta files. It does this by grabbing the contents of every crms.fasta file in the directory, and appending the contents to a list named "newlst.lst," removing any duplicate enhancers in the process and replacing the existing neg.fasta files with this list. 
