# HW6

## Exercise 3.1
### 15

15. Describe an algorithm that inserts an integer $x$ in the appropriate position into the list $a_1, a_2, \ldots, a_n$ of integers that are in increasing order.

Here's an algorithm to insert x into a sorted list:

1. If x is less than the first element (x < a[1]), insert x at the beginning
2. If x is greater than the last element (x > a[n]), insert x at the end
3. Otherwise, scan through the list from left to right:
   - For each position i from 1 to n-1:
   - If a[i] ≤ x ≤ a[i+1], insert x between a[i] and a[i+1]

---

### 29

29. Devise an algorithm that finds a mode in a list of nondecreasing integers. (Recall that a list of integers is nondecreasing if each term is at least as large as the preceding term.)

### answer

Since the list is nondecreasing, equal elements must be consecutive. We can find the mode by:

1. Initialize:
   - current_num = first element
   - current_count = 1 
   - max_count = 1
   - mode = first element

2. For each remaining element x:
   - If x equals current_num:
     - Increment current_count
     - If current_count > max_count:
       - Update max_count = current_count
       - Update mode = current_num
   - Else:
     - Set current_num = x
     - Reset current_count = 1

3. Return mode

This algorithm runs in O(n) time and uses O(1) extra space.

Q.E.D


---

### 63

63. 
- a) Devise a greedy algorithm that determines the fewest lecture halls needed to accommodate $n$ talks given the starting and ending time for each talk. 
- b) Prove that your algorithm is optimal.

### answer

a) The greedy algorithm is as follows:

1. Sort all lectures by start time
2. Maintain a priority queue Q storing the current end time of each lecture hall
3. For each lecture:
   - If Q is empty or the earliest end time in Q is greater than current lecture's start time:
     - Open a new lecture hall, add current lecture's end time to Q
   - Otherwise:
     - Remove the earliest ending hall from Q
     - Schedule current lecture in that hall
     - Update the hall's end time and add back to Q
4. The size of Q is the minimum number of lecture halls needed

b) Proof of optimality:

Suppose there exists a better solution using fewer halls. Then there must be some point in time where two overlapping lectures are scheduled in the same hall. This contradicts the constraint that each hall can only host one lecture at a time.

Therefore our greedy algorithm produces an optimal solution.

Q.E.D

---

## Exercise 3.2

### 2

2. Determine whether each of these functions is $O(x^2)$.  
- a) $f(x) = 17x + 11$  
- b) $f(x) = x^2 + 1000$  
- c) $f(x) = x \log x$  
- d) $f(x) = x^4/2$  
- e) $f(x) = 2^x$  
- f) $f(x) = \lfloor x \rfloor \cdot \lceil x \rceil$

### answer

- a) T
- b) T
- c) T
- d) T
- e) F
- f ) T

### note
原来的错误答案
- a) F
- b) T
- c) F
- d) F
- e) F
- f ) T
事实上忘记考虑了 $O(x)$ 和 $\Theta(x)$ 的区别

---

### 11

11. Show that $3x^4 + 1$ is $O(x^4/2)$ and $x^4/2$ is $O(3x^4 + 1)$.

### answer

$3x^4 + 1$ is $O(x^4/2)$:
$$
|3x^4 + 1| \leq 8|\frac{x^4}{2}| \quad \text{when} \ x \geq 1 
$$
$x^4/2$ is $O(3x^4 + 1)$:
$$
|\frac{x^4}{2}| \leq |3x^4+1| \quad \text{when} \ x \geq 0
$$

---

### 17

17. Suppose that $f(x)$, $g(x)$, and $h(x)$ are functions such that $f(x)$ is $O(g(x))$ and $g(x)$ is $O(h(x))$. Show that $f(x)$ is $O(h(x))$.

### answer

From $f(x)$ is $O(g(x))$, we know that there exist $C_1$ and $k_1$ that:
$$
|f(x)| \leq C_1|g(x)| \quad \text{when} \ x \geq k_1
$$
From $g(x)$ is $O(h(x))$, we know that there exist $C_2$ and $k_2$ that:
$$
|g(x)| \leq C_2|h(x)| \quad \text{when} \ x \geq k_2
$$

So
$$
|f(x)| \leq C_1C_2|h(x)| \quad \text{when} \ x \geq \max(k_1,k_2)
$$
So $f(x)$ is $O(h(x))$.

---

### 25

25. Give as good a big-O estimate as possible for each of these functions.  
- a) $(n^2 + 8)(n + 1)$  
- b) $(n \log n + n^2)(n^3 + 2)$  
- c) $(n! + 2^n)(n^3 + \log(n^2 + 1))$

### answer

- a) $O(n^3)$
- b) $O(n^5)$
- c) $O(n^3*n!)$

---

### 33

33. Show that if $f(x)$ and $g(x)$ are functions from the set of real numbers to the set of real numbers, then $f(x)$ is $\Theta(g(x))$ if and only if there are positive constants $k$, $C_1$, and $C_2$ such that $C_1|g(x)| \leq |f(x)| \leq C_2|g(x)|$ whenever $x > k$.

### answer

Pf: by definition:
$(\implies)$:
If $f(x)$ is $\Theta(g(x))$,then $f(x)$ is $O(g(x))$ and $f(x)$ is $\Omega(g(x))$
then there exists constants $C_1$, $C_2$, $k_1$, $k_2$,
$$
|f(x)| \leq C_1|g(x)| \quad \text{when} \ x \geq k_1    \\
|f(x)| \geq C_2|g(x)| \quad \text{when} \ x \geq k_2
$$
then $C_1|g(x)| \leq |f(x)| \leq C_2|g(x)|$ whenever $x > \max(k_1,k_2)$
$(\impliedby)$:
we know that $C_1|g(x)| \leq |f(x)| \leq C_2|g(x)|$ whenever $x > k$
then
$$
|f(x)| \geq C_1|g(x)| \quad \text{when} \ x > k
|f(x)| \leq C_2|g(x)| \quad \text{when} \ x > k
$$
so $f(x)$ is $O(g(x))$ and $f(x)$ is $\Omega(g(x))$
So $f(x)$ is $\Theta(g(x))$
Q.E.D

---

### 37

37. Explain what it means for a function to be $\Theta(1)$.

### answer

there exists constants $C_1$ and $k_1$ that:
$$
|f(x)| \leq C_1 \quad \text{when} \ x \geq k_1
$$
there exists constants $C_2$ and $k_2$ that:
$$
|f(x)| \geq C_2 \quad \text{when} \ x \geq k_2
$$

---

### 41

41. Suppose that $f(x)$ is $O(g(x))$, where $f$ and $g$ are increasing and unbounded functions. Show that $\log |f(x)|$ is $O(\log |g(x)|)$.

### answer

we know that there exists constants $C_1$ and $k_1$ that:
$$
|f(x)| \leq C_1|g(x)| \quad \text{when} \ x \geq k_1
$$
So
$$
\log|{f(x)}| \leq \log{(C_1|g(x)|)} \quad \text{when} \ x \geq k_1
$$
So
$$
\log|{f(x)}| \leq \log{|g(x)|} + \log C_1 \quad \text{when} \ x \geq k_1
$$
we know that $f$ and $g$ are increasing and unbounded functions, so we note $x_0$,$x_1$ that
$$
f(x) \geq 1 \quad \text{when} \ x \geq x_0 \\
g(x) \geq 1 \quad \text{when} \ x \geq x_1
$$

So
$$
|\log{f(x)}| \leq |\log{g(x)}| + |\log C_1| \quad \text{when} \ x \geq \max(k_1,x_0,x_1)
$$
because $g(x)$ is increasing and unbounded,
so it's obvious that there exists constants $C_2$ and $k_2$
$$
|\log{g(x)}| + |\log C_1| \leq C_2|\log{g(x)}| \quad \text{when} \ x \geq k_2
$$
So
$$
|\log{f(x)}| \leq C_2|\log{g(x)}| \quad \text{when} \ x \geq \max(k_1,k_2,x_1,x_2)
$$
So
$\log |f(x)|$ is $O(\log |g(x)|)$
Q.E.D

---

### 54

54. Show that $x^5y^3 + x^4y^4 + x^3y^5$ is $\Omega(x^3y^3)$.

### answer

we assume that $f(x) = y^3x^5 + y^4x^4 + y^5x^3 = x^3y^3(x^2 + xy + y^2)$,

then $x^3y^3(x^2 + xy + y^2) \geq 3x^3y^3$ when $x \geq 1$ and $y \geq 1$

So $x^5y^3 + x^4y^4 + x^3y^5$ is $\Omega(x^3y^3)$.
Q.E.D

---
