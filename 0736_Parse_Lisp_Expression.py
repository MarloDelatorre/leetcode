from collections import deque
from typing import Deque, Dict, List, Tuple
from unittest import TestCase, main

class Node:
    pass

class IntegerNode(Node):
    def __init__(self, val: int):
        self.val = val

    def __repr__(self):
        return f"IntegerNode: val={self.val}"

class VariableNode(Node):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def __repr__(self):
        return f"VariableNode: identifier={self.identifier}"

class AddNode(Node):
    def __init__(self, op1: Node, op2: Node):
        self.op1 = op1
        self.op2 = op2
    
    def __repr__(self):
        return f"AddNode: op1=\"{self.op1}\" op2=\"{self.op2}\""

class MultiplyNode(Node):
    def __init__(self, op1: Node, op2: Node):
        self.op1 = op1
        self.op2 = op2

    def __repr__(self):
        return f"MultiplyNode: op1=\"{self.op1}\" op2=\"{self.op2}\""

class LetNode(Node):
    def __init__(self, assignments: List[Tuple[str, Node]], expr: Node):
        self.assignments = assignments
        self.expr = expr
    
    def __repr__(self):
        assignment_repr = ""
        for identifier, node in self.assignments:
            assignment_repr += f"{identifier}=\"{node}\" "

        return f"LetNode: assignments=\"{assignment_repr}\" expr=\"{self.expr}\""

class Context:
    def __init__(self, assignments: Dict[str, int], parent_context: "Context"=None):
        self.parent_context = parent_context
        self.assignments = assignments 

    def __repr__(self):
        return f"Parent Context={self.parent_context}, assignments={self.assignments}"

class Tokenizer:
    def tokenize(self, expression: str) -> Deque[str]:
        tokens = []
        token = ""
        
        for char in expression:
            if char == "(":
                tokens.append(char)
            elif char == ")":
                if token: tokens.append(token)
                token = ""
                tokens.append(char)
            elif char == " ":
                if token: tokens.append(token)
                token = ""
            else:
                token += char

        if token: tokens.append(token)

        return deque(tokens)

class Parser:
    @classmethod
    def get_ast(cls, stream: Deque[str]) -> Node:
        return cls._get_expr_node(stream)

    @classmethod
    def _get_expr_node(cls, stream: Deque[str]) -> Node:
        token = stream[0]
        if token == "(":
            operator = stream[1]
            if operator == "let":
                return cls._get_let_node(stream)
            if operator == "add":
                return cls._get_add_node(stream)
            if operator == "mult":
                return cls._get_mult_node(stream)
        elif not token.isnumeric() and token.isalnum():
            return cls._get_var_node(stream)
        else:
            return cls._get_int_node(stream)

    @classmethod
    def _get_add_node(cls, stream: Deque[str]) -> AddNode:
        token = stream.popleft()
        assert token == "("
        token = stream.popleft()
        assert token == "add"

        op1 = cls._get_expr_node(stream)
        op2 = cls._get_expr_node(stream)

        token = stream.popleft()
        assert token == ")"

        return AddNode(op1, op2)
    
    @classmethod
    def _get_int_node(cls, stream: Deque[str]) -> IntegerNode:
        token = stream.popleft()
        assert token[1:].isnumeric() if token[0] == "-" else token.isnumeric()
        return IntegerNode(int(token))

    @classmethod
    def _get_mult_node(cls, stream: Deque[str]) -> MultiplyNode:
        token = stream.popleft()
        assert token == "("
        token = stream.popleft()
        assert token == "mult"

        op1 = cls._get_expr_node(stream)
        op2 = cls._get_expr_node(stream)

        token = stream.popleft()
        assert token == ")"

        return MultiplyNode(op1, op2) 

    @classmethod
    def _get_let_node(cls, stream: Deque[str]) -> LetNode:
        token = stream.popleft()
        assert token == "("
        token = stream.popleft()
        assert token == "let"

        assignments = [] 

        while True:
            var = stream.popleft()
            assert var.isalnum()
            expr = cls._get_expr_node(stream)
            assignments.append((var, expr))
            if stream[1] == ")" or stream[0] == "(" or not stream[0].isalnum():
                break
        
        expr = cls._get_expr_node(stream)

        token = stream.popleft()
        assert token == ")"

        return LetNode(assignments, expr) 

    @classmethod 
    def _get_var_node(cls, stream: Deque[str]) -> VariableNode:
        token = stream.popleft()
        assert token.isalnum()
        return VariableNode(token)
            
class Evaluator:
    def __init__(self, tokenizer: Tokenizer, parser: Parser):
        self.tokenizer = tokenizer
        self.parser = parser

    def evaluate(self, expression: str) -> int:
        tokens = self.tokenizer.tokenize(expression)
        ast = self.parser.get_ast(tokens)
        return self._eval_expr_node(ast)

    @classmethod    
    def _eval_expr_node(cls, node: Node, context: Context=None) -> int:
        if isinstance(node, IntegerNode):
            return cls._eval_integer_node(node)
        elif isinstance(node, AddNode):
            return cls._eval_add_node(node, context)
        elif isinstance(node, MultiplyNode):
            return cls._eval_multiply_node(node, context)
        elif isinstance(node, LetNode):
            return cls._eval_let_node(node, context)
        elif isinstance(node, VariableNode):
            return cls._eval_variable_node(node, context)

    @classmethod
    def _eval_integer_node(cls, node: IntegerNode) -> int:
        return node.val

    @classmethod
    def _eval_add_node(cls, node: AddNode, context: Context) -> int:
        return cls._eval_expr_node(node.op1, context) \
            + cls._eval_expr_node(node.op2, context)

    @classmethod
    def _eval_multiply_node(cls, node: MultiplyNode, context: Context) -> int:
        return cls._eval_expr_node(node.op1, context) \
            * cls._eval_expr_node(node.op2, context)
        
    @classmethod
    def _eval_let_node(cls, node: LetNode, context: Context) -> int:
        new_context = Context({}, context)
        for identifier, val_node in node.assignments:
            new_context.assignments[identifier] = cls._eval_expr_node(val_node, new_context)
        return cls._eval_expr_node(node.expr, new_context)

    @classmethod
    def _eval_variable_node(cls, node: VariableNode, context: Context) -> int:
        return cls._get_variable_value(node.identifier, context)

    @classmethod
    def _get_variable_value(cls, identifier: str, context: Context) -> int:
        if identifier in context.assignments:
            return context.assignments[identifier]
        else:
            return cls._get_variable_value(identifier, context.parent_context)

class TokenizeTest(TestCase):
    def setUp(self):
        self.tokenizer = Tokenizer()

    def test_integer(self):
        self.assertListEqual(list(self.tokenizer.tokenize("3")), ["3"])

    def test_negative_integer(self):
        self.assertListEqual(list(self.tokenizer.tokenize("-3")), ["-3"])

    def test_add_expression(self):
        self.assertListEqual(
            list(self.tokenizer.tokenize("(add 3 4)")),
            ["(", "add", "3", "4", ")"]
        )

    def test_mult_expression(self):
        self.assertListEqual(
            list(self.tokenizer.tokenize("(mult 3 4)")),
            ["(", "mult", "3", "4", ")"]
        )

    def test_let_expression(self):
        self.assertListEqual(
            list(self.tokenizer.tokenize("(let x 1 y 2 z 3 4)")),
            ["(", "let", "x", "1", "y", "2", "z", "3", "4", ")"]
        )

    def test_complex_expression(self):
        self.assertListEqual(
            list(self.tokenizer.tokenize(
                "(let x 2 (add (let x 3 (let x 4 x)) x))")
            ),
            [
                "(", "let", "x", "2", "(", "add", "(", "let", "x",
                "3", "(", "let", "x", "4", "x", ")", ")", "x", ")", ")"
            ]
        )    

class EvaluateTest(TestCase):
    def setUp(self):
        self.evaluator = Evaluator(Tokenizer(), Parser())

    def test_add(self):
        self.assertEqual(
            self.evaluator.evaluate("(add 1 2)"),
            3
        )

    def test_mult(self):
        self.assertEqual(
            self.evaluator.evaluate("(mult 3 (add 2 3))"),
            15
        )

    def test_let_mult(self):
        self.assertEqual(
            self.evaluator.evaluate("(let x 2 (mult x 5))"),
            10
        )

    def test_complex_expression(self):
        self.assertEqual(
            self.evaluator.evaluate(
                "(let x 2 (mult x (let x 3 y 4 (add x y))))"
            ),
            14
         )

    def test_sequential_assignment(self):
        self.assertEqual(
            self.evaluator.evaluate("(let x 3 x 2 x)"),
            2
        )

    def test_sequential_complex_assignment(self):
        self.assertEqual(
            self.evaluator.evaluate("(let x 1 y 2 x (add x y) (add x y))"),
            5
        )

    def test_deepest_scope(self):
        self.assertEqual(
            self.evaluator.evaluate("(let x 2 (add (let x 3 (let x 4 x)) x))"),
            6
        )

    def test_alnum_variable_names(self):
        self.assertEqual(
            self.evaluator.evaluate("(let a1 3 b2 (add a1 1) b2)"),
            4
        )
    
if __name__ == "__main__":
    main()
    