# HintFromOrganizationLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'orglib']
**id** | **int** | The id of the Hint from the organization&#39;s library. | 

## Example

```python
from audithub_sdk.models.hint_from_organization_library import HintFromOrganizationLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of HintFromOrganizationLibrary from a JSON string
hint_from_organization_library_instance = HintFromOrganizationLibrary.from_json(json)
# print the JSON string representation of the object
print(HintFromOrganizationLibrary.to_json())

# convert the object into a dict
hint_from_organization_library_dict = hint_from_organization_library_instance.to_dict()
# create an instance of HintFromOrganizationLibrary from a dict
hint_from_organization_library_from_dict = HintFromOrganizationLibrary.from_dict(hint_from_organization_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


