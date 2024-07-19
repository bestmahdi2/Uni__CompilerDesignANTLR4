from gen.JavaParser import JavaParser
from gen.JavaParserListener import JavaParserListener


class Listener(JavaParserListener):
    """
        Class Listener
    """

    def __init__(self):
        """
            initial method,
        """

        # method types
        self.types = {
            "public": [],
            "private": [],
            "protected": []
        }

        self.all = []

    @property
    def get_type(self) -> str:
        """
            The method to get the classes names,

            Return:
                The string value of all classes names
        """

        res = []

        if self.types['public']: res.append(f"Public Methods:\n{', '.join(self.types['public'])}")
        if self.types['private']: res.append(f"Private Methods:\n{', '.join(self.types['private'])}")
        if self.types['protected']: res.append(f"Protected Methods:\n{', '.join(self.types['protected'])}")

        return "\n\n".join(res)

    # def enterMethodDeclaration(self, ctx:JavaParser.MethodDeclarationContext):
    def enterClassOrInterfaceModifier(self, ctx: JavaParser.ClassOrInterfaceModifierContext):
        """
            The method which enters class-interface and method head and collect its modifier !
        """

        if ctx.getText() in self.types:
            self.all.append(ctx.getText())

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext):
        """
            The method which enters method declaration and collect its name !
        """

        temp = self.all[0]
        self.all = self.all[1:]
        if temp in self.types:
            self.types[temp].append(ctx.identifier().getText())

    def enterClassDeclaration(self, ctx: JavaParser.ClassDeclarationContext):
        """
            The method which enters class declaration remove it from self.all !
        """

        self.all = self.all[1:]
