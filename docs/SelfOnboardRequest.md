# SelfOnboardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 
**onboarding_package** | **str** |  | 

## Example

```python
from audithub_sdk.models.self_onboard_request import SelfOnboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SelfOnboardRequest from a JSON string
self_onboard_request_instance = SelfOnboardRequest.from_json(json)
# print the JSON string representation of the object
print(SelfOnboardRequest.to_json())

# convert the object into a dict
self_onboard_request_dict = self_onboard_request_instance.to_dict()
# create an instance of SelfOnboardRequest from a dict
self_onboard_request_from_dict = SelfOnboardRequest.from_dict(self_onboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


