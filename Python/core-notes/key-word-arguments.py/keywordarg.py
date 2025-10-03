# Keyword arguments = an argument prceded by an indentifier 
#                     helps with readability
#                     order of arguments doesnt matter



def hello(greeting, title, first, last):
    print(f"{greeting} {title}.{first} {last}.")
    
hello(first="Oscar", last="D", greeting="WASSSAAPPP", title="Mr")

#print("1","2","3"  sep="-") will print 1-2-3