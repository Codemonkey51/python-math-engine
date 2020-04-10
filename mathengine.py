def mathLexer(equation):
  equation = equation.split()
  tempEquation = ""
  for i in equation:
    tempEquation += i
  equation = tempEquation
  numbers =[]
  operators = []
  tempString = ""
  tempParenthasis = ""
  parenthasisBool = False
  for i in equation:
    if(i=='+'):
      operators.append(i)
      numbers.append(tempString)
      tempString = ""
    elif(i=='-'):
      operators.append(i)
      numbers.append(tempString)
      tempString = ""
    elif(i=='*'):
      operators.append(i)
      numbers.append(tempString)
      tempString = ""
    elif(i=='/'):
      operators.append(i)
      numbers.append(int(tempString))
      tempString = ""
    else:
      tempString+=i
  numbers.append(int(tempString))
  tempString = ""
  x = 0
  for i in operators:
    if(i=='*'):
      temp = int(numbers[x])*int(numbers[x+1])
      del(numbers[x])
      numbers[x] = temp
    elif(i=='/'):
      temp = int(numbers[x])/int(numbers[x+1])
      temp= int(temp)
      del(numbers[x])
      numbers[x] = temp
    else:
      x += 1
  tempOperators = []
  for i in operators:
    if(i!='*' and i!='/'):
      tempOperators.append(i)
  operators = tempOperators
  x = 0
  for i in operators:
    if(i=='+'):
      temp = int(numbers[x])+int(numbers[x+1])
      del(numbers[x])
      numbers[x] = temp
    elif(i=='-'):
      temp = int(numbers[x])-int(numbers[x+1])
      temp= int(temp)
      del(numbers[x])
      numbers[x] = temp
    else:
      x += 1
  tempOperators = []
  for i in operators:
    if(i!='+' and i!='-'):
      tempOperators.append(i)
  operators = tempOperators
  return(equation + "=" + str(numbers[0]))
