# CustomDetectorFromOrganizationLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'orglib']
**id** | **int** | The id of the Custom Detector from the organization&#39;s library. | 

## Example

```python
from audithub_sdk.models.custom_detector_from_organization_library import CustomDetectorFromOrganizationLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDetectorFromOrganizationLibrary from a JSON string
custom_detector_from_organization_library_instance = CustomDetectorFromOrganizationLibrary.from_json(json)
# print the JSON string representation of the object
print(CustomDetectorFromOrganizationLibrary.to_json())

# convert the object into a dict
custom_detector_from_organization_library_dict = custom_detector_from_organization_library_instance.to_dict()
# create an instance of CustomDetectorFromOrganizationLibrary from a dict
custom_detector_from_organization_library_from_dict = CustomDetectorFromOrganizationLibrary.from_dict(custom_detector_from_organization_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


