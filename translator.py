import argparse
import ast
from visitors.GlobalVariables import GlobalVariableExtraction
from visitors.LocalVariables import LocalVariableExtraction
from visitors.TopLevelProgram import TopLevelProgram
from visitors.Functions import Functions
from generators.StaticMemoryAllocation import StaticMemoryAllocation
from generators.LocalMemoryAllocation import LocalMemoryAllocation
from generators.EntryPoint import EntryPoint
from generators.symbolTable import SymbolTable
def main():
    input_file, print_ast = process_cli()
    with open(input_file) as f:
        source = f.read()
    node = ast.parse(source)
    if print_ast:
        print(ast.dump(node, indent=2))
    else:
        process(input_file, node)
    
def process_cli():
    """"Process Command Line Interface options"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', help='filename to compile (.py)')
    parser.add_argument('--ast-only', default=False, action='store_true')
    args = vars(parser.parse_args())
    return args['f'], args['ast_only']

def process(input_file, root_node):
    print(f'; Translating {input_file}')
    
    # Create symbol table 
    st = SymbolTable()

    extractor = GlobalVariableExtraction(st)
    extractor.visit(root_node)
    memory_alloc = StaticMemoryAllocation(extractor.results)
    print('; Branching to top level (tl) instructions')
    print('\t\tBR tl')
    memory_alloc.generate()
    local_extractor = LocalVariableExtraction(st, extractor.results)
    local_extractor.visit(root_node)
    local_memory_alloc = LocalMemoryAllocation(local_extractor.results)
    local_memory_alloc.generate()
    # functions = Functions(st, extractor.results)
    # functions.visit(root_node)
    top_level = TopLevelProgram('tl',st)
    top_level.visit(root_node)
    ep = EntryPoint(top_level.finalize())
    ep.generate() 

if __name__ == '__main__':
    main()
