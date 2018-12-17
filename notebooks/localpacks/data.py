import pandas as pd

FILENAME= r'../data/box_data.csv'

def get_data(filename = FILENAME , parse_date = True, clean = True):
    '''    
    PARAMETERS
    ----------
    filename: integer (optional)
        path of data directory
    parse_datet: boolean (optional)
        if True, apply format of data column and returns it as pd.index
    clean: boolean (optional)
        if True, apply clean actions
    RETURN
    ------
    data: pandas.DataFrame
        data frame with contains de work data
    EXAMPLES
    --------
    df_clean= get_data( parse_date = True, clean = True) 
    '''
    
    df = pd.read_csv( filename, sep = ',')
    
    if parse_date == True:
        df.index = pd.to_datetime(df['install_time'], format='%Y-%m-%d %H:%M:%S') #parsing the date format and indexing
        del df['install_time'] #del the duplicate feature
    
    if clean == True:
        
        df = clean_data(df)
                
    return df
    
def clean_data(df):
    '''    
    PARAMETERS
    ----------
    df: pandas.DataFrame (required)
        data frame to apply clean actions
    RETURN
    ------
    df: pandas.DataFrame
        data frame with clean data
    '''
    
    df = df.dropna() #drop rows with NAN values
    df = df.drop_duplicates(df.columns[df.columns.isin(['user_id'])], keep = 'first') #work with only one user_id
    df = df[df.gender != 'unknown'] #drop gender with unkwown values
    df = df.loc[df.index > '2018-07-01'] #month filter
    
    return df