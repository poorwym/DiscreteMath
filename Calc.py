import math
from typing import Set, List, Union
import argparse

class DiscreteMathCalculator:
    def __init__(self):
        pass

    # 集合运算
    def union(self, set1: Set, set2: Set) -> Set:
        """计算两个集合的并集"""
        return set1.union(set2)

    def intersection(self, set1: Set, set2: Set) -> Set:
        """计算两个集合的交集"""
        return set1.intersection(set2)

    def complement(self, universal_set: Set, subset: Set) -> Set:
        """计算补集"""
        return universal_set - subset

    # 逻辑运算
    def logical_and(self, p: bool, q: bool) -> bool:
        """逻辑与运算"""
        return p and q

    def logical_or(self, p: bool, q: bool) -> bool:
        """逻辑或运算"""
        return p or q

    def logical_not(self, p: bool) -> bool:
        """逻辑非运算"""
        return not p

    def implication(self, p: bool, q: bool) -> bool:
        """逻辑蕴含运算"""
        return (not p) or q

    # 模运算
    def mod(self, a: int, n: int) -> int:
        """计算a mod n"""
        return a % n

    # 组合数学
    def factorial(self, n: int) -> int:
        """计算n的阶乘"""
        if n < 0:
            raise ValueError("阶乘不能为负数")
        return math.factorial(n)

    def combination(self, n: int, k: int) -> int:
        """计算组合数C(n,k)"""
        if n < 0 or k < 0 or k > n:
            raise ValueError("无效的组合数参数")
        return math.comb(n, k)

    def permutation(self, n: int, k: int) -> int:
        """计算排列数P(n,k)"""
        if n < 0 or k < 0 or k > n:
            raise ValueError("无效的排列数参数")
        return math.perm(n, k)

    # 布尔代数
    def boolean_and(self, a: bool, b: bool) -> bool:
        """布尔与运算"""
        return a and b

    def boolean_or(self, a: bool, b: bool) -> bool:
        """布尔或运算"""
        return a or b

    def boolean_not(self, a: bool) -> bool:
        """布尔非运算"""
        return not a

    def boolean_xor(self, a: bool, b: bool) -> bool:
        """布尔异或运算"""
        return a != b

def main():
    parser = argparse.ArgumentParser(description='离散数学计算器')
    subparsers = parser.add_subparsers(dest='command', help='可用的计算命令')

    # 集合运算命令
    set_parser = subparsers.add_parser('set', help='集合运算')
    set_parser.add_argument('operation', choices=['union', 'intersection', 'complement'], 
                          help='集合运算类型')
    set_parser.add_argument('set1', type=str, help='第一个集合，用逗号分隔的元素')
    set_parser.add_argument('set2', type=str, help='第二个集合，用逗号分隔的元素')

    # 逻辑运算命令
    logic_parser = subparsers.add_parser('logic', help='逻辑运算')
    logic_parser.add_argument('operation', choices=['and', 'or', 'not', 'implication'], 
                            help='逻辑运算类型')
    logic_parser.add_argument('p', type=str, help='第一个命题 (True/False)')
    logic_parser.add_argument('q', type=str, nargs='?', help='第二个命题 (True/False)')

    # 模运算命令
    mod_parser = subparsers.add_parser('mod', help='模运算')
    mod_parser.add_argument('a', type=int, help='被除数')
    mod_parser.add_argument('n', type=int, help='除数')

    # 组合数学命令
    comb_parser = subparsers.add_parser('comb', help='组合数学')
    comb_parser.add_argument('operation', choices=['factorial', 'combination', 'permutation'], 
                           help='运算类型')
    comb_parser.add_argument('n', type=int, help='第一个参数')
    comb_parser.add_argument('k', type=int, nargs='?', help='第二个参数')

    # 布尔代数命令
    bool_parser = subparsers.add_parser('bool', help='布尔代数')
    bool_parser.add_argument('operation', choices=['and', 'or', 'not', 'xor'], 
                           help='布尔运算类型')
    bool_parser.add_argument('a', type=str, help='第一个布尔值 (True/False)')
    bool_parser.add_argument('b', type=str, nargs='?', help='第二个布尔值 (True/False)')

    args = parser.parse_args()
    calc = DiscreteMathCalculator()

    try:
        if args.command == 'set':
            set1 = set(map(int, args.set1.split(',')))
            set2 = set(map(int, args.set2.split(',')))
            if args.operation == 'union':
                result = calc.union(set1, set2)
            elif args.operation == 'intersection':
                result = calc.intersection(set1, set2)
            elif args.operation == 'complement':
                result = calc.complement(set1, set2)
            print(f"结果: {result}")

        elif args.command == 'logic':
            p = args.p.lower() == 'true'
            q = args.q.lower() == 'true' if args.q else None
            if args.operation == 'and':
                result = calc.logical_and(p, q)
            elif args.operation == 'or':
                result = calc.logical_or(p, q)
            elif args.operation == 'not':
                result = calc.logical_not(p)
            elif args.operation == 'implication':
                result = calc.implication(p, q)
            print(f"结果: {result}")

        elif args.command == 'mod':
            result = calc.mod(args.a, args.n)
            print(f"结果: {result}")

        elif args.command == 'comb':
            if args.operation == 'factorial':
                result = calc.factorial(args.n)
            elif args.operation == 'combination':
                result = calc.combination(args.n, args.k)
            elif args.operation == 'permutation':
                result = calc.permutation(args.n, args.k)
            print(f"结果: {result}")

        elif args.command == 'bool':
            a = args.a.lower() == 'true'
            b = args.b.lower() == 'true' if args.b else None
            if args.operation == 'and':
                result = calc.boolean_and(a, b)
            elif args.operation == 'or':
                result = calc.boolean_or(a, b)
            elif args.operation == 'not':
                result = calc.boolean_not(a)
            elif args.operation == 'xor':
                result = calc.boolean_xor(a, b)
            print(f"结果: {result}")

    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()
