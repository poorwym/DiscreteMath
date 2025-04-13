# 离散数学计算器

这是一个基于命令行的离散数学计算器，支持多种离散数学运算。

## 功能特点

- 集合运算（并集、交集、补集）
- 逻辑运算（与、或、非、蕴含）
- 模运算
- 组合数学（阶乘、组合数、排列数）
- 布尔代数运算

## 安装要求

- Python 3.6 或更高版本

## 使用方法

### 集合运算

```bash
# 计算并集
python Calc.py set union 1,2,3 3,4,5

# 计算交集
python Calc.py set intersection 1,2,3 3,4,5

# 计算补集
python Calc.py set complement 1,2,3,4,5 1,2,3
```

### 逻辑运算

```bash
# 逻辑与
python Calc.py logic and True False

# 逻辑或
python Calc.py logic or True False

# 逻辑非
python Calc.py logic not True

# 逻辑蕴含
python Calc.py logic implication True False
```

### 模运算

```bash
# 计算 17 mod 5
python Calc.py mod 17 5
```

### 组合数学

```bash
# 计算阶乘
python Calc.py comb factorial 5

# 计算组合数 C(5,2)
python Calc.py comb combination 5 2

# 计算排列数 P(5,2)
python Calc.py comb permutation 5 2
```

### 布尔代数

```bash
# 布尔与
python Calc.py bool and True False

# 布尔或
python Calc.py bool or True False

# 布尔非
python Calc.py bool not True

# 布尔异或
python Calc.py bool xor True False
```

## 注意事项

1. 集合运算时，元素之间用逗号分隔，不要加空格
2. 逻辑值和布尔值使用 "True" 或 "False"（不区分大小写）
3. 所有数值参数必须为整数
4. 如果遇到错误，程序会显示相应的错误信息

## 示例

```bash
# 计算集合 {1,2,3} 和 {3,4,5} 的并集
python Calc.py set union 1,2,3 3,4,5
# 输出: 结果: {1, 2, 3, 4, 5}

# 计算 5! (阶乘)
python Calc.py comb factorial 5
# 输出: 结果: 120

# 计算 17 mod 5
python Calc.py mod 17 5
# 输出: 结果: 2
``` 