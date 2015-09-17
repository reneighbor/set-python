class Set:

    def __init__(self, initial_elements = []):
        self.elements = {}

        for element in initial_elements:
            if self.contains(element) == False:
                self.elements[element] = True

    def add(self, element):
        self.elements[element] = True

    def remove(self, element):
        if self.elements.get(element):
            self.elements.pop(element)

    def contains(self, element):
        if self.elements.get(element):
            return True
        return False

    def len(self):
        return len(self.elements)

    def equals(self, _set):
        if isinstance(_set, Set) == False:
            return False

        if self.elements == _set.elements:
            return True
        return False


