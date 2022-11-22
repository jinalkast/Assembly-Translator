class SymbolTable():
     def __init__(self):
        self.map = {}

      # Map var name to value in symbol table
     def loadVal(self, variableName):
         temp = variableName
         # len <= 8, no need to change anything
         if len(temp) > 8:
            # if its too long, try removing vowels, if that removes 
            # too much, just splice it 
          vowels = ('a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U")
          temp = ''.join([l for l in variableName if l not in vowels])
          if len(temp) <= 3:
             temp = variableName[0:8]
          
         # if removing vowels wasnt enough, splice it too
          elif len(temp) > 8:
              temp = temp[0:8]

         self.map[variableName] = temp
     
      # Return mapped val in symbol table
     def getVal(self, variableName):
        if variableName in self.map:
          return self.map[variableName]
        else:
           return variableName
                 
