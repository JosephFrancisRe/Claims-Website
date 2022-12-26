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
        self.__upvote_downvote_percentage = 0.0
        self.__unadjusted_net_position = self.__gross_upvotes - self.__gross_downvotes
        self.__adjusted_net_position = self.__unadjusted_net_position
        self.__unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()
        self.__adjusted_aggregate_position = 0.0
        self.__total_upvote_downvote_percentage = 0
        self.__weight_of_upvote_downvote_percentage = 0
        self.__weighted_aggregate_position = 0
        self.__total_weighted_aggregate_position = 0
        self.__weighted_aggregate_position_percentage = 0
        self.__max_weighted_aggregate_position_percentage = 0
        self.__final_score = 0

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
    def upvote_downvote_percentage(self):
        return self.__upvote_downvote_percentage

    @upvote_downvote_percentage.setter
    def upvote_downvote_percentage(self, param):
        self.__upvote_downvote_percentage = param

    @upvote_downvote_percentage.deleter
    def upvote_downvote_percentage(self):
        del self.__upvote_downvote_percentage

    @property
    def total_upvote_downvote_percentage(self):
        return self.__total_upvote_downvote_percentage

    @total_upvote_downvote_percentage.setter
    def total_upvote_downvote_percentage(self, param):
        self.__total_upvote_downvote_percentage = param

    @total_upvote_downvote_percentage.deleter
    def total_upvote_downvote_percentage(self):
        del self.__total_upvote_downvote_percentage

    @property
    def weight_of_upvote_downvote_percentage(self):
        return self.__weight_of_upvote_downvote_percentage

    @weight_of_upvote_downvote_percentage.setter
    def weight_of_upvote_downvote_percentage(self, param):
        self.__weight_of_upvote_downvote_percentage = param

    @weight_of_upvote_downvote_percentage.deleter
    def weight_of_upvote_downvote_percentage(self):
        del self.__weight_of_upvote_downvote_percentage

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
    def adjusted_net_position(self):
        return self.__adjusted_net_position

    @adjusted_net_position.setter
    def adjusted_net_position(self, param):
        self.__adjusted_net_position = param

    @adjusted_net_position.deleter
    def adjusted_net_position(self):
        del self.__adjusted_net_position

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
    def adjusted_aggregate_position(self):
        return self.__adjusted_aggregate_position

    @adjusted_aggregate_position.setter
    def adjusted_aggregate_position(self, param):
        self.__adjusted_aggregate_position = param

    @adjusted_aggregate_position.deleter
    def adjusted_aggregate_position(self):
        del self.__adjusted_aggregate_position

    @property
    def weighted_aggregate_position(self):
        return self.__weighted_aggregate_position

    @weighted_aggregate_position.setter
    def weighted_aggregate_position(self, param):
        self.__weighted_aggregate_position = param

    @weighted_aggregate_position.deleter
    def weighted_aggregate_position(self):
        del self.__weighted_aggregate_position

    @property
    def total_weighted_aggregate_position(self):
        return self.__total_weighted_aggregate_position

    @total_weighted_aggregate_position.setter
    def total_weighted_aggregate_position(self, param):
        self.__total_weighted_aggregate_position = param

    @total_weighted_aggregate_position.deleter
    def total_weighted_aggregate_position(self):
        del self.__total_weighted_aggregate_position

    @property
    def weighted_aggregate_position_percentage(self):
        return self.__weighted_aggregate_position_percentage

    @weighted_aggregate_position_percentage.setter
    def weighted_aggregate_position_percentage(self, param):
        self.__weighted_aggregate_position_percentage = param

    @weighted_aggregate_position_percentage.deleter
    def weighted_aggregate_position_percentage(self):
        del self.__weighted_aggregate_position_percentage

    @property
    def max_weighted_aggregate_position_percentage(self):
        return self.__max_weighted_aggregate_position_percentage

    @max_weighted_aggregate_position_percentage.setter
    def max_weighted_aggregate_position_percentage(self, param):
        self.__max_weighted_aggregate_position_percentage = param

    @max_weighted_aggregate_position_percentage.deleter
    def max_weighted_aggregate_position_percentage(self):
        del self.__max_weighted_aggregate_position_percentage

    @property
    def final_score(self):
        return self.__final_score

    @final_score.setter
    def final_score(self, param):
        self.__final_score = param

    @final_score.deleter
    def final_score(self):
        del self.__final_score

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
        self.update_all()
        if self.__responses == []:
            print(
                f"{type(self)}\nUpvotes: {self.gross_upvotes}\nDownvotes: {self.gross_downvotes}\nUnadjusted Net Position: {self.unadjusted_net_position}\nAdjusted Net Position: {self.adjusted_net_position}\nUnadjusted Aggregate Position: {self.unadjusted_aggregate_position}\nUpvote/Downvote Percentage: {self.upvote_downvote_percentage}\nAdjusted Aggregate Position: {self.adjusted_aggregate_position}\nTotal Upvote/Downvote Percentage: {self.total_upvote_downvote_percentage}\nWeight of Upvote/Downvote Percentage: {self.weight_of_upvote_downvote_percentage}\nWeighted Aggregate Position: {self.weighted_aggregate_position}\nTotal Weighted Aggregate Position: {self.total_weighted_aggregate_position}\nWeighted Aggregate Position Percentage: {self.weighted_aggregate_position_percentage}\nFinal Score: {self.final_score}\nCategory: {self.category}\nSubcategory: {self.subcategory}\nSubject: {self.subject}\nVerb: {self.verb}\nComplement: {self.complement}\nSentence: {self.subject} {self.verb} {self.complement}.\nResponses: None"
            )
        else:
            print(
                f"{type(self)}\nUpvotes: {self.gross_upvotes}\nDownvotes: {self.gross_downvotes}\nUnadjusted Net Position: {self.unadjusted_net_position}\nAdjusted Net Position: {self.adjusted_net_position}\nUnadjusted Aggregate Position: {self.unadjusted_aggregate_position}\nUpvote/Downvote Percentage: {self.upvote_downvote_percentage}\nAdjusted Aggregate Position: {self.adjusted_aggregate_position}\nTotal Upvote/Downvote Percentage: {self.total_upvote_downvote_percentage}\nWeight of Upvote/Downvote Percentage: {self.weight_of_upvote_downvote_percentage}\nWeighted Aggregate Position: {self.weighted_aggregate_position}\nTotal Weighted Aggregate Position: {self.total_weighted_aggregate_position}\nWeighted Aggregate Position Percentage: {self.weighted_aggregate_position_percentage}\nFinal Score: {self.final_score}\nCategory: {self.category}\nSubcategory: {self.subcategory}\nSubject: {self.subject}\nVerb: {self.verb}\nComplement: {self.complement}\nSentence: {self.subject} {self.verb} {self.complement}.\nResponses:\n"
            )
            self.print_responses()

    def print_responses(self):
        for response in self.responses:
            response.print_response()

    def add_response(self, response):
        self.responses.append(response)

    def upvote(self):
        self.gross_upvotes += 1
        self.update_unadjusted_net_position()

    def downvote(self):
        self.gross_downvotes += 1
        self.update_unadjusted_net_position()

    def update_unadjusted_net_position(self):
        if self.gross_downvotes == 0:
            self.upvote_downvote_percentage = self.gross_upvotes / 1
        else:
            self.upvote_downvote_percentage = self.gross_upvotes / self.gross_downvotes
        self.unadjusted_net_position = self.gross_upvotes - self.gross_downvotes
        if self.unadjusted_net_position <= 0:
            self.adjusted_net_position = 0
        else:
            self.adjusted_net_position = self.unadjusted_net_position
        self.unadjusted_aggregate_position = self.update_unadjusted_aggregate_position()
        self.update_adjusted_aggregate_position()
        self.total_upvote_downvote_percentage = self.update_total_vote_percentage()
        self.update_weight_of_upvote_downvote_percentage()
        self.update_weighted_aggregate_position()
        self.total_weighted_aggregate_position = self.update_total_weighted_position()
        self.weighted_aggregate_position_percentage = self.weighted_aggregate_position / self.total_weighted_aggregate_position
        self.update_max_weighted_aggregate_position_percentage()
        self.update_final_score()

    def update_unadjusted_aggregate_position(self):
        acc = 0
        for response in self.__responses:
            if response.polarity == 'support':
                acc += response.update_unadjusted_aggregate_position()
            elif response.polarity == 'negation':
                acc -= response.update_unadjusted_aggregate_position()
        return self.adjusted_net_position + acc

    def update_adjusted_aggregate_position(self):
        self.adjusted_aggregate_position = self.unadjusted_aggregate_position * self.upvote_downvote_percentage

    def update_total_vote_percentage(self):
        acc = 0
        for response in self.__responses:
            acc += response.update_total_vote_percentage()
        return self.upvote_downvote_percentage + acc

    def update_weight_of_upvote_downvote_percentage(self):
        self.weight_of_upvote_downvote_percentage = self.upvote_downvote_percentage / self.total_upvote_downvote_percentage

    def update_weighted_aggregate_position(self):
        self.weighted_aggregate_position = self.weight_of_upvote_downvote_percentage * self.adjusted_aggregate_position

    def update_total_weighted_position(self):
        acc = 0
        for response in self.__responses:
            acc += response.update_total_weighted_position()
        return self.weight_of_upvote_downvote_percentage + acc

    def update_max_weighted_aggregate_position_percentage(self):
        max = self.weighted_aggregate_position_percentage
        for response in self.responses:
            if response.weighted_aggregate_position_percentage > max:
                max = response.weighted_aggregate_position_percentage
        self.max_weighted_aggregate_position_percentage = max

    def update_final_score(self):
        self.final_score = round(self.weighted_aggregate_position_percentage / self.max_weighted_aggregate_position_percentage * 100, 1)

    def update_all(self):
        self.update_unadjusted_net_position()
        self.update_unadjusted_aggregate_position()
        self.update_adjusted_aggregate_position()
