# Hint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this Hint. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']

## Example

```python
from audithub_sdk.models.hint import Hint

# TODO update the JSON string below
json = "{}"
# create an instance of Hint from a JSON string
hint_instance = Hint.from_json(json)
# print the JSON string representation of the object
print(Hint.to_json())

# convert the object into a dict
hint_dict = hint_instance.to_dict()
# create an instance of Hint from a dict
hint_from_dict = Hint.from_dict(hint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


