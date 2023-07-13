# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
list=["Encode","Decode"]
print("What You want to do choose on option")
print(f"1 {list[0]} ")
print(f"2 {list[1]}")
s=int(input("Enter Your Option : "))


if(s==1):
 k=input("Enter text you want to Encrpt: ")
 print("The text  you enter is  : {0} ".format(k))
 g=len(k)
 if (g<=3):
      z="noice"
      t='oo'
      r=k[0]
      k=k[1:]
      k=t+k+r+z
      print("Encrpted Text is equal to : ",k)
 else:
    k=k[::-1]
    print("Encrpted Text is equal to : ",k)
  
elif(s==2):
  k=input("Enter text you want to decrpyt: ")
  print("The text  you enter is  : {0} ".format(k))
  g=len(k)
  if (g<=3):
      z="noice"
      r=k[-1]
      k=k[:-1]
      k=t+r+k+z
      print("decrypted Text is equal to : ",k)
  else:
    k=k[::-1]
    print("decrypted Text is equal to : ",k)




# Another way


#st = input("Enter message")
# words = st.split(" ")
# coding = input("1 for Coding or 0 for Decoding")
# coding = True if (coding=="1") else False
# print(coding)
# if(coding):
#   nwords = []
#   for word in words:
#     if(len(word)>=3):
#       r1 = "dsf"
#       r2 = "jkr"
#       stnew = r1+ word[1:] + word[0] + r2
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))

# else:
#   nwords = []
#   for word in words:
#     if(len(word)>=3): 
#       stnew = word[3:-3]
#       stnew = stnew[-1] + stnew[:-1]
#       nwords.append(stnew)
#     else:
#       nwords.append(word[::-1])
#   print(" ".join(nwords))
  