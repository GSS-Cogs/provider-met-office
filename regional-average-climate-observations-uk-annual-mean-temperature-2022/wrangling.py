import click
import pandas as pd
import numpy as np
import math
from pathlib import Path

@click.command()
@click.argument("input", type=click.Path(exists=True, path_type=Path))
@click.option("--output", default=Path("./output.csv"), type=click.Path(path_type=Path))
def wrangle(input: Path(), output: Path()) -> None:

    df = pd.read_csv("raw.csv")

    df['Measure'] = df.apply(
    lambda x: 'Annual Mean Temperature (Trend)' if 'trend' in x['Geography'] 
                else 'Annual Mean Temperature', axis=1)

    # df['Geography'] = df['Geography'].apply(lambda x: 'K02000001' if 'uk' in x
    #                                     else ('N92000002' if 'northern-ireland' in x
    #                                           else ('E92000001' if 'england' in x
    #                                                 else ('S92000003' if 'scotland' in x
    #                                                       else ('W92000004' if 'wales' in x else x)))))
    
    df['Geography'] = df['Geography'].apply(lambda x: 'United Kingdom' if 'uk' in x
                                        else ('Northern Ireland' if 'northern-ireland' in x
                                              else ('England' if 'england' in x
                                                    else ('Scotland' if 'scotland' in x
                                                          else ('Wales' if 'wales' in x else x)))))
    
    df = df.rename(columns={'Year': 'Period', 'Value': 'Observation'})

    df = df[['Period', 'Geography', 'Measure', 'Observation']] 

    df.to_csv(output, index=False)
    return

if __name__ == "__main__":
    wrangle()