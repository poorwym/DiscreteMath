# HW3(part 1)
## Exercise 1.4
### 5

5. Let $P(x)$ be the statement "$x$ spends more than five hours every weekday in class," where the domain for $x$ consists of all students. Express each of these quantifications in English. 
- a) $\exists x P(x)$ 
- b) $\forall x P(x)$ 
- c) $\exists x \lnot P(x)$ 
- d) $\forall x \lnot P(x)$

### answer

- a) There exists a student that spends more than five hours every weekday in class.
- b) All students spend more than five hours every weekday in class.
- c) There exists a student that spends at most five hours every weekday in class.
- d) All students spend at most five hours every weekday in class.

### note

这里的 c 中 more than five hours 的否命题应该是 at most 5 hours 而不是 less than 5 hours.

---

### 8

8. Translate these statements into English, where $R(x)$ is "$x$ is a rabbit" and $H(x)$ is "$x$ hops" and the domain consists of all animals.  
- a) $\forall x(R(x) \implies H(x))$ 
- b) $\forall x(R(x) \land H(x))$ 
- c) $\exists x(R(x) \implies H(x))$ 
- d) $\exists x(R(x) \land H(x))$

### answer

- a) For all animals, if it's a rabbit, it hops.
- b) For all animals, it's a rabbit and it hops.
- c) There exists a animal that if it's a rabbit, it hops.
- d) There exists a animal that it'a rabbit and it hops.

---

### 12

12. Let $Q(x)$ be the statement "$x + 1 > 2x$." If the domain consists of all integers, what are these truth values? 
- a) $Q(0)$ 
- b) $Q(-1)$ 
- c) $Q(1)$  
- d) $\exists x Q(x)$ 
- e) $\forall x Q(x)$ 
- f ) $\exists x \lnot Q(x)$ 
- g) $\forall x \lnot Q(x)$

### answer

- a) T
- b) T
- c) F
- d) T
- e) F
- f ) T
- g) F

---

### 15

15. Determine the truth value of each of these statements if the domain for all variables consists of all integers. 
- a) $\forall n(n^2 \geq 0)$ 
- b) $\exists n(n^2 = 2)$ 
- c) $\forall n(n^2 \geq n)$ 
- d) $\exists n(n^2 < 0)$

### answer

- a) T
- b) F
- c) T
- d) F

### note 
the domain is **all intergers!**

---

### 19

19. Suppose that the domain of the propositional function $P(x)$ consists of the integers 1, 2, 3, 4, and 5. Express these statements without using quantifiers, instead using only negations($\neg$), disjunctions($\lor$), and conjunctions($\land$).  
- a) $\exists x P(x)$ 
- b) $\forall x P(x)$ 
- c) $\lnot \exists x P(x)$ 
- d) $\lnot \forall x P(x)$ 
- e) $\forall x((x \neq 3) \implies P(x)) \lor \exists x \lnot P(x)$

### answer

- a) $P(1)\lor P(2)\lor P(3)\lor P(4)\lor P(5)$
- b) $P(1)\land P(2)\land P(3)\land P(4)\land P(5)$
- c) $\neg P(1)\land \neg P(2)\land \neg P(3)\land \neg P(4)\land \neg P(5)$
- d) $\neg P(1)\lor \neg P(2)\lor \neg P(3)\lor \neg P(4)\lor \neg P(5)$
- e) $P(1)\land P(2)\land P(4)\land P(5)$

### note
e的错误回答：
- e) $P(1)\land P(2)\land \neg P(3)\land P(4)\land P(5)$
实际上 $x \neq 3$ 左侧恒真，不需要考虑$\lnot P(3)$

---

### 24

24. Translate in two ways each of these statements into logical expressions using predicates, quantifiers, and logical connectives. First, let the domain consist of the students in your class and second, let it consist of all people.  
- a) Everyone in your class has a cellular phone. 
- b) Somebody in your class has seen a foreign movie. 
- c) There is a person in your class who cannot swim. 
- d) All students in your class can solve quadratic equations. 
- e) Some student in your class does not want to be rich.


### answer

- a)

we assume that $P(x)$ means "$x$ has a cellular phone"
$C$ is the set of our class.
$$
\forall x \in C, P(x)
$$

- b)

we assume that $P(x)$ means "$x$ has seen a foreign movie"
$C$ is the set of our class.
$$
\exists x \in C, P(x)
$$

- c)

we assume that $P(x)$ means "$x$ can swim"
$C$ is the set of our class.
$$
\exists x \in C, \neg P(x)
$$

- d)

we assume that $P(x)$ means "$x$ can solve quadratic equations"
$C$ is the set of our class.
$$
\forall x \in C, P(x)
$$

- e)

we assume that $P(x)$ means "$x$ wants to be rich"
$C$ is the set of our class.
$$
\exists x \in C, \neg P(x)
$$

---

### 31

31. Suppose that the domain of $Q(x, y, z)$ consists of triples $x$, $y$, $z$, where $x = 0$, $1$, or $2$, $y = 0$ or $1$, and $z = 0$ or $1$. Write out these propositions using disjunctions and conjunctions.  
- a) $\forall y Q(0, y, 0)$ 
- b) $\exists x Q(x, 1, 1)$ 
- c) $\exists z \lnot Q(0, 0, z)$ 
- d) $\exists x \lnot Q(x, 0, 1)$

### answer

- a) $Q(0, 0, 0) \land Q(0, 1, 0)$
- b) $Q(0, 1, 1) \lor Q(1, 1, 1) \lor Q(2, 1, 1)$
- c) $\lnot Q(0, 0, 0) \lor \lnot Q(0, 0, 1)$
- d) $\lnot Q(0, 0, 1) \lor \lnot Q(1, 0, 1) \lor \lnot Q(2, 0, 1)$

---

### 36

36. Express the negation of each of these statements in terms of quantifiers without using the negation symbol. 
- a) $\forall x(-2 < x < 3)$ 
- b) $\forall x(0 \leq x < 5)$ 
- c) $\exists x(-4 \leq x \leq 1)$ 
- d) $\exists x(-5 < x < -1)$

### answer

- a) $\exists x ((x \leq -2) \lor ( x \geq 3))$ 
- b) $\exists x((x < 0) \lor (x \geq 5))$ 
- c) $\forall x((x < -4) \lor (x > 1))$
- d) $\forall x((x \leq -5) \lor (x \geq -1))$

### note

注意最外层的括号避免歧义

---

### 38

38. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all real numbers. 
- a) $\forall x(x^2 \neq x)$ 
- b) $\forall x(x^2 \neq 2)$ 
- c) $\forall x(|x| > 0)$

### answer

- a) $x=1$
- b) $x=\sqrt{2}$
- c) $x=0$

---

### 46

46. Determine whether $\forall x(P(x) \iff Q(x))$ and $\forall x P(x) \iff \forall x Q(x)$ are logically equivalent. Justify your answer.

### answer

These statements are not logically equivalent. I will provide a counterexample to demonstrate this.

Let's consider a domain with two elements: $X = \{a, b\}$
Define $P$ and $Q$ as follows:
- $P(a) = true$, $P(b) = false$
- $Q(a) = false$, $Q(b) = true$

For the first statement: $\forall x(P(x) \iff Q(x))$
- For $x = a$: $P(a) \iff Q(a)$ is $true \iff false$, which is false
- For $x = b$: $P(b) \iff Q(b)$ is $false \iff true$, which is false
Therefore, $\forall x(P(x) \iff Q(x))$ is false.

For the second statement: $\forall x P(x) \iff \forall x Q(x)$
- $\forall x P(x)$ is false (since $P(b)$ is false)
- $\forall x Q(x)$ is false (since $Q(a)$ is false)
Therefore, $\forall x P(x) \iff \forall x Q(x)$ is $false \iff false$, which is true.

Since we found a case where one statement is true and the other is false, they are not logically equivalent.

### note

#### 好好学习学习，这个ai给的证明。

---

### 49

49. Establish these logical equivalences, where $x$ does not occur as a free variable in $A$. Assume that the domain is nonempty.  
- a) $(\forall x P(x)) \land A \equiv \forall x(P(x) \land A)$ 
- b) $(\exists x P(x)) \land A \equiv \exists x(P(x) \land A)$

### answer

Note the domain of $x$ as $X$

- a)
($\implies$):
we assume $(\forall x P(x)) \land A$ is true.
For any $x \in X$ $A$ is true and $P(x)$ is true
then $A \land P(x)$ is true.
So for any $x \in X$, $\forall x(P(x) \land A)$ is true.
So $(\forall x P(x)) \land A \implies \forall x(P(x) \land A)$
($\impliedby$):
we assume that $\forall x (P(x) \land A)$ is true.
then for any $x \in X$, $P(x) \land A$ is true.
then $P(x)$ is true and $A$ is true.
So for any $x \in X$, $P(x)$ is true and $A$ is true.
So $(\forall x P(x)) \land A$ is true
So $(\forall x P(x)) \land A \impliedby \forall x(P(x) \land A)$ 
So
$$
(\forall x P(x)) \land A \iff \forall x(P(x) \land A)
$$
So
$$
(\forall x P(x)) \land A \equiv \forall x(P(x) \land A)
$$

- b)
($\implies$):
we assume $(\exists x P(x)) \land A$ is true.
then there exists $x \in X$ such that $P(x)$ is true and $A$ is true.
then there exists $x \in X$ such that $P(x) \land A$ is true.
So $\exists x(P(x) \land A)$ is true.
So $(\exists x P(x)) \land A \implies \exists x(P(x) \land A)$
($\impliedby$):
we assume that $\exists x(P(x) \land A)$ is true.
then there exists $x \in X$ such that $P(x) \land A$ is true.
then there exists $x \in X$ such that $P(x)$ is true and $A$ is true.
So $(\exists x P(x)) \land A$ is true.
So $(\exists x P(x)) \land A \impliedby \exists x(P(x) \land A)$
So
$$
(\exists x P(x)) \land A \iff \exists x(P(x) \land A)
$$
So
$$
(\exists x P(x)) \land A \equiv \exists x(P(x) \land A)
$$


---

### 53

53. Show that $\exists x P(x) \land \exists x Q(x)$ and $\exists x(P(x) \land Q(x))$ are not logically equivalent.

### answer

Pf: by case

Assume that $P(x)$ is $x > 0$, $Q(x)$ is $x < 0$
It's obvious that there exists a $x_1$ that $x_1 < 0$ and there exists another $x_2$ that $x_2>0$.
But there exist no $x_3$ that $(x_3 > 0) \land (x_3 < 0)$

---

### 60

60. Suppose that Prolog facts are used to define the predicates mother($M$, $Y$) and father($F$, $X$), which represent that $M$ is the mother of $Y$ and $F$ is the father of $X$, respectively. Give a Prolog rule to define the predicate grandfather($X$, $Y$), which represents that $X$ is the grandfather of $Y$. [Hint: You can write a disjunction in Prolog either by using a semicolon to separate predicates or by putting these predicates on separate lines.]

### answer

grandfather($X$, $Y$) :- father($X$, $Z$), father($Z$, $Y$).
grandfather($X$, $Y$) :- father($X$, $Z$), mother($Z$, $Y$).

---

### 63

63. Let $P(x)$, $Q(x)$, $R(x)$, and $S(x)$ be the statements "$x$ is a baby," "$x$ is logical," "$x$ is able to manage a crocodile," and "$x$ is despised," respectively. Suppose that the domain consists of all people. Express each of these statements using quantifiers; logical connectives; and$P(x)$, $Q(x)$, $R(x)$, and $S(x)$. 
- a) Babies are illogical.  
- b) Nobody is despised who can manage a crocodile.  
- c) Illogical persons are despised.  
- d) Babies cannot manage crocodiles.  
-∗ e) Does (d) follow from (a), (b), and (c)? If not, is there a correct conclusion?

### answer
- a) $\forall x(P(x) \implies \lnot Q(x))$
- b) $\forall x(R(x) \implies \lnot S(x))$
- c) $\forall x(\lnot Q(x) \implies S(x))$
- d) $\forall x(P(x) \implies \lnot R(x))$

- e)
$$
\forall x(R(x) \implies \lnot S(x)) \equiv \forall x(S(x) \implies \lnot R(x)) \\
\forall x((P(x) \implies \lnot Q(x)) \land (\lnot Q(x) \implies S(x)) \land (S(x) \implies \lnot R(x))) \implies \forall x (P(x) \implies \lnot R(x))
$$

So (d) follow from (a), (b), and (c).

---

## Exercise 1.5

4. Let $P(x, y)$ be the statement "Student $x$ has taken class $y$," where the domain for $x$ consists of all students in your class and for $y$ consists of all computer science courses at your school. Express each of these quantifications in English.  
- a) $\exists x \exists y P(x, y)$ 
- b) $\exists x \forall y P(x, y)$  
- c) $\forall x \exists y P(x, y)$ 
- d) $\exists y \forall x P(x, y)$  
- e) $\forall y \exists x P(x, y)$ 
- f ) $\forall x \forall y P(x, y)$

### answer

- a) There exists a student and a class that the student has taken that class.
- b) There exists a student that takes all classes.
- c) Every student takes at least one cs course.
- d) There exists a class that all students take it.
- e) For every classes, at least one student take it.
- f ) For all students, every student take all classes.

### note

这里要注意英语翻译的问题，
原来错误答案：
- c) For all students, there exists a class that everyone takes it.
这里容易引起歧义，容易被理解为“存在一门课，所有学生都选修了”。
实际上应该是，“对于每个学生，存在至少一门计算机科学课程，该学生已经选修了它。”

---

### 8

8. Let $Q(x, y)$ be the statement "Student $x$ has been a contestant on quiz show $y$." Express each of these sentences in terms of $Q(x, y)$, quantifiers, and logical connectives, where the domain for $x$ consists of all students at your school and for $y$ consists of all quiz shows on television. 
- a) There is a student at your school who has been a contestant on a television quiz show. 
- b) No student at your school has ever been a contestant on a television quiz show. 
- c) There is a student at your school who has been a contestant on Jeopardy! and on Wheel of Fortune. 
- d) Every television quiz show has had a student from your school as a contestant. 
- e) At least two students from your school have been contestants on Jeopardy!.

### answer

- a) $\exists x \exists y Q(x,y)$
- b) $\forall x \forall y\lnot Q(x,y)$
- c) $\exists x (Q(x,Jeopardy!) \land Q(x,Wheel of Fortune))$
- d) $\forall y \exists x Q(x,y)$
- e) $\exists x_1,x_2 (x_1 \neq x_2) \land Q(x_1,Jeopardy!) \land Q(x_2,Jeopardy!)$

---

### 18

18. Express each of these system specifications using predicates, quantifiers, and logical connectives, if necessary. 

- a) At least one console must be accessible during every fault condition.
- b) The e-mail address of every user can be retrieved whenever the archive contains at least one message sent by every user on the system. 
- c) For every security breach there is at least one mechanism that can detect that breach if and only if there is a process that has not been compromised. 
- d) There are at least two paths connecting every two distinct endpoints on the network. 
- e) No one knows the password of every user on the system except for the system administrator, who knows all passwords.

### answer

- a) let $P(x,y)$ be the statement that $x$ console can be accessible during fault condition $y$.
$$
\forall y \exists x P(x,y)
$$

- b) let $P(x)$ be the statement that the email address of $x$ can be retrieved, $Q(y,z)$ be the statement that archive contains message $y$ sent by user $z$ on the system.
$$
\forall x(\exists y \forall z Q(y,z) \implies P(x))
$$

- c) let $P(x)$ be the statement that process $x$ has not been compromised, $Q(y,z)$ be the statement that mechanism $y$ can detect breach $z$, and $B(z)$ be the statement that $z$ is a security breach.
$$
\forall z (B(z) \implies (\exists y Q(y,z) \iff \exists x P(x)))
$$

- d) let $P(x,y_1,y_2)$ be the statement that endpoint $y_1$,$y_2$ can be connected by path $x$.
$$
\exists x_1,x_2 (x_1 \neq x_2) \land (\forall y_1 \forall y_2(y_1 \neq y_2 \implies P(x_1,y_1,y_2) \land P(x_2,y_1,y_2)))
$$

- e)
let $P(x_1,x_2)$ be the statement that user $x_1$ know the password of user $x_2$. $Q(x)$ be the statement that user $x$ is the administrator.
$$
\forall x_1((Q(x_1) \iff \forall x_2 P(x_1,x_2)))
$$

### note:
原来的错误答案：
- a):$\exists x \forall y P(x,y)$
$\forall y$ 和 $\exist x$ 的顺序很重要。

- c):
  $\forall z \exists y(B(z) \implies (Q(y,z) \iff \exists x P(x)))$
  说实话我感觉原来的写法没啥毛病，但是为了表意更加清楚，建议改为
  $\forall z (B(z) \implies (\exists y Q(y,z) \iff \exists x P(x)))$


- e):
最好改成$\forall x\Bigl((\lnot Q(x)\implies \exists y\,\lnot P(x,y))\land (Q(x)\implies \forall y\, P(x,y))\Bigr)$。
虽然逻辑上等价，但是表达意思更清楚。

---

### 25

25. Translate each of these nested quantifications into an English statement that expresses a mathematical fact. The domain in each case consists of all real numbers. 
- a) $\exists x \forall y(xy = y)$  
- b) $\forall x \forall y(((x < 0) \land (y < 0)) \implies (xy > 0))$ 
- c) $\exists x \exists y((x^2 > y) \land (x < y))$ 
- d) $\forall x \forall y \exists z(x + y = z)$

### answer

- a) There exists a real number $x$ that for all real numbers, for all real number $y$ , $xy = y$.
- b) For any real number $x$ and $y$, if $x<0$ and $y<0$, then $xy>0$ .
- c) For all real numbers, there exists two real numbers which can be equal to each otehr, $x^2>y$ and $x<y$.
- d) For any real numbers $x$ and $y$, there exists a real number $z$ that $x + y = z$.

### note

英语表达中量词的语序很重要。forall和exist的顺序一定要和命题中一模一样。

---

### 33

33. Rewrite each of these statements so that negations appear only within predicates (that is, so that no negation is outside a quantifier or an expression involving logical connectives).  
- a) $\lnot \forall x \forall y P(x, y)$ 
- b) $\lnot \forall y \exists x P(x, y)$ 
- c) $\lnot \forall y \forall x(P(x, y) \lor Q(x, y))$ 
- d) $\lnot(\exists x \exists y \lnot P(x, y) \land \forall x \forall y Q(x, y))$ 
- e) $\lnot \forall x(\exists y \forall z P(x, y, z) \land \exists z \forall y P(x, y, z))$

### answer

- a) $\exists x \exist y \lnot P(x,y)$
- b) $\exist y \forall x \lnot P(x,y)$
- c) $\exist y \exist x( \lnot P(x,y) \land \lnot Q(x,y))$
- d) $\forall x \forall y P(x,y) \lor \exist x \exist y \lnot Q(x,y)$
- e) $\exist x(\forall y \exist z \lnot P(x,y,z) \lor \forall z \exist y \lnot P(x,y,z))$


---

### 40

40. Find a counterexample, if possible, to these universally quantified statements, where the domain for all variables consists of all integers. 
- a) $\forall x \exists y(x = 1/y)$  
- b) $\forall x \exists y(y^2 - x < 100)$ 
- c) $\forall x \forall y(x^2 \neq y^3)$

### answer

- a) $x=0$
- b) $x=-200$
- c) $x=y$

---