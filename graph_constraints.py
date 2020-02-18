from constraint import *
from subprocess import check_output

#find all subsets of a specific set of vertexes recursively
def sub_sets(sset):
    return subsets_recur([], sorted(sset))


def subsets_recur(current, sset):
    if sset:
        return subsets_recur(current, sset[1:]) + subsets_recur(
            current + [sset[0]], sset[1:])
    return [current]

def edges_duplicate_elimination(edges):
    edges_new = []
    for edge in edges:
        exists = False
        for edge_new in edges_new:
            if ((edge[0]==edge_new[0] and edge[1]==edge_new[1]) or (edge[0]==edge_new[1] and edge[1]==edge_new[0])):
                exists = True
                break
        if exists == False:
            edges_new.append(edge) 
    return edges_new


edges = []


def our_constraint(x):
    array = []
    for i in range(0, len(edges)):
        array.append(0)
    for value in x:
        counter = 0
        for edge in edges:
            for value1 in edge:
                if (value == value1):
                    array[counter] = 1
                    return_value = all(element == 1 for element in array)
                    if (return_value):
                        return True
            counter = counter + 1




def main():
    foo = check_output('./constraints', shell=True)
    input = foo.split()
    print(foo)
    length = input[0]

    v=[]
    for i in range(1,int(length) + 1):
        v.append(i)

    counter = 0
    edge = []
    for item in input[2:]:
        i = int(item)
        edge.append(i)
        counter = counter + 1
        if counter == 2:
            edges.append(edge)
            edge = []
            counter = 0

    problem = Problem()
    vertexes = sub_sets(v)
    problem.addVariable('vertexes', vertexes)
    problem.addConstraint(our_constraint, ['vertexes'])
    solutions = problem.getSolutions()

    minimum = solutions[0]['vertexes']
    minimum_length = len(solutions[0]['vertexes'])
    for solution in solutions[1:]:
        if len(solution['vertexes']) < minimum_length:
            minimum_length = len(solution['vertexes'])
            minimum = solution['vertexes']

    print ('Minimum vertex cover solution is: {}'.format(minimum))
  
if __name__== "__main__":
  main()