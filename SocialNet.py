import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np
import seaborn as sns
import collections
import operator
import measure as me

#return neighbour list
def neighbors(sn_graph, node):
    return list(sn_graph.neighbors(node))


#Add and remove connection between nodes randomly
#Add new connection from each node by the probeblity
def perturbation_connection(sn_graph, prob_new_connection, prob_remove_connection):
    ins_connection = []
    del_connection = []
    for node in sn_graph.nodes():
        connected = [to__ for (from__, to__) in sn_graph.edges(node)]
        not_connected = [node__ for node__ in sn_graph.nodes() if not node__ in connected]
        #Add new connection
        if len(not_connected):
            if random.random() < prob_new_connection:
                new_connection = random.choice(not_connected)
                sn_graph.add_edge(node, new_connection)
                ins_connection.append((node, new_connection))
                not_connected.remove(new_connection)
                connected.append(new_connection)
        #Remove some connection
        if len(connected):
            if random.random() < prob_remove_connection:
                remove_connection = random.choice(connected)
                sn_graph.remove_edge(node, remove_connection)
                del_connection.append((node, remove_connection))
                connected.remove(remove_connection)
                not_connected.append(remove_connection)

    return del_connection, ins_connection

#Perturbation graph Algorithm
def run_algo(dataset_path):
    dataset = nx.read_gml(dataset_path)
    me.display_info(dataset)

    dataset_naive = nx.convert_node_labels_to_integers(dataset, first_label=1,ordering='default')#Naive
    
    nx.draw(dataset_naive, alpha=0.8, edge_color='black', node_color='green', with_labels=True, discard_old_labels=True)
    plt.figure(figsize=(20,20))
    plt.show()

    #Perturbation graph between 10% to 100%
    #100% is completly a random gaph so it loos all utility
    for persent in range(1,10):
        dataset_new = dataset_naive.copy()
        del_connection, new_connection = perturbation_connection(dataset_new, persent*0.1, persent*0.1)
        #removed connection
        nx.draw(dataset_naive, alpha=0.4, edge_color='red', node_color='red', with_labels=True, edgelist=del_connection)
        plt.figure(figsize=(20, 20))
        #new connection
        nx.draw(dataset_naive, alpha=0.8, edge_color='green', node_color='green', with_labels=True, edgelist=new_connection)
        plt.figure(figsize=(20, 20))
        #Graph him self
        nx.draw(dataset_new, alpha=0.8, edge_color='orange', node_color='orange', with_labels=True)
        plt.figure(figsize=(20, 20))
        #Just print the neighbours for a sample node to see the change
        print(" neighbours = ", neighbors(dataset_new, 1))
        #info
        me.display_info(dataset_new)

    print("H0 (node): ",dataset_naive.node[1])
    print("H1 (degree of node): ",dataset_naive.degree(1))
    print("H2 (degree of neighbors): ",list(dataset_naive.degree((dataset_naive.neighbors(1)))))  # H2 queary

    plt.show()


def menu_select():
    print("*********** Social network graph anonymization ***********")
    print("Enter 1 for perturbation")
    menu = input("Enter Number : ")
    dataset=input("Dataset path(leave blank inorder to use default dataset):")
    if dataset=='':
        dataset='dataset.gml'
    if menu=='1':
        run_algo(dataset)


if __name__ == '__main__':
    menu_select()
