# OrganizationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **int** |  | 
**start_time** | **datetime** | Inclusive start in UTC. A task starting exactly at this timestamp may be funded by this subscription.  | 
**end_time** | **datetime** |  | [optional] 
**duration_months** | **int** |  | [optional] 
**purchase_time** | **datetime** |  | 
**purchase_price** | **str** |  | 
**monthly_credits** | **str** |  | [optional] 
**total_credits** | **str** |  | [optional] 
**id** | **int** |  | 
**organization_id** | **int** |  | 
**user_id** | **str** |  | 
**canceled_time** | **datetime** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**stripe_latest_invoice_id** | **str** |  | [optional] 

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


