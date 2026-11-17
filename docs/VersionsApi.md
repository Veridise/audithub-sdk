# audithub_sdk.VersionsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete**](VersionsApi.md#delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete) | **DELETE** /organizations/{organization_id}/projects/{project_id}/versions/{version_id} | Delete Version
[**get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get**](VersionsApi.md#get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/comments-mutation-history | Get Comment Mutation History
[**get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get**](VersionsApi.md#get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/latest | Get Latest Version
[**get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get**](VersionsApi.md#get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/archive | Get Version Archive
[**get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get**](VersionsApi.md#get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/catalog | Get Version Catalog
[**get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get**](VersionsApi.md#get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/comment-threads | Get Version Comment Threads
[**get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get**](VersionsApi.md#get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/comments | Get Version Comments
[**get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get**](VersionsApi.md#get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/file | Get Version File
[**get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get**](VersionsApi.md#get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/findings | Get Version Findings
[**get_version_organizations_organization_id_projects_project_id_versions_version_id_get**](VersionsApi.md#get_version_organizations_organization_id_projects_project_id_versions_version_id_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id} | Get Version
[**get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get**](VersionsApi.md#get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/resource-consumption-detailed | Get Version Resource Detailed
[**get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get**](VersionsApi.md#get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions/{version_id}/resource-consumption-total | Get Version Resource Usage
[**get_versions_organizations_organization_id_projects_project_id_versions_get**](VersionsApi.md#get_versions_organizations_organization_id_projects_project_id_versions_get) | **GET** /organizations/{organization_id}/projects/{project_id}/versions | Get Versions
[**patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch**](VersionsApi.md#patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch) | **PATCH** /organizations/{organization_id}/projects/{project_id}/versions/{version_id} | Patch Version
[**post_temp_version_organizations_organization_id_temp_versions_post**](VersionsApi.md#post_temp_version_organizations_organization_id_temp_versions_post) | **POST** /organizations/{organization_id}/temp-versions | Post Temp Version
[**post_temp_version_with_url_organizations_organization_id_temp_versions_url_post**](VersionsApi.md#post_temp_version_with_url_organizations_organization_id_temp_versions_url_post) | **POST** /organizations/{organization_id}/temp-versions-url | Post Temp Version With Url
[**post_version_organizations_organization_id_projects_project_id_versions_post**](VersionsApi.md#post_version_organizations_organization_id_projects_project_id_versions_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions | Post Version
[**post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post**](VersionsApi.md#post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post) | **POST** /organizations/{organization_id}/projects/{project_id}/versions-url | Post Version With Url


# **delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete**
> SuccessAndMessageResponse delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete(organization_id, project_id, version_id)

Delete Version

Permanently delete a version

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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 

    try:
        # Delete Version
        api_response = await api_instance.delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete(organization_id, project_id, version_id)
        print("The response of VersionsApi->delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->delete_version_organizations_organization_id_projects_project_id_versions_version_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 

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

# **get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get**
> List[CommentWithMutations] get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get(organization_id, project_id, version_id, thread_id=thread_id, original_id=original_id, from_date=from_date, to_date=to_date, created_by=created_by, limit=limit, offset=offset, order_by=order_by)

Get Comment Mutation History

Get all comments along with their analytical mutation history

### Example


```python
import audithub_sdk
from audithub_sdk.models.comment_with_mutations import CommentWithMutations
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    thread_id = 56 # int |  (optional)
    original_id = 56 # int |  (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_by = 'created_by_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order_by = 'original_id' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.     Possible column names are: thread_id,id,original_id,mutates_id,mutation_op,level,created_at,created_by     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.      (optional) (default to 'original_id')

    try:
        # Get Comment Mutation History
        api_response = await api_instance.get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get(organization_id, project_id, version_id, thread_id=thread_id, original_id=original_id, from_date=from_date, to_date=to_date, created_by=created_by, limit=limit, offset=offset, order_by=order_by)
        print("The response of VersionsApi->get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_comment_mutation_history_organizations_organization_id_projects_project_id_versions_version_id_comments_mutation_history_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **thread_id** | **int**|  | [optional] 
 **original_id** | **int**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.     Possible column names are: thread_id,id,original_id,mutates_id,mutation_op,level,created_at,created_by     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.      | [optional] [default to &#39;original_id&#39;]

### Return type

[**List[CommentWithMutations]**](CommentWithMutations.md)

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

# **get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get**
> Version get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get(organization_id, project_id, catalog=catalog, abi=abi)

Get Latest Version

Get latest version of project

### Example


```python
import audithub_sdk
from audithub_sdk.models.version import Version
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    catalog = False # bool |  (optional) (default to False)
    abi = False # bool |  (optional) (default to False)

    try:
        # Get Latest Version
        api_response = await api_instance.get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get(organization_id, project_id, catalog=catalog, abi=abi)
        print("The response of VersionsApi->get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_latest_version_organizations_organization_id_projects_project_id_versions_latest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **catalog** | **bool**|  | [optional] [default to False]
 **abi** | **bool**|  | [optional] [default to False]

### Return type

[**Version**](Version.md)

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

# **get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get**
> str get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get(organization_id, project_id, version_id)

Get Version Archive

Get archive of a project's version

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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 

    try:
        # Get Version Archive
        api_response = await api_instance.get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get(organization_id, project_id, version_id)
        print("The response of VersionsApi->get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_archive_organizations_organization_id_projects_project_id_versions_version_id_archive_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 

### Return type

**str**

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get**
> Directory get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get(organization_id, project_id, version_id)

Get Version Catalog

Get the catalog of a project's version

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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 

    try:
        # Get Version Catalog
        api_response = await api_instance.get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get(organization_id, project_id, version_id)
        print("The response of VersionsApi->get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_catalog_organizations_organization_id_projects_project_id_versions_version_id_catalog_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 

### Return type

[**Directory**](Directory.md)

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

# **get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get**
> List[Thread] get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get(organization_id, project_id, version_id, include_commenter_ids=include_commenter_ids, include_message_count=include_message_count)

Get Version Comment Threads

Get all comment threads a version

### Example


```python
import audithub_sdk
from audithub_sdk.models.thread import Thread
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    include_commenter_ids = False # bool | Include distinct user ids of users who created comments in each thread. (optional) (default to False)
    include_message_count = False # bool | Include the count of messages in each thread. (optional) (default to False)

    try:
        # Get Version Comment Threads
        api_response = await api_instance.get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get(organization_id, project_id, version_id, include_commenter_ids=include_commenter_ids, include_message_count=include_message_count)
        print("The response of VersionsApi->get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_comment_threads_organizations_organization_id_projects_project_id_versions_version_id_comment_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **include_commenter_ids** | **bool**| Include distinct user ids of users who created comments in each thread. | [optional] [default to False]
 **include_message_count** | **bool**| Include the count of messages in each thread. | [optional] [default to False]

### Return type

[**List[Thread]**](Thread.md)

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

# **get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get**
> List[Comment] get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get(organization_id, project_id, version_id, thread_id=thread_id, limit=limit, offset=offset, from_date=from_date, to_date=to_date, order_by=order_by)

Get Version Comments

Get all comments of any thread of the version in chronological order

### Example


```python
import audithub_sdk
from audithub_sdk.models.comment import Comment
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    thread_id = 56 # int |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    order_by = 'created_at DESC' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.     Column values are: thread_id, comment_id, created_by, created_at     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.      (optional) (default to 'created_at DESC')

    try:
        # Get Version Comments
        api_response = await api_instance.get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get(organization_id, project_id, version_id, thread_id=thread_id, limit=limit, offset=offset, from_date=from_date, to_date=to_date, order_by=order_by)
        print("The response of VersionsApi->get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_comments_organizations_organization_id_projects_project_id_versions_version_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **thread_id** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.     Column values are: thread_id, comment_id, created_by, created_at     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.      | [optional] [default to &#39;created_at DESC&#39;]

### Return type

[**List[Comment]**](Comment.md)

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

# **get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get**
> get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get(organization_id, project_id, version_id, relative_path)

Get Version File

Get the contents of a versions's file.

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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    relative_path = 'relative_path_example' # str | 

    try:
        # Get Version File
        await api_instance.get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get(organization_id, project_id, version_id, relative_path)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_file_organizations_organization_id_projects_project_id_versions_version_id_file_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **relative_path** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get**
> List[TaskFIOData] get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get(organization_id, project_id, version_id)

Get Version Findings

Get the findings across all tasks of a version

### Example


```python
import audithub_sdk
from audithub_sdk.models.task_fio_data import TaskFIOData
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 

    try:
        # Get Version Findings
        api_response = await api_instance.get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get(organization_id, project_id, version_id)
        print("The response of VersionsApi->get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_findings_organizations_organization_id_projects_project_id_versions_version_id_findings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 

### Return type

[**List[TaskFIOData]**](TaskFIOData.md)

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

# **get_version_organizations_organization_id_projects_project_id_versions_version_id_get**
> Version get_version_organizations_organization_id_projects_project_id_versions_version_id_get(organization_id, project_id, version_id, catalog=catalog, abi=abi)

Get Version

Get version of project

### Example


```python
import audithub_sdk
from audithub_sdk.models.version import Version
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    catalog = False # bool |  (optional) (default to False)
    abi = False # bool |  (optional) (default to False)

    try:
        # Get Version
        api_response = await api_instance.get_version_organizations_organization_id_projects_project_id_versions_version_id_get(organization_id, project_id, version_id, catalog=catalog, abi=abi)
        print("The response of VersionsApi->get_version_organizations_organization_id_projects_project_id_versions_version_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_organizations_organization_id_projects_project_id_versions_version_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **catalog** | **bool**|  | [optional] [default to False]
 **abi** | **bool**|  | [optional] [default to False]

### Return type

[**Version**](Version.md)

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

# **get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get**
> OrganizationConsumptionDetailed get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get(organization_id, project_id, version_id, months=months)

Get Version Resource Detailed

Returns version detailed consumption

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_consumption_detailed import OrganizationConsumptionDetailed
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    months = 56 # int | Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. (optional)

    try:
        # Get Version Resource Detailed
        api_response = await api_instance.get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get(organization_id, project_id, version_id, months=months)
        print("The response of VersionsApi->get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_resource_detailed_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_detailed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **months** | **int**| Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. | [optional] 

### Return type

[**OrganizationConsumptionDetailed**](OrganizationConsumptionDetailed.md)

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

# **get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get**
> OrganizationConsumption get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get(organization_id, project_id, version_id, months=months)

Get Version Resource Usage

Returns version consumption

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_consumption import OrganizationConsumption
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    months = 56 # int | Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. (optional)

    try:
        # Get Version Resource Usage
        api_response = await api_instance.get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get(organization_id, project_id, version_id, months=months)
        print("The response of VersionsApi->get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_version_resource_usage_organizations_organization_id_projects_project_id_versions_version_id_resource_consumption_total_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **months** | **int**| Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. | [optional] 

### Return type

[**OrganizationConsumption**](OrganizationConsumption.md)

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

# **get_versions_organizations_organization_id_projects_project_id_versions_get**
> List[Version] get_versions_organizations_organization_id_projects_project_id_versions_get(organization_id, project_id)

Get Versions

Get versions by project

### Example


```python
import audithub_sdk
from audithub_sdk.models.version import Version
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Versions
        api_response = await api_instance.get_versions_organizations_organization_id_projects_project_id_versions_get(organization_id, project_id)
        print("The response of VersionsApi->get_versions_organizations_organization_id_projects_project_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->get_versions_organizations_organization_id_projects_project_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**List[Version]**](Version.md)

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

# **patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch**
> SuccessAndMessageResponse patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch(organization_id, project_id, version_id, version_patch)

Patch Version

Patch version of a project

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.version_patch import VersionPatch
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    version_id = 56 # int | 
    version_patch = audithub_sdk.VersionPatch() # VersionPatch | 

    try:
        # Patch Version
        api_response = await api_instance.patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch(organization_id, project_id, version_id, version_patch)
        print("The response of VersionsApi->patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->patch_version_organizations_organization_id_projects_project_id_versions_version_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **version_id** | **int**|  | 
 **version_patch** | [**VersionPatch**](VersionPatch.md)|  | 

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

# **post_temp_version_organizations_organization_id_temp_versions_post**
> TempVersion post_temp_version_organizations_organization_id_temp_versions_post(organization_id, archive, name=name, commit_hash=commit_hash, is_deployed=is_deployed)

Post Temp Version

Post temp version by uploading file

### Example


```python
import audithub_sdk
from audithub_sdk.models.temp_version import TempVersion
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    archive = 'archive_example' # str | A .zip archive with the sources for this version of the project, and possibly the V specifications
    name = 'name_example' # str |  (optional)
    commit_hash = 'commit_hash_example' # str |  (optional)
    is_deployed = False # bool | It denotes if this version is deployed on chain. (optional) (default to False)

    try:
        # Post Temp Version
        api_response = await api_instance.post_temp_version_organizations_organization_id_temp_versions_post(organization_id, archive, name=name, commit_hash=commit_hash, is_deployed=is_deployed)
        print("The response of VersionsApi->post_temp_version_organizations_organization_id_temp_versions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->post_temp_version_organizations_organization_id_temp_versions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **archive** | **str**| A .zip archive with the sources for this version of the project, and possibly the V specifications | 
 **name** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **is_deployed** | **bool**| It denotes if this version is deployed on chain. | [optional] [default to False]

### Return type

[**TempVersion**](TempVersion.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_temp_version_with_url_organizations_organization_id_temp_versions_url_post**
> TempVersion post_temp_version_with_url_organizations_organization_id_temp_versions_url_post(organization_id, input_type, url, name=name, commit_hash=commit_hash, is_deployed=is_deployed, revision=revision, includes_submodules=includes_submodules)

Post Temp Version With Url

Post temp version using url

### Example


```python
import audithub_sdk
from audithub_sdk.models.temp_version import TempVersion
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    input_type = 'input_type_example' # str | The method used to provide sources
    url = 'url_example' # str | In case of git input this is required and its the the repo url. In case of archive its the url of a zip archive
    name = 'name_example' # str |  (optional)
    commit_hash = 'commit_hash_example' # str |  (optional)
    is_deployed = False # bool | It denotes if this version is deployed on chain. (optional) (default to False)
    revision = 'revision_example' # str |  (optional)
    includes_submodules = True # bool |  (optional)

    try:
        # Post Temp Version With Url
        api_response = await api_instance.post_temp_version_with_url_organizations_organization_id_temp_versions_url_post(organization_id, input_type, url, name=name, commit_hash=commit_hash, is_deployed=is_deployed, revision=revision, includes_submodules=includes_submodules)
        print("The response of VersionsApi->post_temp_version_with_url_organizations_organization_id_temp_versions_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->post_temp_version_with_url_organizations_organization_id_temp_versions_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **input_type** | **str**| The method used to provide sources | 
 **url** | **str**| In case of git input this is required and its the the repo url. In case of archive its the url of a zip archive | 
 **name** | **str**|  | [optional] 
 **commit_hash** | **str**|  | [optional] 
 **is_deployed** | **bool**| It denotes if this version is deployed on chain. | [optional] [default to False]
 **revision** | **str**|  | [optional] 
 **includes_submodules** | **bool**|  | [optional] 

### Return type

[**TempVersion**](TempVersion.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_version_organizations_organization_id_projects_project_id_versions_post**
> IdAndMessageResponse post_version_organizations_organization_id_projects_project_id_versions_post(organization_id, project_id, name, archive, commit_hash=commit_hash, is_deployed=is_deployed)

Post Version

Post version by uploading file

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    name = 'name_example' # str | A name that uniquely identifies this version inside the project.
    archive = 'archive_example' # str | A .zip archive with the sources for this version of the project, and possibly the V specifications
    commit_hash = 'commit_hash_example' # str |  (optional)
    is_deployed = False # bool | It denotes if this version is deployed on chain. (optional) (default to False)

    try:
        # Post Version
        api_response = await api_instance.post_version_organizations_organization_id_projects_project_id_versions_post(organization_id, project_id, name, archive, commit_hash=commit_hash, is_deployed=is_deployed)
        print("The response of VersionsApi->post_version_organizations_organization_id_projects_project_id_versions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->post_version_organizations_organization_id_projects_project_id_versions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **name** | **str**| A name that uniquely identifies this version inside the project. | 
 **archive** | **str**| A .zip archive with the sources for this version of the project, and possibly the V specifications | 
 **commit_hash** | **str**|  | [optional] 
 **is_deployed** | **bool**| It denotes if this version is deployed on chain. | [optional] [default to False]

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post**
> IdAndMessageResponse post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post(organization_id, project_id, name, input_type, url, commit_hash=commit_hash, is_deployed=is_deployed, revision=revision, includes_submodules=includes_submodules)

Post Version With Url

Post version using url

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
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
    api_instance = audithub_sdk.VersionsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    name = 'name_example' # str | A name that uniquely identifies this version inside the project.
    input_type = 'input_type_example' # str | The method used to provide sources
    url = 'url_example' # str | In case of git input this is required and its the the repo url. In case of archive this is the url of a zip archive
    commit_hash = 'commit_hash_example' # str |  (optional)
    is_deployed = False # bool | It denotes if this version is deployed on chain. (optional) (default to False)
    revision = 'revision_example' # str |  (optional)
    includes_submodules = True # bool |  (optional)

    try:
        # Post Version With Url
        api_response = await api_instance.post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post(organization_id, project_id, name, input_type, url, commit_hash=commit_hash, is_deployed=is_deployed, revision=revision, includes_submodules=includes_submodules)
        print("The response of VersionsApi->post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionsApi->post_version_with_url_organizations_organization_id_projects_project_id_versions_url_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **name** | **str**| A name that uniquely identifies this version inside the project. | 
 **input_type** | **str**| The method used to provide sources | 
 **url** | **str**| In case of git input this is required and its the the repo url. In case of archive this is the url of a zip archive | 
 **commit_hash** | **str**|  | [optional] 
 **is_deployed** | **bool**| It denotes if this version is deployed on chain. | [optional] [default to False]
 **revision** | **str**|  | [optional] 
 **includes_submodules** | **bool**|  | [optional] 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

