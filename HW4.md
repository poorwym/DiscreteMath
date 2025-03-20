# HW4🚀
## Exercise 2.1
### 7
7. Determine whether each of these pairs of sets are equal.  
- a) ${1, 3, 3, 3, 5, 5, 5, 5, 5} = {5, 3, 1}$  
- b) ${{1}} = {1, {1}}$ 
- c) $\emptyset = {\emptyset}$

### answer

- a) T
- b) F
- c) T

---

### 12

12. Determine whether these statements are true or false.  
- a) $\emptyset \in \{\emptyset\}$
- b) $\emptyset \in \{\emptyset, \{\emptyset\}\}$
- c) $\{\emptyset\} \in \{\emptyset\}$
- d) $\{\emptyset\} \in \{\{\emptyset\}\}$
- e) $\{\emptyset\} \subset \{\emptyset,\{\emptyset\}\}$
- f ) $\{\{\emptyset\}\} \subset \{\emptyset,\{\emptyset\}\}$
- g) $\{\{\emptyset\}\} \subset \{\{\emptyset\},\{\emptyset\}\}$

### answer

- a) T
- b) T
- c) T
- d) T
- e) T
- f ) T
- g) T

---

### 27

27. Prove that $\mathcal{P}(A) \subseteq \mathcal{P}(B)$ if and only if $A \subseteq B$.
  
### answer
Pf:
$(\implies)$:(by contradiction)
we assume that $\mathcal{P}(A) \subseteq \mathcal{P}(B)$ but $A \not\subseteq B$.
then there must exist a element $e$ that $e \in A$ but $e \not\in B$.
By the definition of power set, then $e \in \mathcal{P}(A)$ but $e \not\in \mathcal{P}(B)$, which is contradictory to the assumption.
S0 $(\mathcal{P}(A) \subseteq \mathcal{P}(B)) \implies (A \subseteq B)$

$(\impliedby)$:
For any subset $S \subseteq A$, because $A \subseteq B$, so $S \subseteq B$.
By the definition of power set, if $S \in \mathcal{P}(A)$, and $S \in \mathcal{P}(B)$.
By the definition of subset, $\mathcal{P}(A) \subseteq \mathcal{P}(B)$

So $\mathcal{P}(A) \subseteq \mathcal{P}(B \iff A \subseteq B$.
Q.E.D

---

### 35

35.  Find $A^2$ if  
- a) $A = \{0, 1, 3\}$. 
- b) $A = \{1, 2, a, b\}$.
  
### answer

- a) $A^2 = \{(0,0), (0,1), (0,3), (1,0), (1,1), (1,3), (3,0), (3,1), (3,3)\}$
- b) $A^2 = \{(1,1), (1,2), (1,a), (1,b), (2,1), (2,2), (2,a), (2,b), (a,1), (a,2), (a,a), (a,b), (b,1), (b,2), (b,a), (b,b)\}$

---

### 39

39. How many different elements does $A^n$ have when $A$ has $m$ elements and $n$ is a positive integer?
  
### answer

$m^n$

---

### 42

42.  Explain why $(A \times B) \times (C \times D)$ and $A \times (B \times C) \times D$ are not the same.
  
### answer

we assume that:
- $A:\{1\}$
- $B:\{2\}$
- $C:\{3\}$
- $D:\{4\}$

$(A \times B) \times (C \times D) = \{ (1, 2)\} \times \{ (3, 4)\} = \{ ((1,2),(3,4))\}$

$A \times (B \times C) \times D = \{1\} \times \{(2,3)\} \times \{4\} = \{(1,(2,3),4)\}$

Therefore, $(A \times B) \times (C \times D)$ and $A \times (B \times C) \times D$ are not the same because their element structures are different. The former is a set containing ordered pairs where each element is itself an ordered pair; while the latter is a set containing ordered triples.

Q.E.D

---

## Exercise 2.2
20. Let $A$, $B$, and $C$ be sets. Show that 
- a) $(A \cup B) \subseteq (A \cup B \cup C)$. 
- b) $(A \cap B \cap C) \subseteq (A \cap B)$. 
- c) $(A \setminus B) \setminus C \subseteq A \setminus C$. 
- d) $(A \setminus C) \cap (C \setminus B) = \emptyset$.  
- e) $(B \setminus A) \cup (C \setminus A) = (B \cup C) \setminus A$.
  
### answer

- a) assume that $x \in A \cup B$.
then $x \in A$ or $x \in B$.
If $x \in A$, because $A \subset A \cup B \cup C$, so $x \in A \cup B \cup C$.
If $x \in B$, because $B \subset A \cup B \cup C$, so $x \in A \cup B \cup C$.
So by definition, $(A \cup B) \subseteq (A \cup B \cup C)$.

- b) 
If $x \in A \cap B \cap C$ , then $x \in A$ and $x \in B$ and $x \in C$.
then $x \in A$ and $x \in B$, then $x \in A \cap B$.
So by definition, $(A \cap B \cap C) \subseteq (A \cap B)$.
- c)
If $x \in (A \setminus B) \setminus C$, then $x \in A$ and $x \not\in B$ and $x \not\in C$. then $x \in A$ and $x \not\in C$, then $x \in A \setminus C$.
So by definition, $(A \setminus B) \setminus C \subseteq A \setminus C$
- d)
If $x \in A \setminus C$, then $x \in A$ and $x \not\in C$, then $x \not\in C$, then $x \in \overline{C}$.
If $x \in C \setminus B$, then $x \in C$ and $x \not\in B$, then $x \in C$.
So $x \in \overline{C} \cap C$, so $x \in \emptyset$.
then $(A \setminus B) \setminus C \subseteq A \setminus C$.
- e)
If $x \in (B \setminus A)$, then $x \in B$ and $x \not\in A$.
If $x \in (C \setminus A)$, then $x \in C$ and $x \not\in A$.
So if $x \in (B \setminus A) \cup (C \setminus A)$,  $x \in B$ or $x \in C$ and $x \not\in A$.
So $x \in (B \cup C) \setminus A$.
So by definition, $(B \setminus A) \cup (C \setminus A) = (B \cup C) \setminus A$.

---

### 37

37.  Prove or disprove that for all sets $A$, $B$, and $C$, we have 
- a) $A \times (B \setminus C) = (A \times B) \setminus (A \times C)$. 
- b) $\overline{A} \times \overline{(B \cup C)} = \overline{A \times (B \cup C)}$.
  
### answer

- a)
Pf:(by definition)
we assume that 
$$
\begin{align}
&A = \{a_1, a_2, ...,a_{n_a}\}\quad \notag\\
&B =\{b_1,b_2,...,b_{n_b}, e_1, e_2,...,e_n\}\quad \notag\\
&C =\{c_1,c_2,...,c_{n_c}, e_1, e_2,...,e_n\}  \notag\\
&(n_a, n_b, n_c, n = 0,1,2...)\notag \\
&(b_i \neq c_j \quad i=1,2,...n_b;j=1,2,...n_c) \notag
\end{align}
$$

For the left part:
$$
\begin{align}
B \setminus C &= {b_1,b_2,...b_{n_b}} \notag \\
A \times (B \setminus C) &= \{(a_i,b_j)\} \quad(i = 1,2,...n_a;j=1,2,...n_b) \notag \\
\end{align}
$$

For the right part:
$$
\begin{align}
    A \times B &= \{(a_i,b_j),(a_i,e_k)\} \quad(i = 1,2,...n_a;j=1,2,...n_b;k=1,2,...n) \notag \\
    A \times C &= \{(a_i,c_j),(a_i,e_k)\} \quad(i = 1,2,...n_a;j=1,2,...n_c;k=1,2,...n) \notag \\
    (A \times B) \setminus (A \times C) &= \{(a_i,b_j)\} \quad(i = 1,2,...n_a;j=1,2,...n_b) \notag \\
\end{align}
$$

So
$$
A \times (B \setminus C) = (A \times B) \setminus (A \times C)
$$

- b)
Dispf:
we assume $A = \{1\}$, $B = \{2\}$, $C = \{3\}$ and $U = \{1,2,3,(1,1),(1,2),(1,3)\}$
Then we have:
$$
\begin{align}
\overline{A} \times \overline{(B \cup C)} &= \{2,3\} \times \{1\} = \{(2,1), (3,1)\} \notag\\
\overline{A \times (B \cup C)} &= \overline{\{(1,2), (1,3)\}} = \{1,2,3,(1,1),(2,2),(2,3),(3,2),(3,3)\} \notag
\end{align}
$$

Therefore, $\overline{A} \times \overline{(B \cup C)} \neq \overline{A \times (B \cup C)}$, which disproves the statement.

---

### 47

∗ 47. Suppose that $A$, $B$, and $C$ are sets such that $A \oplus C = B \oplus C$. Must it be the case that $A = B$?
  
### answer

Pf:(by contradiction)
If there exist a $x$ that $x \in A$ but $x \not\in B$,
- case1: $x \in C$, then $x \not\in A \oplus C$, but $x \in B \oplus C$, which is contradictory to the premise $A \oplus C = B \oplus C$
- case2: $x \not\in C$, then $x \in A \oplus C$, but $x \not\in B \oplus C$, which is contradictory to the premise $A \oplus C = B \oplus C$

So there is no $x$ that that $x \in A$ but $x \not\in B$, so $A \subseteq B$.
In the same reason, there is no $x$ that $x \in B$ but $x \not\in A$, so $B \subseteq A$.
So $ A = B$

---

### 56

56. Find $\bigcup_{i=1}^{\infty} A_i$ and $\bigcap_{i=1}^{\infty} A_i$ if for every positive integer $i$,  
- a) $A_i = {i, i + 1, i + 2, \ldots}$.  
- b) $A_i = {0, i}$.  
- c) $A_i = (0, i)$, that is, the set of real numbers $x$ with $0 < x < i$.  
- d) $A_i = (i, \infty)$, that is, the set of real numbers $x$ with $x > i$.

### answer

- a) $\bigcup_{i=1}^{\infty} A_i = \{1,2,...\infty\}$, $\bigcap_{i=1}^{\infty} A_i = \emptyset$
- b) $\bigcup_{i=1}^{\infty} A_i = \{0,1,2,...\infty\}$, $\bigcap_{i=1}^{\infty} A_i = \{0\}$
- c) $\bigcup_{i=1}^{\infty} A_i =(0,\infty)$, $\bigcap_{i=1}^{\infty} A_i = (0,1)$
- d) $\bigcup_{i=1}^{\infty} A_i = (1,\infty)$, $\bigcap_{i=1}^{\infty} A_i = \emptyset$

### note
之前的错误答案：
- c) $\bigcup_{i=1}^{\infty} A_i = \{(0,\infty)\}$, $\bigcap_{i=1}^{\infty} A_i = \{(0,1)\}$
- d) $\bigcup_{i=1}^{\infty} A_i = \{(1,\infty)\}$, $\bigcap_{i=1}^{\infty} A_i = \{\emptyset\}$
题目中已经说明，$A_i = (0, i)$, that is, **the set of real numbers** $x$ with $0 < x < i$.
所以$(0,i)$本身就是一个集合。没必要在外面再套一个。

---

### 71

The Jaccard similarity $J(A, B)$ of the finite sets $A$ and $B$ is $J(A, B) = \frac{|A \cap B|}{|A \cup B|}$, with $J(\emptyset, \emptyset) = 1$. The Jaccard distance $d_J(A, B)$ between $A$ and $B$ equals $d_J(A, B) = 1 - J(A, B)$.

71. Find $J(A, B)$ and $d_J(A, B)$ for these pairs of sets. 
- a) $A = {1, 3, 5}$, $B = {2, 4, 6}$ 
- b) $A = {1, 2, 3, 4}$, $B = {3, 4, 5, 6}$ 
- c) $A = {1, 2, 3, 4, 5, 6}$, $B = {1, 2, 3, 4, 5, 6}$ 
- d) $A = {1}$, $B = {1, 2, 3, 4, 5, 6}$
  
### answer

- a) $0$,$1$
- b) $\frac{1}{3}$,$\frac{2}{3}$
- c) $1$,$0$
- d) $\frac{1}{6}$,$\frac{5}{6}$

---
