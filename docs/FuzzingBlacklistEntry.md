# FuzzingBlacklistEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contract** | **str** | The contract name containing the accompanying function | 
**function** | **str** | The function within the specified contract | 

## Example

```python
from audithub_sdk.models.fuzzing_blacklist_entry import FuzzingBlacklistEntry

# TODO update the JSON string below
json = "{}"
# create an instance of FuzzingBlacklistEntry from a JSON string
fuzzing_blacklist_entry_instance = FuzzingBlacklistEntry.from_json(json)
# print the JSON string representation of the object
print(FuzzingBlacklistEntry.to_json())

# convert the object into a dict
fuzzing_blacklist_entry_dict = fuzzing_blacklist_entry_instance.to_dict()
# create an instance of FuzzingBlacklistEntry from a dict
fuzzing_blacklist_entry_from_dict = FuzzingBlacklistEntry.from_dict(fuzzing_blacklist_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


