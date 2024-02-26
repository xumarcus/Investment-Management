from openbb import obb
import pandas as pd
obb.account.login(pat="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdXRoX3Rva2VuIjoib2gwQWFoV0M2YTlLMDdnNHRqemhZOFZHdGs4OUVYYm5sM0xuZVRyOCIsImV4cCI6MTczOTE4MzQ1N30.0fJdlhtST1wAh8lF7NALrG370QDRbwEdJp0OeoUN0CY")

output = obb.equity.price.historical("AAPL")
df = output.to_dataframe()
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(df)

