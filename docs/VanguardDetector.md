# VanguardDetector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**caption** | **str** |  | 
**tool** | **str** |  | 

## Example

```python
from audithub_sdk.models.vanguard_detector import VanguardDetector

# TODO update the JSON string below
json = "{}"
# create an instance of VanguardDetector from a JSON string
vanguard_detector_instance = VanguardDetector.from_json(json)
# print the JSON string representation of the object
print(VanguardDetector.to_json())

# convert the object into a dict
vanguard_detector_dict = vanguard_detector_instance.to_dict()
# create an instance of VanguardDetector from a dict
vanguard_detector_from_dict = VanguardDetector.from_dict(vanguard_detector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


