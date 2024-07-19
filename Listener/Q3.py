import argparse
from antlr4 import *

from metricQ3 import Listener
from gen.CPP14Lexer import CPP14Lexer
from gen.CPP14Parser import CPP14Parser


class Q3:
    """
        Class Question 3
    """

    def __init__(self) -> None:
        """
            initial method,
        """

        # get the file name and create args
        input_file = input("Enter the c++ file name (default=Q3.cpp) > ")
        if not input_file: input_file = "Q3"

        parser = argparse.ArgumentParser()
        parser.add_argument('-n', '--file', default=input_file + '.cpp')

        self.args = parser.parse_args()

    def main(self):
        """
            the main method,
        """

        input_file = FileStream(self.args.file, encoding='utf8')

        # create the lexer
        lexer = CPP14Lexer(input_file)

        # create tokens
        token = CommonTokenStream(lexer)

        # create parser tree
        parsed = CPP14Parser(token)
        parser_tree = parsed.translationUnit()

        # create listener
        listener = Listener()

        # create a walker
        tree_walker = ParseTreeWalker()
        tree_walker.walk(t=parser_tree, listener=listener)

        # print result
        print(f"Class Count = {listener.get_class_count}")
        print(f"Class Names = {listener.get_name}")


if __name__ == '__main__':
    q3 = Q3()
    q3.main()
