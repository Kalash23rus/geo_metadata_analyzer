import pandas as pd

def transform_dataframe_to_dict(df):
    column_name = 0
    result_dict = {}
    current_key = None
    current_sample_key = None

    for index, row in df.iterrows():
        if row[column_name].startswith("^"):
            key_value = row[column_name].split("=")
            current_key = key_value[0][1:].strip()  # remove "^" from key
            if current_key == "SAMPLE":
                current_sample_key = key_value[1].strip()
                if current_key not in result_dict:
                    result_dict[current_key] = {}
                result_dict[current_key][current_sample_key] = {}
            else:
                if current_key not in result_dict:
                    result_dict[current_key] = {}
        elif row[column_name].startswith("!") and current_key:
            key_value = row[column_name].split("=")
            if len(key_value) == 2:
                if current_key == "SAMPLE":
                    result_dict[current_key][current_sample_key][key_value[0][1:].strip()] = key_value[1].strip()  # remove "!" from key
                else:
                    result_dict[current_key][key_value[0][1:].strip()] = key_value[1].strip()  # remove "!" from key

    return result_dict
# usage
url = 'ftp.ncbi.nlm.nih.gov/geo/series/GSE113nnn/GSE113264/soft/GSE113264_family.soft.gz'
df = pd.read_csv(url,sep='\t',header=None)
result_dict = transform_dataframe_to_dict(df)
