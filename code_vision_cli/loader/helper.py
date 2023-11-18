from pycparser import c_generator, c_ast


class AbstractCGenerator(c_generator.CGenerator):

    def visit_Constant(self, n):
        return "CONST"

    def visit_ID(self, n):
        return "ID"

    def visit_ArrayRef(self, n):
        arrref = "ARR"
        return arrref + '[' + self.visit(n.subscript) + ']'

    def visit_StructRef(self, n):
        sref = "STRUCT"
        return sref + n.type + self.visit(n.field)

    def visit_FuncCall(self, n):
        fref = "FUNC"
        return fref + '(' + self.visit(n.args) + ')'

    def visit_Label(self, n):
        return "LABEL" + ':\n' + self._generate_stmt(n.stmt)

    def visit_Goto(self, n):
        return 'goto ' + "LABEL" + ';'

    def _generate_struct_union(self, n, name):
        s = name
        if name == 'struct':
            s += ' ' + ("STRUCT" or '')
        elif name == 'union':
            s += ' ' + ("UNION" or '')
        if n.decls:
            s += '\n'
            s += self._make_indent()
            self.indent_level += 2
            s += '{\n'
            for decl in n.decls:
                s += self._generate_stmt(decl)
            self.indent_level -= 2
            s += self._make_indent() + '}'
        return s

    def _generate_type(self, n, modifiers=[]):
        typ = type(n)
        # ~ print(n, modifiers)

        if typ == c_ast.TypeDecl:
            s = ''
            if n.quals: s += ' '.join(n.quals) + ' '
            s += self.visit(n.type)

            nstr = "ID" if n.declname else ''
            # Resolve modifiers.
            # Wrap in parens to distinguish pointer to array and pointer to
            # function syntax.
            #
            for i, modifier in enumerate(modifiers):
                if isinstance(modifier, c_ast.ArrayDecl):
                    nstr = "ARR"
                    if i != 0 and isinstance(modifiers[i - 1], c_ast.PtrDecl):
                        nstr = '(' + nstr + ')'
                    nstr += '[' + self.visit(modifier.dim) + ']'
                elif isinstance(modifier, c_ast.FuncDecl):
                    nstr = "FUNC"
                    if i != 0 and isinstance(modifiers[i - 1], c_ast.PtrDecl):
                        nstr = '(' + nstr + ')'
                    nstr += '(' + self.visit(modifier.args) + ')'
                elif isinstance(modifier, c_ast.PtrDecl):
                    if modifier.quals:
                        nstr = '* %s %s' % (' '.join(modifier.quals), nstr)
                    else:
                        nstr = '*' + nstr
            if nstr: s += ' ' + nstr
            return s
        elif typ == c_ast.Decl:
            return self._generate_decl(n.type)
        elif typ == c_ast.Typename:
            return self._generate_type(n.type)
        elif typ == c_ast.IdentifierType:
            return ' '.join(n.names) + ' '
        elif typ in (c_ast.ArrayDecl, c_ast.PtrDecl, c_ast.FuncDecl):
            return self._generate_type(n.type, modifiers + [n])
        else:
            return self.visit(n)
