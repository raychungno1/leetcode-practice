class Solution:
    def decodeString(self, s: str) -> str:
        stack = [""]
        repeat = 0

        for c in s:
            # Store a "recursive" call on the stack
            if c == "[":
                stack.append(repeat)
                stack.append("")
                repeat = 0

            # Recover a "recursive" call, and add it to the current string
            elif c == "]":
                cur = stack.pop()
                repeat = stack.pop()
                stack[-1] += cur * repeat
                repeat = 0

            # Parse digit values
            elif c.isdigit():
                repeat = repeat * 10 + int(c)

            # Parse string values
            else:
                stack[-1] += c

        return stack[-1]
