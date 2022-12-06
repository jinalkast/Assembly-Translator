from .LocalVariables import LocalVariableExtraction
from generators.LocalMemoryAllocation import LocalMemoryAllocation
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
          self.__func_count = 0
          self.st = st

     """We supports assignments and input/print calls"""
    
     def finalize(self):
          self.__instructions.append((None, '.END'))
          return self.__instructions

     def visit_FunctionDef(self, node):
          # define memory
          self.__local_vars = {}
          # Record entry point
          # subtract stack pointer
          # allocate memory for local variables, parameters and return value
          local_extractor = LocalVariableExtraction(self.st)
          local_extractor.visit(node)
          local_memory_alloc = LocalMemoryAllocation(local_extractor.results, self.st)
          local_memory_alloc.generate(self.__func_count)
          # Visiting the body of the function
          for contents in node.body:
               self.visit(contents)
          self.__func_count += 1        
     def visit_Return(self,node):
          self.__instructions.append((None, f'LDWA {node.value.id},s'))
          self.__instructions.append((None, f'STWA retVal,s'))
          self.__instructions.append((None, f'ADDSP 2,i'))
          self.__instructions.append((None, f'RET'))

     
