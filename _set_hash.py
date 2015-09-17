class Set:

    def __init__(self, initial_elements = []):
        self.elements = {}

        for element in initial_elements:
            if self.contains(element) == False:
                self.elements[element] = True


    def add(self, element):
        self.elements[element] = True

    def contains(self, element):
        # if element in self.element.keys() // Inefficient way, 
        # need to iterate thru whole list
        if self.elements.get(element):
            return True
        return False