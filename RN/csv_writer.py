from pandas import DataFrame, read_csv
from tensorflow.python.lib.io.file_io import file_exists

def write_data_to_table (columns_and_values: dict, unique_identifier: str, table_path:str, write_over: bool = True) -> None:
        """
            Obs: All the dict data has to be str or number.

            columns_and_values:
                A dict with label and data

            unique_identifier:
                Column name that has unique values

            table_path:
                Path of csv file to save and load
        """
        new_data = DataFrame([columns_and_values])
        new_data.set_index(unique_identifier, inplace=True)

        if file_exists(table_path):
            dataframe = read_csv(table_path, index_col=0)
        else:
            dataframe = DataFrame(columns = columns_and_values.keys())
            dataframe.set_index(unique_identifier, inplace=True)

        if dataframe.empty:
            dataframe = dataframe.append(new_data)

        else: 
            if columns_and_values[unique_identifier] in dataframe.index and write_over: # checks if the table has data with the same unique identifier
                index = columns_and_values.pop(unique_identifier)
                dataframe.loc[dataframe.index == index, list(columns_and_values.keys())] = list(columns_and_values.values())
                #dataframe.at[dataframe[unique_identifier] == columns_and_values[unique_identifier], columns_and_values.keys()] = columns_and_values.values() 
                # and subscribe in the line
            else:
                if not (columns_and_values[unique_identifier] in dataframe.index):
                    dataframe = dataframe.append(new_data)

        if dataframe.index.name != unique_identifier:
            dataframe.set_index(unique_identifier, inplace=True)
        dataframe.to_csv(table_path)