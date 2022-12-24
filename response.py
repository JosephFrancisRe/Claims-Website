import claim

class Response(claim.Claim):
    def __init__(self, c, polarity):
        super().__init__()
        # Claim components
        self.__subject = c.subject
        self.__verb = c.verb
        self.__complement = c.complement

        # Score
        self.__gross_upvotes = c.gross_upvotes
        self.__gross_downvotes = c.gross_downvotes
        self.__unadjusted_net_position = c.unadjusted_net_position
        self.__irrelevancy_score = 0
        self.__irrelevancy = False

        # Identity
        self.__polarity = polarity
        self.__category = c.category
        self.__subcategory = c.subcategory
        self.__responses = []

    @property
    def form(self):
        return self.__polarity

    @form.setter
    def form(self, param):
        self.__polarity = param

    @form.deleter
    def form(self):
        del self.__polarity

    @property
    def irrelevancy(self):
        return self.__irrelevancy_score

    @form.setter
    def irrelevancy(self, param):
        self.__irrelevancy_score = param

    @form.deleter
    def irrelevancy(self):
        del self.__irrelevancy_score

    @property
    def irrelevancy(self):
        return self.__irrelevancy
    
    @irrelevancy.setter
    def irrelevancy(self, param):
        self.__irrelevancy = param

    @irrelevancy.deleter
    def irrelevancy(self):
        del self.__irrelevancy

    def print_response(self):
        if self.__responses == []:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses: None')
        else:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses:\n')
            for subresponse in self.__responses:
                subresponse.print_response()

    def provide_response(self, claim):
        self.__responses.append(claim)