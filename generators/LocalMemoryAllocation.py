
class LocalMemoryAllocation():

    def __init__(self, local_vars: dict()) -> None:
        self.__local_vars = local_vars

    def generate(self):
        for n in self.__local_vars:
            print(f'{n+":":<9}\t.EQUATE {self.__local_vars[n]}') # reserving memory
