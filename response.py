import claim as c

class Response(c.Claim):
    def __init__(self, c, polarity):
        super().__init__()
        # Identity
        self.__polarity = polarity
        self.__category = c.category
        self.__subcategory = c.subcategory
        self.__responses = []
        
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
        self.__adjusted_net_position = 0
        self.__unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()

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

    @property
    def responses(self):
        return self.__responses

    @responses.setter
    def responses(self, param):
        self.__responses = param

    @responses.deleter
    def responses(self):
        del self.__responses

    def print_response(self):
        if self.__responses == []:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses: None\n')
        else:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nResponses:\n')
            for subresponse in self.__responses:
                subresponse.print_response()

    def upvote(self):
        self.__gross_upvotes += 1
        self.update_unadjusted_net_position()

    def downvote(self):
        self.__gross_downvotes += 1
        self.update_unadjusted_net_position()

    def update_unadjusted_net_position(self):
        self.unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.adjusted_net_position = self.unadjusted_net_position

    def provide_response(self, claim):
        self.__responses.append(claim)

    def irrelevancy_vote(self):
        self.__irrelevancy_score += 1
        if self.__irrelevancy_score >= self.__gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False

    def remove_irrelevancy_vote(self):
        self.__irrelevancy_score -= 1
        if self.__irrelevancy_score >= self.__gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False

    def update_adjusted_net_position(self):
        if self.__irrelevancy:
            return 0
        else:
            self.__adjusted_net_position = self.__unadjusted_net_position

    def update_unadjusted_aggregate_position(self):
        return None
