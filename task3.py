from pyswip import Prolog

# Initialize Prolog interpreter
prolog = Prolog()

# Define the KB
prolog.assertz("parent(jane, rigsby)")
prolog.assertz("parent(jane, lisbon)")
prolog.assertz("parent(jane, maggie)")
prolog.assertz("parent(grace, rigsby)")
prolog.assertz("parent(grace, lisbon)")
prolog.assertz("parent(grace, maggie)")
prolog.assertz("parent(abraham, jane)")
prolog.assertz("parent(mona, jane)")
prolog.assertz("parent(clancy, grace)")
prolog.assertz("parent(jacqueline, grace)")
prolog.assertz("sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \\= Y")

# Run queries and print results
print(list(prolog.query("sibling(rigsby, lisbon)")))
print(list(prolog.query("parent(jane, maggie)")))
print(list(prolog.query("sibling(maggie, lisbon)")))
print(list(prolog.query("sibling(X, Y)")))
