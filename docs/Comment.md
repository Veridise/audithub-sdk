# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**version_id** | **int** |  | [optional] 
**thread_id** | **int** |  | 
**data** | **str** |  | 
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**system_generated** | **bool** |  | [optional] 
**is_modified** | **bool** |  | 
**is_deleted** | **bool** |  | 

## Example

```python
from audithub_sdk.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


