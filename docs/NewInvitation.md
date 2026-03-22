# NewInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitee_email** | **str** | The email of the user to receive the invitation. The user can accept the invitation only using this email address | 
**invitee_name** | **str** |  | [optional] 
**valid_for_days** | **int** | Number of days an invitation is valid after its creation | [optional] [default to 7]
**custom_message** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.new_invitation import NewInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of NewInvitation from a JSON string
new_invitation_instance = NewInvitation.from_json(json)
# print the JSON string representation of the object
print(NewInvitation.to_json())

# convert the object into a dict
new_invitation_dict = new_invitation_instance.to_dict()
# create an instance of NewInvitation from a dict
new_invitation_from_dict = NewInvitation.from_dict(new_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


