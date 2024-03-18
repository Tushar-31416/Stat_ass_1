import statistics
import math

file = open("1ss_1_6th.txt","r")
f = file.readlines()


#   READING     THE     INFO    FROM    THE     COLUMNS *****************************************

column = []
english = []
turkish = []
for k in range(len(f)):
    sub_cut=[]
    for i in range(len(f[k])):
        if(f[k][i]=="%"):
            sub_cut.append(i)
    a = 2
    for j in range(len(sub_cut)):
        if(j==0):
            english.append(float(f[k][a:sub_cut[j]]))
            a = sub_cut[j]+2
        else:
            turkish.append(float(f[k][a:sub_cut[j]]))
#print("This the splitted version of the entire thing : ",splited)
print("english : ",english)
print("turkish : ",turkish)

file.close()

#************************************************************************************************

#   CHECKING    THE     INFORMATION     ENTROPY ************************************************

def entropy(x):
    S = 0
    for i in range(len(x)):
        if(x[i]>0):
            S = S - (x[i]/100)*math.log((x[i]/100))
    return S

print("Entropy of English is : ",entropy(english))
print("Entropy of Turkish is : ",entropy(turkish))


#************************************************************************************************


#   BIGRAM ENGLISH ************************************************

file2 = open("bigram_english.txt","r")
file3 = open("bigram_turkish.txt","r")
f2 = file2.readlines()
f3 = file3.readlines()

#   READING     THE     INFO    FROM    THE     COLUMNS *****************************************

english_b = []
turkish_b = []


for k in range(len(f2)):
       english_b.append(float(f2[k][3:8]))
#            a = sub_cut[j]+2
#        else:
#            turkish.append(float(f[k][a:sub_cut[j]]))
#print("This the splitted version of the entire thing : ",splited)
print("english_b : ",english_b)


for k in range(len(f3)):
       turkish_b.append(float(f3[k][3:9]))
#            a = sub_cut[j]+2
#        else:
#            turkish.append(float(f[k][a:sub_cut[j]]))
#print("This the splitted version of the entire thing : ",splited)
print("turkish_b : ",turkish_b)


print("Conditional entropy of English is : ",entropy(english_b))
print("Conditional entropy of Turkish is : ",entropy(turkish_b))



file2.close()
file3.close()


