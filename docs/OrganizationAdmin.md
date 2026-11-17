# OrganizationAdmin


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
**deleted** | **bool** | If true, then the Organization has been soft-deleted. | 

## Example

```python
from audithub_sdk.models.organization_admin import OrganizationAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAdmin from a JSON string
organization_admin_instance = OrganizationAdmin.from_json(json)
# print the JSON string representation of the object
print(OrganizationAdmin.to_json())

# convert the object into a dict
organization_admin_dict = organization_admin_instance.to_dict()
# create an instance of OrganizationAdmin from a dict
organization_admin_from_dict = OrganizationAdmin.from_dict(organization_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


