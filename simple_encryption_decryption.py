
def tokenize(omsg):
    tmsg=list(omsg)
    return tmsg


def encryption(tmsg):
    for i in range(len(tmsg)):
        if(tmsg[i] in alpha1):
            if(tmsg[i]=='o'):
                emsg.append('+')
            elif(tmsg[i]=='v'):
                emsg.append(alpha1[7])
            elif(tmsg[i]=='x'):
                emsg.append(alpha1[6])
            elif(tmsg[i]!='v' and tmsg[i]!='x'):
                iia=alpha1.index(tmsg[i])#iia=i in alpha
                newi=iia+2
                emsg.append(alpha1[newi])
        elif(tmsg[i] in alpha2):
            if(tmsg[i]=='c'):
                emsg.append(alpha2[1])
            elif(tmsg[i]=='f'):
                emsg.append(alpha2[0])
            elif(tmsg[i]!='c' and tmsg[i]!='f'):
                iia=alpha2.index(tmsg[i])#iia=i in alpha
                newi=iia-2
                emsg.append(alpha2[newi])
        elif(tmsg[i] in alpha3):
            if(tmsg[i]=='b'):
                emsg.append('-')
            else:
                iia=alpha3.index(tmsg[i])#iia=i in alpha
                newi=iia-1
                emsg.append(alpha3[newi])
        elif(tmsg[i] in space):
            key.append(tmsg[i])
            emsg.append('?')
    return emsg,key

def decryption(xmsg):
    for i in range(len(xmsg)):
        if(xmsg[i]=='+'):
            dmsg.append('o')
        elif(xmsg[i] in alpha1):
             if(tmsg[i]=='v'):
                dmsg.append(alpha1[7])
             elif(tmsg[i]=='x'):
                 dmsg.append(alpha1[6])
             elif(tmsg[i]!='v' and tmsg[i]!='x'):
                 iia=alpha1.index(xmsg[i])#iia=i in alpha
                 newi=iia-2
                 dmsg.append(alpha1[newi])
        elif(xmsg[i] in alpha2):
             if(tmsg[i]=='c'):
                dmsg.append(alpha2[1])
             elif(tmsg[i]=='f'):
                dmsg.append(alpha2[0])
             elif(tmsg[i]!='c' and tmsg[i]!='f'):
                iia=alpha2.index(xmsg[i])#iia=i in alpha
                newi=iia+2
                dmsg.append(alpha2[newi])
        elif(xmsg[i] in alpha3):
                iia=alpha3.index(xmsg[i])#iia=i in alpha
                newi=iia+1
                dmsg.append(alpha3[newi])
        elif(xmsg[i]=='?'):
            dmsg.append(key[0])
            key.remove(key[0])
        elif(xmsg[i]=='-'):
            dmsg.append('b')
    return dmsg

def newmsg(emsg):        
    xmsg=''
    for i in range(len(emsg)):
        xmsg=xmsg+emsg[i]
    return xmsg

alpha1=list('aehlouvx')
alpha2=list('cfkmqrtwz')
alpha3=list('bdgijnpsy')
space=list('!@#$%^&*()_+1234567890-=<>?:"{}|,./;[]'+' ')
imsg=input('enter your message')
omsg=imsg.lower()
tmsg=tokenize(omsg)
emsg=[]
dmsg=[]
key=[]
emsg,key=encryption(tmsg)
xmsg=newmsg(emsg)
print('encrypted msg: ',xmsg)
dmsg=decryption(xmsg)
originalmsg=newmsg(dmsg)
print('decryption msg:',originalmsg)

