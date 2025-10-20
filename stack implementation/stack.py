class Stack:
    def __init__(self):
        self.internal_list = []

    def push(self, item):

        self.internal_list.append(item)
        pass  # ends the method when it's empty

    def pop(self):
        if len(self.internal_list) > 0:
            x = self.internal_list[-1]
            del self.internal_list[-1]
            return x
        else:
            return None

    def peep(self):
        if len(self.internal_list) > 0:
            return self.internal_list[-1]
        pass

    def __str__(self):
        return self.internal_list.__str__()