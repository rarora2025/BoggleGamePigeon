
filer = open('word-list.txt', 'r')
lines = filer.readlines()
filer.close()

def printBoggle(boggleToPrint):
    for line in boggleToPrint:
        for character in line:
          #end paramater, to keep on same line
          print(character.upper() + " ", end = "")
        
        print()
    
def canMake(word, positions, boggle):
  
  if positions == []:
    toreturn = []
    for line in range(len(boggle)):
      for character in range(len(boggle[line])):
        if(boggle[line][character] == word[0]):
         
          toreturn.append([line, character])
         
    
    if len(toreturn) == 1:
      return canMake(word, [toreturn[0]], boggle)

    for xy in range(len(toreturn)-1):
      
      if canMake(word, [toreturn[xy]], boggle):
        
        return canMake(word, [toreturn[xy]], boggle)
      else:
        
        return canMake(word, [toreturn[xy+1]], boggle)

  
  if(len(positions) == 0 or positions[len(positions)-1][0] > 3 or positions[len(positions)-1][0] < 0 or positions[len(positions)-1][1] > 3 or positions[len(positions)-1][1] < 0):
    return False

  x = positions[len(positions)-1][0]
  y = positions[len(positions)-1][1]

  if boggle[x][y] != word[len(positions)-1]:
    return False

  for y in range(len(positions)-1):
    if positions[-1] == positions[y]:
      return False
  

  if (len(positions) == len(word)):
    #print(positions)
    return True

  
  else:
    #return all direction coords + original pos
    return canMake(word, positions + [[1 + positions[-1][0], positions[-1][1]]] , boggle) or canMake(word, positions + [[positions[-1][0] - 1, positions[-1][1]]] , boggle) or canMake(word, positions + [[positions[-1][0], positions[-1][1]+1]] , boggle) or canMake(word, positions + [[positions[-1][0], positions[-1][1]-1]] , boggle) or canMake(word, positions + [[positions[-1][0] - 1, positions[-1][1]-1]] , boggle) or canMake(word, positions + [[positions[-1][0] + 1, positions[-1][1]+1]] , boggle) or canMake(word, positions + [[positions[-1][0] + 1, positions[-1][1]-1]] , boggle) or canMake(word, positions + [[positions[-1][0] - 1, positions[-1][1]+1]] , boggle)


#bogglegrid  = returnBoggle()
bogglegrid = []
for x in range(4):
  inner = []
  for y in range(4):
    inner.append(input("enter: "))
  bogglegrid.append(inner)

print("The Boggle Grid is: ")
print("-------------------")
printBoggle(bogglegrid)
print()
print("The following words were found:")
print("-------------------------------")
format = 0

for line in lines:
  if (canMake(line.strip(), [], bogglegrid)):
    
    print(" " + line.strip(), end = "")
    format += 1
    if(format %5 == 0):
      print()
    else:
      print(", ", end = "")

