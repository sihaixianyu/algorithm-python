import asyncio
from typing import List


def left_bound(nums: List[int], tar: int) -> int:
    lp, rp = 0, len(nums)

    while lp < rp:
        mid = lp + (rp - lp) // 2
        if nums[mid] >= tar:
            rp = mid
        else:
            lp = mid + 1

    return lp


async def test_case1():
    nums = [1, 2, 2, 3]
    tar = 2

    res = left_bound(nums, tar)
    assert res == 1, res
    print("case1: PASS")


async def test_case2():
    nums = [1, 2, 3, 4, 4]
    tar = 4

    res = left_bound(nums, tar)
    assert res == 3, res
    print("case2: PASS")


async def main():
    await asyncio.gather(
        test_case1(),
        test_case2(),
    )


if __name__ == "__main__":
    print("test start......")
    asyncio.run(main())
    print("test end......")
