# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**support_channel** | **str** |  | [optional] 
**user_limit** | **int** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**tools_only** | **bool** | Indicates if this organization is a tools-only organization. Tools-only organizations have no access to auditing features. | [optional] [default to False]
**id** | **int** |  | 
**plan_seats** | **int** |  | 
**extra_seats** | **int** |  | 
**manual_user_limit** | **int** |  | 
**gh_connected** | **bool** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from audithub_sdk.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


