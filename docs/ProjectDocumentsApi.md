# audithub_sdk.ProjectDocumentsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete**](ProjectDocumentsApi.md#delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete) | **DELETE** /organizations/{organization_id}/projects/{project_id}/documents/{document_id} | Delete Document
[**get_document_organizations_organization_id_projects_project_id_documents_document_id_get**](ProjectDocumentsApi.md#get_document_organizations_organization_id_projects_project_id_documents_document_id_get) | **GET** /organizations/{organization_id}/projects/{project_id}/documents/{document_id} | Get Document
[**get_documents_organizations_organization_id_projects_project_id_documents_get**](ProjectDocumentsApi.md#get_documents_organizations_organization_id_projects_project_id_documents_get) | **GET** /organizations/{organization_id}/projects/{project_id}/documents | Get Documents
[**post_document_organizations_organization_id_projects_project_id_documents_post**](ProjectDocumentsApi.md#post_document_organizations_organization_id_projects_project_id_documents_post) | **POST** /organizations/{organization_id}/projects/{project_id}/documents | Post Document
[**put_document_organizations_organization_id_projects_project_id_documents_document_id_put**](ProjectDocumentsApi.md#put_document_organizations_organization_id_projects_project_id_documents_document_id_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/documents/{document_id} | Put Document


# **delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete**
> SuccessAndMessageResponse delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete(organization_id, project_id, document_id)

Delete Document

Soft delete a project document

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.ProjectDocumentsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    document_id = 56 # int | 

    try:
        # Delete Document
        api_response = await api_instance.delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete(organization_id, project_id, document_id)
        print("The response of ProjectDocumentsApi->delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentsApi->delete_document_organizations_organization_id_projects_project_id_documents_document_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **document_id** | **int**|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_organizations_organization_id_projects_project_id_documents_document_id_get**
> ProjectDocument get_document_organizations_organization_id_projects_project_id_documents_document_id_get(organization_id, project_id, document_id)

Get Document

Get a project document

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_document import ProjectDocument
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.ProjectDocumentsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    document_id = 56 # int | 

    try:
        # Get Document
        api_response = await api_instance.get_document_organizations_organization_id_projects_project_id_documents_document_id_get(organization_id, project_id, document_id)
        print("The response of ProjectDocumentsApi->get_document_organizations_organization_id_projects_project_id_documents_document_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentsApi->get_document_organizations_organization_id_projects_project_id_documents_document_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **document_id** | **int**|  | 

### Return type

[**ProjectDocument**](ProjectDocument.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_organizations_organization_id_projects_project_id_documents_get**
> List[ProjectDocument] get_documents_organizations_organization_id_projects_project_id_documents_get(organization_id, project_id)

Get Documents

List active project documents

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_document import ProjectDocument
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.ProjectDocumentsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Documents
        api_response = await api_instance.get_documents_organizations_organization_id_projects_project_id_documents_get(organization_id, project_id)
        print("The response of ProjectDocumentsApi->get_documents_organizations_organization_id_projects_project_id_documents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentsApi->get_documents_organizations_organization_id_projects_project_id_documents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**List[ProjectDocument]**](ProjectDocument.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document_organizations_organization_id_projects_project_id_documents_post**
> IdAndMessageResponse post_document_organizations_organization_id_projects_project_id_documents_post(organization_id, project_id, project_document_data)

Post Document

Create a project document

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.project_document_data import ProjectDocumentData
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.ProjectDocumentsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    project_document_data = audithub_sdk.ProjectDocumentData() # ProjectDocumentData | 

    try:
        # Post Document
        api_response = await api_instance.post_document_organizations_organization_id_projects_project_id_documents_post(organization_id, project_id, project_document_data)
        print("The response of ProjectDocumentsApi->post_document_organizations_organization_id_projects_project_id_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentsApi->post_document_organizations_organization_id_projects_project_id_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **project_document_data** | [**ProjectDocumentData**](ProjectDocumentData.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document_organizations_organization_id_projects_project_id_documents_document_id_put**
> SuccessAndMessageResponse put_document_organizations_organization_id_projects_project_id_documents_document_id_put(organization_id, project_id, document_id, project_document_data)

Put Document

Replace a project document's name and data

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_document_data import ProjectDocumentData
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://audithub.dev.veridise.tools/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = audithub_sdk.Configuration(
    host = "https://audithub.dev.veridise.tools/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Enter a context with an instance of the API client
async with audithub_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audithub_sdk.ProjectDocumentsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    document_id = 56 # int | 
    project_document_data = audithub_sdk.ProjectDocumentData() # ProjectDocumentData | 

    try:
        # Put Document
        api_response = await api_instance.put_document_organizations_organization_id_projects_project_id_documents_document_id_put(organization_id, project_id, document_id, project_document_data)
        print("The response of ProjectDocumentsApi->put_document_organizations_organization_id_projects_project_id_documents_document_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectDocumentsApi->put_document_organizations_organization_id_projects_project_id_documents_document_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **document_id** | **int**|  | 
 **project_document_data** | [**ProjectDocumentData**](ProjectDocumentData.md)|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

