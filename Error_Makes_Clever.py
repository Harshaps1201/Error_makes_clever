class goa:
    name="blah"
    drink=""
    def party(self):
        print("Lets party")
    def beach(self):
        print("Enjoying the beach")

Ramesh= goa()
Suresh= goa()

Ramesh.party()
Ramesh.name="Ramesh"
Suresh.name="Suresh"
Ramesh.drink="Yes"
Suresh.drink="No"
print(Ramesh.name)
print("drink:",Ramesh.drink)
print(Suresh.name)
print("drink:",Suresh.drink)

Ramesh.party()
Suresh.beach()