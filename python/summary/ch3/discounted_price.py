shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]


def get_max_discounted_price(prices: list[int], coupons: list[int]):
    prices.sort(reverse=True)
    coupons.sort(reverse=True)
    prices_len = len(prices)
    coupons_len = len(coupons)
    sum = 0

    for i in range(prices_len):
        if i < coupons_len and coupons[i]:
            sum += prices[i] * ((100 - coupons[i]) / 100)
        else:
            sum += prices[i]

    return int(sum)


print(
    "정답 = 926000 / 현재 풀이 값 = ",
    get_max_discounted_price([30000, 2000, 1500000], [20, 40]),
)
print(
    "정답 = 485000 / 현재 풀이 값 = ",
    get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]),
)
print(
    "정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [])
)
print(
    "정답 = 1458000 / 현재 풀이 값 = ",
    get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]),
)
