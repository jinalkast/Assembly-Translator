import ast

class GlobalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all the left hand side of the global (top-level) assignments
    """
    
    def __init__(self, st) -> None:
        super().__init__()
        self.results = dict()
        self.st = st

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError("Only unary assignments are supported")
        
        # Load value into symbol table
        self.st.loadVal(node.targets[0].id)
        
        if self.st.getVal(node.targets[0].id) not in self.results:
            # if node value is constant, pass value into result
            if isinstance(node.value, ast.Constant):
                self.results[self.st.getVal(node.targets[0].id)] = node.value.value
            
            # if node value not constant
            else:
                # if the variable is assigned to a binary operation, try and compute its value for optimization
                if isinstance(node.value, ast.BinOp):
                    left = None
                    right = None 

                    # if the left element is a known variable, copy the value from its assignment
                    if isinstance(node.value.left, ast.Name):
                        if self.st.getVal(node.value.left.id) in self.results:
                            left = self.results[self.st.getVal(node.value.left.id)]
                    # if the left element is not a variable name, it's a constant - copy its value
                    else:
                        left = node.value.left.value

                    #same for right element
                    if isinstance(node.value.right, ast.Name):
                        if self.st.getVal(node.value.right.id) in self.results:
                            right = self.results[self.st.getVal(node.value.right.id)]
                    else:
                        right = node.value.right.value

                    # if both elements are statically known at compilation, perform the binOp and pass the value into the result - otherwise, pass None
                    if left != None and right != None:
                        if isinstance(node.value.op, ast.Add):
                            self.results[self.st.getVal(node.targets[0].id)] = left + right
                        else:
                            self.results[self.st.getVal(node.targets[0].id)] = left - right
                    else:
                        self.results[self.st.getVal(node.targets[0].id)] = None

                # pass None if the variable is not assigned to binOp
                else:
                    self.results[self.st.getVal(node.targets[0].id)] = None


    def visit_FunctionDef(self, node):
        """We do not visit function definitions, they are not global by definition"""
        pass
