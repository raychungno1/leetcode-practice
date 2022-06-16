class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        buffer = [words[0]]
        bLen = len(words[0])
        out = []

        # Iterate through each word
        for i in range(1, len(words)):

            l = len(words[i])
            # If adding this word to the buffer results in bLen > maxWidth
            # its time to process a new line to our output
            if bLen + l + 1 > maxWidth:
                extra = maxWidth - bLen

                # If buffer length is 1
                if len(buffer) == 1:
                    out.append(buffer.pop(0) + " " * extra)

                # Otherwise, calculate the space paddings necessary
                # then construct the line
                else:
                    spaceCount = extra // (len(buffer) - 1) + 1
                    extraSpace = extra % (len(buffer) - 1)

                    line = ""

                    while buffer:
                        line += buffer.pop(0)
                        if buffer:
                            line += " " * spaceCount
                            if extraSpace:
                                line += " "
                                extraSpace -= 1

                    out.append(line)

                bLen = l
            else:
                bLen += l + 1

            buffer.append(words[i])

        # Taking care of extra words in our buffer
        if buffer:
            out.append(" ".join(buffer) + " " * (maxWidth - bLen))

        return out
