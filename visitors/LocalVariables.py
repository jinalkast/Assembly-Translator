import ast

class LocalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all of the details related to local (function) assignments
    """
    
    def __init__(self, st) -> None:
        super().__init__()
        self.results = {}
        self.st = st

    def visit_FunctionDef(self, node):
        local_vars = []
        parameters = [arg.arg for arg in node.args.args]
        returnExists = False

        for contents in node.body:
            if isinstance(contents, ast.Assign) and contents.targets[0].id not in local_vars:
                local_vars.append(contents.targets[0].id)
                
            elif isinstance(contents, ast.Return):
                returnExists = True

        i = (len(local_vars) - 1) * 2

        if returnExists:
            paramIndex = i + 4
            
        else:
            paramIndex = i + 2

        for param in parameters:
            self.results[param] = paramIndex
            paramIndex += 2

        for var in local_vars:
            self.results[var] = i
            i -= 2