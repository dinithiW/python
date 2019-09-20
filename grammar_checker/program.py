# -*- coding: utf-8 -*-
import nltk
import codecs
from nltk.draw.util import CanvasFrame
from nltk.draw import TreeWidget
from nltk import Tree

def check_validity(sentence):
        sent_split = sent.split()
        rd_parser = nltk.RecursiveDescentParser(load_grammar)
        for tree_struc in rd_parser.parse(sent_split):
                s = str(tree_struc)
                return s;
        return False

f = open("output.txt", 'w')
f.write("************BEGINNING OF FILE************\n")
f.close()

load_grammar = nltk.data.load('file:grammar.cfg')
file_input = codecs.open('input.txt', 'r', 'utf-8-sig')

for sent in file_input:
        output_str = "\n"
        sent = sent.rstrip("\r\n");
        validation_output = check_validity(sent)
        if validation_output is not False:
                output_str+= (sent + ":VALID GRAMMAR\n")
                output_str+= "PARSE TREE IS\n"
                output_str += validation_output+ "\n\n"
                cf = CanvasFrame()
                t = Tree.fromstring(validation_output)
                tc = TreeWidget(cf.canvas(),t)
                cf.add_widget(tc,10,10) 
        else:
                output_str+= sent + ": INVALID GRAMMAR\n"
        f = open("output.txt", "a", encoding="utf-8")
        f.write(output_str)

f.write("\n************END OF FILE************\n")
f.close()
#Exercise:
#Modify this code to display the unicode text properly and
#save the outputs to a file
