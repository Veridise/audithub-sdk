# UserAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**email** | **str** |  | 
**roles** | **List[str]** |  | 
**enabled** | **bool** |  | 
**created_at** | **datetime** |  | 
**organizations** | **List[int]** |  | 

## Example

```python
from audithub_sdk.models.user_admin import UserAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of UserAdmin from a JSON string
user_admin_instance = UserAdmin.from_json(json)
# print the JSON string representation of the object
print(UserAdmin.to_json())

# convert the object into a dict
user_admin_dict = user_admin_instance.to_dict()
# create an instance of UserAdmin from a dict
user_admin_from_dict = UserAdmin.from_dict(user_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


