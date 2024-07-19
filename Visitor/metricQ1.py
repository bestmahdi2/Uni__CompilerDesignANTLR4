from gen.JavaParser import JavaParser
from gen.JavaParserVisitor import JavaParserVisitor

# for final variables:
getter = []
# for others:
setter = []

done_getter = []
done_setter = []



class Visitor1(JavaParserVisitor):
    def visitClassBodyDeclaration(self, ctx: JavaParser.ClassBodyDeclarationContext):
        if ";" in ctx.getText() and "(" not in ctx.getText() and ctx.getText().startswith("private"):
            if ctx.getText()[7:].startswith("final"):
                getter.append(ctx.getText()[12:])

            else:
                setter.append(ctx.getText()[7:])


class Visitor2(JavaParserVisitor):
    def visitVariableDeclarators(self, ctx: JavaParser.VariableDeclaratorsContext):
        for i in getter + setter:
            if i.endswith(ctx.getText() + ";"):
                if i in getter:
                    done_getter.append([i[:-len(ctx.getText()) - 1], ctx.getText()])
                    var = i, 'g'
                    break

                else:
                    done_setter.append([i[:-len(ctx.getText()) - 1], ctx.getText()])
                    var = i, 's'
                    break
        else:
            return

        if var[1] == 'g':
            getter.remove(var[0])

        else:
            setter.remove(var[0])
