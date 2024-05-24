import pandas as pd
# First attmempt
def getDataframeSize(players: pd.DataFrame) -> list[int]:
    rows = len(players.axes[0])
 
    # computing number of columns
    cols = len(players.axes[1])
    return [rows, cols]

def get_dataframe_size(players: pd.DataFrame) -> list[int]:
    return list(players.shape)