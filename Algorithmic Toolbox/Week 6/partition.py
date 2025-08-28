def can_partition_into_three(values):
    from functools import lru_cache

    total = sum(values)
    if total % 3 != 0:
        return 0

    target = total // 3
    n = len(values)

    @lru_cache(maxsize=None)
    def dfs(used_mask, curr_sum, groups_left):
        if groups_left == 0:
            return used_mask == (1 << n) - 1  # all elements used

        if curr_sum == target:
            # one group completed, move to next group
            return dfs(used_mask, 0, groups_left - 1)

        for i in range(n):
            if not (used_mask & (1 << i)) and curr_sum + values[i] <= target:
                if dfs(used_mask | (1 << i), curr_sum + values[i], groups_left):
                    return True
        return False

    return 1 if dfs(0, 0, 3) else 0

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().split()))
    print(can_partition_into_three(values))