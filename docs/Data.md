# Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**start_time** | **datetime** | New inclusive start in UTC. Task funding uses start_time &lt;&#x3D; task.started_at &lt; end_time. The entire subscription must have no task allocations; all periods are regenerated. | 
**end_time** | **datetime** |  | [optional] 
**monthly_credits** | [**MonthlyCredits2**](MonthlyCredits2.md) |  | 

## Example

```python
from audithub_sdk.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


