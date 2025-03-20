# HW6

## Exercise 3.1
### 15

15. Describe an algorithm that inserts an integer $x$ in the appropriate position into the list $a_1, a_2, \ldots, a_n$ of integers that are in increasing order.

```
if x < a[0]:
    insert(x, 0)
else if x > a[n]:
    insert(x, n)
for i := 1 to m:
    if a[i] <= x <= a[i+1]

```

---

### 29

29. Devise an algorithm that finds a mode in a list of nondecreasing integers. (Recall that a list of integers is nondecreasing if each term is at least as large as the preceding term.)

---

### 63

63. 
- a) Devise a greedy algorithm that determines the fewest lecture halls needed to accommodate $n$ talks given the starting and ending time for each talk. 
- b) Prove that your algorithm is optimal.

---

## Exercise 3.2

### 2

2. Determine whether each of these functions is $O(x^2)$.  
   a) $f(x) = 17x + 11$  
   b) $f(x) = x^2 + 1000$  
   c) $f(x) = x \log x$  
   d) $f(x) = x^4/2$  
   e) $f(x) = 2^x$  
   f) $f(x) = \lfloor x \rfloor \cdot \lceil x \rceil$

---

### 11

11. Show that $3x^4 + 1$ is $O(x^4/2)$ and $x^4/2$ is $O(3x^4 + 1)$.

---

### 17

17. Suppose that $f(x)$, $g(x)$, and $h(x)$ are functions such that $f(x)$ is $O(g(x))$ and $g(x)$ is $O(h(x))$. Show that $f(x)$ is $O(h(x))$.

---

### 25

25. Give as good a big-O estimate as possible for each of these functions.  
   a) $(n^2 + 8)(n + 1)$  
   b) $(n \log n + n^2)(n^3 + 2)$  
   c) $(n! + 2^n)(n^3 + \log(n^2 + 1))$

---

### 33

33. Show that if $f(x)$ and $g(x)$ are functions from the set of real numbers to the set of real numbers, then $f(x)$ is $\Theta(g(x))$ if and only if there are positive constants $k$, $C_1$, and $C_2$ such that $C_1|g(x)| \leq |f(x)| \leq C_2|g(x)|$ whenever $x > k$.

---

### 37

37. Explain what it means for a function to be $\Theta(1)$.

---

### 41

41. Suppose that $f(x)$ is $O(g(x))$, where $f$ and $g$ are increasing and unbounded functions. Show that $\log |f(x)|$ is $O(\log |g(x)|)$.

---

### 54

54. Show that $x^5y^3 + x^4y^4 + x^3y^5$ is $\Omega(x^3y^3)$.

---
