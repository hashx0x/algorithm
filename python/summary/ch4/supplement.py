import heapq

# Q. 라면 공장에서는 하루에 밀가루를 1톤씩 사용합니다.
# 원래 밀가루를 공급받던 공장의 고장으로 앞으로 k일 이후에야 밀가루를 공급받을 수 있기 때문에 해외 공장에서 밀가루를 수입해야 합니다.
# 해외 공장에서는 향후 밀가루를 공급할 수 있는 날짜와 수량을 알려주었고,
# 라면 공장에서는 운송비를 줄이기 위해 최소한의 횟수로 밀가루를 공급받고 싶습니다.
# 현재 공장에 남아있는 밀가루 수량 stock, 밀
# 가루 공급 일정(dates)과 해당 시점에 공급 가능한 밀가루 수량(supplies),
# 원래 공장으로부터 공급받을 수 있는 시점 k가 주어질 때,
# 밀가루가 떨어지지 않고 공장을 운영하기 위해서 최소한 몇 번 해외 공장으로부터 밀가루를 공급받아야 하는지를 반환 하시오.

# dates[i]에는 i번째 공급 가능일이 들어있으며, supplies[i]에는 dates[i] 날짜에 공급 가능한 밀가루 수량이 들어 있습니다.

# ramen_stock = 4
# supply_dates = [4, 10, 15]
# supply_supplies = [20, 5, 10]
# supply_recover_k = 30

# stock = 0
# dates = [0, 20, 25]
# supplies = [20, 10, 15]
# k = 35

# stock = 0
# k = 100
# dates = [0, 10, 50]
# supplies = [20, 10, 100]


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    # dates 기준으로 계산후 남은 날수 보다 재고가 적으면 그날 가져와야한다,
    supply_idx = 0
    max_heap = []
    count = 0
    while stock < k:
        while supply_idx < len(supplies) and dates[supply_idx] <= stock:
            heapq.heappush(
                max_heap, supplies[supply_idx] * -1
            )  # 최대힙에 현재 보충 가능한 날짜의 공급량 추가
            supply_idx += 1

        if not max_heap:
            return "failed"

        stock += heapq.heappop(max_heap) * -1
        count += 1

    return count


print(
    get_minimum_count_of_overseas_supply(
        ramen_stock, supply_dates, supply_supplies, supply_recover_k
    )
)
print(
    "정답 = 2 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30),
)
print(
    "정답 = 4 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40),
)
print(
    "정답 = 1 / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11),
)

print(
    "정답 = ? / 현재 풀이 값 = ",
    get_minimum_count_of_overseas_supply(0, [0, 10, 50], [20, 10, 100], 100),
)
