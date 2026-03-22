# audithub_sdk.ToolsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post**](ToolsApi.md#post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/model_tool | Post Tool Model
[**post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post**](ToolsApi.md#post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/orca | Post Tool Orca
[**post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post**](ToolsApi.md#post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/picus | Post Tool Picus
[**post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post**](ToolsApi.md#post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/picus-v2 | Post Tool Picus
[**post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post**](ToolsApi.md#post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/vanguard-v2 | Post Tool Vanguard V2
[**post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post**](ToolsApi.md#post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/zk-vanguard | Post Tool Zk Vanguard
[**post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post**](ToolsApi.md#post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/tools/zk-vanguard-v2 | Post Tool Zk Vanguard V2


# **post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post**
> TaskCreation post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post(organization_id, project_id, version_id, model_tool_input)

Post Tool Model

Post a task for the model tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.model_tool_input import ModelToolInput
from audithub_sdk.models.task_creation import TaskCreation
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    model_tool_input = audithub_sdk.ModelToolInput() # ModelToolInput | 

    try:
        # Post Tool Model
        api_response = await api_instance.post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post(organization_id, project_id, version_id, model_tool_input)
        print("The response of ToolsApi->post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_model_organizations_organization_id_projects_project_id_versions_version_id_tools_model_tool_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **model_tool_input** | [**ModelToolInput**](ModelToolInput.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post**
> TaskCreation post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post(organization_id, project_id, version_id, or_ca_input)

Post Tool Orca

Post a task for the OrCa fuzz testing tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.or_ca_input import OrCaInput
from audithub_sdk.models.task_creation import TaskCreation
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    or_ca_input = audithub_sdk.OrCaInput() # OrCaInput | 

    try:
        # Post Tool Orca
        api_response = await api_instance.post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post(organization_id, project_id, version_id, or_ca_input)
        print("The response of ToolsApi->post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_orca_organizations_organization_id_projects_project_id_versions_version_id_tools_orca_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **or_ca_input** | [**OrCaInput**](OrCaInput.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post**
> TaskCreation post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post(organization_id, project_id, version_id, picus_input)

Post Tool Picus

Post a task for the Picus tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.picus_input import PicusInput
from audithub_sdk.models.task_creation import TaskCreation
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    picus_input = audithub_sdk.PicusInput() # PicusInput | 

    try:
        # Post Tool Picus
        api_response = await api_instance.post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post(organization_id, project_id, version_id, picus_input)
        print("The response of ToolsApi->post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **picus_input** | [**PicusInput**](PicusInput.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post**
> TaskCreation post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post(organization_id, project_id, version_id, picus_v2_input)

Post Tool Picus

Post a task for the PicusV2 tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.picus_v2_input import PicusV2Input
from audithub_sdk.models.task_creation import TaskCreation
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    picus_v2_input = audithub_sdk.PicusV2Input() # PicusV2Input | 

    try:
        # Post Tool Picus
        api_response = await api_instance.post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post(organization_id, project_id, version_id, picus_v2_input)
        print("The response of ToolsApi->post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_picus_organizations_organization_id_projects_project_id_versions_version_id_tools_picus_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **picus_v2_input** | [**PicusV2Input**](PicusV2Input.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post**
> TaskCreation post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post(organization_id, project_id, version_id, defi_vanguard_v2_input)

Post Tool Vanguard V2

Post a task for the DeFi Vanguard v2 static analyzer tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.defi_vanguard_v2_input import DefiVanguardV2Input
from audithub_sdk.models.task_creation import TaskCreation
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    defi_vanguard_v2_input = audithub_sdk.DefiVanguardV2Input() # DefiVanguardV2Input | 

    try:
        # Post Tool Vanguard V2
        api_response = await api_instance.post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post(organization_id, project_id, version_id, defi_vanguard_v2_input)
        print("The response of ToolsApi->post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_vanguard_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **defi_vanguard_v2_input** | [**DefiVanguardV2Input**](DefiVanguardV2Input.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post**
> TaskCreation post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post(organization_id, project_id, version_id, zk_vanguard_input)

Post Tool Zk Vanguard

Post a task for the ZK Vanguard static analyzer tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.task_creation import TaskCreation
from audithub_sdk.models.zk_vanguard_input import ZKVanguardInput
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    zk_vanguard_input = audithub_sdk.ZKVanguardInput() # ZKVanguardInput | 

    try:
        # Post Tool Zk Vanguard
        api_response = await api_instance.post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post(organization_id, project_id, version_id, zk_vanguard_input)
        print("The response of ToolsApi->post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_zk_vanguard_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **zk_vanguard_input** | [**ZKVanguardInput**](ZKVanguardInput.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

# **post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post**
> TaskCreation post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post(organization_id, project_id, version_id, zk_vanguard_v2_input)

Post Tool Zk Vanguard V2

Post a task for the ZK Vanguard v2 static analyzer tool

### Example


```python
import audithub_sdk
from audithub_sdk.models.task_creation import TaskCreation
from audithub_sdk.models.zk_vanguard_v2_input import ZKVanguardV2Input
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
    api_instance = audithub_sdk.ToolsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | The id of the project for which this task will execute
    version_id = 56 # int | The version id whose archive this task will process
    zk_vanguard_v2_input = audithub_sdk.ZKVanguardV2Input() # ZKVanguardV2Input | 

    try:
        # Post Tool Zk Vanguard V2
        api_response = await api_instance.post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post(organization_id, project_id, version_id, zk_vanguard_v2_input)
        print("The response of ToolsApi->post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ToolsApi->post_tool_zk_vanguard_v2_organizations_organization_id_projects_project_id_versions_version_id_tools_zk_vanguard_v2_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**| The id of the project for which this task will execute | 
 **version_id** | **int**| The version id whose archive this task will process | 
 **zk_vanguard_v2_input** | [**ZKVanguardV2Input**](ZKVanguardV2Input.md)|  | 

### Return type

[**TaskCreation**](TaskCreation.md)

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

