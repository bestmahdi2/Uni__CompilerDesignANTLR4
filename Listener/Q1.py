import argparse
from antlr4 import *

from metricQ1 import Listener
from gen.JavaLexer import JavaLexer
from gen.JavaParser import JavaParser


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

        # create listener
        listener = Listener()

        # create a walker
        tree_walker = ParseTreeWalker()
        tree_walker.walk(t=parser_tree, listener=listener)

        # print result
        print(listener.get_type)


if __name__ == '__main__':
    q1 = Q1()
    q1.main()
