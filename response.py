import claim as c

class Response(c.Claim):
    def __init__(self, claim, polarity, origin):
        super().__init__(subject=claim.subject, verb=claim.verb, complement=claim.complement, category=claim.category, subcategory=claim.subcategory)
        # Identity
        self.__polarity = polarity
        self.__origin = origin

        # Score
        self.__irrelevancy_score = 0
        self.__irrelevancy = False

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
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, param):
        self.__origin = param

    @origin.deleter
    def origin(self):
        del self.__origin

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

    def print_response(self):
        self.update_all()
        if self.responses == []:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.gross_upvotes}\nDownvotes: {self.gross_downvotes}\nUnadjusted Net Position: {self.unadjusted_net_position}\nAdjusted Net Position: {self.adjusted_net_position}\nUnadjusted Aggregate Position: {self.unadjusted_aggregate_position}\nUpvote/Downvote Percentage: {self.upvote_downvote_percentage}\nAdjusted Aggregate Position: {self.adjusted_aggregate_position}\nTotal Upvote/Downvote Percentage: {self.total_upvote_downvote_percentage}\nWeight of Upvote/Downvote Percentage: {self.weight_of_upvote_downvote_percentage}\nWeighted Aggregate Position: {self.weighted_aggregate_position}\nTotal Weighted Aggregate Position: {self.total_weighted_aggregate_position}\nWeighted Aggregate Position Percentage: {self.weighted_aggregate_position_percentage}\nMax Weighted Aggregate Position Percentage: {self.max_weighted_aggregate_position_percentage}\nFinal Score: {self.final_score}\nCategory: {self.category}\nSubcategory: {self.subcategory}\nSubject: {self.subject}\nVerb: {self.verb}\nComplement: {self.complement}\nSentence: {self.subject} {self.verb} {self.complement}.\nOrigin: {self.__origin}\nResponses: None\n')
        else:
            print(f'{type(self)}\nPolarity: {self.__polarity}\nIrrelevancy: {self.__irrelevancy}\nIrrelevancy Score: {self.__irrelevancy_score}\nUpvotes: {self.gross_upvotes}\nDownvotes: {self.gross_downvotes}\nUnadjusted Net Position: {self.unadjusted_net_position}\nAdjusted Net Position: {self.adjusted_net_position}\nUnadjusted Aggregate Position: {self.unadjusted_aggregate_position}\nUpvote/Downvote Percentage: {self.upvote_downvote_percentage}\nAdjusted Aggregate Position: {self.adjusted_aggregate_position}\nTotal Upvote/Downvote Percentage: {self.total_upvote_downvote_percentage}\nWeight of Upvote/Downvote Percentage: {self.weight_of_upvote_downvote_percentage}\nWeighted Aggregate Position: {self.weighted_aggregate_position}\nTotal Weighted Aggregate Position: {self.total_weighted_aggregate_position}\nWeighted Aggregate Position Percentage: {self.weighted_aggregate_position_percentage}\nMax Weighted Aggregate Position Percentage: {self.max_weighted_aggregate_position_percentage}\nFinal Score: {self.final_score}\nCategory: {self.category}\nSubcategory: {self.subcategory}\nSubject: {self.subject}\nVerb: {self.verb}\nComplement: {self.complement}\nSentence: {self.subject} {self.verb} {self.complement}.\nOrigin: {self.__origin}\nResponses:\n')
            for subresponse in self.responses:
                subresponse.print_response()

    def update_unadjusted_net_position(self):
        if self.gross_downvotes == 0:
            self.upvote_downvote_percentage = self.gross_upvotes / 1
        else:
            self.upvote_downvote_percentage = self.gross_upvotes / self.gross_downvotes
        self.unadjusted_net_position = self.gross_upvotes - self.gross_downvotes
        self.update_adjusted_net_position()
        self.unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()
        self.update_adjusted_aggregate_position()
        self.update_total_upvote_downvote_percentage()
        self.update_weight_of_upvote_downvote_percentage()
        self.update_weighted_aggregate_position()
        self.total_weighted_aggregate_position = self.update_total_weighted_aggregate_position()
        self.weighted_aggregate_position_percentage = self.weighted_aggregate_position / self.total_weighted_aggregate_position
        self.update_max_weighted_aggregate_position_percentage()
        self.update_final_score()

    def irrelevancy_vote(self):
        self.__irrelevancy_score += 1
        if self.__irrelevancy_score >= self.gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False
        self.update_adjusted_net_position()

    def remove_irrelevancy_vote(self):
        self.__irrelevancy_score -= 1
        if self.__irrelevancy_score >= self.gross_upvotes:
            self.__irrelevancy = True
        else:
            self.__irrelevancy = False
        self.update_adjusted_net_position()

    def update_adjusted_net_position(self):
        if self.__irrelevancy or self.unadjusted_net_position <= 0:
            self.adjusted_net_position = 0
        else:
            self.adjusted_net_position = self.unadjusted_net_position
        self.unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()

    def update_total_upvote_downvote_percentage(self):
        temp = self
        while not isinstance(temp.origin, c.Claim):
            temp = temp.origin
        temp = temp.origin
        self.total_upvote_downvote_percentage = temp.total_upvote_downvote_percentage
        return self.upvote_downvote_percentage

    def update_total_weighted_aggregate_position(self):
        temp = self
        while not isinstance(temp.origin, c.Claim):
            temp = temp.origin
        temp = temp.origin
        return temp.total_weighted_aggregate_position

    '''def update_max_weighted_aggregate_position_percentage(self):
        max = self.weighted_aggregate_position_percentage
        for response in self.responses:
            if response.weighted_aggregate_position_percentage > max:
                max = response.weighted_aggregate_position_percentage
        self.max_weighted_aggregate_position_percentage = max'''
