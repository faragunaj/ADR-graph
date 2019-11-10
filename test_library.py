###
# Test for prediction library
###

#import the module
import EdgePrediction, json

#create a new instance
ep = EdgePrediction.EdgePrediction()

#load data from edge list
ep.CSV_to_graph(fname = 'data/data.csv', header = True, srcNameCol = 0, srcTypeCol = 1, tgtNameCol = 4, tgtTypeCol = 3, edgeTypeCol = 2)

#filter the source nodes in all graphs so that all the source nodes are common to all input graphs
#keep those nodes and all their edges
#create adjacency matrix
ep.preprocess()

#type of edge to predict
ep.to_predict = 'HAS_SIDE_EFFECT'

#the order can be important as if there are ties, the result found first is returned
#ties may make different predictions
ep.network_order = ['HAS_SIDE_EFFECT', 'DRUG_TARGETS', 'INDICATED_FOR']

#train the model
# target_name = "C0027849"
result = ep.predictAll(calculate_auc = True)

#predicted (unknown) causes of the target ADR
new_predictions = result['new_hits']
# print(new_predictions)

#the optimised weights from the model
weights = result['weights']

#the score for all drugs using the trained model
scores = ep.getScores(target_name, weights)
# print(scores)
