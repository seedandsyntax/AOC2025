import re
"""
This day problem has a string of numbers, and we need to simply 
- Find largest 2 single digits.
- Combine them sequencially (giving higher place value to the first of the found numbers in the prior set.)
- Sum all the numbers up.

We will approach by taking the string value of the problem, in this case I will read it through the text file because this one has huge inputs.
Now I need to get a sample set as well... because checking before pure execution is better.
I shall go over the characters of pure digits twice, first to get the initial largest then a modified format of it which won't have the largest in its index.
wait, we will be storing the index anyways, we could try going through it once, store index of the largest, when a new, larger value arrives... wait.
we can:
- Assume starting to be largest.
- if another largest is found, update the index to pull value from, this is basic of what first search will get us.
- The second would simply not have the value that the first search got, but this doesn't matter to us, what matters is we get the remaining largest's index.
- It can be assumed as well that the second largest isn't the assumed first largest, 
  - so as the values of assumed get thrown away, we simply point the prior assumption to be the larger place value (because we are traversing left to right).
This makes sense let me do a little dry run:
- 81119 => 
  assume 8 is larger, initially, wait.. if is it were to be 91118, then our algorithm could return 19 instead of 91!
We need a better plan, it is true that the former assumption at the very beginning is true too, our algorithm is solid for the moments this wasn't true!
because this is an binary scenario, throwing a state check won't be a hassle, I will simply see if we falter for that situation, if we do we would loop back for the value...
wait, if 9 is largest in 91118, then we can also say that there can't be larger single digit number digit than this, it is impossible.
This implies that 9 will always be the starting position no matter the cost.
This indicates that perhaps, just maybe... we could turn the checking upside-down? I should try assuming that the larger place value digit is found first!
so in this case, it is safe to assume that the other one would be smaller...

wait what am I doing... I mean I could try these methods but I suppose I tunneled visioned, I should simply sort this in descending order and get... wait! That's a trap...
sorting kills the order! But this gives me a little out of box vision too, I could try prying away what I don't need from here, hmmm...
I was thinking of removing each unique digit one at a time, storing each unique one away until the string goes empty,
- our solution could be the last two unique taken out,
- but that is wrong too because it gets uniques where the solution is allowed to have duplicates.

I shall go back to what I was thinking, that is the way,
lets do the dry run again:
- 7239 =>
  assume 7 is larger placevalue digit, 2 is assumed to be smaller, 
  we go forward and find 3 > 2, so we just update lower place value.
  we go forward and find 9 > 3 as well as 9 > 7, so we update lower place value with a 9.
  as 7 < 3 and 7 < 2 we never updated 7.
but if we had 72399 =>
  we would now step to 9 >= 9 and 9 >= 7 as well, this updates 7 to be prior found 9 as well.
  this works! This seems to be how it is meant to be done.
This means there are cases:
- When checked number is smaller than both higher_place_value and lower_place_value, ignore.
- When checked number is smaller than higher_place_value but larger than lower_place_value, update lower_place_value to be the value checked.
- When checked number is larger than both higher_place_value and lower_place_value, update with higher_place_value = lower_place_value then lower_place_value = checked value.
- When checked number is larger than higher_place_value but smaller than lower_place_value, same as prior case, update with higher_place_value = lower_place_value then lower_place_value = checked value.

Welp we are off, we need 357 and got 287.
It looks like out output works for the first and last case but wait! we formulated exactly the largest possible in the else case we stated long ago.
But why did this failed? let me dry run again:
8119 =>
- assumed 8 and 1
- oh wait we are checking from the start! we should not!
- but that doesn't fixes the issue, so we shall continue
- the third place one triggers replacement of lower only, but there's barely any value of that...
- the last digit triggers lower to be 9 but also gives its value of 1 to higher, this is a bug we didn't want...
- this will be valid for scenarios when higher > lower but lower stumbles upon smth higher than both higher and lower.
- This mean the fix is within the case number 3, we assumed lower to be larger, and thus a replacement. I could add another if statement to ensure that doesn't happen.
Wait, I see this as a states problem, we could add a new case with side to it than nest more if statements inside.
so sub cases that will side adjacent with other cases will be:
- If higher > lower and we get digit > lower < higher, then lower = digit only!
- If higher < lower and we get digit > lower > higher, then we do what we were doing...
Hmmmm it seems to now give 81 instead of 89... it should update as per... wait... I didn't changed the checks' conditions.
Wow, so cutting one bug causes another now, we got an issue now with the 4th case. it should give 92 but gives 89

Ok, it is actually correct! the way the algorithm works gives us largest two digit numbers, but it is blind from totality of how there simply can be larger numbers.
This complicate things, it seems to be a completely alien to cases we got. 

wait... there might be a way? We are assuming higher to be "higher" because its weightage will be X10 than normal.
we should try to compare it as if the higher is actually, always 10 times, this splits the checks even further...

now the check will have higher compared with digit separately, where higher will ... wait this doesn't seems to work... 

I could also put a completely different if conditional where it will keep on checking if the digit, lower and higher after all the conditions could be replaced like this?
Yes, that seems plausible, wait hold up...

this condition is hit if lower > higher > digit, is this case covered? Is this true for all those one? apparently yes,
1231 =>
- 31 here must be highest, at the end the lower > higher > digit condition is hit: 3 > 2 > 1
our program simply ignores it, let me add that too.

I am losing track let me see if I described the ignored state like that:
> - When checked number is smaller than both higher_place_value and lower_place_value, ignore.
this translates to: digit < higher and digit < lower, but it does not speak about things in between.
I suppose all the rest of non-written cases could be ignored now... lets see.
Oh My text file itself had extra \n, that's why it could not do it.
The answer given out was 17250 but this isn't right, this implies that there are cases I must consider and not ignore!

We must work all the cases ever possible, hmmm:
- we got 3 states and 4 checks, we could conduct permutations through 4 checks:
placing all states in this order:
H <= L <= D 
H >= L <= D 
H <= L >= D 
H >= L >= D 

now we add more with swapping as well...

H <= L <= D 
H >= L <= D 
H <= L >= D 
H >= L >= D 

L <= H <= D 
L >= H <= D 
L <= H >= D 
L >= H >= D 

...

Do we really care about all of them? there's like (3 * 2 * 1) * 4 = 24 different if else checks I need to write for.
You know what, I will do it!

wait, this doesn't seems right, there are some ambiguous checks which I should simply ignore, reducing permutations from 24 to 12.
but then what values could possibly escape? let me check by a dry run:
2313241 =>
- 2 and 3 and 1 no update
- 2 and 3 and 3 update H = 3, L = 3
- 3 and 3 and 2 no update
- 3 and 3 and 4 update H = 3, L = 4
- 3 and 4 and 1 update H = 4, L = 1
- maximum is 41 here, seems fine.
231361 =>
- 2 and 3 and 1 no update
- 2 and 3 and 3 update H = 3, L = 3
- 3 and 3 and 6 update H = 3, L = 6
- 3 and 6 and 1 update H = 3, L = 6
........
oh I figured... it should be simpler then,
whenever higher > lower (but not equal or greater) then we ignore if lower > digit, else we just update lower = digit.
in latter situation where higher <= lower, we update both no matter if lower is less, large or equal to the digit, like H = L then L = D.

let me write that out too.
this is significantly trimmed out, and gives exact value as before, which means we got much optimal setting than our prior case check.
We are definitely missing a case then, or smth else, I should peek into those massive sets of data now.
those sets are super massive, let me try trimming then iterate upon smth:
5657323833536351353333363782336373322831333642333243533331333328332333353233285222557336315323313364
5 6 5 no update
5 6 7 update to 6 7
6 7 3 update to 7 3
...
skipping until 83...
7 3 8 update to 7 8
7 8 3 update to 8 3
...
skipping until 85...
8 5 8 update to 8 (this happened in the past which means it will be 8 8 8 check now)
8 8 8 update to 8 8 (the else if plays)
8 8 5 update to 8 5 (HIT, WE GOT WHAT CAUSED IT!)

The algorithm we got assumed that all the cases where H <= L, disregarding D would lead to H = L and then L = D 
This is wrong, in case of H >= L > D, we MUST ignore!
let me update that...

SUCCESS! part 1 done!

Oh well, part 2 now wants 12 of highest digits instead of two, can we generalize our learned knowledge?
I suppose we can think of a different way, in this scenario rather than 12 let us consider 4:

315323313364
check from back, we firstly get:
- 3364
- 1336 (drop 4 from set of [3, 3, 6, 4])
- 3136 (drop 1 from set of [1, 3, 3, 6], because it is less)
- 2336 (drop 1 from set of [3, 6, 3, 1] , because it is less)
- 3336 (drop 1 from set of [2, 6, 3, 1] , because it is less)
oh well, this is complicated now... wait if I consider this as list to drop lowest only from, then somehow it seems to work...
let me implement that now...
but wait, this ignores incoming digit to be checked as well, OH WAIT, just check for lowest among all of them, drop accordingly!
"""
inputs_list: list[str] = []
with open("./code-snippets/day3data.txt", 'r') as fr:
    inputs_list = fr.readlines()

inputs_list = [usin.rstrip('\n') for usin in inputs_list]

sample_inputs_list: list[str] = [
    "987654321111111",
    "811111111111119",
    "234234234234278",
    "818181911112111"
]

batteries_set_to_sum: list[int] = []
override_batt_set_to_sum: list[int] = []

for usin in inputs_list:
    higher_place_value: int = int(usin[0])
    lower_place_value: int = int(usin[1])
    for digit in usin[2:]:
        num_digit: int = int(digit)
        if (higher_place_value >= lower_place_value) and lower_place_value < num_digit:
            lower_place_value = num_digit
        elif (higher_place_value < lower_place_value):
            higher_place_value = lower_place_value
            lower_place_value = num_digit

    batteries_set_to_sum.append(higher_place_value * 10 + lower_place_value)

print(batteries_set_to_sum)
print(sum(batteries_set_to_sum))

for usin in sample_inputs_list:
    limit_of_set: int = 12
    temp_dropper_set: list[int] = [int(digit) for digit in list(usin[-limit_of_set:])]
    for digit in range(len(usin) - len(temp_dropper_set), -1, -1):
        temp_dropper_set.insert(0, int(usin[digit]))
        print(f"usin: {usin} => {temp_dropper_set}")
        idx_of_dropped_digit = -1 # assumed the last digit in dropped list, we will iterate from the back.
        for iter_digit in range(len(temp_dropper_set) -1 , 0, -1):
            if temp_dropper_set[idx_of_dropped_digit] > temp_dropper_set[iter_digit]:
                idx_of_dropped_digit = iter_digit
        temp_dropper_set.pop(idx_of_dropped_digit)
    batt_combo: str = "".join([str(digit) for digit in temp_dropper_set])
    override_batt_set_to_sum.append(int(batt_combo))
print(override_batt_set_to_sum)
print(sum(override_batt_set_to_sum))
