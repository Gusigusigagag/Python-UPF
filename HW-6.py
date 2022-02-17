
import fileinput
import sys

def calculate_pdb_chain_mean_minimum_distances(pdb_file_path):

    from cmath import sqrt
    dic_all = {}
    for line in fileinput.input(files=(pdb_file_path)):
        if line.startswith("ATOM"):
            line1 = line.split()
            dic_all[line1[1], int(line1[5]), line1[4]] = line1[6:9]

    min_distances = {}
    for x, y in dic_all.items():
        for i, j in dic_all.items():
            if (x[0] != i[0]) and x[2] == i[2] and x[1] != i[1]:
                distance = sqrt(((float(y[0]) - float(j[0]))**2) + ((float(y[1])-float(j[1]))**2) + ((float(y[2])-float(j[2]))**2))
                if ((x[1], i[1], x[2]) not in min_distances and (i[1], x[1], x[2]) not in min_distances):
                    min_distances[x[1], i[1], x[2]] = distance.real
                elif ((x[1], i[1], x[2]) in min_distances and distance.real < min_distances[x[1], i[1], x[2]]):
                    min_distances[x[1], i[1], x[2]] = distance.real
                elif ((i[1], x[1], x[2]) in min_distances and distance.real < min_distances[i[1], x[1], x[2]]):
                    min_distances[i[1], x[1], x[2]] = distance.real

    mean_distances = {}
    lenghts = {}
    for x, y in min_distances.items():
        if (x[2] not in lenghts):
            lenghts[x[2]] = 1
        else:
            lenghts[x[2]] += 1

        if (x[2] not in mean_distances):
            mean_distances[x[2]] = y
        else:
            mean_distances[x[2]] += y

    for x, y in mean_distances.items():
        mean_distances[x] = round(mean_distances[x] / lenghts[x], 4)
    
    for x, y in mean_distances.items():
        print("{0}: {1}".format(x,y))

    fileinput.close()

if __name__=="__main__":
    if (len(sys.argv) > 1):
        inp = sys.argv
        calculate_pdb_chain_mean_minimum_distances(inp)
    else:
        calculate_pdb_chain_mean_minimum_distances(input())

#calculate_pdb_chain_mean_minimum_distances()
