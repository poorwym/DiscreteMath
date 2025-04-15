## Set
### subset

### Power Set
给定一个集合 $S$，$S$ 的幂集是 $S$ 的所有子集构成的集合。$S$ 的幂集记作 $\mathcal{P}(S)$。

### Ordered n-turple

有序 n 元组 $(a_1, a_2, \ldots, a_n)$ 是一个有序集合，其中 $a_1$ 是第一个元素，$a_2$ 是第二个元素，$\ldots$，$a_n$ 是第 $n$ 个元素。

### Cartesian Products
设有两个集合 A 和 B，它们的 笛卡尔积 记作：

$A \times B = \{ (a, b) \mid a \in A, b \in B \}$

意思是：从 A 中取一个元素，从 B 中取一个元素，组成一个有序对 $(a, b)$，把所有这样的有序对放在一起，就得到了 $A \times B$。

集合 $A_1, A_2, \ldots, A_n$ 的笛卡尔积，记作 $A_1 \times A_2 \times \cdots \times A_n$，是由所有有序 $n$ 元组 $(a_1, a_2, \ldots, a_n)$ 组成的集合，其中 $a_i \in A_i$，对于 $i = 1, 2, \ldots, n$。换句话说，$A_1 \times A_2 \times \cdots \times A_n = \{(a_1, a_2, \ldots, a_n) \mid a_i \in A_i，对于 i = 1, 2, \ldots, n\}$。

## function

如果 $f$ 是从集合 $A$ 到集合 $B$ 的函数，我们称 $A$ 是 $f$ 的定义域（domain），$B$ 是 $f$ 的陪域（codomain）。如果 $f(a) = b$，我们称 $b$ 是 $a$ 的像（image），$a$ 是 $b$ 的原像（preimage）。$f$ 的值域（range）或像（image）是 $A$ 中所有元素的像构成的集合。此外，如果 $f$ 是从 $A$ 到 $B$ 的函数，我们称 $f$ 将 $A$ 映射到 $B$。

设 $f_1$ 和 $f_2$ 是从集合 $A$ 到实数集 $\mathbb{R}$ 的函数。那么 $f_1 + f_2$ 和 $f_1 \cdot f_2$ 也是从 $A$ 到 $\mathbb{R}$ 的函数，对于所有 $x \in A$，它们定义为：
$(f_1 + f_2)(x) = f_1(x) + f_2(x)$，
$(f_1 \cdot f_2)(x) = f_1(x) \cdot f_2(x)$。

设 $f$ 是从集合 $A$ 到集合 $B$ 的函数，$S$ 是 $A$ 的子集。$S$ 在函数 $f$ 下的像是 $B$ 的一个子集，它由 $S$ 中元素的像组成。我们将 $S$ 的像记为 $f(S)$，所以 $f(S) = \{t \mid \exists s \in S (t = f(s))\}$。我们也使用简写 $\{f(s) \mid s \in S\}$ 来表示这个集合。


### one-to-one map (injection) 单射
**定义：**

一个函数 $f: A \to B$ 是单射，如果不同的输入映射到不同的输出，即：

$\forall a_1, a_2 \in A, \quad f(a_1) = f(a_2) \Rightarrow a_1 = a_2$

也就是说：
- 没有两个不同的元素在 $A$ 中被映射成 $B$ 中的同一个元素。

**图示理解：**

每个 $A$ 中的点只指向唯一的 $B$ 中的点，并且不会出现多个 $A$ 的元素指向同一个 $B$ 的点。

### onto map (surjection) 满射
**定义：**

一个函数 $f: A \to B$ 是满射，如果每个 $B$ 中的元素至少被某个 $A$ 中的元素映射到，即：

$\forall b \in B, \ \exists a \in A \quad \text{使得} \ f(a) = b$

也就是说：
- $B$ 中的每一个元素都有前像，函数的"覆盖范围"是整个集合 $B$。

**图示理解：**

$B$ 中没有"孤立"的点，每个点至少被 $A$ 中的某个点映射到。

### one-to-one correspondence (bijective) 双射
**定义：**

一个函数是双射，当它既是单射又是满射，即：

$\forall b \in B, \ \exists! a \in A \quad \text{使得} \ f(a) = b$
- "唯一存在"：每个 $B$ 中的元素被唯一一个 $A$ 中的元素映射到。
- 表示集合 $A$ 和 $B$ 大小一样（集合等势）。

**图示理解：**

一一对应，没有缺少也没有重复——完美配对。

### inverse function
设 $g$ 是从集合 $A$ 到集合 $B$ 的函数，$f$ 是从集合 $B$ 到集合 $C$ 的函数。函数 $f$ 和 $g$ 的复合，对于所有 $a \in A$ 记为 $f \circ g$，是从 $A$ 到 $C$ 的函数，定义为 $(f \circ g)(a) = f(g(a))$。

### graph of function 函数图像
设 $f$ 是从集合 $A$ 到集合 $B$ 的函数。函数 $f$ 的图像是有序对的集合 $\{(a, b) \mid a \in A \text{ 且 } f(a) = b\}$。

### Partial Function

**定义：**

偏函数(partial function) $f$ 从集合 $A$ 到集合 $B$ 是将 $A$ 的一个子集（称为 $f$ 的定义域）中的每个元素 $a$ 唯一地映射到 $B$ 中的元素 $b$。集合 $A$ 和 $B$ 分别称为 $f$ 的域（domain）和陪域（codomain）。

对于 $A$ 中不在 $f$ 定义域内的元素，我们称 $f$ 在这些元素上是未定义的。

当 $f$ 的定义域等于整个集合 $A$ 时，我们称 $f$ 为全函数（total function）。

## Cardinity
一个集合 $A$ 的基数（cardinality）是指它包含的元素个数，通常记作：

$|A| \quad \text{或} \quad \text{card}(A)$

如果存在从集合 $A$ 到集合 $B$ 的**单射函数**，则集合 $A$ 的基数小于或等于集合 $B$ 的基数，我们记作 $|A| \leq |B|$。此外，当 $|A| \leq |B|$ 且 $A$ 和 $B$ 具有不同的基数时，我们称集合 $A$ 的基数小于集合 $B$ 的基数，记作 $|A| < |B|$。

### Countable Sets(可数集合)

一个集合如果是**有限的**或者与**正整数集合具有相同的基数**，则称为可数集合（countable set）。不可数的集合称为不可数集合（uncountable set）。当一个无限集合 $S$ 是可数的，我们用 $\aleph_0$ 表示 $S$ 的基数（其中 $\aleph$ 是希伯来字母表的第一个字母 aleph）

#### Positive rational numbers are countable
#### Positive real number are uncountable

