# audithub_sdk.TasksApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_task_organizations_organization_id_tasks_task_id_delete**](TasksApi.md#delete_task_organizations_organization_id_tasks_task_id_delete) | **DELETE** /organizations/{organization_id}/tasks/{task_id} | Delete Task
[**get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get**](TasksApi.md#get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/artifacts/{artifact_id} | Get Artifact
[**get_info_organizations_organization_id_tasks_task_id_get**](TasksApi.md#get_info_organizations_organization_id_tasks_task_id_get) | **GET** /organizations/{organization_id}/tasks/{task_id} | Get Info
[**get_output_organizations_organization_id_tasks_task_id_step_code_output_get**](TasksApi.md#get_output_organizations_organization_id_tasks_task_id_step_code_output_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/{step_code}/output | Get Output
[**get_status_organizations_organization_id_tasks_task_id_status_get**](TasksApi.md#get_status_organizations_organization_id_tasks_task_id_status_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/status | Get Status
[**get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get**](TasksApi.md#get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/accounting | Get Task Accounting
[**get_task_archive_organizations_organization_id_tasks_task_id_archive_get**](TasksApi.md#get_task_archive_organizations_organization_id_tasks_task_id_archive_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/archive | Get Task Archive
[**get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get**](TasksApi.md#get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/catalog | Get Task Catalog
[**get_task_file_organizations_organization_id_tasks_task_id_file_get**](TasksApi.md#get_task_file_organizations_organization_id_tasks_task_id_file_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/file | Get Task File
[**get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get**](TasksApi.md#get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/findings/{analysis_result_id} | Get Task Findings For Analysis Result
[**get_task_findings_organizations_organization_id_tasks_task_id_findings_get**](TasksApi.md#get_task_findings_organizations_organization_id_tasks_task_id_findings_get) | **GET** /organizations/{organization_id}/tasks/{task_id}/findings | Get Task Findings
[**get_tasks_organizations_organization_id_tasks_get**](TasksApi.md#get_tasks_organizations_organization_id_tasks_get) | **GET** /organizations/{organization_id}/tasks | Get Tasks
[**patch_task_organizations_organization_id_tasks_task_id_patch**](TasksApi.md#patch_task_organizations_organization_id_tasks_task_id_patch) | **PATCH** /organizations/{organization_id}/tasks/{task_id} | Patch Task
[**put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put**](TasksApi.md#put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put) | **PUT** /organizations/{organization_id}/tasks/{task_id}/findings/actions | Put Task Finding Actions


# **delete_task_organizations_organization_id_tasks_task_id_delete**
> SuccessAndMessageResponse delete_task_organizations_organization_id_tasks_task_id_delete(organization_id, task_id)

Delete Task

Delete task

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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Delete Task
        api_response = await api_instance.delete_task_organizations_organization_id_tasks_task_id_delete(organization_id, task_id)
        print("The response of TasksApi->delete_task_organizations_organization_id_tasks_task_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->delete_task_organizations_organization_id_tasks_task_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get**
> get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get(organization_id, task_id, artifact_id)

Get Artifact

Download the content of an artifact

### Example


```python
import audithub_sdk
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    artifact_id = 'artifact_id_example' # str | 

    try:
        # Get Artifact
        await api_instance.get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get(organization_id, task_id, artifact_id)
    except Exception as e:
        print("Exception when calling TasksApi->get_artifact_organizations_organization_id_tasks_task_id_artifacts_artifact_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **artifact_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_info_organizations_organization_id_tasks_task_id_get**
> Task get_info_organizations_organization_id_tasks_task_id_get(organization_id, task_id)

Get Info

Get task info

### Example


```python
import audithub_sdk
from audithub_sdk.models.task import Task
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Get Info
        api_response = await api_instance.get_info_organizations_organization_id_tasks_task_id_get(organization_id, task_id)
        print("The response of TasksApi->get_info_organizations_organization_id_tasks_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_info_organizations_organization_id_tasks_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

[**Task**](Task.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_output_organizations_organization_id_tasks_task_id_step_code_output_get**
> List[str] get_output_organizations_organization_id_tasks_task_id_step_code_output_get(task_id, organization_id, step_code, disable_filtering=disable_filtering, show_timestamp=show_timestamp)

Get Output

### Example


```python
import audithub_sdk
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
    api_instance = audithub_sdk.TasksApi(api_client)
    task_id = 56 # int | 
    organization_id = 56 # int | 
    step_code = 'step_code_example' # str | 
    disable_filtering = True # bool | When set to true, the raw, unfiltered output of the task will be provided. (optional) (default to True)
    show_timestamp = False # bool | When set to true, the log entry is prepended with timestamp (optional) (default to False)

    try:
        # Get Output
        api_response = await api_instance.get_output_organizations_organization_id_tasks_task_id_step_code_output_get(task_id, organization_id, step_code, disable_filtering=disable_filtering, show_timestamp=show_timestamp)
        print("The response of TasksApi->get_output_organizations_organization_id_tasks_task_id_step_code_output_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_output_organizations_organization_id_tasks_task_id_step_code_output_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**|  | 
 **organization_id** | **int**|  | 
 **step_code** | **str**|  | 
 **disable_filtering** | **bool**| When set to true, the raw, unfiltered output of the task will be provided. | [optional] [default to True]
 **show_timestamp** | **bool**| When set to true, the log entry is prepended with timestamp | [optional] [default to False]

### Return type

**List[str]**

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Return the output of the task |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_organizations_organization_id_tasks_task_id_status_get**
> TaskStatus get_status_organizations_organization_id_tasks_task_id_status_get(organization_id, task_id)

Get Status

Get task status

### Example


```python
import audithub_sdk
from audithub_sdk.models.task_status import TaskStatus
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Get Status
        api_response = await api_instance.get_status_organizations_organization_id_tasks_task_id_status_get(organization_id, task_id)
        print("The response of TasksApi->get_status_organizations_organization_id_tasks_task_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_status_organizations_organization_id_tasks_task_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

[**TaskStatus**](TaskStatus.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get**
> List[AccountingData] get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get(organization_id, task_id, step_code=step_code, container_name=container_name)

Get Task Accounting

Get all accounting entries of a task

### Example


```python
import audithub_sdk
from audithub_sdk.models.accounting_data import AccountingData
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    step_code = 'step_code_example' # str |  (optional)
    container_name = 'container_name_example' # str |  (optional)

    try:
        # Get Task Accounting
        api_response = await api_instance.get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get(organization_id, task_id, step_code=step_code, container_name=container_name)
        print("The response of TasksApi->get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_accounting_organizations_organization_id_tasks_task_id_accounting_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **step_code** | **str**|  | [optional] 
 **container_name** | **str**|  | [optional] 

### Return type

[**List[AccountingData]**](AccountingData.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_archive_organizations_organization_id_tasks_task_id_archive_get**
> str get_task_archive_organizations_organization_id_tasks_task_id_archive_get(organization_id, task_id)

Get Task Archive

Download the content of a project's version augmented with the task execution output

### Example


```python
import audithub_sdk
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Get Task Archive
        api_response = await api_instance.get_task_archive_organizations_organization_id_tasks_task_id_archive_get(organization_id, task_id)
        print("The response of TasksApi->get_task_archive_organizations_organization_id_tasks_task_id_archive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_archive_organizations_organization_id_tasks_task_id_archive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

**str**

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get**
> Directory get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get(organization_id, task_id)

Get Task Catalog

Get the catalog of a project's version augmented with the task execution output

### Example


```python
import audithub_sdk
from audithub_sdk.models.directory import Directory
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Get Task Catalog
        api_response = await api_instance.get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get(organization_id, task_id)
        print("The response of TasksApi->get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_catalog_organizations_organization_id_tasks_task_id_catalog_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

[**Directory**](Directory.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_file_organizations_organization_id_tasks_task_id_file_get**
> get_task_file_organizations_organization_id_tasks_task_id_file_get(organization_id, task_id, relative_path)

Get Task File

Get the contents of a task's file.

### Example


```python
import audithub_sdk
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    relative_path = 'relative_path_example' # str | 

    try:
        # Get Task File
        await api_instance.get_task_file_organizations_organization_id_tasks_task_id_file_get(organization_id, task_id, relative_path)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_file_organizations_organization_id_tasks_task_id_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **relative_path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get**
> List[FIOData] get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get(organization_id, task_id, analysis_result_id, state_digest=state_digest)

Get Task Findings For Analysis Result

Get the findings of a specific analysis_result_id

### Example


```python
import audithub_sdk
from audithub_sdk.models.fio_data import FIOData
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    analysis_result_id = 'analysis_result_id_example' # str | 
    state_digest = 56 # int |  (optional)

    try:
        # Get Task Findings For Analysis Result
        api_response = await api_instance.get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get(organization_id, task_id, analysis_result_id, state_digest=state_digest)
        print("The response of TasksApi->get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_findings_for_analysis_result_organizations_organization_id_tasks_task_id_findings_analysis_result_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **analysis_result_id** | **str**|  | 
 **state_digest** | **int**|  | [optional] 

### Return type

[**List[FIOData]**](FIOData.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_findings_organizations_organization_id_tasks_task_id_findings_get**
> List[FIOData] get_task_findings_organizations_organization_id_tasks_task_id_findings_get(organization_id, task_id)

Get Task Findings

Get the findings of a task's execution

### Example


```python
import audithub_sdk
from audithub_sdk.models.fio_data import FIOData
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 

    try:
        # Get Task Findings
        api_response = await api_instance.get_task_findings_organizations_organization_id_tasks_task_id_findings_get(organization_id, task_id)
        print("The response of TasksApi->get_task_findings_organizations_organization_id_tasks_task_id_findings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_task_findings_organizations_organization_id_tasks_task_id_findings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

[**List[FIOData]**](FIOData.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks_organizations_organization_id_tasks_get**
> List[Task] get_tasks_organizations_organization_id_tasks_get(organization_id, offset=offset, limit=limit, project_id=project_id, version_id=version_id, from_created_at=from_created_at, to_created_at=to_created_at, order_by=order_by)

Get Tasks

Get list of a organization's tasks, potentially limiting them with query parameters

### Example


```python
import audithub_sdk
from audithub_sdk.models.task import Task
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    offset = 56 # int | Offset. If specified, skip the first offset tasks from results. (optional)
    limit = 56 # int | Limit. If specified, limits the number of results to this number. (optional)
    project_id = 56 # int | Project id. If specified, limits the results to this project. (optional)
    version_id = 56 # int | Version id. If specified, limits the results to this version. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started on or after (>=) this time (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started before (<) this time (optional)
    order_by = 'order_by_example' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: project_id, version_id, task_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.          (optional)

    try:
        # Get Tasks
        api_response = await api_instance.get_tasks_organizations_organization_id_tasks_get(organization_id, offset=offset, limit=limit, project_id=project_id, version_id=version_id, from_created_at=from_created_at, to_created_at=to_created_at, order_by=order_by)
        print("The response of TasksApi->get_tasks_organizations_organization_id_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->get_tasks_organizations_organization_id_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **offset** | **int**| Offset. If specified, skip the first offset tasks from results. | [optional] 
 **limit** | **int**| Limit. If specified, limits the number of results to this number. | [optional] 
 **project_id** | **int**| Project id. If specified, limits the results to this project. | [optional] 
 **version_id** | **int**| Version id. If specified, limits the results to this version. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started on or after (&gt;&#x3D;) this time | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started before (&lt;) this time | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: project_id, version_id, task_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.          | [optional] 

### Return type

[**List[Task]**](Task.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_task_organizations_organization_id_tasks_task_id_patch**
> SuccessAndMessageResponse patch_task_organizations_organization_id_tasks_task_id_patch(organization_id, task_id, task_patch)

Patch Task

Patch task

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.task_patch import TaskPatch
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    task_patch = audithub_sdk.TaskPatch() # TaskPatch | 

    try:
        # Patch Task
        api_response = await api_instance.patch_task_organizations_organization_id_tasks_task_id_patch(organization_id, task_id, task_patch)
        print("The response of TasksApi->patch_task_organizations_organization_id_tasks_task_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->patch_task_organizations_organization_id_tasks_task_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **task_patch** | [**TaskPatch**](TaskPatch.md)|  | 

### Return type

[**SuccessAndMessageResponse**](SuccessAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put**
> object put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put(organization_id, task_id, pending_finding_actions)

Put Task Finding Actions

Add finding actions

### Example


```python
import audithub_sdk
from audithub_sdk.models.pending_finding_actions import PendingFindingActions
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
    api_instance = audithub_sdk.TasksApi(api_client)
    organization_id = 56 # int | 
    task_id = 56 # int | 
    pending_finding_actions = audithub_sdk.PendingFindingActions() # PendingFindingActions | 

    try:
        # Put Task Finding Actions
        api_response = await api_instance.put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put(organization_id, task_id, pending_finding_actions)
        print("The response of TasksApi->put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TasksApi->put_task_finding_actions_organizations_organization_id_tasks_task_id_findings_actions_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **task_id** | **int**|  | 
 **pending_finding_actions** | [**PendingFindingActions**](PendingFindingActions.md)|  | 

### Return type

**object**

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

