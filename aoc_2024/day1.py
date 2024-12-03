import os
def part_one(list1, list2):
    # Returns the difference between elements across both lists
    assert len(list1) == len(list2)
    total_distance = 0
    for x, y in zip(list1, list2):
        total_distance += abs(x - y)
    return total_distance

def part_two(list1, list2):
    # Returns the similarity score of elements across both lists
    assert len(list1) == len(list2)
    location_counts = {}
    for y in list2:
        curr_count = location_counts.get(y, 0)
        location_counts[y] = curr_count + 1
    
    similarity_score = 0
    for x in list1:
        similarity_score += x * location_counts.get(x, 0)

    return similarity_score


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
    print(part_one(list1, list2))
    print(part_two(list1, list2))

