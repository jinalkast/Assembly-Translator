import ast

class LocalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all of the details related to local (function) assignments
    """
    
    def __init__(self, st) -> None:
        super().__init__()
        self.st = st
        self.returnExists = False
        self.local_vars = {}
        self.parameters = {}

    def visit_FunctionDef(self, node):
        local_vars = []
        parameters = [arg.arg for arg in node.args.args]

        for contents in node.body:
            if isinstance(contents, ast.Assign) and contents.targets[0].id not in local_vars and contents.targets[0].id not in parameters:
                local_vars.append(contents.targets[0].id)
                
            elif isinstance(contents, ast.Return):
                self.returnExists = True

        i = (len(local_vars) - 1) * 2

        paramIndex = i + 4
 

        for param in parameters:
            self.parameters[param] = paramIndex
            paramIndex += 2

        for var in local_vars:
            self.local_vars[var] = i
            i -= 2