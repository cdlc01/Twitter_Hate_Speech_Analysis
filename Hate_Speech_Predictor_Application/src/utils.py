import pandas as pd
import pickle

def extract_feature_values(data):
    """ Given a params dict, return the values for feeding into a model"""
    
    #with open('src/feature_names.pkl', 'rb') as f:
        #expected_features = pickle.load(f)
    
    #EXPECTED_FEATURES = expected_features
    
    #values = []
    #for feature in EXPECTED_FEATURES:
        #if feature in data:
            #values.append(1)
        #else:
            #values.append(0)
            
    #new_values = [values]
    
    #return pd.DataFrame(new_values, columns=EXPECTED_FEATURES)
    
    return [[data]]
