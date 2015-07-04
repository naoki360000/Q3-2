def fix_second(s):
    ret = s[0:1] + s[1:].replace(s[2],"*")
    return ret

print fix_second("eel")
print fix_second("goooogle")
print fix_second("apple")
    
