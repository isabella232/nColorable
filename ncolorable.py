# Undirected graph is stored in a adjacency matrix with 1 if graph goes from index i to j
# The program should output an array called colors that goes from 1 to n. colors[i] returns the color from 1 to n assigned to vertex i

import csv


def checkVertex(graph, curIndex, colors, color,
                numVertices):  # Function checks if it's okay to assign color to this vertex
    for i in range(0, numVertices):
        if graph[curIndex][i] == 1 and colors[i] == color:  # Checks if a connected vertex already has this color
            return False
    return True


def graphColoring(graph, n, colors, curIndex, numVertices):
    if curIndex == numVertices:  # Not sure this is necessary
        return True
    for i in range(1, n + 1):
        if checkVertex(graph, curIndex, colors, i, numVertices) == True:
            colors[curIndex] = i  # Assign color i to current index
            if graphColoring(graph, n, colors, curIndex + 1, numVertices) == True:  # recursively call for next index
                return True
            colors[curIndex] = 0  # if previous conditionals weren't satisfied, it doesn't assign a color


def colorDriver(graph, n, colors, numVertices):
    if graphColoring(graph, n, colors, 0, numVertices) == None:  # Returns False if graph cannot be colored
        return False
    return True


def initColors(numVertices):
    colors = [0] * numVertices
    return colors


def fileReader(filename, numVertices):
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        graph = [[0 for x in range(numVertices)] for y in range(numVertices)]  # Initialize graph matrix
        curRow = 0
        for row in csvfile:
            rowNums = [int(x) for x in row.split(',') if x.strip().isdigit()]
            graph[curRow] = rowNums
            curRow = curRow + 1
    return graph


def main():
    numVertices = int(input("Enter number of vertices: "))
    graph = fileReader("test.csv", numVertices)

    n = int(input("Enter n: "))

    colors = initColors(numVertices)  # initalizes colors to all 0s

    if colorDriver(graph, n, colors, numVertices) == False:
        print("Graph cannot be colored")
    else:
        print("The color assignments are: ")
        for color in colors:
            print(color)


if __name__ == "__main__":
    main()
