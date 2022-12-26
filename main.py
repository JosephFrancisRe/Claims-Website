import claim as c
import response as r

# CREATING INITIAL CLAIM
initial_claim = c.Claim('Derek Jeter', 'is', 'the greatest Yankee of all time', 'Sports', 'MLB')

# CREATING SECOND CLAIM
second_claim = c.Claim('Derek Jeter', 'is', 'bad at defense', 'Sports', 'MLB')

# CREATING THIRD CLAIM
third_claim = c.Claim('Defense', 'is', 'overrated', 'Sports', 'MLB')

# CREATING FOURTH CLAIM
fourth_claim = c.Claim('Derek Jeter', 'has', 'the highest career batting average of any Yankee', 'Sports', 'MLB')

# CREATING FIFTH CLAIM
fifth_claim = c.Claim('Derek Jeter', 'got', 'his hits by swinging softly to only ever get singles', 'Sports', 'MLB')

# CREATING SIXTH CLAIM
sixth_claim = c.Claim('Derek Jeter', 'infected', 'all of Hollywood with herpes', 'Sports', 'MLB')

# PROVIDING SECOND CLAIM AS RESPONSE TO INITIAL CLAIM
initial_claim.add_response(r.Response(claim = second_claim, polarity = 'negation', origin = initial_claim))

# PROVIDING THIRD CLAIM AS RESPONSE TO SECOND CLAIM
initial_claim.responses[0].add_response(r.Response(claim = third_claim, polarity = 'negation', origin = initial_claim.responses[0]))

# PROVIDING FOURTH CLAIM AS RESPONSE TO INITIAL CLAIM
initial_claim.add_response(r.Response(claim = fourth_claim, polarity = 'support', origin = initial_claim))

# PROVIDING FIFTH CLAIM AS RESPONSE TO FOURTH CLAIM
initial_claim.responses[1].add_response(r.Response(claim = fifth_claim, polarity = 'negation', origin = initial_claim.responses[1]))

# PROVIDING SIXTH CLAIM AS RESPONSE TO FOURTH CLAIM
initial_claim.responses[1].add_response(r.Response(claim = sixth_claim, polarity = 'negation', origin = initial_claim.responses[1]))

# 'Derek Jeter is the greatest Yankee of all time' votes
for i in range(10):
    initial_claim.upvote()

for i in range(5):
    initial_claim.downvote()

# 'Derek Jeter is bad at defense' votes
for i in range(15):
    initial_claim.responses[0].upvote()

for i in range(7):
    initial_claim.responses[0].downvote()

initial_claim.responses[0].irrelevancy_vote()

# 'Defense is overrated' votes
for i in range(9):
    initial_claim.responses[0].responses[0].upvote()

for i in range(4):
    initial_claim.responses[0].responses[0].downvote()

# 'Derek Jeter has the highest career batting average of any Yankee' votes
for i in range(8):
    initial_claim.responses[1].upvote()

for i in range(3):
    initial_claim.responses[1].downvote()

for i in range(2):
    initial_claim.responses[1].irrelevancy_vote()

# 'Derek Jeter got his hits by swinging softly to only ever get singles' votes
for i in range(2):
    initial_claim.responses[1].responses[0].upvote()

for i in range(4):
    initial_claim.responses[1].responses[0].downvote()

# 'Derek Jeter infected all of Hollywood with herpes' votes
for i in range(10):
    initial_claim.responses[1].responses[1].upvote()

for i in range(2):
    initial_claim.responses[1].responses[1].downvote()

for i in range(12):
    initial_claim.responses[1].responses[1].irrelevancy_vote()

initial_claim.print_claim()
