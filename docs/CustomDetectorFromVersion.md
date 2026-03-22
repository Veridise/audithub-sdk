# CustomDetectorFromVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'version']
**relative_path** | **str** | Relative path from the version archive&#39;s root | 

## Example

```python
from audithub_sdk.models.custom_detector_from_version import CustomDetectorFromVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDetectorFromVersion from a JSON string
custom_detector_from_version_instance = CustomDetectorFromVersion.from_json(json)
# print the JSON string representation of the object
print(CustomDetectorFromVersion.to_json())

# convert the object into a dict
custom_detector_from_version_dict = custom_detector_from_version_instance.to_dict()
# create an instance of CustomDetectorFromVersion from a dict
custom_detector_from_version_from_dict = CustomDetectorFromVersion.from_dict(custom_detector_from_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


