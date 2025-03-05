# n C r
# dataset_example = {"data": [1], "next": 2}


def combination(n: int, r: int):

    result = []
    stack = [{"data": [i], "next": i + 1} for i in range(n, 0, -1)]

    while stack:
        popped = stack.pop()

        cur_data, next = popped.values()

        if len(cur_data) == r:
            result.append(cur_data)
            continue

        # 거꾸로 stack에 넣어준다
        for i in range(n, next - 1, -1):
            stack.append({"data": cur_data + [i], "next": i + 1})

    return result


combination(5, 3)
