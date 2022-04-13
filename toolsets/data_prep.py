import pandas as pd
import numpy as np
def make_split_index(data, train_ratio = 0.8, test_ratio = 0.2):
    #     first check if the dataframe has a split index or not
    if 'split_index' in data.columns:
        print("this dataset has split index already")
    else:
        split_index = np.random.choice([1, 2], size=len(data), p=[train_ratio, test_ratio])
        data['split_index']=split_index
    return(data)

def dataset_prep(data):
    original_colnames = list(data.columns)
    data.columns = map(str.lower, data.columns)
    smi_cols = list(data.loc[:, data.columns.str.startswith('smi')].columns)
    rt_cols = list(data.loc[:, data.columns.str.startswith(('retention','rt'))].columns)
    if (len(smi_cols)>1 or len(rt_cols)>1):
        print("you have passed a dataframe with more than 1 potential smiles code/rention time column; plz try again")
        return(np.NAN)
    index_smi =data.columns.get_loc(smi_cols[0])
    index_rt =data.columns.get_loc(rt_cols[0])
    original_colnames[index_smi] = 'SMILES'
    original_colnames[index_rt] = 'retention_time'
    data.columns = original_colnames
    return(data)


# def pre_process_data(data):
#     # change column name if needed
#     count = 0
#     count2 = 0
#     for col in data.columns:
#         data.columns = map(str.lower, data.columns)
#         if 'smi' in col:
#             smi_cols = [col for col in data.columns if 'smi' in col]
#             if len(smi_cols) > 1:
#                 print('Error, more than one column of smiles code in dataset')
#             else:
#                 column_name = smi_cols[0]
#                 smi_index = data.columns.get_loc(column_name)
#                 data.columns.values[smi_index] = 'smiles'
#         else:
#             count = count + 1
#     if count == len(data.columns):
#         print('no smiles code in this dataset')
#     for col in data.columns:
#         data.columns = map(str.lower, data.columns)
#         if any(s in col for s in ['rt', 'ret']):
#             rt_cols = [col for col in data.columns if any(s in col for s in ['rt', 're'])]
#             if len(rt_cols) > 1:
#                 print('Error, more than one column of retention time in dataset')
#             else:
#                 rt_column_name = rt_cols[0]
#                 rt_index = data.columns.get_loc(rt_column_name)
#                 data.columns.values[rt_index] = 'rt'
#         else:
#             count2 = count2 + 1
#     if count2 == len(data.columns):
#         print('no retention time in this dataset')
#     return(data)