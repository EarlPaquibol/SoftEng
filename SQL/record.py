class Record:
    """A record class"""

    def __init__(self, first, last, size, type, pay):
        self.first = first
        self.last = last
        self.size = size
        self.type = type
        self.pay = pay

    # @property
    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Record('{}', '{}', '{}', '{}', '{}')".format(self.first, self.last, self.size, self.type, self.pay)
