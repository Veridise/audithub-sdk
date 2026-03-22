# VSpecWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **str** | The filename for this V Spec. | 
**contents** | **str** | The contents of this file | 
**encoding** | **str** | The encoding of the contents. Currently, only &#39;plain&#39; is supported, which simply places the value of the contents JSON key to the file | [optional] [default to 'plain']
**id** | **int** | The id of this V specification | 

## Example

```python
from audithub_sdk.models.v_spec_with_id import VSpecWithId

# TODO update the JSON string below
json = "{}"
# create an instance of VSpecWithId from a JSON string
v_spec_with_id_instance = VSpecWithId.from_json(json)
# print the JSON string representation of the object
print(VSpecWithId.to_json())

# convert the object into a dict
v_spec_with_id_dict = v_spec_with_id_instance.to_dict()
# create an instance of VSpecWithId from a dict
v_spec_with_id_from_dict = VSpecWithId.from_dict(v_spec_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


