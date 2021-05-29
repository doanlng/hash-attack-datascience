# hash-attack-datascience
Expanding upon a hash attacker in python from a school assignment, 
we have included a graph that shows how long it took for a brute force attack each password

The way we use it is: we choose passwords from a given dictionary in combination without repeats
Using itertools we create permutations of each password from a given list, hash it, and see if the hashes match
