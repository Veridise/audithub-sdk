# Thread


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **int** |  | 
**version_id** | **int** |  | [optional] 
**type** | **str** |  | 
**subject** | [**Subject**](Subject.md) |  | 
**title** | **str** |  | [optional] 
**id** | **int** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 
**commenter_ids** | **List[str]** |  | [optional] 
**resolved** | **bool** |  | [optional] [default to False]
**resolved_at** | **datetime** |  | [optional] 
**resolved_by** | **str** |  | [optional] 
**message_count** | **int** |  | [optional] 

## Example

```python
from audithub_sdk.models.thread import Thread

# TODO update the JSON string below
json = "{}"
# create an instance of Thread from a JSON string
thread_instance = Thread.from_json(json)
# print the JSON string representation of the object
print(Thread.to_json())

# convert the object into a dict
thread_dict = thread_instance.to_dict()
# create an instance of Thread from a dict
thread_from_dict = Thread.from_dict(thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


