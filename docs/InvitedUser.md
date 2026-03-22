# InvitedUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | 
**invited_at** | **datetime** |  | 
**invited_by** | **str** |  | 
**expires_at** | **datetime** |  | 

## Example

```python
from audithub_sdk.models.invited_user import InvitedUser

# TODO update the JSON string below
json = "{}"
# create an instance of InvitedUser from a JSON string
invited_user_instance = InvitedUser.from_json(json)
# print the JSON string representation of the object
print(InvitedUser.to_json())

# convert the object into a dict
invited_user_dict = invited_user_instance.to_dict()
# create an instance of InvitedUser from a dict
invited_user_from_dict = InvitedUser.from_dict(invited_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


