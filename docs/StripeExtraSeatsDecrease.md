# StripeExtraSeatsDecrease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_seats** | **int** | Number of extra seats to remove. Must be greater than 0. | 

## Example

```python
from audithub_sdk.models.stripe_extra_seats_decrease import StripeExtraSeatsDecrease

# TODO update the JSON string below
json = "{}"
# create an instance of StripeExtraSeatsDecrease from a JSON string
stripe_extra_seats_decrease_instance = StripeExtraSeatsDecrease.from_json(json)
# print the JSON string representation of the object
print(StripeExtraSeatsDecrease.to_json())

# convert the object into a dict
stripe_extra_seats_decrease_dict = stripe_extra_seats_decrease_instance.to_dict()
# create an instance of StripeExtraSeatsDecrease from a dict
stripe_extra_seats_decrease_from_dict = StripeExtraSeatsDecrease.from_dict(stripe_extra_seats_decrease_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


