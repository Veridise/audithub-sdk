# audithub_sdk.AdminApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**about_admin_about_get**](AdminApi.md#about_admin_about_get) | **GET** /admin/about | About
[**get_active_tasks_admin_active_tasks_get**](AdminApi.md#get_active_tasks_admin_active_tasks_get) | **GET** /admin/active_tasks | Get Active Tasks
[**get_digest_admin_digest_get**](AdminApi.md#get_digest_admin_digest_get) | **GET** /admin/digest | Get Digest
[**get_invitations_admin_invitations_get**](AdminApi.md#get_invitations_admin_invitations_get) | **GET** /admin/invitations | Get Invitations
[**get_projects_admin_projects_get**](AdminApi.md#get_projects_admin_projects_get) | **GET** /admin/projects | Get Projects
[**get_sources_admin_sources_get**](AdminApi.md#get_sources_admin_sources_get) | **GET** /admin/sources | Get Sources
[**get_specs_admin_specs_get**](AdminApi.md#get_specs_admin_specs_get) | **GET** /admin/specs | Get Specs
[**get_statistics_for_tasks_all_admin_statistics_tasks_all_get**](AdminApi.md#get_statistics_for_tasks_all_admin_statistics_tasks_all_get) | **GET** /admin/statistics/tasks/all | Get task statistics for all users
[**get_statistics_for_tasks_external_admin_statistics_tasks_external_get**](AdminApi.md#get_statistics_for_tasks_external_admin_statistics_tasks_external_get) | **GET** /admin/statistics/tasks/external | Get task statistics for external users
[**get_tasks_admin_tasks_get**](AdminApi.md#get_tasks_admin_tasks_get) | **GET** /admin/tasks | Get Tasks
[**get_user_profile_admin_users_user_id_profile_get**](AdminApi.md#get_user_profile_admin_users_user_id_profile_get) | **GET** /admin/users/{user_id}/profile | Get User Profile
[**get_users_admin_users_get**](AdminApi.md#get_users_admin_users_get) | **GET** /admin/users | Get Users
[**get_versions_admin_versions_get**](AdminApi.md#get_versions_admin_versions_get) | **GET** /admin/versions | Get Versions
[**onboard_requests_admin_onboard_requests_get**](AdminApi.md#onboard_requests_admin_onboard_requests_get) | **GET** /admin/onboard/requests | Onboard Requests
[**onboard_user_admin_onboard_get**](AdminApi.md#onboard_user_admin_onboard_get) | **GET** /admin/onboard | Onboard User
[**patch_project_admin_projects_patch**](AdminApi.md#patch_project_admin_projects_patch) | **PATCH** /admin/projects | Patch Project
[**put_user_profile_admin_users_user_id_profile_put**](AdminApi.md#put_user_profile_admin_users_user_id_profile_put) | **PUT** /admin/users/{user_id}/profile | Put User Profile
[**qa_cleanup_admin_qa_cleanup_get**](AdminApi.md#qa_cleanup_admin_qa_cleanup_get) | **GET** /admin/qa-cleanup | Qa Cleanup
[**remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete**](AdminApi.md#remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete) | **DELETE** /admin/organizations/{organization_id}/users/{email} | Remove User Assignment Or Invitation
[**user_onboard_options_admin_onboard_options_get**](AdminApi.md#user_onboard_options_admin_onboard_options_get) | **GET** /admin/onboard/options | User Onboard Options


# **about_admin_about_get**
> object about_admin_about_get()

About

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
    api_instance = audithub_sdk.AdminApi(api_client)

    try:
        # About
        api_response = await api_instance.about_admin_about_get()
        print("The response of AdminApi->about_admin_about_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->about_admin_about_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_tasks_admin_active_tasks_get**
> object get_active_tasks_admin_active_tasks_get(organization_id=organization_id, tool_name=tool_name)

Get Active Tasks

Get the number of active tasks per organization and tool, potentially limiting them with query parameters.

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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | Organization id. If specified, limits the results to this organization. (optional)
    tool_name = 'tool_name_example' # str | Tool name. If specified, limits the results to this tool. (optional)

    try:
        # Get Active Tasks
        api_response = await api_instance.get_active_tasks_admin_active_tasks_get(organization_id=organization_id, tool_name=tool_name)
        print("The response of AdminApi->get_active_tasks_admin_active_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_active_tasks_admin_active_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization id. If specified, limits the results to this organization. | [optional] 
 **tool_name** | **str**| Tool name. If specified, limits the results to this tool. | [optional] 

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

# **get_digest_admin_digest_get**
> object get_digest_admin_digest_get(user_id=user_id, from_created_at=from_created_at)

Get Digest

Prepare daily user digests, optionally filtered by user_id

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
    api_instance = audithub_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | User id. If specified, limits the results to this user. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Comment dates to include in the digest notification (optional)

    try:
        # Get Digest
        api_response = await api_instance.get_digest_admin_digest_get(user_id=user_id, from_created_at=from_created_at)
        print("The response of AdminApi->get_digest_admin_digest_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_digest_admin_digest_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. If specified, limits the results to this user. | [optional] 
 **from_created_at** | **datetime**| Comment dates to include in the digest notification | [optional] 

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

# **get_invitations_admin_invitations_get**
> List[Invitation] get_invitations_admin_invitations_get(organization_id=organization_id)

Get Invitations

Get all invitations

### Example


```python
import audithub_sdk
from audithub_sdk.models.invitation import Invitation
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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | Organization id. If specified, limits the results to this organization. (optional)

    try:
        # Get Invitations
        api_response = await api_instance.get_invitations_admin_invitations_get(organization_id=organization_id)
        print("The response of AdminApi->get_invitations_admin_invitations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_invitations_admin_invitations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization id. If specified, limits the results to this organization. | [optional] 

### Return type

[**List[Invitation]**](Invitation.md)

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

# **get_projects_admin_projects_get**
> List[ProjectAdmin] get_projects_admin_projects_get(organization_id=organization_id, project_id=project_id, created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, order_by=order_by)

Get Projects

Get list of all projects, potentially limiting them with query parameters

### Example


```python
import audithub_sdk
from audithub_sdk.models.project_admin import ProjectAdmin
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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | Organization id. If specified, limits the results to this organization. (optional)
    project_id = 56 # int | Project id. If specified, limits the results to this project. (optional)
    created_by = 'created_by_example' # str | Created by user. If specified, limits the results to the projects created by this user. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to projects created on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to projects created before (<) this time. (optional)
    include_deleted = True # bool | Also list soft-deleted projects. By default only active projects are retrieved. (optional)
    order_by = 'order_by_example' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.          (optional)

    try:
        # Get Projects
        api_response = await api_instance.get_projects_admin_projects_get(organization_id=organization_id, project_id=project_id, created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, order_by=order_by)
        print("The response of AdminApi->get_projects_admin_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_projects_admin_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization id. If specified, limits the results to this organization. | [optional] 
 **project_id** | **int**| Project id. If specified, limits the results to this project. | [optional] 
 **created_by** | **str**| Created by user. If specified, limits the results to the projects created by this user. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to projects created on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to projects created before (&lt;) this time. | [optional] 
 **include_deleted** | **bool**| Also list soft-deleted projects. By default only active projects are retrieved. | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.          | [optional] 

### Return type

[**List[ProjectAdmin]**](ProjectAdmin.md)

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

# **get_sources_admin_sources_get**
> str get_sources_admin_sources_get(task_id=task_id)

Get Sources

Get version sources by task

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
    api_instance = audithub_sdk.AdminApi(api_client)
    task_id = 56 # int | Task id for which sources are returned (optional)

    try:
        # Get Sources
        api_response = await api_instance.get_sources_admin_sources_get(task_id=task_id)
        print("The response of AdminApi->get_sources_admin_sources_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_sources_admin_sources_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task id for which sources are returned | [optional] 

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

# **get_specs_admin_specs_get**
> str get_specs_admin_specs_get(task_id=task_id)

Get Specs

Get V specs specified at the task level, as a .zip archive

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
    api_instance = audithub_sdk.AdminApi(api_client)
    task_id = 56 # int | Task id for which V specs are returned (optional)

    try:
        # Get Specs
        api_response = await api_instance.get_specs_admin_specs_get(task_id=task_id)
        print("The response of AdminApi->get_specs_admin_specs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_specs_admin_specs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **int**| Task id for which V specs are returned | [optional] 

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

# **get_statistics_for_tasks_all_admin_statistics_tasks_all_get**
> object get_statistics_for_tasks_all_admin_statistics_tasks_all_get(from_created_at=from_created_at, to_created_at=to_created_at)

Get task statistics for all users

Get aggregate statistics for tasks

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
    api_instance = audithub_sdk.AdminApi(api_client)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started before (<) this time. (optional)

    try:
        # Get task statistics for all users
        api_response = await api_instance.get_statistics_for_tasks_all_admin_statistics_tasks_all_get(from_created_at=from_created_at, to_created_at=to_created_at)
        print("The response of AdminApi->get_statistics_for_tasks_all_admin_statistics_tasks_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_statistics_for_tasks_all_admin_statistics_tasks_all_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started before (&lt;) this time. | [optional] 

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

# **get_statistics_for_tasks_external_admin_statistics_tasks_external_get**
> object get_statistics_for_tasks_external_admin_statistics_tasks_external_get(from_created_at=from_created_at, to_created_at=to_created_at)

Get task statistics for external users

Get aggregate statistics for tasks, excluding all veridise staff

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
    api_instance = audithub_sdk.AdminApi(api_client)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started before (<) this time. (optional)

    try:
        # Get task statistics for external users
        api_response = await api_instance.get_statistics_for_tasks_external_admin_statistics_tasks_external_get(from_created_at=from_created_at, to_created_at=to_created_at)
        print("The response of AdminApi->get_statistics_for_tasks_external_admin_statistics_tasks_external_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_statistics_for_tasks_external_admin_statistics_tasks_external_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started before (&lt;) this time. | [optional] 

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

# **get_tasks_admin_tasks_get**
> List[TaskAdmin] get_tasks_admin_tasks_get(organization_id=organization_id, project_id=project_id, version_id=version_id, task_id=task_id, created_by=created_by, tool_name=tool_name, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, offset=offset, limit=limit, order_by=order_by)

Get Tasks

Get list of a all tasks, potentially limiting them with query parameters

### Example


```python
import audithub_sdk
from audithub_sdk.models.task_admin import TaskAdmin
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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | Organization id. If specified, limits the results to this organization. (optional)
    project_id = 56 # int | Project id. If specified, limits the results to this project. (optional)
    version_id = 56 # int | Version id. If specified, limits the results to this version. (optional)
    task_id = 56 # int | Task id. If specified, limits the results to this task. (optional)
    created_by = 'created_by_example' # str | Created by user. If specified, limits the results to the tasks created by this user. (optional)
    tool_name = 'tool_name_example' # str | Tool name. If specified, limits the results to the tasks created for this tool. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started before (<) this time. (optional)
    include_deleted = True # bool | Also list soft-deleted tasks. By default only active versions are retrieved. (optional)
    offset = 56 # int | Offset. If specified, skip the first offset tasks from results. (optional)
    limit = 56 # int | Limit. If specified, limits the number of results to this number. (optional)
    order_by = 'order_by_example' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, version_id, task_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.          (optional)

    try:
        # Get Tasks
        api_response = await api_instance.get_tasks_admin_tasks_get(organization_id=organization_id, project_id=project_id, version_id=version_id, task_id=task_id, created_by=created_by, tool_name=tool_name, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, offset=offset, limit=limit, order_by=order_by)
        print("The response of AdminApi->get_tasks_admin_tasks_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_tasks_admin_tasks_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization id. If specified, limits the results to this organization. | [optional] 
 **project_id** | **int**| Project id. If specified, limits the results to this project. | [optional] 
 **version_id** | **int**| Version id. If specified, limits the results to this version. | [optional] 
 **task_id** | **int**| Task id. If specified, limits the results to this task. | [optional] 
 **created_by** | **str**| Created by user. If specified, limits the results to the tasks created by this user. | [optional] 
 **tool_name** | **str**| Tool name. If specified, limits the results to the tasks created for this tool. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started before (&lt;) this time. | [optional] 
 **include_deleted** | **bool**| Also list soft-deleted tasks. By default only active versions are retrieved. | [optional] 
 **offset** | **int**| Offset. If specified, skip the first offset tasks from results. | [optional] 
 **limit** | **int**| Limit. If specified, limits the number of results to this number. | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, version_id, task_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.          | [optional] 

### Return type

[**List[TaskAdmin]**](TaskAdmin.md)

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

# **get_user_profile_admin_users_user_id_profile_get**
> UserForAdmin get_user_profile_admin_users_user_id_profile_get(user_id)

Get User Profile

Get a user's profile

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_for_admin import UserForAdmin
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
    api_instance = audithub_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Profile
        api_response = await api_instance.get_user_profile_admin_users_user_id_profile_get(user_id)
        print("The response of AdminApi->get_user_profile_admin_users_user_id_profile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_profile_admin_users_user_id_profile_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserForAdmin**](UserForAdmin.md)

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

# **get_users_admin_users_get**
> List[UserAdmin] get_users_admin_users_get(user_id=user_id, email=email, from_created_at=from_created_at, to_created_at=to_created_at, order_by=order_by)

Get Users

Get list of all users, potentially limiting them with query parameters

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_admin import UserAdmin
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
    api_instance = audithub_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | User id. If specified, limits the results to this user. (optional)
    email = 'email_example' # str | Email. If specified, limits the results to this user. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to tasks started before (<) this time. (optional)
    order_by = 'order_by_example' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: user_id, email, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.          (optional)

    try:
        # Get Users
        api_response = await api_instance.get_users_admin_users_get(user_id=user_id, email=email, from_created_at=from_created_at, to_created_at=to_created_at, order_by=order_by)
        print("The response of AdminApi->get_users_admin_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_users_admin_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id. If specified, limits the results to this user. | [optional] 
 **email** | **str**| Email. If specified, limits the results to this user. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to tasks started before (&lt;) this time. | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: user_id, email, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.          | [optional] 

### Return type

[**List[UserAdmin]**](UserAdmin.md)

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

# **get_versions_admin_versions_get**
> List[VersionAdmin] get_versions_admin_versions_get(organization_id=organization_id, project_id=project_id, version_id=version_id, created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, order_by=order_by)

Get Versions

Get list of all versions, potentially limiting them with query parameters

### Example


```python
import audithub_sdk
from audithub_sdk.models.version_admin import VersionAdmin
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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | Organization id. If specified, limits the results to this organization. (optional)
    project_id = 56 # int | Project id. If specified, limits the results to this project. (optional)
    version_id = 56 # int | Version id. If specified, limits the results to this version. (optional)
    created_by = 'created_by_example' # str | Created by user. If specified, limits the results to the versions created by this user. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to the versions created on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to the versions created before (<) this time. (optional)
    include_deleted = True # bool | Also list soft-deleted versions. By default only active versions are retrieved. (optional)
    order_by = 'order_by_example' # str | Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, version_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \"created_by, created_at DESC\" orders the results per user, with the most recent task first for each user.          (optional)

    try:
        # Get Versions
        api_response = await api_instance.get_versions_admin_versions_get(organization_id=organization_id, project_id=project_id, version_id=version_id, created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted, order_by=order_by)
        print("The response of AdminApi->get_versions_admin_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_versions_admin_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**| Organization id. If specified, limits the results to this organization. | [optional] 
 **project_id** | **int**| Project id. If specified, limits the results to this project. | [optional] 
 **version_id** | **int**| Version id. If specified, limits the results to this version. | [optional] 
 **created_by** | **str**| Created by user. If specified, limits the results to the versions created by this user. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to the versions created on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to the versions created before (&lt;) this time. | [optional] 
 **include_deleted** | **bool**| Also list soft-deleted versions. By default only active versions are retrieved. | [optional] 
 **order_by** | **str**| Order of results, as a comma-separated list of columns and, optionally, a direction.         Column values are: organization_id, project_id, version_id, created_by, created_at         If direction in specified for any column, separate it with a space from the column name and provide ASC or DESC for ascending or descending order.         e.g., \&quot;created_by, created_at DESC\&quot; orders the results per user, with the most recent task first for each user.          | [optional] 

### Return type

[**List[VersionAdmin]**](VersionAdmin.md)

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

# **onboard_requests_admin_onboard_requests_get**
> List[OnboardingRequest] onboard_requests_admin_onboard_requests_get(request_status=request_status)

Onboard Requests

List onboarding requests

### Example


```python
import audithub_sdk
from audithub_sdk.models.onboarding_request import OnboardingRequest
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
    api_instance = audithub_sdk.AdminApi(api_client)
    request_status = 'request_status_example' # str | The status of the onboarding requests to list (optional)

    try:
        # Onboard Requests
        api_response = await api_instance.onboard_requests_admin_onboard_requests_get(request_status=request_status)
        print("The response of AdminApi->onboard_requests_admin_onboard_requests_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->onboard_requests_admin_onboard_requests_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_status** | **str**| The status of the onboarding requests to list | [optional] 

### Return type

[**List[OnboardingRequest]**](OnboardingRequest.md)

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

# **onboard_user_admin_onboard_get**
> object onboard_user_admin_onboard_get(user_id, create_organization=create_organization, new_organization_name=new_organization_name, populate=populate, grant_access_to_organization=grant_access_to_organization)

Onboard User

Execute user onboarding

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
    api_instance = audithub_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | User id to onboard
    create_organization = False # bool | If specified, a new organization will be created and the user will be granted access to it (optional) (default to False)
    new_organization_name = 'new_organization_name_example' # str | If specified, this will be the name of the new organization (optional)
    populate = 'populate_example' # str | Custom template for populating the user's initial data (e.g., projects , versions etc.). and/or restrictions (optional)
    grant_access_to_organization = 56 # int | If specified, the user will be granted access to this pre-existing organization (optional)

    try:
        # Onboard User
        api_response = await api_instance.onboard_user_admin_onboard_get(user_id, create_organization=create_organization, new_organization_name=new_organization_name, populate=populate, grant_access_to_organization=grant_access_to_organization)
        print("The response of AdminApi->onboard_user_admin_onboard_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->onboard_user_admin_onboard_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User id to onboard | 
 **create_organization** | **bool**| If specified, a new organization will be created and the user will be granted access to it | [optional] [default to False]
 **new_organization_name** | **str**| If specified, this will be the name of the new organization | [optional] 
 **populate** | **str**| Custom template for populating the user&#39;s initial data (e.g., projects , versions etc.). and/or restrictions | [optional] 
 **grant_access_to_organization** | **int**| If specified, the user will be granted access to this pre-existing organization | [optional] 

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

# **patch_project_admin_projects_patch**
> SuccessAndMessageResponse patch_project_admin_projects_patch(admin_resource_patch, project_id=project_id, project_name=project_name)

Patch Project

Patch project

### Example


```python
import audithub_sdk
from audithub_sdk.models.admin_resource_patch import AdminResourcePatch
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
    api_instance = audithub_sdk.AdminApi(api_client)
    admin_resource_patch = audithub_sdk.AdminResourcePatch() # AdminResourcePatch | 
    project_id = 56 # int | Project id. If specified, apply the patch action to the project with this project_id. (optional)
    project_name = 'project_name_example' # str | Project name. If specified, apply the patch action to all the projects with this project_name. (optional)

    try:
        # Patch Project
        api_response = await api_instance.patch_project_admin_projects_patch(admin_resource_patch, project_id=project_id, project_name=project_name)
        print("The response of AdminApi->patch_project_admin_projects_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->patch_project_admin_projects_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_resource_patch** | [**AdminResourcePatch**](AdminResourcePatch.md)|  | 
 **project_id** | **int**| Project id. If specified, apply the patch action to the project with this project_id. | [optional] 
 **project_name** | **str**| Project name. If specified, apply the patch action to all the projects with this project_name. | [optional] 

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

# **put_user_profile_admin_users_user_id_profile_put**
> SuccessAndMessageResponse put_user_profile_admin_users_user_id_profile_put(user_id, put_user)

Put User Profile

Update the adjustable parts of a user's profile

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
    api_instance = audithub_sdk.AdminApi(api_client)
    user_id = 'user_id_example' # str | 
    put_user = audithub_sdk.PutUser() # PutUser | 

    try:
        # Put User Profile
        api_response = await api_instance.put_user_profile_admin_users_user_id_profile_put(user_id, put_user)
        print("The response of AdminApi->put_user_profile_admin_users_user_id_profile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->put_user_profile_admin_users_user_id_profile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
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

# **qa_cleanup_admin_qa_cleanup_get**
> SuccessAndMessageResponse qa_cleanup_admin_qa_cleanup_get()

Qa Cleanup

Cleanup Q/A data

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
    api_instance = audithub_sdk.AdminApi(api_client)

    try:
        # Qa Cleanup
        api_response = await api_instance.qa_cleanup_admin_qa_cleanup_get()
        print("The response of AdminApi->qa_cleanup_admin_qa_cleanup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->qa_cleanup_admin_qa_cleanup_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete**
> SuccessAndMessageResponse remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete(organization_id, email)

Remove User Assignment Or Invitation

Remove user assignment or invitation

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
    api_instance = audithub_sdk.AdminApi(api_client)
    organization_id = 56 # int | 
    email = 'email_example' # str | 

    try:
        # Remove User Assignment Or Invitation
        api_response = await api_instance.remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete(organization_id, email)
        print("The response of AdminApi->remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_user_assignment_or_invitation_admin_organizations_organization_id_users_email_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **email** | **str**|  | 

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

# **user_onboard_options_admin_onboard_options_get**
> object user_onboard_options_admin_onboard_options_get()

User Onboard Options

Available options for a user onboarding

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
    api_instance = audithub_sdk.AdminApi(api_client)

    try:
        # User Onboard Options
        api_response = await api_instance.user_onboard_options_admin_onboard_options_get()
        print("The response of AdminApi->user_onboard_options_admin_onboard_options_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->user_onboard_options_admin_onboard_options_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

