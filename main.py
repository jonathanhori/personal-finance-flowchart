#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 14:34:23 2019

@author: jonathanhori

Implement interactive flowchart:
https://www.reddit.com/r/personalfinance/comments/4gdlu9/how_to_prioritize
_spending_your_money_a_flowchart/
    
"""

import os
os.chdir('/Users/jonathanhori/Desktop/personal-finace-flowchart')
import pandas as pd

node_file = 'nodes.xlsx'

###############################################################################
class Node:
    def __init__(self, id_num, title, description, phase, prior):
        self.prior = prior                     # list
        self.next = None                       # list
        self.id = id_num                       # int
        self.type = None                       # string
        self.title = title                     # string
        self.description = description         # string
        self.phase = phase                     # int
        self.prior_answer = None               # bool
        self.next_terminal = None              # bool
        
    def __repr__(self):
        return 'Node {id}: {title}'.format(id=self.id, title=self.title)
    
    def __str__(self):
        return 'Node {id}: {title}'.format(id=self.id, title=self.title)
    
    def prompt(self):
        return self.title
        
    
class Question(Node):
    def __init__(self, id_num, title, description, phase, prior):
        super().__init__(id_num, title, description, phase, prior)
        self.next_yes = None
        self.next_no = None
        
    def prompt(self):
        return input(self.title)
    
    def get_next(self, answer):
        answer = answer.lower()
        if answer in ['yes', 'y']:
            return self.next_yes
        else:
            return self.next_no
    
        
class Graph:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        """Adds one node to the existing graph from a line of the file"""
        if self.head is None:
            self.head = node
        else:
            return
        
    def return_node(self, node_id):
        """Returns a pointer to the node with the given id number"""
        return
        
    def from_dict(self, flowchart_dict):
        id = 0
        """Creates a flowchart graph from a pre-existing dict of nodes"""
        while id >= 0:  # Node -1 is the beginning and end of the chart
            current_node = flowchart_dict[id]
        return

###############################################################################
def read_data(data_file):
    file = pd.read_excel(data_file)
    file.columns = [x.lower() for x in list(file)]
    return file


def create_node(data_row, chart_dict):
    question_status = data_row['question']
    if question_status == 1:
        graph_node = Question(data_row['id'], data_row['title'], \
                          data_row['description'], data_row['phase'], \
                          data_row['previous'])
        graph_node.next_yes = data_row['next_yes']
        graph_node.next_no = data_row['next_no']
    else:
        graph_node = Node(data_row['id'], data_row['title'], \
                          data_row['description'], data_row['phase'], \
                          data_row['previous'])
        graph_node.next = data_row['next']
    chart_dict[(graph_node.id)] = graph_node
    
    return graph_node
        

def create_flowchart_dict(node_dataframe):
    flowchart = dict()
    node_dataframe.apply(lambda x: create_node(x, flowchart), axis=1)
    return flowchart

###############################################################################
if __name__ == "__main__":
    node_dataframe = read_data(node_file)
    flowchart = create_flowchart(node_dataframe)