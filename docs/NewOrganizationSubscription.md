# NewOrganizationSubscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_id** | **int** |  | 
**start_time** | **datetime** | Inclusive start in UTC. A task starting exactly at this timestamp may be funded by this subscription.  | 
**end_time** | **datetime** |  | [optional] 
**duration_months** | **int** |  | [optional] 
**purchase_time** | **datetime** |  | 
**purchase_price** | [**PurchasePrice**](PurchasePrice.md) |  | 
**monthly_credits** | [**MonthlyCredits**](MonthlyCredits.md) |  | [optional] 
**total_credits** | [**TotalCredits**](TotalCredits.md) |  | [optional] 

## Example

```python
from audithub_sdk.models.new_organization_subscription import NewOrganizationSubscription

# TODO update the JSON string below
json = "{}"
# create an instance of NewOrganizationSubscription from a JSON string
new_organization_subscription_instance = NewOrganizationSubscription.from_json(json)
# print the JSON string representation of the object
print(NewOrganizationSubscription.to_json())

# convert the object into a dict
new_organization_subscription_dict = new_organization_subscription_instance.to_dict()
# create an instance of NewOrganizationSubscription from a dict
new_organization_subscription_from_dict = NewOrganizationSubscription.from_dict(new_organization_subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


