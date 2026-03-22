# OnboardingRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the onboarding request. | 
**created_by** | **str** | The id of user that made the onboarding request. | 
**created_at** | **datetime** | The date that the onboarding request has been created. | 
**organization_id** | **int** |  | [optional] 
**approved_by** | **str** |  | [optional] 
**approved_at** | **datetime** |  | [optional] 

## Example

```python
from audithub_sdk.models.onboarding_request import OnboardingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OnboardingRequest from a JSON string
onboarding_request_instance = OnboardingRequest.from_json(json)
# print the JSON string representation of the object
print(OnboardingRequest.to_json())

# convert the object into a dict
onboarding_request_dict = onboarding_request_instance.to_dict()
# create an instance of OnboardingRequest from a dict
onboarding_request_from_dict = OnboardingRequest.from_dict(onboarding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


