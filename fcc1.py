import re

def arithmetic_arranger(problems,flag = False):
  if len(problems) > 5:
    return "Error: Too many problems."
#---------------------------------------------------------------------------------------------------
  def make(prob):
    x = prob.split()
    if x[1] != '+' and x[1] != '-':
      return "Error: Operator must be '+' or '-'."
    if len(x[0]) > 4 or len(x[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    if re.search('[a-zA-Z]', x[0]) or re.search('[a-zA-Z]', x[2]):
      return "Error: Numbers must only contain digits."
    result = []
    if len(x[0]) < len(x[2]):
      result.append(2 * ' ' + (len(x[2]) - len(x[0]) ) * ' ' + x[0])
      result.append(x[1] + ' ' + x[2])
    elif len(x[0]) > len(x[2]):
      result.append(2 * ' ' + x[0])
      result.append(x[1] + ( (1 + len(x[0]) - len(x[2])) * ' ') + x[2])
    else:
      result.append(2*' '+ x[0])
      result.append(x[1] + ' ' + x[2])
    result.append(len(result[1]) * '-')
    res = 0
    if(x[1] == '-'):
      res = str(int(x[0]) - int(x[2]))
    else:
      res = str(int(x[0]) + int(x[2]))
    result.append((len(result[2]) - len(res)) * ' ' + res)
    return result
#---------------------------------------------------------------------------------------------------
  solved = []
  for a in problems:
    solved.append(make(a))
    if(type(solved[len(solved)-1]) is str):
      return solved[len(solved)-1]
  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''
  for i in range(len(problems)):
    line1 += solved[i][0]
    line2 += solved[i][1]
    line3 += solved[i][2]
    line4 += solved[i][3]
    if i < (len(problems) - 1):
      line1 += 4 * ' '
      line2 += 4 * ' '
      line3 += 4 * ' '
      line4 += 4 * ' '
    else:
      line1 += '\n'
      line2 += '\n'
  if flag == True:
    line3 += '\n'
    return (line1+line2+line3+line4)
  return (line1+line2+line3)
#---------------------------------------------------------------------------------------------------