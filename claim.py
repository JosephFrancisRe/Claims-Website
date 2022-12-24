class Claim:
    def __init__(self, subject="", verb="", complement="", category="", subcategory=""):
        # Identity
        self.__category = category
        self.__subcategory = subcategory
        self.__responses = []
        
        # Claim components
        self.__subject = subject
        self.__verb = verb
        self.__complement = complement

        # Scores
        self.__gross_upvotes = 0
        self.__gross_downvotes = 0
        self.__unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.__adjusted_net_position = self.__unadjusted_net_position
        self.__unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()

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
    def gross_upvotes(self):
        return self.__gross_upvotes

    @gross_upvotes.setter
    def gross_upvotes(self, param):
        self.__gross_upvotes = param

    @gross_upvotes.deleter
    def gross_upvotes(self):
        del self.__gross_upvotes

    @property
    def gross_downvotes(self):
        return self.__gross_downvotes

    @gross_downvotes.setter
    def gross_downvotes(self, param):
        self.__gross_downvotes = param

    @gross_downvotes.deleter
    def gross_downvotes(self):
        del self.__gross_downvotes

    @property
    def unadjusted_net_position(self):
        return self.__unadjusted_net_position

    @unadjusted_net_position.setter
    def unadjusted_net_position(self, param):
        self.__unadjusted_net_position = param

    @unadjusted_net_position.deleter
    def unadjusted_net_position(self):
        del self.__unadjusted_net_position

    @property
    def unadjusted_aggregate_position(self):
        return self.__unadjusted_aggregate_position

    @unadjusted_aggregate_position.setter
    def unadjusted_aggregate_position(self, param):
        self.__unadjusted_aggregate_position = param

    @unadjusted_aggregate_position.deleter
    def unadjusted_aggregate_position(self):
        del self.__unadjusted_aggregate_position

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

    @property
    def responses(self):
        return self.__responses

    @responses.setter
    def responses(self, param):
        self.__responses = param

    @responses.deleter
    def responses(self):
        del self.__responses

    def print_claim(self):
        if self.__responses == []:
            print(
                f"{type(self)}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses: None"
            )
        else:
            print(
                f"{type(self)}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses:\n"
            )
            self.print_responses()

    def print_responses(self):
        for response in self.__responses:
            response.print_response()

    def add_response(self, response):
        self.__responses.append(response)

    def upvote(self):
        self.__gross_upvotes += 1
        self.update_unadjusted_net_position()

    def downvote(self):
        self.__gross_downvotes += 1
        self.update_unadjusted_net_position()

    def update_unadjusted_net_position(self):
        self.unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.adjusted_net_position = self.unadjusted_net_position
        self.update_unadjusted_aggregate_position()

    def update_unadjusted_aggregate_position(self):
        acc = 0
        for response in self.__responses:
            if response.polarity == 'support':
                acc += response.update_unadjusted_aggregate_position()
            elif response.polarity == 'negation':
                acc -= response.update_unadjusted_aggregate_position()
        return self.__adjusted_net_position + acc
