def fix_second(s):
    ret = s[0].replace(s[1],"*") + s[1] + s[2:].replace(s[1],"*")
    return ret

print fix_second("eel")
print fix_second("goooogle")
print fix_second("apple")
    
