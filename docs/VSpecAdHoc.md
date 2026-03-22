# VSpecAdHoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'adhoc']
**filename** | **str** | The filename for this V Spec. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']

## Example

```python
from audithub_sdk.models.v_spec_ad_hoc import VSpecAdHoc

# TODO update the JSON string below
json = "{}"
# create an instance of VSpecAdHoc from a JSON string
v_spec_ad_hoc_instance = VSpecAdHoc.from_json(json)
# print the JSON string representation of the object
print(VSpecAdHoc.to_json())

# convert the object into a dict
v_spec_ad_hoc_dict = v_spec_ad_hoc_instance.to_dict()
# create an instance of VSpecAdHoc from a dict
v_spec_ad_hoc_from_dict = VSpecAdHoc.from_dict(v_spec_ad_hoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


