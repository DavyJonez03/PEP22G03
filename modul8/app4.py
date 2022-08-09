# remove empty lines from a text using filter

def remove_empty_lines(text:str):
    file = open(text, "r")
    result = file.read()
    #print(result)
    return filter(lambda line:line, result.splitlines())
#print(remove_empty_lines("MyFile"))
for i in remove_empty_lines("MyFile"):
    print(i)


