# CustomDetector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this Custom Detector. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']

## Example

```python
from audithub_sdk.models.custom_detector import CustomDetector

# TODO update the JSON string below
json = "{}"
# create an instance of CustomDetector from a JSON string
custom_detector_instance = CustomDetector.from_json(json)
# print the JSON string representation of the object
print(CustomDetector.to_json())

# convert the object into a dict
custom_detector_dict = custom_detector_instance.to_dict()
# create an instance of CustomDetector from a dict
custom_detector_from_dict = CustomDetector.from_dict(custom_detector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


