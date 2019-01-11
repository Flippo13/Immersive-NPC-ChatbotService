import glob 
import os
import ast

def build_domain():
    with open("domain/domain.yml", "w") as outfile:
        intents(outfile)
        entities(outfile)
        slots(outfile)
        templates(outfile)
        actions(outfile)
        forms(outfile)

def write_sub_file(outfile, subFileName, spacer):
    with open (subFileName) as infile:
        for line in infile.readlines():
            outfile.write(spacer + line)


def intents(outfile):
    outfile.write("\n\nintents:\n")
    write_sub_file(outfile, "domain/intents.yml", " ")

def entities(outfile):
    outfile.write("\n\nentities:\n")
    write_sub_file(outfile, "domain/entities.yml", " ")

def slots(outfile):
    outfile.write("\n\nslots:\n")
    write_sub_file(outfile, "domain/slots.yml", " ")

def forms(outfile):
    outfile.write("\n\nforms:\n")
    write_sub_file(outfile, "domain/forms.yml", " ")

def templates(outfile):
    outfile.write("\n\ntemplates:")
    utterance_files = glob.glob("domain/utterances/*.yml")
    for fname in utterance_files:
        outfile.write("\n utter_" + os.path.basename(fname)[:-4] + ":\n")
        write_sub_file(outfile, fname, " ")


def actions(outfile):
    outfile.write("\n\nactions:")
    utterance_files = glob.glob("domain/utterances/*.yml")
    for fname in utterance_files:
        outfile.write("\n  - utter_" + os.path.basename(fname)[:-4])

    files = glob.glob("domain/actions/*.py")
    for fname in files:
        str = "  "
        with open(fname) as infile:
            str = infile.read()

            p = ast.parse(str)
            classes = [node for node in ast.walk(p) if isinstance(node, ast.ClassDef)]
            for item in classes:
                if (item.bases[0].id == "Action" or item.bases[0].id == "FormAction"):
                    outfile.write("\n  - action_" + item.name.lower())


if __name__ == '__main__':
    build_domain()