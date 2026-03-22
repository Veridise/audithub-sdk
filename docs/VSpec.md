# VSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this V Spec. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']

## Example

```python
from audithub_sdk.models.v_spec import VSpec

# TODO update the JSON string below
json = "{}"
# create an instance of VSpec from a JSON string
v_spec_instance = VSpec.from_json(json)
# print the JSON string representation of the object
print(VSpec.to_json())

# convert the object into a dict
v_spec_dict = v_spec_instance.to_dict()
# create an instance of VSpec from a dict
v_spec_from_dict = VSpec.from_dict(v_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


