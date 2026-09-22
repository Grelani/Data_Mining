from mintic.ensemble.random_forest import bootstrap_sample, build_id3_tree, build_random_forest, predict_ensemble
from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
car_evaluation = fetch_ucirepo(id=19) 
  
# data (as pandas dataframes) 
X = car_evaluation.data.features 
y = car_evaluation.data.targets 

X_sample,y_sample=bootstrap_sample(X,y,random_state=42)
tree = build_id3_tree(X_sample, y_sample)
forest = build_random_forest(X, y, n_trees=10, random_state=42)
predictions = predict_ensemble(forest, X)

print("Se ejecutó bien")
print("Primeras 10 predicciones:", predictions[:10])