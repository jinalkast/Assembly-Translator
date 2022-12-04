import ast

class LocalVariableExtraction(ast.NodeVisitor):
    """ 
        We extract all of the details related to local (function) assignments
    """
    
    def __init__(self, st, global_vars) -> None:
        super().__init__()
        self.results = {}
        self.st = st
        self.global_vars = global_vars

    def visit_FunctionDef(self, node):
        local_vars = []
        for contents in node.body:
            if isinstance(contents, ast.Assign) and contents.targets[0].id not in self.global_vars and contents.targets[0].id not in local_vars:
                local_vars.append(contents.targets[0].id)
        max_index = len(local_vars) * 2
        for i in range (max_index, -1, -2):
            self.results[local_vars[i//2 - 1]] = i
    
