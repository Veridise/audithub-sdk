# MyOrganization


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
**is_favorite** | **bool** |  | [optional] [default to False]

## Example

```python
from audithub_sdk.models.my_organization import MyOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of MyOrganization from a JSON string
my_organization_instance = MyOrganization.from_json(json)
# print the JSON string representation of the object
print(MyOrganization.to_json())

# convert the object into a dict
my_organization_dict = my_organization_instance.to_dict()
# create an instance of MyOrganization from a dict
my_organization_from_dict = MyOrganization.from_dict(my_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


