class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for row in range(n):
            for col in range(n):
                image[row][col] = abs(image[row][col] - 1)

            image[row] = image[row][::-1]


        return image