# UserAccessRestriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | **str** |  | 
**value** | **int** |  | [optional] 
**detector** | **str** |  | [optional] 
**project_id** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.user_access_restriction import UserAccessRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of UserAccessRestriction from a JSON string
user_access_restriction_instance = UserAccessRestriction.from_json(json)
# print the JSON string representation of the object
print(UserAccessRestriction.to_json())

# convert the object into a dict
user_access_restriction_dict = user_access_restriction_instance.to_dict()
# create an instance of UserAccessRestriction from a dict
user_access_restriction_from_dict = UserAccessRestriction.from_dict(user_access_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


