# SubscriptionPlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | 
**monthly_credits** | **str** | Credits per month for paid subscriptions, or a one-time credit grant for free subscriptions. | 
**enforce_monthly_quota_bound** | **bool** | Grant credits per month without rollover. | 
**prohibit_ai_engineer_access** | **bool** |  | 
**user_limit** | **int** |  | [optional] 
**project_limit** | **int** |  | [optional] 
**org_restrictions** | [**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md) |  | [optional] 
**is_free** | **bool** | Identifies the free plan. Only one free plan is allowed. | [optional] [default to False]
**is_enterprise** | **bool** | Identifies an enterprise plan. | [optional] [default to False]
**price** | **str** |  | [optional] 
**id** | **int** |  | 
**supports_extra_seats** | **bool** | Indicates whether the plan supports extra seats. If True, the plan can be upgraded with extra seats. If False, the plan cannot be upgraded with extra seats. | [optional] [default to False]

## Example

```python
from audithub_sdk.models.subscription_plan import SubscriptionPlan

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPlan from a JSON string
subscription_plan_instance = SubscriptionPlan.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPlan.to_json())

# convert the object into a dict
subscription_plan_dict = subscription_plan_instance.to_dict()
# create an instance of SubscriptionPlan from a dict
subscription_plan_from_dict = SubscriptionPlan.from_dict(subscription_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


