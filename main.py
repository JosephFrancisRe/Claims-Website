import claim as c
import response as r

# CREATING INITIAL CLAIM
initial_claim = c.Claim('Derek Jeter', 'is', 'the greatest Yankee of all time', 'Sports', 'MLB')
initial_claim.upvote()

# CREATING SECOND CLAIM
second_claim = c.Claim('Derek Jeter', 'is', 'bad at defense', 'Sports', 'MLB')

# CREATING THIRD CLAIM
third_claim = c.Claim('Defense', 'is', 'overrated', 'Sports', 'MLB')

# PROVIDING SECOND CLAIM AS RESPONSE TO INITIAL CLAIM
initial_claim.provide_response(r.Response(second_claim, polarity = 'negation'))

# PROVIDING THIRD CLAIM AS RESPONSE TO SECOND CLAIM
initial_claim.responses[0].provide_response(r.Response(third_claim, polarity = 'negation'))

initial_claim.print_claim()