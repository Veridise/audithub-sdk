# NewSubscriptionPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**monthly_credits** | [**MonthlyCredits1**](MonthlyCredits1.md) |  | 
**enforce_monthly_quota_bound** | **bool** | Grant credits per month without rollover. | 
**prohibit_ai_engineer_access** | **bool** |  | 
**user_limit** | **int** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**org_restrictions** | [**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md) |  | [optional] 
**is_free** | **bool** | Identifies the free plan. Only one free plan is allowed. | [optional] [default to False]
**is_enterprise** | **bool** | Identifies an enterprise plan. | [optional] [default to False]
**price** | [**Price**](Price.md) |  | [optional] 
**stripe_price_id** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.new_subscription_plan import NewSubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of NewSubscriptionPlan from a JSON string
new_subscription_plan_instance = NewSubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(NewSubscriptionPlan.to_json())

# convert the object into a dict
new_subscription_plan_dict = new_subscription_plan_instance.to_dict()
# create an instance of NewSubscriptionPlan from a dict
new_subscription_plan_from_dict = NewSubscriptionPlan.from_dict(new_subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


