# ExtraFunctionArguments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | **str** |  | [optional] 
**pr** | **str** |  | [optional] 
**commit** | **str** |  | [optional] 

## Example

```python
from audithub_sdk.models.extra_function_arguments import ExtraFunctionArguments

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraFunctionArguments from a JSON string
extra_function_arguments_instance = ExtraFunctionArguments.from_json(json)
# print the JSON string representation of the object
print(ExtraFunctionArguments.to_json())

# convert the object into a dict
extra_function_arguments_dict = extra_function_arguments_instance.to_dict()
# create an instance of ExtraFunctionArguments from a dict
extra_function_arguments_from_dict = ExtraFunctionArguments.from_dict(extra_function_arguments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


