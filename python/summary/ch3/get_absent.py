all = ["A", "B", "C", "D", "E"]
presents = ["A", "C", "D", "E"]


def get_absent_from_all(all, presents):
    hash_table = {key: True for key in all}
    answer = []

    for present in presents:
        del hash_table[present]

    for absent in hash_table.keys():
        answer.append(absent)

    return answer


print(f"absent : {get_absent_from_all(all, presents)}")
