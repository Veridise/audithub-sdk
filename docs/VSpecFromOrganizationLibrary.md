# VSpecFromOrganizationLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'orglib']
**id** | **int** | The id of the V specification from the organization&#39;s library. | 

## Example

```python
from audithub_sdk.models.v_spec_from_organization_library import VSpecFromOrganizationLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of VSpecFromOrganizationLibrary from a JSON string
v_spec_from_organization_library_instance = VSpecFromOrganizationLibrary.from_json(json)
# print the JSON string representation of the object
print(VSpecFromOrganizationLibrary.to_json())

# convert the object into a dict
v_spec_from_organization_library_dict = v_spec_from_organization_library_instance.to_dict()
# create an instance of VSpecFromOrganizationLibrary from a dict
v_spec_from_organization_library_from_dict = VSpecFromOrganizationLibrary.from_dict(v_spec_from_organization_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


