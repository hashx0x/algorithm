shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_existing_target_number_binary(target, array):
    index_max = len(array) - 1
    index_min = 0
    index_mid = (index_max - index_min) // 2

    if target == array[index_min] or target == array[index_max]:
        return True

    while index_min <= index_max:
        if target == array[index_mid]:
            return True
        if target < array[index_mid]:
            index_max = index_mid - 1
        elif target > array[index_mid]:
            index_min = index_mid + 1

        index_mid = (index_max + index_min) // 2

    return False


def is_possible_order(menus, orders):
    # dictionary 만들기, set 으로도 가능 -> 탐색시 O(1)
    shop_menus_dic = {key: True for key in shop_menus}
    print(f"shop menus : {shop_menus_dic}")

    for order_menu in shop_orders:
        if shop_menus_dic[order_menu] != True:
            return False
    return True


result = is_possible_order(shop_menus, shop_orders)
print(result)


# sol 2: 존재여부 -> 이진탐색
def is_possible_order_binary_search(menus, orders):
    # 이진탐색 위한 정렬
    menus.sort()

    for order in orders:
        if not is_existing_target_number_binary(order, menus):
            return False

    return True


print(f"bs result : {is_possible_order_binary_search(shop_menus, shop_orders)}")


# list로 dictionary 만들기
# 기본 문법 : my_dict = {key: {value가 될 값} for key in {keys}}
# keys = ['a', 'b', 'c']
# default_value = 0  # 모든 키의 기본값
# my_dict = {key: default_value for key in keys}
# print(my_dict)

# key, value 각 리스트로 dictionary 만들기
# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
# my_dict = {key: value for key, value in zip(keys, values)}
# print(my_dict)  # 출력: {'a': 1, 'b': 2, 'c': 3}
