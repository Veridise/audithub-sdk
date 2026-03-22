# ApplicationFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**caption** | **str** |  | 
**has_value** | **bool** |  | 
**applicability** | **int** |  | 
**per_project** | **bool** |  | 
**per_detector** | **bool** |  | 

## Example

```python
from audithub_sdk.models.application_function import ApplicationFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFunction from a JSON string
application_function_instance = ApplicationFunction.from_json(json)
# print the JSON string representation of the object
print(ApplicationFunction.to_json())

# convert the object into a dict
application_function_dict = application_function_instance.to_dict()
# create an instance of ApplicationFunction from a dict
application_function_from_dict = ApplicationFunction.from_dict(application_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


