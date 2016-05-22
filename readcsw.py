import os,sys

def cut():
    csv=[]
    cut="\","
    cut2="\""
    cut3=","

    for i in range(len(line)):
        csv.append(line[i].split(cut))

    for i in range(len(csv)):
        for k in range(len(csv[i])):
            if cut2 in csv[i][k]:
                csv[i][k]=csv[i][k].replace("\"","")
                #print (csv[i][k])
            elif cut3 in csv[i][k]:
                csv2=csv[i][k].split(cut3)
                del csv[i][k]
                for j in range(len(csv2)):
                    csv[i].insert(k+j,csv2[j])
            #elif cut4 in csv[i][k]:
            #    print (csv[i][k])
        #print (csv[i])
    return csv

def print_start():
    return ("<table border='1'>")

def print_end():
    return ("</table>")

with open("sample.csv","r") as f:
    #line=f.readlines()
    line=[l for l in f.readlines()]
csv=[]
csv=cut()
with open("sample.html","w") as w:
    count=0
    w.write(print_start())
    w.write("\n")
    for i in range(len(csv)):
        for k in range(len(csv[i])):
            if  csv[i][k].isnumeric():
                w.write("<td align='right'>{0}</td>".format(csv[i][k]))
                w.write("\n")
                if k==len(csv[i])-1:
                    w.write("</tr>")
                    w.write("\n")

            else:
                w.write("<tr>")
                w.write("\n")
                w.write("<td>{0}</td>".format(csv[i][k]))
                w.write("\n")
    w.write(print_end())
    w.write("\n")
#print (csv)
