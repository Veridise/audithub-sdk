# OrganizationAccessRestriction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function** | **str** |  | 
**value** | **int** |  | [optional] 
**detector** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.organization_access_restriction import OrganizationAccessRestriction

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationAccessRestriction from a JSON string
organization_access_restriction_instance = OrganizationAccessRestriction.from_json(json)
# print the JSON string representation of the object
print(OrganizationAccessRestriction.to_json())

# convert the object into a dict
organization_access_restriction_dict = organization_access_restriction_instance.to_dict()
# create an instance of OrganizationAccessRestriction from a dict
organization_access_restriction_from_dict = OrganizationAccessRestriction.from_dict(organization_access_restriction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


