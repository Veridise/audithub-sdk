# HintWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this Hint. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']
**id** | **int** | The id of this Hint | 

## Example

```python
from audithub_sdk.models.hint_with_id import HintWithId

# TODO update the JSON string below
json = "{}"
# create an instance of HintWithId from a JSON string
hint_with_id_instance = HintWithId.from_json(json)
# print the JSON string representation of the object
print(HintWithId.to_json())

# convert the object into a dict
hint_with_id_dict = hint_with_id_instance.to_dict()
# create an instance of HintWithId from a dict
hint_with_id_from_dict = HintWithId.from_dict(hint_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


