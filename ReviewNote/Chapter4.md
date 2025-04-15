# Number Theory and Cryptography
## mod and div
### division
如果 $a$ 和 $b$ 是整数且 $a \neq 0$，当存在整数 $c$ 使得 $b = ac$ 时（或等价地，如果 $\frac{b}{a}$ 是整数），我们说 $a$ 整除 $b$。当 $a$ 整除 $b$ 时，我们说 $a$ 是 $b$ 的因子或除数，而 $b$ 是 $a$ 的倍数。记号 $a \mid b$ 表示 $a$ 整除 $b$。我们用 $a \nmid b$ 表示 $a$ 不整除 $b$。

### div and mod
在除法算法给出的等式中，$d$ 称为除数(divisor)，$a$ 称为被除数(dividend)，$q$ 称为商(quotient)，$r$ 称为余数(remainder)。使用以下记号表示商和余数：$q = a \text{ div } d$，$r = a \text{ mod } d$。

### congruence(同余)
如果 $a$ 和 $b$ 是整数且 $m$ 是正整数，当 $m$ 整除 $a - b$ 时，我们说 $a$ 同余于 $b$ 模 $m$。我们用记号 $a \equiv b \pmod{m}$ 表示 $a$ **同余**于 $b$ 模 $m$。我们称 $a \equiv b \pmod{m}$ 为同余式，$m$ 为其模数。如果 $a$ 和 $b$ 不同余模 $m$，我们记作 $a \not\equiv b \pmod{m}$。

### Theorem
设 $a$ 和 $b$ 是整数，$m$ 是正整数。则 $a \equiv b \pmod{m}$ 当且仅当 $a \bmod m = b \bmod m$。

### Theorem
设 $m$ 是正整数。整数 $a$ 和 $b$ 对模数 $m$ 同余，当且仅当存在整数 $k$ 使得 $a = b + km$。

### Theorem
设 $m$ 是正整数。如果 $a \equiv b \pmod{m}$ 且 $c \equiv d \pmod{m}$，则 $a + c \equiv b + d \pmod{m}$ 且 $ac \equiv bd \pmod{m}$。

### Theorem
设 $b$ 是大于 1 的整数。如果 $n$ 是正整数，则它可以唯一地表示为如下形式：$n = a_kb^k + a_{k-1}b^{k-1} + \cdots + a_1b + a_0$，其中 $k$ 是非负整数，$a_0, a_1, \ldots, a_k$ 是小于 $b$ 的非负整数，且 $a_k \neq 0$。

#### definition 
定理1称为 $n$ 的 $b$ **进制展开**。$n$ 的 $b$ 进制展开记作 $(a_ka_{k-1} \cdots a_1a_0)_b$。例如，$(245)_8$ 表示 $2 \cdot 8^2 + 4 \cdot 8 + 5 = 165$。通常情况下，对于10进制展开，下标10会被省略，因为10进制（十进制）展开是表示整数最常用的方式。

### Fast Modular Exponentiation.
令 n 的二进制表示为：
$$
n = (a_{k-1}a_{k-2}\dots a_1a_0)_2
$$
那么：
$$
b^n \mod m = \prod_{i=0}^{k-1} \left( b^{2^i} \mod m \right)^{a_i}
$$
## Prime

### THE FUNDAMENTAL THEOREM OF ARITHMETIC
每个大于1的整数都可以唯一地表示为一个素数或多个素数的乘积，其中素因子按非递减顺序排列。

即对于任意整数 $n > 1$，存在唯一的素数序列 $p_1, p_2, \dots, p_k$ 满足:
$$n = p_1p_2\cdots p_k \quad \text{其中} \quad p_1 \leq p_2 \leq \cdots \leq p_k$$

## Greatest Common Divisors(GCD)
设 $a$ 和 $b$ 是整数且不全为零。最大的整数 $d$ 满足 $d \mid a$ 且 $d \mid b$ 称为 $a$ 和 $b$ 的最大公约数。$a$ 和 $b$ 的最大公约数记作 $\gcd(a,b)$。

## Least Common Multiples(LCM)
设 $a$ 和 $b$ 是正整数，$a$ 和 $b$ 的最小公倍数是能被 $a$ 和 $b$ 同时整除的最小正整数。$a$ 和 $b$ 的最小公倍数记作 $\text{lcm}(a,b)$。

### Theorem
设 $a$ 和 $b$ 是正整数，则 $ab = \gcd(a,b) \cdot \text{lcm}(a,b)$。

### Theorem
**裴蜀定理**
设 $a$ 和 $b$ 是正整数，则存在整数 $s$ 和 $t$ 使得 $\gcd(a,b) = sa + tb$。

### definition
如果 $a$ 和 $b$ 是正整数，则满足 $\gcd(a,b) = sa + tb$ 的整数 $s$ 和 $t$ 称为 $a$ 和 $b$ 的**裴蜀系数**（以18世纪法国数学家 Étienne Bézout 命名）。等式 $\gcd(a,b) = sa + tb$ 称为**裴蜀恒等式**。

### Theorem
设 $m$ 是正整数，$a$、$b$ 和 $c$ 是整数。如果 $ac \equiv bc \pmod{m}$ 且 $\gcd(c,m) = 1$，则 $a \equiv b \pmod{m}$。

## Solving Congruences
设 $a$ 和 $m$ 是互素的整数且 $m > 1$，则 $a$ 模 $m$ 的乘法逆元存在。此外，这个乘法逆元在模 $m$ 意义下是唯一的。（即存在唯一的小于 $m$ 的正整数 $\overline{a}$ 是 $a$ 模 $m$ 的乘法逆元，且 $a$ 模 $m$ 的任何其他乘法逆元都与 $\overline{a}$ 模 $m$ 同余。）

## The Chinese Remainder Theorem
### 中国剩余定理
设 $m_1, m_2, \ldots, m_n$ 是两两互素的大于1的正整数，$a_1, a_2, \ldots, a_n$ 是任意整数。那么同余方程组
$$
\begin{align}
x &\equiv a_1 \pmod{m_1}\\
x &\equiv a_2 \pmod{m_2}\\
&\vdots\\
x &\equiv a_n \pmod{m_n}
\end{align}
$$
有唯一解模 $m = m_1m_2 \cdots m_n$。（即存在一个解 $x$ 满足 $0 \leq x < m$，且所有其他解都与这个解模 $m$ 同余。）

Pf:
证明：为了建立这个定理，我们需要证明解存在且模 $m$ 唯一。我们将通过描述构造这个解的方法来证明解的存在；证明解模 $m$ 唯一是练习30。为了构造一个同时满足所有条件的解，首先令 $M_k = m/m_k$ 对于 $k = 1, 2, \ldots, n$。也就是说，$M_k$ 是除了 $m_k$ 以外所有模数的乘积。因为当 $i \neq k$ 时，$m_i$ 和 $m_k$ 没有大于1的公因子，所以 $\gcd(m_k, M_k) = 1$。因此，根据定理1，我们知道存在整数 $y_k$，它是 $M_k$ 模 $m_k$ 的逆元，使得 $M_k y_k \equiv 1 \pmod{m_k}$。

为了构造同时满足所有条件的解，形成和 $x = a_1 M_1 y_1 + a_2 M_2 y_2 + \cdots + a_n M_n y_n$。

我们现在将证明 $x$ 是一个同时满足所有条件的解。首先，注意到当 $j \neq k$ 时，$M_j \equiv 0 \pmod{m_k}$，所以这个和中除了第 $k$ 项以外的所有项模 $m_k$ 都同余于0。因为 $M_k y_k \equiv 1 \pmod{m_k}$，我们看到

$x \equiv a_k M_k y_k \equiv a_k \pmod{m_k}$

对于 $k = 1, 2, \ldots, n$。我们已经证明了 $x$ 是这 $n$ 个同余式的同时解。


## Fermat’s Little Theorem
如果 $p$ 是素数且 $a$ 是不能被 $p$ 整除的整数，则 $a^{p-1} \equiv 1 \pmod{p}$。此外，对于每个整数 $a$，我们有 $a^p \equiv a \pmod{p}$。

## Euler's Theorem
### 欧拉定理
如果 $\gcd(a, n) = 1$，则 $a^{\phi(n)} \equiv 1 \pmod{n}$，其中 $\phi(n)$ 是欧拉函数，表示小于等于 $n$ 且与 $n$ 互素的正整数的个数。
Pf:
证明：设 $R = \{r_1, r_2, \ldots, r_{\phi(n)}\}$ 是完全剩余系模 $n$ 中与 $n$ 互素的元素集合，即 $R$ 包含了所有小于 $n$ 且与 $n$ 互素的正整数。

考虑集合 $S = \{ar_1 \bmod n, ar_2 \bmod n, \ldots, ar_{\phi(n)} \bmod n\}$，其中 $a$ 是与 $n$ 互素的整数。**我们将证明 $S$ 与 $R$ 包含相同的元素（可能顺序不同）。**

首先，由于 $\gcd(a,n) = 1$ 且 $\gcd(r_i,n) = 1$，根据整除性质，我们有 $\gcd(ar_i,n) = 1$。因此 $S$ 中的每个元素都与 $n$ 互素。

其次，我们需要证明 $S$ 中的元素两两不同。假设存在 $i \neq j$ 使得 $ar_i \equiv ar_j \pmod{n}$。由于 $\gcd(a,n) = 1$，根据消去律，我们有 $r_i \equiv r_j \pmod{n}$，这与 $R$ 中元素两两不同矛盾。

因此，$S$ 包含 $\phi(n)$ 个与 $n$ 互素的不同剩余类，这意味着 $S$ 与 $R$ 包含相同的元素（可能顺序不同）。

现在，考虑以下乘积（$a$与$n$互素，所以可以随便乘）：
$$r_1 \cdot r_2 \cdot \ldots \cdot r_{\phi(n)} \equiv (ar_1) \cdot (ar_2) \cdot \ldots \cdot (ar_{\phi(n)}) \pmod{n}$$

右侧可以重写为：
$$a^{\phi(n)} \cdot r_1 \cdot r_2 \cdot \ldots \cdot r_{\phi(n)} \pmod{n}$$

由于两侧相等，且 $r_1 \cdot r_2 \cdot \ldots \cdot r_{\phi(n)}$ 与 $n$ 互素，我们可以消去它，得到：
$$a^{\phi(n)} \equiv 1 \pmod{n}$$

这就证明了欧拉定理。


#### 注意
欧拉定理是费马小定理的推广。当 $n = p$ 是素数时，$\phi(p) = p - 1$，此时欧拉定理即为费马小定理。

## Pseudoprimes（伪素数）

### definition
设 $b$ 是一个正整数。如果 $n$ 是一个合数，且 $b^{n-1} \equiv 1 \pmod{n}$，则称 $n$ 是以 $b$ 为底的伪素数。

### definition
如果一个合数 $n$ 满足对于所有与 $n$ 互素的正整数 $b$，都有 $b^{n-1} \equiv 1 \pmod{n}$，则称 $n$ 为 Carmichael 数。（这些数字以 Robert Carmichael 命名，他在二十世纪初期研究了这些数。）

## Cryptography

密码系统是一个五元组 $(P, C, K, \mathcal{E}, \mathcal{D})$，其中 $P$ 是明文字符串集合，$C$ 是密文字符串集合，$K$ 是密钥空间（所有可能密钥的集合），$\mathcal{E}$ 是加密函数集合，$\mathcal{D}$ 是解密函数集合。我们用 $E_k$ 表示 $\mathcal{E}$ 中对应于密钥 $k$ 的加密函数，用 $D_k$ 表示 $\mathcal{D}$ 中解密使用 $E_k$ 加密的密文的解密函数，即对于所有明文字符串 $p$，有 $D_k(E_k(p)) = p$。

### RSA
### RSA 密钥生成过程

步骤如下：
1. 选择两个大质数 $p$ 和 $q$（随机产生且保密）
2. 计算 $n = p \cdot q$，这就是模数
3. 计算欧拉函数 $\phi(n) = (p-1)(q-1)$
4. 选择一个整数 $e$，满足：
   - $1 < e < \phi(n)$
   - $\gcd(e, \phi(n)) = 1$
5. 计算 $d \equiv e^{-1} \pmod{\phi(n)}$，即 $e \cdot d \equiv 1 \pmod{\phi(n)}$

最终：
- 公钥：$(e, n)$
- 私钥：$(d, n)$

### 加密和解密过程

设明文为整数 $P$，要求 $P < n$

加密：
$$C = P^e \bmod n$$

解密：
$$P = C^d \bmod n$$

根据欧拉定理，有：
$$
(P^e)^d \equiv P^{ed} \equiv P \pmod{n}
$$
