h=int(input())
m=int(input())
words=["one","two","three","four","five","six","seven","eight","nine","ten","eleven",
     "twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen",
     "nineteen","twenty","twenty one","twenty two","twenty three","twenty four",
     "twenty five","twenty six","twenty seven","twenty eight","twenty nine"]
if m>0 and m<30 and m!=15 and m!=1:
    print(words[m-1]+" minutes "+"past "+words[h-1])
if m==1:
    print(words[0]+" minute"+" past "+words[h-1] )
if m>30 and m!=45:
    print(words[60-m-1]+" minutes"+" to "+words[h])
if m==15:
    print("quarter past "+words[h-1])
if m==45:
    print("quarter to "+words[h])
if m==0:
    print(words[h-1] +" o'"+" clock")
if m ==30:
    print("half past "+words[h-1])
    