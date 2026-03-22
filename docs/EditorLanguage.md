# EditorLanguage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Language name. This should be unique. | 
**extensions** | **List[str]** | List of file extensions associated with the language. At least one is required. Any file extension can be referenced by a single language | 
**definition** | **Dict[str, object]** | A Monarch language definition | 
**configuration** | **Dict[str, object]** |  | [optional] 

## Example

```python
from audithub_sdk.models.editor_language import EditorLanguage

# TODO update the JSON string below
json = "{}"
# create an instance of EditorLanguage from a JSON string
editor_language_instance = EditorLanguage.from_json(json)
# print the JSON string representation of the object
print(EditorLanguage.to_json())

# convert the object into a dict
editor_language_dict = editor_language_instance.to_dict()
# create an instance of EditorLanguage from a dict
editor_language_from_dict = EditorLanguage.from_dict(editor_language_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


