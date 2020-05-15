# Author: Stratos mansalis

import numpy as np
import pandas as pd

def clean_NaN(df):

    """
        Clean the sentences from NaN (Not a Number) and empty rows.
        Note! Drop the unnecessary columns first and then use this function.

        Arguments
        ---------
        df: the given dataframe  

        Usage
        -----
        new_df = clean_rows(df)

        Returns
        -------
        A dataframe cleaned from empty rows or rows contain NaNs

        """
    
    
    # there are few nan as text values, not np.nan
    df = df.replace('nan', '') 
    df = df.replace('NaN', '')

    # replace field that's entirely space (or empty) with NaN
    df = df.replace(r'^\s*$', np.nan, regex=True)
    
    # total number of NaNs
    total_nan = df.isna().sum().sum()
    
    # total number of rows
    total_rows = df
    print('There are ',total_nan,' rows that contain NaN values.')
    print('Removing these rows ...')
    
    columns = df.columns.astype(str).tolist()
    
    df.dropna(subset=columns, inplace=True)
    print('Succesfully Deleted!')
    
    return df
