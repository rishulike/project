import os
print(os.walk(os.getcwd()))
for dirname,dirpath,filename in os.walk("E:\\Software Engineering"):
    print(dirname)
    print(dirpath)
    print(filename)
print(os.environ.get("path"))
print(os.path.join(os.getcwd(),"text.txt"))


pa=os.path.join(os.getcwd(),"E:\\text.txt")
file=open(pa,"w")
file.write("hello")
file.close()
file=open(pa,'a')
file.writelines(["\tBye\n","hi"])
file.close()
file=open(pa,"w")
val='''sdyouyrtdyfygkhljfdeoiuyjedfvnb
oyytrsxcedfgmnbcvb
iuytreasyjytrrazxcvbiuytfc
nbvcsertygxcvt'''
file.write(val)
file.close()
print(val)
file=open(pa,'a')
file.write("\n next file")
file.close
print(pa)
file=open(pa,'r')
print(file.read())
for lines in file.readlines():
    print(line)
    file.close()


                   
