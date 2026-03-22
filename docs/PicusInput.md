# PicusInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | An optional name for this task. If not specified, the current time in UTC will be used. | [optional] 
**parameters** | [**PicusParameters**](PicusParameters.md) | The parameters to pass to Picus | 

## Example

```python
from audithub_sdk.models.picus_input import PicusInput

# TODO update the JSON string below
json = "{}"
# create an instance of PicusInput from a JSON string
picus_input_instance = PicusInput.from_json(json)
# print the JSON string representation of the object
print(PicusInput.to_json())

# convert the object into a dict
picus_input_dict = picus_input_instance.to_dict()
# create an instance of PicusInput from a dict
picus_input_from_dict = PicusInput.from_dict(picus_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


