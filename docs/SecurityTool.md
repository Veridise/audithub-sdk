# SecurityTool


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from audithub_sdk.models.security_tool import SecurityTool

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityTool from a JSON string
security_tool_instance = SecurityTool.from_json(json)
# print the JSON string representation of the object
print(SecurityTool.to_json())

# convert the object into a dict
security_tool_dict = security_tool_instance.to_dict()
# create an instance of SecurityTool from a dict
security_tool_from_dict = SecurityTool.from_dict(security_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


