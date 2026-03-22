# UserToOrganizationAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 

## Example

```python
from audithub_sdk.models.user_to_organization_assignment import UserToOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of UserToOrganizationAssignment from a JSON string
user_to_organization_assignment_instance = UserToOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(UserToOrganizationAssignment.to_json())

# convert the object into a dict
user_to_organization_assignment_dict = user_to_organization_assignment_instance.to_dict()
# create an instance of UserToOrganizationAssignment from a dict
user_to_organization_assignment_from_dict = UserToOrganizationAssignment.from_dict(user_to_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


