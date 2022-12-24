class Claim():
    def __init__(self, subject = '', verb = '', complement = '', category = '', subcategory = ''):
        # Sentence components
        self.__subject = subject
        self.__verb = verb
        self.__complement = complement

        # Ratings
        self.__gross_upvotes = 0
        self.__gross_downvotes = 0
        self.__unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.__irrelevancy = 0
        self.__irrelevancy_flag = False
        self.__unadjusted_net_position = set_adjusted_net_position(self)
        self.__aggregate_score = 0

        acc_

        # Qualities
        self.__category = category
        self.__subcategory = subcategory
        self.__responses = []

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
    def verb(self):
        return self.__verb

    @verb.setter
    def verb(self, param):
        self.__verb = param

    @verb.deleter
    def verb(self):
        del self.__verb

    @property
    def complement(self):
        return self.__complement

    @complement.setter
    def complement(self, param):
        self.__complement = param

    @complement.deleter
    def complement(self):
        del self.__complement

    @property
    def support(self):
        return self.__support

    @support.setter
    def support(self, param):
        self.__support = param

    @support.deleter
    def support(self):  
        del self.__support

    @property
    def category(self):
        return self.__category
    
    @category.setter
    def category(self, param):
        self.__category = param

    @category.deleter
    def category(self):
        del self.__category

    @property
    def subcategory(self):
        return self.__subcategory
    
    @subcategory.setter
    def subcategory(self, param):
        self.__subcategory = param

    @subcategory.deleter
    def subcategory(self):
        del self.__subcategory

    def print_claim(self):
        print(f'Class: Claim\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses: {self.__responses}\n')

    def provide_response(self, claim):
        self.__responses.append(claim)

    def upvote(self, claim):
        self.__upvotes += 1
        self.update_score()

    def downvote(self, claim):
        self.__downvotes += 1
        self.update_score()

    def update_score(self):
        self.__score = self.upvotes - self.downvote

    def update_aggregate_score(self):
        acc = 0
        for score in self.__responses:
            score
            acc = score.score
        self.__score = self.upvotes - self.downvote

    def set_adjusted_net_position(self):
        if self.__irrelevancy_flag:
            return 0
        else:
            return self.__unadjusted_net_position
