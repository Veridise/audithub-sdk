# PackageData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_name** | **str** |  | 
**user_limit** | **int** |  | 
**projects** | [**List[ProjectData]**](ProjectData.md) |  | 
**org_restrictions** | [**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md) |  | 
**user_restrictions** | [**List[UserAccessRestriction]**](UserAccessRestriction.md) |  | 
**subscription** | [**PackageSubscription**](PackageSubscription.md) |  | 

## Example

```python
from audithub_sdk.models.package_data import PackageData

# TODO update the JSON string below
json = "{}"
# create an instance of PackageData from a JSON string
package_data_instance = PackageData.from_json(json)
# print the JSON string representation of the object
print(PackageData.to_json())

# convert the object into a dict
package_data_dict = package_data_instance.to_dict()
# create an instance of PackageData from a dict
package_data_from_dict = PackageData.from_dict(package_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


