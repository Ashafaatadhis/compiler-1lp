class Interpreter:
    def __init__(self):
        self.env = {}

    def eval_stm(self, node):
        tag = node[0]

        if tag == 'seq':
            self.eval_stm(node[1])
            self.eval_stm(node[2])

        elif tag == 'assign':
            _, var, exp = node
            self.env[var] = self.eval_exp(exp)

        elif tag == 'print':
            _, exps = node
            values = [self.eval_exp(e) for e in exps]
            print(*values)

    def eval_exp(self, node):
        tag = node[0]

        if tag == 'num':
            return node[1]

        if tag == 'id':
            return self.env[node[1]]

        if tag == 'binop':
            _, op, left, right = node
            l = self.eval_exp(left)
            r = self.eval_exp(right)
            return {
                '+': l + r,
                '-': l - r,
                '*': l * r,
                '/': l / r
            }[op]

        if tag == 'eseq':
            _, stm, exp = node
            self.eval_stm(stm)
            return self.eval_exp(exp)
