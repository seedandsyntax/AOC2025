# Day 1?

I did the day 1 in the 2025 time, but I only ever did them after which I didn't came back until now. I would solve them again after I solve the rest.

# Solving Day 2

- The problem wanted me to find invalid sets and send a sum of their values.
- Because I am using multi-line strings for this problem, I split each range of IDs possible from the input with regex and collect invalid formats into a separate list.

## Part 1

- Firstly, simply `continue` if the number of digits in a string of digits is an odd value.
- For even number of digits found, check first half of those digits being equal in value against the second half by:
        - Take out the first half by `usin % (10*n) == 0` where `n` is `len(usin) / 2`.

## Part 2

- The prior part wasn't general, and works only for entire digits, we need to now check for every possible repetition possible in the digits given.
- We increase the scope of the algorithm to check for every grouping possible. This one compares the ASCII values of the characters for comparisons.
