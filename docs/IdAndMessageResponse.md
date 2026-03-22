# IdAndMessageResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**message** | **str** |  | 

## Example

```python
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IdAndMessageResponse from a JSON string
id_and_message_response_instance = IdAndMessageResponse.from_json(json)
# print the JSON string representation of the object
print(IdAndMessageResponse.to_json())

# convert the object into a dict
id_and_message_response_dict = id_and_message_response_instance.to_dict()
# create an instance of IdAndMessageResponse from a dict
id_and_message_response_from_dict = IdAndMessageResponse.from_dict(id_and_message_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


