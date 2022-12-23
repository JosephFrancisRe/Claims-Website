class Claim():
    def __init__(self):
        self.__subject = ''
        self.__text = ''
        self.__support = []

    def print_claim(self):
        print(f'Class: Claim\nSubject: {self.__subject}\nText: {self.__text}')


        @property
        def subject(self):
            return self.__subject
        
        @subject.setter
        def subject(self, param):
            self.__subject = param

        @subject.deleter
        def subject(self):
            del self.__subject

        
        @property
        def text(self):
            return self.__text

        @text.setter
        def text(self, param):
            self.__text = param

        @text.deleter
        def text(self):
            del self.__text

        
        @property
        def support(self):
            return self.__support

        @support.setter
        def support(self, param):
            self.__support = param

        @support.deleter
        def support(self):
            del self.__support

c = Claim()
c.subject = 'Derek Jeter'
c.text = 'is the greatest Yankee of all time.'
c.print_claim()