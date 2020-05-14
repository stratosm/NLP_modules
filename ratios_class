# Author: Stratos Mansalis

import pandas as pd


def ratio_(df, cl):

    """
        Calculates the frequency by class of the dataframe

        Arguments
        ---------
        df: the given dataframe
        cl: the name of the class       

        Usage
        -----
        df = ratio_(data, 'class')

        Returns
        -------
        A dataframe with two columns:
        - the first named 'Class' contains the name of each class.
        - the second named 'Total' contains the frequency

        """

    df = df[cl].value_counts()
    df = df.to_frame()
    df.reset_index(level=0, inplace=True)
    df.columns = ['Class', 'Total']
       
    return df
