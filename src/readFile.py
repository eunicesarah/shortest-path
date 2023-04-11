
def readFileUCS(filename):
    try:
        with open('test/' + filename + '.txt', 'r') as file:
            nodes = file.readline().strip().split(', ')
            graph = []
            for line in file:
                weights = line.split()
                graph.append([int(num) for num in weights])
            if len(graph) != len(nodes):
                raise ValueError("Jumlah baris tidak sama dengan jumlah node!")
            for i in range(len(graph)):
                if len(graph[i]) != len(nodes):
                    raise ValueError(f"Baris {i+2} tidak memiliki jumlah elemen yang sama dengan jumlah node!")
                if graph[i][i] != 0:
                    raise ValueError(f"Elemen diagonal graph[{i}][{i}] harus bernilai 0!")
                for j in range(i+1, len(graph)):
                    if graph[i][j] != graph[j][i]:
                        raise ValueError(f"Graph[{i}][{j}] harus sama dengan graph[{j}][{i}]!")
        return nodes, graph
    except FileNotFoundError:
        print(f"File {filename}.txt tidak ditemukan!")
    except ValueError as e:
        print(str(e))
    return None, None

def readFileAStar(filename):
    try:
        with open('test/' + filename + '.txt', 'r') as file:
            # Read the first line to get the node names
            nodes = file.readline().strip().split(', ')

            # Read the next lines to get the graph
            graph = []
            for i in range(len(nodes)):
                line = file.readline().strip()
                weights = list(map(int, line.split()))
                if len(weights) != len(nodes):
                    raise ValueError("Jumlah elemen di baris tidak sama dengan jumlah node!")
                graph.append(list(weights))

            # Read the next lines to get the coordinates
            coordinat = []
            for i in range(len(nodes)):
                line = file.readline().strip()
                coordinate = list(map(int, line.split(',')))
                if len(coordinate) != 2:
                    raise ValueError("Jumlah elemen di baris tidak sama dengan 2!")
                coordinat.append(list(coordinate))

            # Validate the graph
            if len(graph) != len(nodes):
                raise ValueError("Jumlah baris tidak sama dengan jumlah node!")
            for i in range(len(graph)):
                if len(graph[i]) != len(nodes):
                    raise ValueError(f"Baris {i+2} tidak memiliki jumlah elemen yang sama dengan jumlah node!")
                if graph[i][i] != 0:
                    raise ValueError(f"Elemen diagonal graph[{i}][{i}] harus bernilai 0!")
                for j in range(i+1, len(graph)):
                    if graph[i][j] != graph[j][i]:
                        raise ValueError(f"Graph[{i}][{j}] harus sama dengan graph[{j}][{i}]!")

            # Return the nodes, graph, and coordinates
            return nodes, graph, coordinat
    except FileNotFoundError:
        print(f"File {filename}.txt tidak ditemukan!")
    except ValueError as e:
        print(str(e))
    return None, None, None