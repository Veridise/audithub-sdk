# ProjectDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Display name of document | 
**data** | **str** |  | 
**id** | **int** |  | 
**project_id** | **int** |  | 
**created_by** | **str** |  | 
**created_at** | **datetime** |  | 
**is_deleted** | **bool** |  | 

## Example

```python
from audithub_sdk.models.project_document import ProjectDocument

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectDocument from a JSON string
project_document_instance = ProjectDocument.from_json(json)
# print the JSON string representation of the object
print(ProjectDocument.to_json())

# convert the object into a dict
project_document_dict = project_document_instance.to_dict()
# create an instance of ProjectDocument from a dict
project_document_from_dict = ProjectDocument.from_dict(project_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


