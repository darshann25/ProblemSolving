class Solution:
    def computer_infestation(self, input):
        global col
        list = input.split("\n")

        matrix = []

        for i in list:
            iList = []
            iList.extend(i)
            inputList = []
            for j in iList:
                inputList.append(int(j))

            matrix.append(inputList)

        print matrix

        min = 0
        max = len(matrix) - 1

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if row - 1 < min and col - 1 < min:
                    matrix[row][col] += matrix[min][col] + matrix[row + 1][col] \
                                        + matrix[row][min] + matrix[row][col + 1]
                    continue

                if row - 1 < min and col + 1 > max:
                    matrix[row][col] += matrix[min][col] + matrix[row + 1][col] \
                                        + matrix[row][col - 1] + matrix[row][max]
                    continue

                if row + 1 > max and col + 1 > max:
                    matrix[row][col] += matrix[row - 1][col] + matrix[max][col] \
                                        + matrix[row][col - 1] + matrix[row][max]
                    continue

                if row + 1 > max and col - 1 < min:
                    matrix[row][col] += matrix[row - 1][col] + matrix[max][col] \
                                        + matrix[row][min] + matrix[row][col + 1]
                    continue

                if row - 1 < min:
                    matrix[row][col] += matrix[min][col] + matrix[row + 1][col] \
                                        + matrix[row][col - 1] + matrix[row][col + 1]
                    continue

                if col - 1 < min:
                    matrix[row][col] += matrix[row - 1][col] + matrix[row + 1][col] \
                                        + matrix[row][min] + matrix[row][col + 1]
                    continue

                if row + 1 > max:
                    matrix[row][col] += matrix[row - 1][col] + matrix[max][col] \
                                        + matrix[row][col - 1] + matrix[row][col + 1]
                    continue

                if col + 1 > max:
                    matrix[row][col] += matrix[row - 1][col] + matrix[row + 1][col] \
                                        + matrix[row][col - 1] + matrix[row][max]
                    continue

                matrix[row][col] += matrix[row - 1][col] + matrix[row + 1][col] \
                                    + matrix[row][col - 1] + matrix[row][col + 1]

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] <= 1 :
                    matrix[row][col] = 0
                if matrix[row][col] > 1 :
                    matrix[row][col] = 1

        print matrix


str = "0000010\n1100000\n0000010\n0000001\n0110000\n0000000\n0001000"
str1 = "00000000\n01010000\n00010000\n01001000\n00010010\n00001000\n00001001\n01000000"
s = Solution()
s.computer_infestation(str1)
