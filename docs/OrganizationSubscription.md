# OrganizationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_type** | **str** | Subscription type can be S for subscription and E for extension. | [optional] [default to 'S']
**from_date** | **datetime** |  | 
**to_date** | **datetime** |  | 
**monthly_cpu_minutes** | **int** |  | [optional] 
**storage_mb** | **int** |  | [optional] 
**package_name** | **str** |  | [optional] 
**enforce_monthly_resource_consumption** | **bool** | It indicates how to enforce quotas: a) when True, monthly quotas can only be consumed within the specific month, and b) when False, quota are freely consumed any time within the subscription time window | [optional] [default to False]
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**last_updated_at** | **datetime** |  | 
**last_updated_by** | **str** |  | 

## Example

```python
from audithub_sdk.models.organization_subscription import OrganizationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationSubscription from a JSON string
organization_subscription_instance = OrganizationSubscription.from_json(json)
# print the JSON string representation of the object
print(OrganizationSubscription.to_json())

# convert the object into a dict
organization_subscription_dict = organization_subscription_instance.to_dict()
# create an instance of OrganizationSubscription from a dict
organization_subscription_from_dict = OrganizationSubscription.from_dict(organization_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


