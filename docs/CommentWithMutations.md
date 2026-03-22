# CommentWithMutations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **int** |  | 
**original_id** | **int** |  | 
**id** | **int** |  | 
**mutates_id** | **int** |  | 
**mutation_op** | **str** |  | 
**data** | **str** |  | 
**level** | **int** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**system_generated** | **bool** |  | 

## Example

```python
from audithub_sdk.models.comment_with_mutations import CommentWithMutations

# TODO update the JSON string below
json = "{}"
# create an instance of CommentWithMutations from a JSON string
comment_with_mutations_instance = CommentWithMutations.from_json(json)
# print the JSON string representation of the object
print(CommentWithMutations.to_json())

# convert the object into a dict
comment_with_mutations_dict = comment_with_mutations_instance.to_dict()
# create an instance of CommentWithMutations from a dict
comment_with_mutations_from_dict = CommentWithMutations.from_dict(comment_with_mutations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


