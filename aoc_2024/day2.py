import os

def is_safe(reports: list[int]) -> bool:
    report_pairs = list(zip(reports, reports[1:]))
    pair_growth = []

    # Capture growth, returning false if growth differs by less than one or more than 3
    for (curr, next) in report_pairs:
        curr_growth = curr - next
        if abs(curr_growth) < 1 or abs(curr_growth) > 3:
            return False
        pair_growth.append(curr - next)

    # Check for increasing or decreasing growth invariants
    return all(x == 1 or x == 2 or x == 3 for x in pair_growth) or all(x == -1 or x == -2 or x == -3 for x in pair_growth)



if __name__ == "__main__":
    safe_count = 0
    with open(os.path.join(os.path.dirname(__file__), "day2input.txt"), "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            reports = [int(x) for x in line.split()]
            if is_safe(reports):
                safe_count+=1
        print(safe_count)
