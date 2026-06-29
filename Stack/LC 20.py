#Valid parentheses
s="()[{}]"
class Solution(object):

    def isValid(self, s):

        class Stack:

            def __init__(self):
                self.values = []

            def push(self, x):
                self.values.append(x)

            def pop(self):
                self.values.pop()

            def peek(self):
                return self.values[-1]
        st = Stack()
        for i in s:
            if i in "([{":
                st.push(i)
            else:
                if st.values == []:
                    return False

                elif i == ")" and st.peek() == "(":
                    st.pop()

                elif i == "]" and st.peek() == "[":
                    st.pop()

                elif i == "}" and st.peek() == "{":
                    st.pop()

                else:
                    return False

        return st.values == []






ss=Solution()
print(ss.isValid(s))