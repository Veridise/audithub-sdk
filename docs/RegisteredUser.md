# RegisteredUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**ignored_for_quota** | **bool** |  | [optional] [default to False]

## Example

```python
from audithub_sdk.models.registered_user import RegisteredUser

# TODO update the JSON string below
json = "{}"
# create an instance of RegisteredUser from a JSON string
registered_user_instance = RegisteredUser.from_json(json)
# print the JSON string representation of the object
print(RegisteredUser.to_json())

# convert the object into a dict
registered_user_dict = registered_user_instance.to_dict()
# create an instance of RegisteredUser from a dict
registered_user_from_dict = RegisteredUser.from_dict(registered_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


