# PicusV2Input


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**PicusV2Parameters**](PicusV2Parameters.md) | The parameters to pass to PicusV2 | 

## Example

```python
from audithub_sdk.models.picus_v2_input import PicusV2Input

# TODO update the JSON string below
json = "{}"
# create an instance of PicusV2Input from a JSON string
picus_v2_input_instance = PicusV2Input.from_json(json)
# print the JSON string representation of the object
print(PicusV2Input.to_json())

# convert the object into a dict
picus_v2_input_dict = picus_v2_input_instance.to_dict()
# create an instance of PicusV2Input from a dict
picus_v2_input_from_dict = PicusV2Input.from_dict(picus_v2_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


