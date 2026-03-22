# NewOrganizationPackage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**org_restrictions** | [**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md) |  | [optional] 
**user_restrictions** | [**List[UserAccessRestriction]**](UserAccessRestriction.md) |  | [optional] 
**user_limit** | **int** |  | [optional] 
**subscription** | [**PackageSubscription**](PackageSubscription.md) |  | 
**org_name** | **str** | Template name for creating new organization. Available keywords to be replaced are user attributes &#39;name&#39;, &#39;email&#39;, &#39;id&#39; and &#39;timestamp&#39; that the organization gets created | [optional] [default to 'demo-organization-{email}']
**name** | **str** |  | 

## Example

```python
from audithub_sdk.models.new_organization_package import NewOrganizationPackage

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrganizationPackage from a JSON string
new_organization_package_instance = NewOrganizationPackage.from_json(json)
# print the JSON string representation of the object
print(NewOrganizationPackage.to_json())

# convert the object into a dict
new_organization_package_dict = new_organization_package_instance.to_dict()
# create an instance of NewOrganizationPackage from a dict
new_organization_package_from_dict = NewOrganizationPackage.from_dict(new_organization_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


