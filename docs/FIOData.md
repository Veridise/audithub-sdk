# FIOData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_digest** | **int** |  | 
**analysis_result_id** | **str** |  | 
**is_filtered** | **bool** |  | 
**data** | **Dict[str, object]** |  | [optional] 
**actions** | [**List[FindingAction]**](FindingAction.md) |  | 

## Example

```python
from audithub_sdk.models.fio_data import FIOData

# TODO update the JSON string below
json = "{}"
# create an instance of FIOData from a JSON string
fio_data_instance = FIOData.from_json(json)
# print the JSON string representation of the object
print(FIOData.to_json())

# convert the object into a dict
fio_data_dict = fio_data_instance.to_dict()
# create an instance of FIOData from a dict
fio_data_from_dict = FIOData.from_dict(fio_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


