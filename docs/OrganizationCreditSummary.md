# OrganizationCreditSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** | Credits granted in the selected periods; -1 means unlimited. | 
**consumed** | **str** | Credits consumed or reserved by tasks in the selected periods. | 
**available** | **str** | Unconsumed credits in the selected periods, clamped to zero per period; -1 means unlimited. | 

## Example

```python
from audithub_sdk.models.organization_credit_summary import OrganizationCreditSummary

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCreditSummary from a JSON string
organization_credit_summary_instance = OrganizationCreditSummary.from_json(json)
# print the JSON string representation of the object
print(OrganizationCreditSummary.to_json())

# convert the object into a dict
organization_credit_summary_dict = organization_credit_summary_instance.to_dict()
# create an instance of OrganizationCreditSummary from a dict
organization_credit_summary_from_dict = OrganizationCreditSummary.from_dict(organization_credit_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


