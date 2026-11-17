# OrganizationSubscriptionLight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**plan_id** | **int** |  | 
**start_time** | **datetime** |  | 
**end_time** | **datetime** |  | 
**monthly_credits** | **str** |  | 
**enforce_monthly_quota_bound** | **bool** |  | 

## Example

```python
from audithub_sdk.models.organization_subscription_light import OrganizationSubscriptionLight

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSubscriptionLight from a JSON string
organization_subscription_light_instance = OrganizationSubscriptionLight.from_json(json)
# print the JSON string representation of the object
print(OrganizationSubscriptionLight.to_json())

# convert the object into a dict
organization_subscription_light_dict = organization_subscription_light_instance.to_dict()
# create an instance of OrganizationSubscriptionLight from a dict
organization_subscription_light_from_dict = OrganizationSubscriptionLight.from_dict(organization_subscription_light_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


