'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Example 1:

Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
'''

from collections import deque

def floodFill(image, sr, sc, color):
    row_max = len(image)
    col_max = len(image[0])

    dq = deque()
    if image[sr][sc] != color:
        dq.append([sr, sc])

    compare_with = image[sr][sc]

    while dq:
        size = len(dq)

        while size:
            element = dq.popleft()

            i = element[0]
            j = element[1]

            if i - 1 >= 0 and image[i - 1][j] == compare_with:
                dq.append([i - 1, j])
                image[i - 1][j] = color

            if i + 1 < row_max and image[i + 1][j] == compare_with:
                dq.append([i + 1, j])
                image[i + 1][j] = color
            
            if j - 1 >= 0 and image[i][j - 1] == compare_with:
                dq.append([i, j - 1])
                image[i][j - 1] = color

            if j + 1 < col_max and image[i][j + 1] == compare_with:
                dq.append([i, j + 1])
                image[i][j + 1] = color

            image[i][j] = color

            size -= 1

    return image

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))

image = [[0, 0, 0], [0, 0, 0]]
sr = 0
sc = 0
color = 0
print(floodFill(image, sr, sc, color))