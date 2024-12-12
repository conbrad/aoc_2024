import os
import re
  

def part_one(input: str):
    pattern = re.compile(r'mul\((\d+),(\d+)\)+')
    matches = pattern.findall(input)
    sum = 0
    for lhs, rhs in matches:
        sum += int(lhs) * int(rhs)
    return sum

def part_two(input: str):
    pattern = re.compile(r"((?:do\(\)|don't\(\)).*?)*mul\((\d+),(\d+)\)+")
    matches = pattern.findall(input)
    sum = 0
    enabled = True
    for cond, lhs, rhs in matches:
        if cond == '':
            # no-op
            enabled = enabled
        elif cond.startswith("do()"):
            enabled = True
        elif cond.startswith("don't()"):
            enabled = False
        
        if enabled:
            sum += int(lhs) * int(rhs)
    return sum            

if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), "day3input.txt"), "r") as f:
        
        input = f.read()
        output = part_two(input)
        print(output)
