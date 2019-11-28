arg=b('nis')
koneksi=0
while (arg != "") : 
    first = substr(arg,0,1)

    if first=="'" :
        indarg = indarg + "'"
    elif first==" " :
        indarg = indarg + " "
    elif first=="O" :
        indarg = indarg + "O"
    elif first=="R" :
        indarg = indarg + "R"
    elif first=="1" :
        indarg = indarg + "1"
    elif first=="=" :
        indarg = indarg + "="
    elif first=="-" :
        indarg = indarg + "-"
    
    arg = substr(arg,1)
u="xpto1" + indarg + "xpto2"
z(u,koneksi)
