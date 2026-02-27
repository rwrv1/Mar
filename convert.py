import sys

args = sys.argv

help_text = "Mar Conversion Help\n\nUsage: convert.py inputfile outputfile"

if len(args) != 3:
    print(help_text)
    print(f"Error: Missing or extra arguments. Expected 2, got {len(args)-1}")
    exit(1)

try:
    inputfile = open(args[1], "r")
except FileNotFoundError:
    print(help_text)
    print(f"Error: File \"{args[1]}\" does not exist.")

try:
    outputfile = open(args[2], "x")
except FileExistsError:
    overwrite = input(f"File \"{args[2]}\" already exists. Overwrite [Y/N]? ")
    if overwrite.lower()[0] == "y":
        outputfile = open(args[2], "w")
    else:
        print(help_text)
        priint(f"Error: File \"{args[2]}\" already exists.")

inputfile_content = inputfile.read()

outputfile_content =   inputfile_content.replace("moo", "mar").replace("mOo", "mAr").replace("moO", "maR").replace("mOO", "mAR").replace("Moo", "Mar").replace("MOo", "MAr").replace("MoO", "MaR").replace("MOO", "MAR").replace("OOO", "mrr").replace("MMM", "MRR").replace("OOM", "Mrr").replace("oom", "mrR")
outputfile.write(outputfile_content)
outputfile.close()
inputfile.close()
print("Done.")
