class Solution:
    def diffWaysToCompute(self, input: str):
        res = []
        for i in range(len(input)):
            if input[i] == '+' or input[i] == '-' or input[i] == '*':
                ls = self.diffWaysToCompute(input[:i])
                rs = self.diffWaysToCompute(input[i + 1:])
                print(ls, rs)
                for l in ls:
                    for r in rs:
                        if input[i] == '+':
                            res.append(l + r)
                        elif input[i] == '-':
                            res.append(l - r)
                        elif input[i] == '*':
                            res.append(l * r)
        if not res:
            res.append(int(input))
        return res