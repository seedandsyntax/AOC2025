import re
example_set: str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

actual_set: str = "9191906840-9191941337,7671-13230,2669677096-2669816099,2-12,229599-392092,48403409-48523311,96763-229430,1919163519-1919240770,74928-96389,638049-668065,34781-73835,736781-819688,831765539-831907263,5615884-5749554,14101091-14196519,7134383-7169141,413340-625418,849755289-849920418,7745350-7815119,16717-26267,4396832-4549887,87161544-87241541,4747436629-4747494891,335-549,867623-929630,53-77,1414-3089,940604-1043283,3444659-3500714,3629-7368,79-129,5488908-5597446,97922755-98097602,182-281,8336644992-8336729448,24-47,613-1077"

"""

approach 1st: 
- regex to get the range to check from.
- collect invalid ones and sum them up with a sum method of list.

Done with the range creation, now we need a boolean function that returns true for invalid conditions.

OH THE RANGE IS INCLUSIVE TOO! We just needed to add a plus one to make the range syntax include the ending integer included as well!
"""

def check_invalid(check_num: int) -> bool:
    """
    So we need to check half of the digits on left and right to be the same.
    This eliminates all the odd number of digits situations, even 999 was not shown as 'invalid'.
    let me iterate some invalid examples:
    -> 99 = 90 + 9
    -> 9191 = 9100 + 91
    -> 261261 = 261000 + 261
    ...

    we can get 'dddd' to reduce to 'dd00' by modulus?
    dddd % 100 = '00dd'!
    no we get the opposite end, wait I shall keep that latter part too.
    So if we did dddd - (dddd  % 100) => 'dd00', that does work, we just need to now make this for d+ situation.
    firstly, we need a way to count digits itself, does 'int' class has anything useful to use? let me look up...
    I don't see anything which can directly give us advantage in the class itself from basic documentation search.
    I would convert it back to string and simplify the checks.

    SUCCESS

    Part 2 makes the odd assumption revoked, we need to now remove that segment.
    The rule is more inclusive of patterns with "any repeating set of digits (2 or more than 2)"
    So I will remove the direct splicing too.

    There's only brute-force way I could think of as of now...
    There's an interesting example of `565656` which has 6565 oh wait I realised this isn't special case! lol, detection of such pair might require a way...
    But won't that be too much for brute-force? if it is then I shall search up a mathematical method for it...
    I had an oversight, the sequence is 565656 so there's 3 repetitions... this might be easy to brute-force...

    oh right, so my concern was wrongly put, all numbers in example range of 2121212118-2121212124 would had been true because there is "some" repeating digits... but they want to see sequence in entire number.
    I would simply keep slicing original to parts and compare...
    dry run:
    - 12345 => 1-2-3-4-5 (iteration == 1, digit_count == 5, digit_count % iteration = 0)
    - 12345 => 12-34-5 -----> auto rejection! (iteration == 2, digit_count == 5, digit_count % iteration = 1)
    - 12345 => 123-45 -----> auto rejection! (iteration == 3, digit_count == 5, digit_count % iteration = 2) ### WE SHOULD HALT HERE... I would put a condition for that too...
    - 12345 => 1234-5 -----> auto rejection! (iteration == 4, digit_count == 5, digit_count % iteration = 1)
    - 12345 => 12345 -----> auto rejection! (iteration == 5, digit_count == 5, digit_count % iteration = 0)

    this allowed 12 to pass, how?:
    - 12 => 1-2 (iteration == 1, digit_count == 2, digit_count % iteration = 0)
    - 12 => 12 (iteration == 2, digit_count == 2, digit_count % iteration = 0) ???

    wait, it accepts all the conditions below 3 digits! and rejects all beyond 3 digits, this is completely wrong...
    oh well, we might be doing it wrong, we are not allowing it to check and ending its trials before hand!

    partial success! however numbers like 446446 can't be matched!... implies that iterations perhaps end faster... let me check by targetting 446446...
    ```
    set_check: 0 iter: 1 digits: 6
    str_num[0: 1] str_num[1: 2]
    set_check: 1 iter: 1 digits: 6
    str_num[1: 2] str_num[2: 3]
    NUMBER:  446446
    set_check: 0 iter: 2 digits: 6
    str_num[0: 2] str_num[2: 4]
    ```
    as suspected, iteration ends before going to third let us allow it to go to the third.

    SUCCESS! WE GOT IT.
    This is taking a while because of string based brute-force... but after about 30 seconds of processing we get [REDACTED].
    """

    str_num: str = str(check_num)
    digit_count: int = len(str_num)
    for iteration in range (1, int(digit_count / 2) + 1): # for 446446 this will go range(1, 3, 1) but that is a problem! 3rd is not inclusive and hence we shall add a plus 1.
        print("NUMBER: ", check_num)
        seq_found_trigger: bool = True # assume the said sequence exists.
        # print(f"iter: {iteration} digits: {digit_count} int-digits:{int(digit_count/2)}")
        if int(digit_count / 2) < iteration:
            return False
        if digit_count % iteration != 0:
            continue
        for set_check in range(0, digit_count, iteration):
            if set_check + iteration * 2 > digit_count:
                break
            if str_num == '446446':
                print(f"set_check: {set_check} iter: {iteration} digits: {digit_count}")
                print(f"str_num[{set_check}: {set_check + iteration}] str_num[{set_check + iteration}: {set_check + iteration * 2}]")
            if str_num[set_check: set_check + iteration] != str_num[set_check + iteration: set_check + iteration * 2]:
                # print(f"{str_num[set_check: set_check + iteration]} ?= {str_num[set_check + iteration: set_check + iteration * 2]}")
                seq_found_trigger = False
                break # break the current iteration and turn the assumption for this iteration as false.
        if seq_found_trigger:
            print("invalid: ", check_num)
            return True

    return False

invalid_list: list = []

def sum_invalid(id_set: str) -> int:
    """
    Success on part 1 of this challenge!
    """
    list_of_ranges = [str_range_set.group().split('-') for str_range_set in re.finditer(r"\d+\-\d+", id_set)]
    for str_range_set in list_of_ranges:
        temp_list: list = [int(range_item) for range_item in str_range_set]
        temp_list.append(1)
        range_set: range = range(temp_list[0], temp_list[1]+1, temp_list[2])
        # print(range(temp_list[0], temp_list[0], temp_list[0]))
        invalid_list.extend([invalid for invalid in range_set if check_invalid(invalid)])
    print("Invalid ID's sum is: ", sum(invalid_list))
    return sum(invalid_list)

if __name__ == "__main__":
    sum_invalid(actual_set)
