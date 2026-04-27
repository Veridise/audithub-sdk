# audithub_sdk.ProjectsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete**](ProjectsApi.md#delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete) | **DELETE** /organizations/{organization_id}/projects/{project_id}/gh-link | Delete Github Link
[**delete_project_organizations_organization_id_projects_project_id_delete**](ProjectsApi.md#delete_project_organizations_organization_id_projects_project_id_delete) | **DELETE** /organizations/{organization_id}/projects/{project_id} | Delete Project
[**get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get**](ProjectsApi.md#get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get) | **GET** /organizations/{organization_id}/projects/{project_id}/issue-transitions | Get Issue Transitions
[**get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get**](ProjectsApi.md#get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get) | **GET** /organizations/{organization_id}/projects/{project_id}/comment-threads | Get Project Comment Threads
[**get_project_comments_organizations_organization_id_projects_project_id_comments_get**](ProjectsApi.md#get_project_comments_organizations_organization_id_projects_project_id_comments_get) | **GET** /organizations/{organization_id}/projects/{project_id}/comments | Get Project Comments
[**get_project_findings_organizations_organization_id_projects_project_id_findings_get**](ProjectsApi.md#get_project_findings_organizations_organization_id_projects_project_id_findings_get) | **GET** /organizations/{organization_id}/projects/{project_id}/findings | Get Project Findings
[**get_project_organizations_organization_id_projects_project_id_get**](ProjectsApi.md#get_project_organizations_organization_id_projects_project_id_get) | **GET** /organizations/{organization_id}/projects/{project_id} | Get Project
[**get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get**](ProjectsApi.md#get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get) | **GET** /organizations/{organization_id}/projects/{project_id}/resource-consumption-detailed | Get Project Resource Detailed
[**get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get**](ProjectsApi.md#get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get) | **GET** /organizations/{organization_id}/projects/{project_id}/resource-consumption-total | Get Project Resource Usage
[**get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get**](ProjectsApi.md#get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get) | **GET** /organizations/{organization_id}/projects/{project_id}/revision/{revision} | Get Project Revision
[**get_projects_organizations_organization_id_projects_get**](ProjectsApi.md#get_projects_organizations_organization_id_projects_get) | **GET** /organizations/{organization_id}/projects | Get Projects
[**get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get**](ProjectsApi.md#get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get) | **GET** /organizations/{organization_id}/projects/{project_id}/revisions | Get Projects Revisions
[**get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get**](ProjectsApi.md#get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get) | **GET** /organizations/{organization_id}/projects/{project_id}/user-settings | Get User Project Settings
[**get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get**](ProjectsApi.md#get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get) | **GET** /organizations/{organization_id}/projects/{project_id}/threads/{thread_id}/user-settings | Get User Thread Settings
[**get_users_organizations_organization_id_projects_project_id_users_get**](ProjectsApi.md#get_users_organizations_organization_id_projects_project_id_users_get) | **GET** /organizations/{organization_id}/projects/{project_id}/users | Get Users
[**patch_project_organizations_organization_id_projects_project_id_patch**](ProjectsApi.md#patch_project_organizations_organization_id_projects_project_id_patch) | **PATCH** /organizations/{organization_id}/projects/{project_id} | Patch Project
[**patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch**](ProjectsApi.md#patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch) | **PATCH** /organizations/{organization_id}/projects/{project_id}/threads/{thread_id} | Patch Thread
[**post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post**](ProjectsApi.md#post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post) | **POST** /organizations/{organization_id}/projects/{project_id}/threads/{thread_id} | Post New Comment
[**post_project_organizations_organization_id_projects_post**](ProjectsApi.md#post_project_organizations_organization_id_projects_post) | **POST** /organizations/{organization_id}/projects | Post Project
[**put_github_link_organizations_organization_id_projects_project_id_gh_link_put**](ProjectsApi.md#put_github_link_organizations_organization_id_projects_project_id_gh_link_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/gh-link | Put Github Link
[**put_project_organizations_organization_id_projects_project_id_put**](ProjectsApi.md#put_project_organizations_organization_id_projects_project_id_put) | **PUT** /organizations/{organization_id}/projects/{project_id} | Put Project
[**put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put**](ProjectsApi.md#put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/user-settings | Put User Project Settings
[**put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put**](ProjectsApi.md#put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/threads/{thread_id}/user-settings | Put User Thread Settings


# **delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete**
> SuccessAndMessageResponse delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete(organization_id, project_id)

Delete Github Link

Remove link to GitHub project

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Delete Github Link
        api_response = await api_instance.delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete(organization_id, project_id)
        print("The response of ProjectsApi->delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_github_link_organizations_organization_id_projects_project_id_gh_link_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

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

# **delete_project_organizations_organization_id_projects_project_id_delete**
> SuccessAndMessageResponse delete_project_organizations_organization_id_projects_project_id_delete(organization_id, project_id)

Delete Project

Permanently delete a project

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Delete Project
        api_response = await api_instance.delete_project_organizations_organization_id_projects_project_id_delete(organization_id, project_id)
        print("The response of ProjectsApi->delete_project_organizations_organization_id_projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project_organizations_organization_id_projects_project_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

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

# **get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get**
> List[IssueStatusTransition] get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get(organization_id, project_id, issue_id=issue_id, from_date=from_date, to_date=to_date, created_by=created_by, limit=limit, offset=offset, order_by=order_by)

Get Issue Transitions

Returns all issue transitions of project's issues

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_status_transition import IssueStatusTransition
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int |  (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    created_by = 'created_by_example' # str |  (optional)
    limit = 56 # int |  (optional)
    offset = 56 # int |  (optional)
    order_by = 'created_at DESC' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.     Possible column names are: issue_id,id,function_id,from_status_id,created_at,created_by     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.      (optional) (default to 'created_at DESC')

    try:
        # Get Issue Transitions
        api_response = await api_instance.get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get(organization_id, project_id, issue_id=issue_id, from_date=from_date, to_date=to_date, created_by=created_by, limit=limit, offset=offset, order_by=order_by)
        print("The response of ProjectsApi->get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_issue_transitions_organizations_organization_id_projects_project_id_issue_transitions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | [optional] 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 
 **created_by** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.     Possible column names are: issue_id,id,function_id,from_status_id,created_at,created_by     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.      | [optional] [default to &#39;created_at DESC&#39;]

### Return type

[**List[IssueStatusTransition]**](IssueStatusTransition.md)

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

# **get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get**
> List[Thread] get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get(organization_id, project_id, include_commenter_ids=include_commenter_ids, include_message_count=include_message_count)

Get Project Comment Threads

Get all comment threads of a project

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    include_commenter_ids = False # bool | Include distinct user ids of users who created comments in each thread. (optional) (default to False)
    include_message_count = False # bool | Include the count of messages in each thread. (optional) (default to False)

    try:
        # Get Project Comment Threads
        api_response = await api_instance.get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get(organization_id, project_id, include_commenter_ids=include_commenter_ids, include_message_count=include_message_count)
        print("The response of ProjectsApi->get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_comment_threads_organizations_organization_id_projects_project_id_comment_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
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

# **get_project_comments_organizations_organization_id_projects_project_id_comments_get**
> List[Comment] get_project_comments_organizations_organization_id_projects_project_id_comments_get(organization_id, project_id, limit, offset, thread_id=thread_id, from_date=from_date, to_date=to_date, order_by=order_by)

Get Project Comments

Get all comments of any thread of any version in chronological order

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    limit = 56 # int | 
    offset = 56 # int | 
    thread_id = 56 # int |  (optional)
    from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    order_by = 'created_at DESC' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.     Column values are: thread_id, comment_id, created_by, created_at     If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.     e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.      (optional) (default to 'created_at DESC')

    try:
        # Get Project Comments
        api_response = await api_instance.get_project_comments_organizations_organization_id_projects_project_id_comments_get(organization_id, project_id, limit, offset, thread_id=thread_id, from_date=from_date, to_date=to_date, order_by=order_by)
        print("The response of ProjectsApi->get_project_comments_organizations_organization_id_projects_project_id_comments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_comments_organizations_organization_id_projects_project_id_comments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **limit** | **int**|  | 
 **offset** | **int**|  | 
 **thread_id** | **int**|  | [optional] 
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

# **get_project_findings_organizations_organization_id_projects_project_id_findings_get**
> List[TaskFIOData] get_project_findings_organizations_organization_id_projects_project_id_findings_get(organization_id, project_id)

Get Project Findings

Get the findings across all tasks of a project

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Project Findings
        api_response = await api_instance.get_project_findings_organizations_organization_id_projects_project_id_findings_get(organization_id, project_id)
        print("The response of ProjectsApi->get_project_findings_organizations_organization_id_projects_project_id_findings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_findings_organizations_organization_id_projects_project_id_findings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

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

# **get_project_organizations_organization_id_projects_project_id_get**
> Project get_project_organizations_organization_id_projects_project_id_get(organization_id, project_id)

Get Project

Returns project attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.project import Project
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Project
        api_response = await api_instance.get_project_organizations_organization_id_projects_project_id_get(organization_id, project_id)
        print("The response of ProjectsApi->get_project_organizations_organization_id_projects_project_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_organizations_organization_id_projects_project_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**Project**](Project.md)

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

# **get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get**
> OrganizationConsumptionDetailed get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get(organization_id, project_id, months=months)

Get Project Resource Detailed

Returns project detailed consumption

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    months = 56 # int | Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. (optional)

    try:
        # Get Project Resource Detailed
        api_response = await api_instance.get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get(organization_id, project_id, months=months)
        print("The response of ProjectsApi->get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_resource_detailed_organizations_organization_id_projects_project_id_resource_consumption_detailed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
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

# **get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get**
> OrganizationConsumption get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get(organization_id, project_id, months=months)

Get Project Resource Usage

Returns project consumption

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    months = 56 # int | Number of months, since today, to report on. When not defined, active subscription period will be used, if any. Otherwise a default period of 3 months will be used. (optional)

    try:
        # Get Project Resource Usage
        api_response = await api_instance.get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get(organization_id, project_id, months=months)
        print("The response of ProjectsApi->get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_resource_usage_organizations_organization_id_projects_project_id_resource_consumption_total_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
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

# **get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get**
> ProjectInfoOutput get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get(organization_id, project_id, revision)

Get Project Revision

Returns project attributes for a specific revision

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_info_output import ProjectInfoOutput
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    revision = 'revision_example' # str | 

    try:
        # Get Project Revision
        api_response = await api_instance.get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get(organization_id, project_id, revision)
        print("The response of ProjectsApi->get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_revision_organizations_organization_id_projects_project_id_revision_revision_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **revision** | **str**|  | 

### Return type

[**ProjectInfoOutput**](ProjectInfoOutput.md)

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

# **get_projects_organizations_organization_id_projects_get**
> List[Project] get_projects_organizations_organization_id_projects_get(organization_id)

Get Projects

Returns all projects of a organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.project import Project
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Projects
        api_response = await api_instance.get_projects_organizations_organization_id_projects_get(organization_id)
        print("The response of ProjectsApi->get_projects_organizations_organization_id_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_organizations_organization_id_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[Project]**](Project.md)

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

# **get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get**
> object get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get(organization_id, project_id)

Get Projects Revisions

Returns all revisions of a project

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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Projects Revisions
        api_response = await api_instance.get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get(organization_id, project_id)
        print("The response of ProjectsApi->get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects_revisions_organizations_organization_id_projects_project_id_revisions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

**object**

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

# **get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get**
> UserProjectSetting get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get(organization_id, project_id)

Get User Project Settings

Get the user's project settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_project_setting import UserProjectSetting
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get User Project Settings
        api_response = await api_instance.get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get(organization_id, project_id)
        print("The response of ProjectsApi->get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_user_project_settings_organizations_organization_id_projects_project_id_user_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**UserProjectSetting**](UserProjectSetting.md)

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

# **get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get**
> UserThreadSetting get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get(organization_id, project_id, thread_id)

Get User Thread Settings

Get the user's thread settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_thread_setting import UserThreadSetting
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    thread_id = 56 # int | 

    try:
        # Get User Thread Settings
        api_response = await api_instance.get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get(organization_id, project_id, thread_id)
        print("The response of ProjectsApi->get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **thread_id** | **int**|  | 

### Return type

[**UserThreadSetting**](UserThreadSetting.md)

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

# **get_users_organizations_organization_id_projects_project_id_users_get**
> List[UserInformation] get_users_organizations_organization_id_projects_project_id_users_get(organization_id, project_id)

Get Users

The users that have a access to a project within an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_information import UserInformation
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Users
        api_response = await api_instance.get_users_organizations_organization_id_projects_project_id_users_get(organization_id, project_id)
        print("The response of ProjectsApi->get_users_organizations_organization_id_projects_project_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_users_organizations_organization_id_projects_project_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**List[UserInformation]**](UserInformation.md)

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

# **patch_project_organizations_organization_id_projects_project_id_patch**
> SuccessAndMessageResponse patch_project_organizations_organization_id_projects_project_id_patch(organization_id, project_id, resource_patch)

Patch Project

Patch project

### Example


```python
import audithub_sdk
from audithub_sdk.models.resource_patch import ResourcePatch
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    resource_patch = audithub_sdk.ResourcePatch() # ResourcePatch | 

    try:
        # Patch Project
        api_response = await api_instance.patch_project_organizations_organization_id_projects_project_id_patch(organization_id, project_id, resource_patch)
        print("The response of ProjectsApi->patch_project_organizations_organization_id_projects_project_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_project_organizations_organization_id_projects_project_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **resource_patch** | [**ResourcePatch**](ResourcePatch.md)|  | 

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

# **patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch**
> SuccessAndMessageResponse patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch(organization_id, project_id, thread_id, thread_patch)

Patch Thread

Alter thread status

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.thread_patch import ThreadPatch
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    thread_id = 56 # int | 
    thread_patch = audithub_sdk.ThreadPatch() # ThreadPatch | 

    try:
        # Patch Thread
        api_response = await api_instance.patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch(organization_id, project_id, thread_id, thread_patch)
        print("The response of ProjectsApi->patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->patch_thread_organizations_organization_id_projects_project_id_threads_thread_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **thread_id** | **int**|  | 
 **thread_patch** | [**ThreadPatch**](ThreadPatch.md)|  | 

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

# **post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post**
> SuccessAndMessageResponse post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post(organization_id, project_id, thread_id, thread_comment)

Post New Comment

Post new thread comment

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.thread_comment import ThreadComment
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    thread_id = 56 # int | 
    thread_comment = audithub_sdk.ThreadComment() # ThreadComment | 

    try:
        # Post New Comment
        api_response = await api_instance.post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post(organization_id, project_id, thread_id, thread_comment)
        print("The response of ProjectsApi->post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_new_comment_organizations_organization_id_projects_project_id_threads_thread_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **thread_id** | **int**|  | 
 **thread_comment** | [**ThreadComment**](ThreadComment.md)|  | 

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

# **post_project_organizations_organization_id_projects_post**
> IdAndMessageResponse post_project_organizations_organization_id_projects_post(organization_id, project_info_input, temp_version_id=temp_version_id, version_name=version_name)

Post Project

Post initial data and its first source version

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.project_info_input import ProjectInfoInput
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_info_input = audithub_sdk.ProjectInfoInput() # ProjectInfoInput | 
    temp_version_id = 'temp_version_id_example' # str |  (optional)
    version_name = 'version_name_example' # str |  (optional)

    try:
        # Post Project
        api_response = await api_instance.post_project_organizations_organization_id_projects_post(organization_id, project_info_input, temp_version_id=temp_version_id, version_name=version_name)
        print("The response of ProjectsApi->post_project_organizations_organization_id_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->post_project_organizations_organization_id_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_info_input** | [**ProjectInfoInput**](ProjectInfoInput.md)|  | 
 **temp_version_id** | **str**|  | [optional] 
 **version_name** | **str**|  | [optional] 

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

# **put_github_link_organizations_organization_id_projects_project_id_gh_link_put**
> SuccessAndMessageResponse put_github_link_organizations_organization_id_projects_project_id_gh_link_put(organization_id, project_id, project_git_hub_link)

Put Github Link

Lik and re-link to GitHub project

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_git_hub_link import ProjectGitHubLink
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    project_git_hub_link = audithub_sdk.ProjectGitHubLink() # ProjectGitHubLink | 

    try:
        # Put Github Link
        api_response = await api_instance.put_github_link_organizations_organization_id_projects_project_id_gh_link_put(organization_id, project_id, project_git_hub_link)
        print("The response of ProjectsApi->put_github_link_organizations_organization_id_projects_project_id_gh_link_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_github_link_organizations_organization_id_projects_project_id_gh_link_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **project_git_hub_link** | [**ProjectGitHubLink**](ProjectGitHubLink.md)|  | 

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

# **put_project_organizations_organization_id_projects_project_id_put**
> ProjectUpdateResponse put_project_organizations_organization_id_projects_project_id_put(organization_id, project_id, project_info_input)

Put Project

Update project attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_info_input import ProjectInfoInput
from audithub_sdk.models.project_update_response import ProjectUpdateResponse
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    project_info_input = audithub_sdk.ProjectInfoInput() # ProjectInfoInput | 

    try:
        # Put Project
        api_response = await api_instance.put_project_organizations_organization_id_projects_project_id_put(organization_id, project_id, project_info_input)
        print("The response of ProjectsApi->put_project_organizations_organization_id_projects_project_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_project_organizations_organization_id_projects_project_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **project_info_input** | [**ProjectInfoInput**](ProjectInfoInput.md)|  | 

### Return type

[**ProjectUpdateResponse**](ProjectUpdateResponse.md)

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

# **put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put**
> SuccessAndMessageResponse put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put(organization_id, project_id, put_user)

Put User Project Settings

Updates the user's project settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.put_user import PutUser
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    put_user = audithub_sdk.PutUser() # PutUser | 

    try:
        # Put User Project Settings
        api_response = await api_instance.put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put(organization_id, project_id, put_user)
        print("The response of ProjectsApi->put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_user_project_settings_organizations_organization_id_projects_project_id_user_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **put_user** | [**PutUser**](PutUser.md)|  | 

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

# **put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put**
> SuccessAndMessageResponse put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put(organization_id, project_id, thread_id, put_user)

Put User Thread Settings

Updates the user's project settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.put_user import PutUser
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
    api_instance = audithub_sdk.ProjectsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    thread_id = 56 # int | 
    put_user = audithub_sdk.PutUser() # PutUser | 

    try:
        # Put User Thread Settings
        api_response = await api_instance.put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put(organization_id, project_id, thread_id, put_user)
        print("The response of ProjectsApi->put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->put_user_thread_settings_organizations_organization_id_projects_project_id_threads_thread_id_user_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **thread_id** | **int**|  | 
 **put_user** | [**PutUser**](PutUser.md)|  | 

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

