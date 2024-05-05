flag = open("flag.txt", "r").read()
awaflag = open("awawa.txt", "w")

# lookup table containing the AwaSCII coding
lookup = "AWawJELYHOSIUMjelyhosiumPCNTpcntBDFGRbdfgr0123456789 .,!'()~_/;\n"

# never forget the leading awa
output = "awa"

for c in flag:
    # look up character in AwaSCII coding
    awascii_code = lookup.index(c)
    
    # convert code into binary (copied this off of stackoverflow)
    binary_awascii = format(awascii_code, '#010b')[2:]
    
    # convert binary to awas
    awascii = binary_awascii.replace("0", " awa").replace("1", "wa")
    
    output += awascii
    
awaflag.write(output)