from .TopLevelProgram import TopLevelProgram
import ast

LabeledInstruction = tuple[str, str]
assigned = {}

class Functions(ast.NodeVisitor):
     def __init__(self, st, global_vars) -> None:
          super().__init__()
          self.__instructions = list()
          self.__should_save = True
          self.__local_vars = {}
          self.__current_variable = None
          self.__elem_id = 0
          self.__in_loop = False
          self.__global_vars = global_vars
          self.st = st

     """We supports assignments and input/print calls"""
    
     def finalize(self):
          self.__instructions.append((None, '.END'))
          return self.__instructions

     def visit_FunctionDef(self, node):
          # define memory
          self.__local_vars = {}
          self.allocate_function_memory(node)
          # Record entry point
          # subtract stack pointer

          # Visiting the body of the function
          for contents in node.body:
               self.visit(contents)

     

          print(node.name)

     def visit_Return(self,node):
          self.__instructions.append((None, f'LDWA {node.value.id},s'))
          self.__instructions.append((None, f'STWA retVal,s'))
          self.__instructions.append((None, f'ADDSP 2,i'))
          self.__instructions.append((None, f'RET'))

     
     def allocate_function_memory(self, node):
          for content in node.body:
               if type(content) == ast.Assign:
                    self.st.loadVal(content.targets[0].id)
                    if content.targets[0].id not in self.st:
                         self.__local_vars[content.targets[0].id] = None
                    else:
                         # is global constant 
                         pass
                        # if self.__global_vars[self.st.getVal(content.targets[0].id)] != None:
                              
