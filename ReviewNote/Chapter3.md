# Algorithm

## Searching Algorithm
### Linear Search
### Binary Search
## Sorting
### The Bubble Sort
### The Insert Sort
## Greedy Algorithm


## Big-O
### definition
设 $f$ 和 $g$ 是从整数集合或实数集合到实数集合的函数。我们称 $f(x)$ 是 $O(g(x))$ 如果存在常数 $C$ 和 $k$ 使得当 $x > k$ 时有 
$$|f(x)| \leq C|g(x)|$$[这读作"$f(x)$ 是 $g(x)$ 的大 O"]

### Theorem 1
设 $f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$，其中 $a_0, a_1, \ldots, a_{n-1}, a_n$ 是实数。则 $f(x)$ 是 $O(x^n)$。

### Theorem 2
 假设 $f_1(x)$ 是 $O(g_1(x))$ 且 $f_2(x)$ 是 $O(g_2(x))$。那么 $(f_1 + f_2)(x)$ 是 $O(g(x))$，其中 $g(x) = \max(|g_1(x)|, |g_2(x)|)$ 对所有 $x$ 成立。

### corollary 1

### Theorem 3
假设 $f_1(x)$ 是 $O(g_1(x))$ 且 $f_2(x)$ 是 $O(g_2(x))$。那么 $(f_1f_2)(x)$ 是 $O(g_1(x)g_2(x))$。

## Big-Omega and Big-Theta Notation
### definition
设 $f$ 和 $g$ 是从整数集合或实数集合到实数集合的函数。我们称 $f(x)$ 是 $\Omega(g(x))$ 如果存在正常数 $C$ 和常数 $k$ 使得当 $x > k$ 时有 
$$|f(x)| \geq C|g(x)|$$[这读作"$f(x)$ 是 $g(x)$ 的大 Omega"]

### definition
设 $f$ 和 $g$ 是从整数集合或实数集合到实数集合的函数。我们称 $f(x)$ 是 $\Theta(g(x))$ 
如果 $f(x)$ 是 $O(g(x))$ 且 $f(x)$ 是 $\Omega(g(x))$。当 $f(x)$ 是 $\Theta(g(x))$ 时，我们说 $f$ 是 $g(x)$ 的大 Theta，$f(x)$ 是 $g(x)$ 的阶(order)，且 $f(x)$ 和 $g(x)$ 是同阶(same order)的。
$$C_1|g(x)| \leq |f(x)| \leq C_2|g(x)|$$

### Theorem 4
设 $f(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$，其中 $a_0, a_1, \ldots, a_{n-1}, a_n$ 是实数且 $a_n \neq 0$。那么 $f(x)$ 是 $\Theta(x^n)$。

### Algorithmic Paradigm
“Algorithmic Paradigm（算法范式）” 是指设计和组织算法的基本思维框架或策略。它帮助我们系统性地解决各类问题。