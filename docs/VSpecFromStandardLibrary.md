# VSpecFromStandardLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'stdlib']
**library_version** | **str** |  | [optional] 
**category** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from audithub_sdk.models.v_spec_from_standard_library import VSpecFromStandardLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of VSpecFromStandardLibrary from a JSON string
v_spec_from_standard_library_instance = VSpecFromStandardLibrary.from_json(json)
# print the JSON string representation of the object
print(VSpecFromStandardLibrary.to_json())

# convert the object into a dict
v_spec_from_standard_library_dict = v_spec_from_standard_library_instance.to_dict()
# create an instance of VSpecFromStandardLibrary from a dict
v_spec_from_standard_library_from_dict = VSpecFromStandardLibrary.from_dict(v_spec_from_standard_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


