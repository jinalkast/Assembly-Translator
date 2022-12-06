
class LocalMemoryAllocation():

    def __init__(self, local_vars: dict(), st) -> None:
        self.__local_vars = local_vars
        self.st = st

    def generate(self, func_id:int):
        for n in self.__local_vars:
            print(f'{self.st.getLocalName(n, func_id)+":":<9}\t.EQUATE {self.__local_vars[n]}') # reserving memory
