import os

def check_growth(pair_growth: list[int]):
    # Check for increasing or decreasing growth invariants
    increasing = [x == 1 or x == 2 or x == 3 for x in pair_growth].count(True)
    decreasing = [x == -1 or x == -2 or x == -3 for x in pair_growth].count(True)

    return increasing == len(pair_growth) or decreasing == len(pair_growth)

def is_safe(reports: list[int]) -> bool:
    for i, _ in enumerate(reports):
        remove_step = reports[:i] + reports[i+1 :]
        report_pairs = list(zip(remove_step, remove_step[1:]))
        pair_growth = [curr - next for (curr, next) in report_pairs]
        if check_growth(pair_growth):
            return True



if __name__ == "__main__":
    safe_count = 0
    with open(os.path.join(os.path.dirname(__file__), "day2input.txt"), "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            reports = [int(x) for x in line.split()]
            if is_safe(reports):
                safe_count+=1
        print(safe_count)
