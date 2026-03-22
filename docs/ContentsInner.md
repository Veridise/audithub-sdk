# ContentsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**type** | **str** |  | [optional] [default to 'f']
**size** | **int** |  | 
**contents** | [**List[ContentsInner]**](ContentsInner.md) |  | [optional] [default to []]

## Example

```python
from audithub_sdk.models.contents_inner import ContentsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ContentsInner from a JSON string
contents_inner_instance = ContentsInner.from_json(json)
# print the JSON string representation of the object
print(ContentsInner.to_json())

# convert the object into a dict
contents_inner_dict = contents_inner_instance.to_dict()
# create an instance of ContentsInner from a dict
contents_inner_from_dict = ContentsInner.from_dict(contents_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


