import os
import sys
import time
import json
import bs4
from bs4 import BeautifulSoup

def giant_to_input(giant_filename, debug=False):
    output_text_filename = giant_filename[:-4]+"_text.txt"
    output_label_filename = giant_filename[:-4]+"_label.txt"
    output_text_file = open(output_text_filename, "w")
    output_label_file = open(output_label_filename, "w")

    giant_file = open(giant_filename)
    lineid = 0
    for line in giant_file.readlines():
        line = line.strip()
        line = line.strip('"')
        text, label = preprocess_ref_string(line, debug=False)
        if debug:
            print("\n\n"+line)
            print("****** result ******")
            print(text)
            print(label)
        output_text_file.write(" ".join(text)+"\n")
        output_label_file.write(" ".join(label)+"\n")
        lineid += 1
        #if lineid > 50: break

    return output_text_filename, output_label_filename

###
# input e.g.,1: <author><given>C.</given> <family>Tengelmann</family></author>, in <container-title>Das Recht Des Einkaufs</container-title>, <publisher>Gabler Verlag</publisher>, <issued><year>1964</year></issued>, pp. <page>84–89</page>.

#Note1: keep the out most label, e.g., author, issued
#Note2: ignore words without tags
###
def preprocess_ref_string(raw_string, debug=False):
    tokens = []
    labels = []

    # Removing white spaces in between the strings
    #raw_string = raw_string.replace("> <", "><")
    soup = BeautifulSoup(raw_string, 'html.parser')
    #print(soup.prettify())

    for child in soup.children:
        # If the child is not a tag instance, skip
        if not isinstance(child, bs4.element.Tag):
            continue
        # If the child has no content, skip
        if len(str(child.contents)) == 0:
            continue

        if debug:
            print("***** child", child, type(child))
            print(child.get_text())
            print([w for w in child.stripped_strings])

        # Get all text and label of this pair
        label = child.name
        child_tokens = child.get_text().split()
        tokens.extend(child_tokens)
        labels.extend([label]*len(child_tokens))

    assert len(tokens) == len(labels)
    return tokens, labels


if __name__=="__main__":
    print("***** Starting at", time.asctime(), "*****")

    # remove tags of giant text strings
    giant_filename = sys.argv[1] # filepath of a giant data file
    input_filename, label_filename = giant_to_input(giant_filename)
    print("***** A Giant data file is transformed to input files at", time.asctime(), "*****")