# StripeExtraSeatsIncrease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_seats** | **int** | Number of extra seats to add. Must be greater than 0. | 

## Example

```python
from audithub_sdk.models.stripe_extra_seats_increase import StripeExtraSeatsIncrease

# TODO update the JSON string below
json = "{}"
# create an instance of StripeExtraSeatsIncrease from a JSON string
stripe_extra_seats_increase_instance = StripeExtraSeatsIncrease.from_json(json)
# print the JSON string representation of the object
print(StripeExtraSeatsIncrease.to_json())

# convert the object into a dict
stripe_extra_seats_increase_dict = stripe_extra_seats_increase_instance.to_dict()
# create an instance of StripeExtraSeatsIncrease from a dict
stripe_extra_seats_increase_from_dict = StripeExtraSeatsIncrease.from_dict(stripe_extra_seats_increase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


