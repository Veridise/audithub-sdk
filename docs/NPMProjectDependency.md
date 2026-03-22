# NPMProjectDependency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool** | **str** |  | 
**lockfile** | **bool** |  | 
**node_version** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.npm_project_dependency import NPMProjectDependency

# TODO update the JSON string below
json = "{}"
# create an instance of NPMProjectDependency from a JSON string
npm_project_dependency_instance = NPMProjectDependency.from_json(json)
# print the JSON string representation of the object
print(NPMProjectDependency.to_json())

# convert the object into a dict
npm_project_dependency_dict = npm_project_dependency_instance.to_dict()
# create an instance of NPMProjectDependency from a dict
npm_project_dependency_from_dict = NPMProjectDependency.from_dict(npm_project_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


