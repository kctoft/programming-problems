# Intuition

The problem "*Two Sum*" asks us to return the indicies of  the elements that equate to the sum of `target` from the given array, `nums`.

If we want to be clever we can find the complement.

Mathematically, `target = i + j` is the same as `target - i = j`. Therefore, if we have a table we can use to check if `j` exists, then we can answer quickly whether or not the sum pair exists in the array or not.

# Approach

1. **Brute Force** - use two loops to track the possible combinations that equal to the target and return those indicies
1. Use a **Hash Map** - create a hash table to store the elements using the keys as indicies and values as the element value. Calculate the complement by subtracting it from the target (e.g., `complement = target - nums[i]`).


# Code

## Method 1: Brute Force - Using two loops to iterate over the array

```java
//  brute force: using 2 loops
public int[] twoSum(int[] nums, int target) {
  // i & j are cursors for the two integers to sum up to the vaue of `target`
  for (int i = 0; i < nums.length; i++) { // start at idx = 0
    for (int j = i + 1; j < nums.length; j++) { // start at idx + 1
      if (nums[i] + nums[j] == target) {
        return new int[] {i, j};
      }
    }
  }
  return new int[] {};
}
```

# Algorithm Steps

## Hash Map

1. Create an empty hash table to store elements in their respective indices.
1. Iterate through the array from left to right (i.e. `0` to `nums.length`).
1. For each element `nums[i]`, calculate the `complement` by subtracting it from the `target` (e.g., `complement = target - nums[i]`).
1. Check if the complement exists in the hash table. If it does, we have found a solution and can return those indicies.
1. If the complement does not exist in the hash table, add the current element `nums[i]` to the hash table with its index as the value.
1. Repeat steps 3-5 until we find a solution or reach the end of the array.
1. If no solution is found, return an empty array or an appropriate indicator.

```java
public int[] twoSum(int[] nums, int target) {
  //  hash map: TC O(n)
  Map<Integer, Integer> res = new HashMap<>();
  for (int i = 0; i < nums.length; i++) {
    // calculate the complement for each element in the array
    int complement = target - nums[i];
    // check if we found a match & return those indicies
    if (res.containsKey(complement)) {
      return new int[] {res.get(complement), i};
    }

    res.put(nums[i], i); // add new element to the hash table
  }
  return new int[] {}; // no solution found
}
```

# Complexity

- **Time Compplexity**: `O(n^2)` since we need two loops (**Brute Force**)
- **Time Compplexity**: `O(n)` only requires one pass through the array (**Hash Map**)
<!-- <**!-- - **Space Complexity**: `O()` -->
