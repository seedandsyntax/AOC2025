# Introduction

- I thought of completing Advent of Code 2025 before the next one arrives this December.

## Day 1?

I did the day 1 in the 2025 time, but I only ever did them after which I didn't came back until now. I would solve them again after I solve the rest.

---

## Solving Day 2

- The problem wanted me to find invalid sets and send a sum of their values.
- Because I am using multi-line strings for this problem, I split each range of IDs possible from the input with regex and collect invalid formats into a separate list.

### Part 1

- Firstly, simply `continue` if the number of digits in a string of digits is an odd value.
- For even number of digits found, check first half of those digits being equal in value against the second half by:
        - Take out the first half by `usin % (10*n) == 0` where `n` is `len(usin) / 2`.

### Part 2

- The prior part wasn't general, and works only for entire digits, we need to now check for every possible repetition possible in the digits given.
- We increase the scope of the algorithm to check for every grouping possible. It is brute-force so it took about 30 seconds of execution to get the actual solution.

---

## Solving Day 3

- The problem here wants to find maximum Nth number of digits selected to create the largest digit, without shifting their positions relative to each other.

### Part 1

- This was sort of done with hard-coding the greedy logic, I wasn't concerned of scaling the solution at this point so I got it right.

### Part 2

- This one was tripping me, I had to look up threads on Reddit to get a final idea of what I actually should do. I went to implement what they did:
        - Create a sliced window to check from, taking `(len(input_digits_lenght) - N) + 1 - D` digits there initially.
                - Where `N` = no. of digits to choose, `D` total discarded digits so far.
        - Now check the highest from there, anything selected at the index (`idx`) shall mark all other, lesser indexes (`<idx`) within the sliced window to be discarded from selection.
                - Also keep a count of the discarded (`D`), increment for the amount discard with `D += idx`.
        - The traversal goes for the entire list of digits given to it, it is guaranteed to stop before any "out of index" error could be hit.

---
