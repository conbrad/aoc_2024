import os
def solve(list1, list2):
    assert len(list1) == len(list2)
    total_distance = 0
    for x, y in zip(list1, list2):
        total_distance += abs(x - y)
    return total_distance

if __name__ == "__main__":
    list1 = []
    list2 = []
    with open(os.path.join(os.path.dirname(__file__), "day1input.txt"), "r") as f:
        all_lines = f.readlines()
        for line in all_lines:
            x, y = line.split()
            list1.append(int(x))
            list2.append(int(y))

    list1.sort()
    list2.sort()
    print(solve(list1, list2))
