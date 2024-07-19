import argparse
from antlr4 import *

from metricQ1 import Visitor1, Visitor2, done_setter, done_getter
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser

# antlr4 -Dlanguage=Python3 -visitor -no-listener JavaParser.g4

class Q1:
    """
        Class Question 1
    """

    def __init__(self) -> None:
        """
            initial method,
        """

        # get the file name and create args
        input_file = input("Enter the Java file name (default=Q1.java) > ")
        if not input_file: input_file = "Q1"

        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--file', default=input_file + '.java')

        self.args = parser.parse_args()

    def main(self):
        """
            the main method,
        """

        input_file = FileStream(self.args.file, encoding='utf8')

        # create the lexer
        lexer = JavaLexer(input_file)

        # create tokens
        token = CommonTokenStream(lexer)

        # create parser tree
        parsed = JavaParser(token)
        parser_tree = parsed.compilationUnit()

        # create visitor
        visitor1 = Visitor1()
        visitor1.visit(parser_tree)

        # create visitor
        visitor2 = Visitor2()
        visitor2.visit(parser_tree)

        print("Results >> \n")
        print(str(input_file)[:-2] + self.make_setter_getter() + "\n}")

    def make_setter_getter(self) -> str:
        """
            a method to make any setter and getter for all variables !
        """

        result = ""

        for i in done_setter:
            name = i[1][0].capitalize() + i[1][1:]
            result += f"\n\n\tpublic {i[0]} get{name}()\n\t{{\n\t\treturn {i[1]};\n\t}}"
            result += f"\n\n\tprivate void set{name}({i[0]} value)\n\t{{\n\t\t{i[1]} = value;\n\t}}"

        for i in done_getter:
            name = i[1][0].capitalize() + i[1][1:]
            result += f"\n\n\tpublic {i[0]} get{name}()\n\t{{\n\t\treturn {i[1]};\n\t}}"

        return result


if __name__ == '__main__':
    q1 = Q1()
    q1.main()
