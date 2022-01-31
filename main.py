# a test input data, this could be a file to be read 
testStr = "hamid1reza123mol53.1noori"

# a funciton to detect a digit or a dot 
def belongsToNumber(char):
  return char.isdigit() or char=="." 

# main code
numbers = []
record = ""
for i in range(0, len(testStr)):
  ch = testStr[i]

  if (belongsToNumber(testStr[i])):
    record = record + ch
  elif (record != ""):
    numbers.append(float(record))
    record = ""    

# testing the code
print (numbers)
