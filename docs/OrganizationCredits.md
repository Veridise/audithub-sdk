# OrganizationCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[OrganizationSubscriptionLight]**](OrganizationSubscriptionLight.md) |  | 
**extra_credits** | [**List[OrganizationExtra]**](OrganizationExtra.md) |  | 
**credits_per_period** | [**List[OrganizationCreditPeriod]**](OrganizationCreditPeriod.md) |  | 
**tasks** | [**List[CreditTask]**](CreditTask.md) |  | 

## Example

```python
from audithub_sdk.models.organization_credits import OrganizationCredits

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCredits from a JSON string
organization_credits_instance = OrganizationCredits.from_json(json)
# print the JSON string representation of the object
print(OrganizationCredits.to_json())

# convert the object into a dict
organization_credits_dict = organization_credits_instance.to_dict()
# create an instance of OrganizationCredits from a dict
organization_credits_from_dict = OrganizationCredits.from_dict(organization_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


