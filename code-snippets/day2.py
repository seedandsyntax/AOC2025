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
    """
    temp_num: str = str(check_num)
    if len(temp_num) % 2 != 0:
        return False
    mid_way: int = int(len(temp_num) / 2)
    # print(f"{temp_num[0:mid_way] } ?= { temp_num[mid_way:]}")
    if temp_num[0:mid_way] == temp_num[mid_way:]:
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
