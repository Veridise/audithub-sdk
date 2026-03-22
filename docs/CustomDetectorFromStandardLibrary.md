# CustomDetectorFromStandardLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'stdlib']
**library_version** | **str** |  | [optional] 
**category** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from audithub_sdk.models.custom_detector_from_standard_library import CustomDetectorFromStandardLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDetectorFromStandardLibrary from a JSON string
custom_detector_from_standard_library_instance = CustomDetectorFromStandardLibrary.from_json(json)
# print the JSON string representation of the object
print(CustomDetectorFromStandardLibrary.to_json())

# convert the object into a dict
custom_detector_from_standard_library_dict = custom_detector_from_standard_library_instance.to_dict()
# create an instance of CustomDetectorFromStandardLibrary from a dict
custom_detector_from_standard_library_from_dict = CustomDetectorFromStandardLibrary.from_dict(custom_detector_from_standard_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


