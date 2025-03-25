# Autocomplete API words extraction
Note: I have written the code for extraction from v1 version. I was unable to complete the assignment as there was a timeout error while accessing the API.

V1(only alphabets)
CONSTRAINTS:
->	The API only returns the first ten words for the respective query
->	The rate limit is 100 words per minute
ALGORITHM:
->	Starting from query=’a’ , if the count was 10 , I checked the common partial string between results[0] and results[9] and compared it with partial common string between results[8] and result[9].
->	If both are same , it means we have to check from the next query=common string+ the next letter in result[9] since the common string will return the same result as the initial query.
->	If both are not same, we check for the next query=common string  between result[8 and result[9] because this query is lexicographically higher which may return words more than those present in the result of initial query.
-> Under the recursion , we run a loop from the argument ‘char’( the last character of the passed string) till the exhaustion of alphabets.
->	This optimizes the search for the words such that we don’t have to check for every possible string and at the same time leaving no exceptions.
-> We add a query counter and a time counter to ensure that whenever the function reaches 100 calls, we wait till the rate limit refreshes to ensure proper implementation.

V2(numbers and alphabets): Probably the same logic with different loop range
V3(numbers,special characters,alphabets): Probably the same logic with different loop range

