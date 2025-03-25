# Autocomplete API – Word Extraction

### Note:
I implemented the extraction logic for version 1 (`v1`), but I was unable to complete the assignment due to a timeout error while accessing the API.

## Version 1 (Only Alphabets)

### Constraints:
- The API returns a maximum of **10 words** per query.
- The rate limit is **100 words per minute**.

### Algorithm:
1. **Querying Strategy:**  
   - We begin with `query = 'a'`. If the API returns exactly **10 words**, we analyze the common prefix between `results[0]` and `results[9]`, then compare it with the common prefix between `results[8]` and `results[9]`.  
   - If both prefixes match, it indicates that querying with just the common prefix would yield the same results. Instead, the next query should be `common prefix + the next letter in results[9]`.  
   - If the prefixes differ, we use `query = common prefix between results[8] and results[9]`, as this is lexicographically larger and may return additional words beyond those in the initial query.  

2. **Recursive Expansion:**  
   - A recursive loop iterates through characters, starting from the last character of the passed query string until all possible alphabetic combinations are exhausted.  
   - This approach optimizes the search process by reducing redundant queries while ensuring complete word coverage.  

3. **Rate Limiting:**  
   - A query counter and a time tracker are implemented to prevent exceeding the **100 words per minute** limit.  
   - If the function reaches **100 queries**, it pauses execution until the rate limit resets.  

---

## Version 2 (Alphabets + Numbers)
The same logic applies, but the loop range is adjusted to include numerical characters.

## Version 3 (Alphabets + Numbers + Special Characters)
This version extends the loop range further to handle special characters in addition to alphabets and numbers.

