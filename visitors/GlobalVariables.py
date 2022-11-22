import ast

class GlobalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all the left hand side of the global (top-level) assignments
    """
    
    def __init__(self) -> None:
        super().__init__()
        self.results = dict()

    def visit_Assign(self, node):
        if len(node.targets) != 1:
            raise ValueError("Only unary assignments are supported")
        
        # if node value == constant pass in value as well
        if isinstance(node.value, ast.Constant):
            self.results[node.targets[0].id] = node.value.value
        
        elif node.targets[0].id not in self.results:
            if isinstance(node.value, ast.BinOp):
                left = None
                right = None 

                if isinstance(node.value.left, ast.Name):
                    if node.value.left.id in self.results:
                        left = self.results[node.value.left.id]
                else:
                    left = node.value.left.value

                if isinstance(node.value.right, ast.Name):
                    if node.value.right.id in self.results:
                        right = self.results[node.value.right.id]
                else:
                    right = node.value.right.value

                if left != None and right != None:
                    if isinstance(node.value.op, ast.Add):
                        self.results[node.targets[0].id] = left + right
                    else:
                        self.results[node.targets[0].id] = left - right
            else:
                self.results[node.targets[0].id] = None


    def visit_FunctionDef(self, node):
        """We do not visit function definitions, they are not global by definition"""
        pass
   