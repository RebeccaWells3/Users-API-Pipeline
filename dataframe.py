import pandas as pd


def create_dataframe(fd):
    '''create dataframe'''
    df = pd.DataFrame(fd)

    return df



def load_to_sqlite(df,table_name, connection, if_exists):
    '''insert dataframe into sqlite table'''
    df.to_sql(table_name, connection, if_exists=if_exists, index=False)


