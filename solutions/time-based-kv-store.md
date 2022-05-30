### Title

Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the `TimeMap` class:

* `TimeMap()` Initializes the object of the data structure.
* `void set(String key, String value, int timestamp)` Stores the key `key` with the value `value` at the given time `timestamp`.
* `String get(String key, int timestamp)` Returns a value such that `set` was called previously, with `timestamp_prev <= timestamp`. If there are multiple such values, it returns the value associated with the largest `timestamp_prev`. If there are no values, it returns `""`.

---

<details>
<summary><b>Hint for Optimal Solution</b></summary>
  
In this problem, a single key must be mapped to multiple values; use a HashMap linked to an array of these values. Since the timestamps are always increasing, use a binary search to find the proper timestamp. 

</details>

---
<details>
<summary><b>Optimal</b></summary>

At the core of this class is a HashMap, mapping each key to a set of values.

When looking up the key-values with a timestamp, it is not guarenteed that a given timestamp exists. Therefore a second HashMap to map timestamps to values will not work. 

However, since the timestamps called in `set()` are strictly increasingly, let's store these values as an array of tuples formatted as `(timestamp, value)`. This array will be sorted in increasing order, so a binary search can be used to identify the most recent timestamp. 

So, to write our set method, simply append this `(timestamp, value)` tuple to the array mapped to by `key`. If `key` does not exist, map it to a new array.

To write our get method, perform a binary search on the array mapped to by `key`. Search for the closest value less than or equal to `timestamp`. Finally, return the associated value.  

*Time: `O(1)`/`O(1)`/`O(log(n))`*
>Initialing and setting a value are both constant time operations, since we are only adding values to a HashMap or appending values to an array. Getting a value is logarithmic, since a binary search is performed. 

*Space: `O(n)`*
> One copy of each value is stored in the object.

```python
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
        if key not in self.d: return ""
  
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
```

---