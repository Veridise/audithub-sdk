# OrganizationQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_quota** | [**OrganizationActiveQuota**](OrganizationActiveQuota.md) |  | 

## Example

```python
from audithub_sdk.models.organization_quota import OrganizationQuota

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationQuota from a JSON string
organization_quota_instance = OrganizationQuota.from_json(json)
# print the JSON string representation of the object
print(OrganizationQuota.to_json())

# convert the object into a dict
organization_quota_dict = organization_quota_instance.to_dict()
# create an instance of OrganizationQuota from a dict
organization_quota_from_dict = OrganizationQuota.from_dict(organization_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


