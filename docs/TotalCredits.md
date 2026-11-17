# TotalCredits

An alternative way to specify credits. If provided, duration_months must also be provided and monthly_credits will be computed by dividing total_credits with duration_ months. You can't specify both this and monthly_credits together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from audithub_sdk.models.total_credits import TotalCredits

# TODO update the JSON string below
json = "{}"
# create an instance of TotalCredits from a JSON string
total_credits_instance = TotalCredits.from_json(json)
# print the JSON string representation of the object
print(TotalCredits.to_json())

# convert the object into a dict
total_credits_dict = total_credits_instance.to_dict()
# create an instance of TotalCredits from a dict
total_credits_from_dict = TotalCredits.from_dict(total_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


