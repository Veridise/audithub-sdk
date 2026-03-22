# HintAdHoc


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this Hint. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']
**type** | **str** |  | [optional] [default to 'adhoc']

## Example

```python
from audithub_sdk.models.hint_ad_hoc import HintAdHoc

# TODO update the JSON string below
json = "{}"
# create an instance of HintAdHoc from a JSON string
hint_ad_hoc_instance = HintAdHoc.from_json(json)
# print the JSON string representation of the object
print(HintAdHoc.to_json())

# convert the object into a dict
hint_ad_hoc_dict = hint_ad_hoc_instance.to_dict()
# create an instance of HintAdHoc from a dict
hint_ad_hoc_from_dict = HintAdHoc.from_dict(hint_ad_hoc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


