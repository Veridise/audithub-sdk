# HintFromStandardLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'stdlib']
**library_version** | **str** |  | [optional] 
**category** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from audithub_sdk.models.hint_from_standard_library import HintFromStandardLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of HintFromStandardLibrary from a JSON string
hint_from_standard_library_instance = HintFromStandardLibrary.from_json(json)
# print the JSON string representation of the object
print(HintFromStandardLibrary.to_json())

# convert the object into a dict
hint_from_standard_library_dict = hint_from_standard_library_instance.to_dict()
# create an instance of HintFromStandardLibrary from a dict
hint_from_standard_library_from_dict = HintFromStandardLibrary.from_dict(hint_from_standard_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


