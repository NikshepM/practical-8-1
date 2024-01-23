fh =open("prac 8.1.txt",'w')
abc=[9,3,2,6,1,0]
fh.write("Before Sorting:"+str(abc))
abc.sort(reverse=True)
fh.write("After Sorting:"+str(abc))
fh.close()
