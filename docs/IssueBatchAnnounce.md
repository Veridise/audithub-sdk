# IssueBatchAnnounce


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_ids** | **List[int]** | A list of issue ids, which are in the appropriate state to be shared with developers. | 

## Example

```python
from audithub_sdk.models.issue_batch_announce import IssueBatchAnnounce

# TODO update the JSON string below
json = "{}"
# create an instance of IssueBatchAnnounce from a JSON string
issue_batch_announce_instance = IssueBatchAnnounce.from_json(json)
# print the JSON string representation of the object
print(IssueBatchAnnounce.to_json())

# convert the object into a dict
issue_batch_announce_dict = issue_batch_announce_instance.to_dict()
# create an instance of IssueBatchAnnounce from a dict
issue_batch_announce_from_dict = IssueBatchAnnounce.from_dict(issue_batch_announce_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


