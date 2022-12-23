import claim as c

a = c.Claim()
a.category = 'Sports'
a.subcategory = 'MLB'
a.subject = 'Derek Jeter'
a.verb = 'is'
a.complement = 'the greatest Yankee of all time'
a.print_claim()

b = c.Claim()
b.category = 'Sports'
b.subcategory = 'MLB'
b.subject = 'Derek Jeter'
b.verb = 'is'
b.complement = 'bad at defense'
b.print_claim()

a.provide_response(b)
a.print_claim()