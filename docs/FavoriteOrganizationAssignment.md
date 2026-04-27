# FavoriteOrganizationAssignment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **int** |  | 

## Example

```python
from audithub_sdk.models.favorite_organization_assignment import FavoriteOrganizationAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of FavoriteOrganizationAssignment from a JSON string
favorite_organization_assignment_instance = FavoriteOrganizationAssignment.from_json(json)
# print the JSON string representation of the object
print(FavoriteOrganizationAssignment.to_json())

# convert the object into a dict
favorite_organization_assignment_dict = favorite_organization_assignment_instance.to_dict()
# create an instance of FavoriteOrganizationAssignment from a dict
favorite_organization_assignment_from_dict = FavoriteOrganizationAssignment.from_dict(favorite_organization_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


