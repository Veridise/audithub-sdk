# UserPatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | 
**email** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.user_patch import UserPatch

# TODO update the JSON string below
json = "{}"
# create an instance of UserPatch from a JSON string
user_patch_instance = UserPatch.from_json(json)
# print the JSON string representation of the object
print(UserPatch.to_json())

# convert the object into a dict
user_patch_dict = user_patch_instance.to_dict()
# create an instance of UserPatch from a dict
user_patch_from_dict = UserPatch.from_dict(user_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


