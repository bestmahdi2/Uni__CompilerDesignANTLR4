from gen.CPP14Parser import CPP14Parser
from gen.CPP14ParserListener import CPP14ParserListener


class Listener(CPP14ParserListener):
    """
        Class Listener
    """

    def __init__(self):
        """
            initial method,
        """

        # class counter
        self.cc = 0

        # class names
        self.names = []

    @property
    def get_class_count(self) -> int:
        """
            The method to get the class' counter,

            Return:
                The integer number of classes
        """

        return self.cc

    @property
    def get_name(self) -> str:
        """
            The method to get the classes names,

            Return:
                The string value of all classes names
        """

        return ", ".join(self.names)

    def enterClassHeadName(self, ctx: CPP14Parser.ClassHeadNameContext) -> None:
        """
            The method which enters class head and collect its name and add the counter !
        """

        self.cc += 1
        self.names.append(ctx.getText())
