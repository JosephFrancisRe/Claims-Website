import claim as c

class Response(c.Claim):
    def __init__(self, claim, polarity, origin):
        super().__init__()
        # Identity
        self.__polarity = polarity
        self.__category = claim.category
        self.__subcategory = claim.subcategory
        self.__origin = origin
        self.__responses = []
        
        # Claim components
        self.__subject = claim.subject
        self.__verb = claim.verb
        self.__complement = claim.complement

        # Score
        self.__gross_upvotes = 0
        self.__gross_downvotes = 0
        self.__unadjusted_net_position = 0
        self.__irrelevancy_score = 0
        self.__irrelevancy = False
        self.__adjusted_net_position = 0
        self.__unadjusted_aggregate_position = 0

    @property
    def polarity(self):
        return self.__polarity

    @polarity.setter
    def polarity(self, param):
        self.__polarity = param

    @polarity.deleter
    def polarity(self):
        del self.__polarity

    @property
    def irrelevancy_score(self):
        return self.__irrelevancy_score

    @irrelevancy_score.setter
    def irrelevancy_score(self, param):
        self.__irrelevancy_score = param

    @irrelevancy_score.deleter
    def irrelevancy_score(self):
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
    def adjusted_net_position(self):
        return self.__adjusted_net_position
    
    @adjusted_net_position.setter
    def adjusted_net_position(self, param):
        self.__adjusted_net_position = param

    @adjusted_net_position.deleter
    def adjusted_net_position(self):
        del self.__adjusted_net_position

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
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nAdjusted Net Position: {self.__adjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nOrigin: {self.__origin}\nResponses: None\n')
        else:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.__gross_upvotes}\nDownvotes: {self.__gross_downvotes}\nUnadjusted Net Position: {self.__unadjusted_net_position}\nAdjusted Net Position: {self.__adjusted_net_position}\nUnadjusted Aggregate Position: {self.__unadjusted_aggregate_position}\nCategory: {self.__category}\nSubcategory: {self.__subcategory}\nSubject: {self.__subject}\nVerb: {self.__verb}\nComplement: {self.__complement}\nSentence: {self.__subject} {self.__verb} {self.__complement}.\nOrigin: {self.__origin}\nResponses:\n')
            for subresponse in self.__responses:
                subresponse.print_response()

    def upvote(self):
        self.__gross_upvotes += 1
        self.update_unadjusted_net_position()

    def downvote(self):
        self.__gross_downvotes += 1
        self.update_unadjusted_net_position()

    def update_unadjusted_net_position(self):
        self.__unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.update_adjusted_net_position()

    def add_response(self, response):
        self.__responses.append(response)

    def irrelevancy_vote(self):
        self.__irrelevancy_score += 1
        if self.__irrelevancy_score >= self.__gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False
        self.update_adjusted_net_position()

    def remove_irrelevancy_vote(self):
        self.__irrelevancy_score -= 1
        if self.__irrelevancy_score >= self.__gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False
        self.update_adjusted_net_position()

    def update_adjusted_net_position(self):
        if self.__irrelevancy:
            self.__adjusted_net_position = 0
        else:
            self.__adjusted_net_position = self.__unadjusted_net_position
        self.update_unadjusted_aggregate_position()
