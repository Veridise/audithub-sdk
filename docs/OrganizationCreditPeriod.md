# OrganizationCreditPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | [**CreditSourceType**](CreditSourceType.md) |  | 
**source_id** | **int** |  | 
**period_start** | **datetime** |  | 
**period_end** | **datetime** |  | 
**consumed_credits** | **str** |  | 
**available_credits** | **str** |  | 

## Example

```python
from audithub_sdk.models.organization_credit_period import OrganizationCreditPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreditPeriod from a JSON string
organization_credit_period_instance = OrganizationCreditPeriod.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreditPeriod.to_json())

# convert the object into a dict
organization_credit_period_dict = organization_credit_period_instance.to_dict()
# create an instance of OrganizationCreditPeriod from a dict
organization_credit_period_from_dict = OrganizationCreditPeriod.from_dict(organization_credit_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


