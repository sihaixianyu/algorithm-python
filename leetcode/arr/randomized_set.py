from random import randint


class RandomizedSet:
    def __init__(self):
        self.vals = []
        self.val_to_idx = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False

        self.vals.append(val)
        self.val_to_idx[val] = len(self.vals) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False

        idx = self.val_to_idx[val]

        self.val_to_idx[self.vals[-1]] = idx
        del self.val_to_idx[val]

        self.vals[idx], self.vals[-1] = self.vals[-1], self.vals[idx]
        self.vals.pop()

        return True

    def getRandom(self) -> int:
        idx = randint(0, len(self.vals) - 1)
        return self.vals[idx]


if __name__ == "__main__":
    r = RandomizedSet()
    print(r.insert(1))
    print(r.remove(2))
    print(r.insert(2))
    print(r.getRandom())
    print(r.remove(1))
    print(r.insert(2))
    print(r.getRandom())
