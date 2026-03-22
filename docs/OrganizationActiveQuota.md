# OrganizationActiveQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date_from** | **datetime** |  | 
**date_to** | **datetime** |  | 
**cpu_minutes** | **int** |  | 
**storage_mb** | **int** |  | 

## Example

```python
from audithub_sdk.models.organization_active_quota import OrganizationActiveQuota

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationActiveQuota from a JSON string
organization_active_quota_instance = OrganizationActiveQuota.from_json(json)
# print the JSON string representation of the object
print(OrganizationActiveQuota.to_json())

# convert the object into a dict
organization_active_quota_dict = organization_active_quota_instance.to_dict()
# create an instance of OrganizationActiveQuota from a dict
organization_active_quota_from_dict = OrganizationActiveQuota.from_dict(organization_active_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


