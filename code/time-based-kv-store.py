class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If key exists, append to existing array
        if key in self.d:
            self.d[key].append((timestamp, value))

        # If key doesn't exist, create new array
        else:
            self.d[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""

        # Binary search
        # We want l to point to the element after that we are looking for
        # so that l - 1 is guarenteed to be
        # the closest value less than or equal to timestamp
        tl = self.d[key]
        l, r = 0, len(tl) - 1
        while l <= r:
            mid = (l + r) // 2
            pair = tl[mid]

            if pair[0] <= timestamp:
                l = mid + 1
            else:
                r = mid - 1

        # If l is 0, then the element does not exist
        return tl[l - 1][1] if l else ""
