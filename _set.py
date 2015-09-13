class Set:

    def __init__(self, initial_elements = []):
        self.elements = []

        for element in initial_elements:
            if element not in self.elements:
                self.elements.append(element)

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def len(self):
        return len(self.elements)

    def contains(self, item):
        if item in self.elements:
            return True
        return False

    def equals(self, _set):
        if isinstance(_set, Set) == False:
            return False
        if sorted(self.elements) == sorted(_set.elements):
            return True
        return False

    def subset_of(self, _set):
        if isinstance(_set, Set) == False:
            return False
        for element in self.elements:
            if element not in _set.elements:
                return False
        return True

    def union(self, _set):
        new_set = Set(self.elements)

        for element in _set.elements:
            if element not in self.elements:
                new_set.elements.append(element)

        return new_set

    def intersect(self, _set):
        new_set = Set()

        for element in _set.elements:
            if element in self.elements:
                new_set.elements.append(element)

        return new_set

    def difference(self, _set):
        new_set = Set()

        for element in _set.elements:
            if element not in self.elements:
                new_set.elements.append(element)

        for element in self.elements:
            if element not in _set.elements:
                new_set.elements.append(element)
        
        return new_set