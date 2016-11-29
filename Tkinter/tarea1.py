import tkFileDialog
def file_save(m):
    f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save=""
    for x in xrange(len(m)):
        if x==len(m)-1:
            text2save+=str(m[x])
        else:
            text2save+=str(m[x])+" "
    f.write(text2save)
    f.close() # `()` was missing.
def open_file():
    f = tkFileDialog.askopenfile(mode='r', defaultextension=".txt")
    f=f.read().split(" ")
    return f
l=[int(x) for x in open_file()]
print l
count=3
try:
    while True:
        bandera=True
        for x in l:
            if(count%x==0):
                bandera=False
        if bandera:
            l.append(count)
        count+=1
except KeyboardInterrupt:
    file_save(l)
