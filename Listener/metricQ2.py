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
        self.max = {
        }

        self.current_method = None
        self.temp_state = []
        self.states = []

    def find_depth(self) -> int:
        """
            The method to get the max depth of any loop,

            Return:
                The max depth of the loop.
        """

        max = 0

        for state in self.states:
            maxx = 1
            x = -1

            while x > -len(state):
                if (state[x].startswith("for(") or state[x].startswith("while(")) and state[x] in state[x - 1]:
                    maxx += 1

                x -= 1

            if maxx > max:
                max = maxx

        return max

    @property
    def get_type(self) -> str:
        """
            The method to get the classes names,

            Return:
                The string value of all classes names
        """

        res = [f'\'{i}\' loops depth: {self.max[i]}' for i in self.max]

        return "\n".join(res)

    def enterMethodDeclaration(self, ctx: JavaParser.MethodDeclarationContext) -> None:
        """
            The method which enters method declaration and collect its name !
        """

        self.current_method = ctx.identifier().getText()
        self.max[self.current_method] = 0

    def exitMethodBody(self, ctx: JavaParser.MethodBodyContext) -> None:
        """
            The method which exit method body and save the depth into self.max,
        """

        self.max[self.current_method] = self.find_depth()

        if not ctx.getText().count("for(") + ctx.getText().count("while("):
            self.max[self.current_method] = 0

        self.states = []

    def enterStatement(self, ctx: JavaParser.StatementContext) -> None:
        """
            The method which enters a statement and add it to temp_state !
        """

        self.temp_state.append(ctx.getText())

    def exitStatement(self, ctx: JavaParser.StatementContext) -> None:
        """
            The method which exits a statement and check if it's a parent statement to add to states !
        """

        if self.temp_state[0] == ctx.getText():
            self.states.append(self.temp_state)
            self.temp_state = []
