class Set:

    def __init__(self, initial_elements = []):
        self.elements = []

        for element in initial_elements:
            if element not in self.elements:
                self.elements.append(element)


   