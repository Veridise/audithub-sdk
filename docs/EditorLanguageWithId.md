# EditorLanguageWithId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Language name. This should be unique. | 
**extensions** | **List[str]** | List of file extensions associated with the language. At least one is required. Any file extension can be referenced by a single language | 
**definition** | **Dict[str, object]** | A Monarch language definition | 
**configuration** | **Dict[str, object]** |  | [optional] 
**id** | **int** | The id of this language | 

## Example

```python
from audithub_sdk.models.editor_language_with_id import EditorLanguageWithId

# TODO update the JSON string below
json = "{}"
# create an instance of EditorLanguageWithId from a JSON string
editor_language_with_id_instance = EditorLanguageWithId.from_json(json)
# print the JSON string representation of the object
print(EditorLanguageWithId.to_json())

# convert the object into a dict
editor_language_with_id_dict = editor_language_with_id_instance.to_dict()
# create an instance of EditorLanguageWithId from a dict
editor_language_with_id_from_dict = EditorLanguageWithId.from_dict(editor_language_with_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


