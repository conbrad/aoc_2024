import os
def compute_distance(list1, list2):
    assert len(list1) == len(list2)
    total_distance = 0
    for x, y in zip(list1, list2):
        total_distance += abs(x - y)
    return total_distance

def compute_similarity(list1, list2):
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
    print(compute_distance(list1, list2))
    print(compute_similarity(list1, list2))

