# Sum-of-Two-Numbers
>21 May 2021 06:54 PM

Ah yes of course - the legendary Two Sum :)

***Question: Given a list of numbers nums and a number k, return whether any two elements from the list add up to k. You may not use the same element twice***

Nice to meet you Mr. Two Sum

This is a question which is apparently very popular in interviews - in fact I think some of my friend's have actually got it in their preliminary assessments. 

I, obviously, started out with the brute force method because that's the only one that came to my mind. And even though it works it does hit the time limit exceeded problem again. 

The final solution, however, works in a simpler way. We initialise a set first. Then we iterate through the nums list and if "k-e" is in the set we return True and then keep adding e to the set. k-e is another way of hitting the target instead of using i+j.

Honestly took my head a bit to wrap around the problem.

I also learned that "in" checks for a list in O(n) while it checks for a set in O(1). Thus making this code more efficient.
