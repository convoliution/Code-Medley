import numpy as np


nums = np.sort(np.random.permutation(24)[:12]).tolist()
target = np.random.choice(24)
print(f"find {target} in {nums} at index {nums.index(target) if target in nums else None}")

print([(i
        if found or i != l
        else None,
        bounds.append((l, i)
                      if nums[i] > target
                      else (i, r))
        if not found and i != l
        else None)[0]
       for bounds in [[(0, len(nums))]]
       for l, r in iter(bounds)
       for i in [(l+r)//2]
       for found in [nums[i] == target]])
