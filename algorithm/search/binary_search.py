import asyncio
from typing import List


def binary_search(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums)

    while lp < rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] == tar:
            return mid
        elif nums[mid] < tar:
            lp = mid + 1
        elif nums[mid] > tar:
            rp = mid

    return -1


async def test_case1():
    nums = [1, 2, 3]
    tar = 2

    res = binary_search(nums, tar)
    assert res == 1, res
    await asyncio.sleep(3)
    print("case1: PASS")


async def test_case2():
    nums = [1, 2, 3, 4]
    tar = 3

    res = binary_search(nums, tar)
    assert res == 2, res
    print("case2: PASS")


async def main():
    await asyncio.gather(
        test_case1(),
        test_case2(),
    )


if __name__ == "__main__":
    print("test start......")
    asyncio.run(main())
    print("test start......")
