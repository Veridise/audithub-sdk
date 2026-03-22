# ActiveOrganizationUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registered** | [**List[RegisteredUser]**](RegisteredUser.md) |  | 
**invited** | [**List[InvitedUser]**](InvitedUser.md) |  | 
**users** | [**Dict[str, IncludedUserInfo]**](IncludedUserInfo.md) |  | 

## Example

```python
from audithub_sdk.models.active_organization_users import ActiveOrganizationUsers

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveOrganizationUsers from a JSON string
active_organization_users_instance = ActiveOrganizationUsers.from_json(json)
# print the JSON string representation of the object
print(ActiveOrganizationUsers.to_json())

# convert the object into a dict
active_organization_users_dict = active_organization_users_instance.to_dict()
# create an instance of ActiveOrganizationUsers from a dict
active_organization_users_from_dict = ActiveOrganizationUsers.from_dict(active_organization_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


