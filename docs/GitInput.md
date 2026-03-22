# GitInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_type** | **str** |  | [optional] [default to 'git']
**url** | **str** | This is the repo url | 
**includes_submodules** | **bool** |  | [optional] 
**revision** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.git_input import GitInput

# TODO update the JSON string below
json = "{}"
# create an instance of GitInput from a JSON string
git_input_instance = GitInput.from_json(json)
# print the JSON string representation of the object
print(GitInput.to_json())

# convert the object into a dict
git_input_dict = git_input_instance.to_dict()
# create an instance of GitInput from a dict
git_input_from_dict = GitInput.from_dict(git_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


