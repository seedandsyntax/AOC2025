import re

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

def max_jolt(row: str, maximum_selected: int):
    length = len(row)
    chosen_positions = []

    for i in range(maximum_selected):
        if chosen_positions:
            start = chosen_positions[-1] + 1
        else:
            start = 0

        picks_left_after_this = maximum_selected - i - 1
        stop = length - picks_left_after_this

        window = row[start:stop]
        offset = window.index(max(window))
        chosen_positions.append(start + offset)
    total = 0
    for power, idx in enumerate(reversed(chosen_positions)):
        total += (10 ** power) * int(row[idx])
    return total


print("sample_inputs_list total for maximum_selected = 2: \t\t", sum(max_jolt(row, 2) for row in sample_inputs_list))
print("inputs_list total for maximum_selected = 2: \t\t\t", sum(max_jolt(row, 2) for row in inputs_list))
print("sample_inputs_list total for maximum_selected = 12: \t\t", sum(max_jolt(row, 12) for row in sample_inputs_list))
print("inputs_list total for maximum_selected = 12: \t\t\t", sum(max_jolt(row, 12) for row in inputs_list))

