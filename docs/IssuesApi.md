# audithub_sdk.IssuesApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_announce_organizations_organization_id_projects_project_id_issues_patch**](IssuesApi.md#batch_announce_organizations_organization_id_projects_project_id_issues_patch) | **PATCH** /organizations/{organization_id}/projects/{project_id}/issues/ | Batch Announce
[**export_issues_organizations_organization_id_projects_project_id_issues_export_get**](IssuesApi.md#export_issues_organizations_organization_id_projects_project_id_issues_export_get) | **GET** /organizations/{organization_id}/projects/{project_id}/issues/export | Export Issues
[**get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get**](IssuesApi.md#get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get) | **GET** /organizations/{organization_id}/projects/{project_id}/issues/{issue_id} | Get Issue
[**get_issues_organizations_organization_id_projects_project_id_issues_get**](IssuesApi.md#get_issues_organizations_organization_id_projects_project_id_issues_get) | **GET** /organizations/{organization_id}/projects/{project_id}/issues | Get Issues
[**patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch**](IssuesApi.md#patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch) | **PATCH** /organizations/{organization_id}/projects/{project_id}/issues/{issue_id} | Patch Issue
[**post_issue_organizations_organization_id_projects_project_id_issues_post**](IssuesApi.md#post_issue_organizations_organization_id_projects_project_id_issues_post) | **POST** /organizations/{organization_id}/projects/{project_id}/issues | Post Issue
[**post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post**](IssuesApi.md#post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post) | **POST** /organizations/{organization_id}/projects/{project_id}/issues/{issue_id}/gh-issue | Post Issue To Github
[**post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post**](IssuesApi.md#post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post) | **POST** /organizations/{organization_id}/projects/{project_id}/issues/{issue_id}/gh-security-advisory | Post Security Advisory To Github
[**put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put**](IssuesApi.md#put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put) | **PUT** /organizations/{organization_id}/projects/{project_id}/issues/{issue_id} | Put Issue


# **batch_announce_organizations_organization_id_projects_project_id_issues_patch**
> SuccessAndMessageResponse batch_announce_organizations_organization_id_projects_project_id_issues_patch(organization_id, project_id, issue_batch_announce)

Batch Announce

Batch announce

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_batch_announce import IssueBatchAnnounce
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_batch_announce = audithub_sdk.IssueBatchAnnounce() # IssueBatchAnnounce | 

    try:
        # Batch Announce
        api_response = await api_instance.batch_announce_organizations_organization_id_projects_project_id_issues_patch(organization_id, project_id, issue_batch_announce)
        print("The response of IssuesApi->batch_announce_organizations_organization_id_projects_project_id_issues_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->batch_announce_organizations_organization_id_projects_project_id_issues_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_batch_announce** | [**IssueBatchAnnounce**](IssueBatchAnnounce.md)|  | 

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

# **export_issues_organizations_organization_id_projects_project_id_issues_export_get**
> object export_issues_organizations_organization_id_projects_project_id_issues_export_get(organization_id, project_id)

Export Issues

Returns all issues of project

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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Export Issues
        api_response = await api_instance.export_issues_organizations_organization_id_projects_project_id_issues_export_get(organization_id, project_id)
        print("The response of IssuesApi->export_issues_organizations_organization_id_projects_project_id_issues_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->export_issues_organizations_organization_id_projects_project_id_issues_export_get: %s\n" % e)
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

# **get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get**
> IssueDetails get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get(organization_id, project_id, issue_id)

Get Issue

Returns an issue by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_details import IssueDetails
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int | 

    try:
        # Get Issue
        api_response = await api_instance.get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get(organization_id, project_id, issue_id)
        print("The response of IssuesApi->get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issue_organizations_organization_id_projects_project_id_issues_issue_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | 

### Return type

[**IssueDetails**](IssueDetails.md)

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

# **get_issues_organizations_organization_id_projects_project_id_issues_get**
> List[IssueForList] get_issues_organizations_organization_id_projects_project_id_issues_get(organization_id, project_id)

Get Issues

Returns all issues of project

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_for_list import IssueForList
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Get Issues
        api_response = await api_instance.get_issues_organizations_organization_id_projects_project_id_issues_get(organization_id, project_id)
        print("The response of IssuesApi->get_issues_organizations_organization_id_projects_project_id_issues_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->get_issues_organizations_organization_id_projects_project_id_issues_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 

### Return type

[**List[IssueForList]**](IssueForList.md)

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

# **patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch**
> SuccessAndMessageResponse patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch(organization_id, project_id, issue_id, issue_patch)

Patch Issue

Patch issue

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_patch import IssuePatch
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int | 
    issue_patch = audithub_sdk.IssuePatch() # IssuePatch | 

    try:
        # Patch Issue
        api_response = await api_instance.patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch(organization_id, project_id, issue_id, issue_patch)
        print("The response of IssuesApi->patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->patch_issue_organizations_organization_id_projects_project_id_issues_issue_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | 
 **issue_patch** | [**IssuePatch**](IssuePatch.md)|  | 

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

# **post_issue_organizations_organization_id_projects_project_id_issues_post**
> IdAndMessageResponse post_issue_organizations_organization_id_projects_project_id_issues_post(organization_id, project_id, issue_info_base_complete)

Post Issue

Post a new issue

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.issue_info_base_complete import IssueInfoBaseComplete
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_info_base_complete = audithub_sdk.IssueInfoBaseComplete() # IssueInfoBaseComplete | 

    try:
        # Post Issue
        api_response = await api_instance.post_issue_organizations_organization_id_projects_project_id_issues_post(organization_id, project_id, issue_info_base_complete)
        print("The response of IssuesApi->post_issue_organizations_organization_id_projects_project_id_issues_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->post_issue_organizations_organization_id_projects_project_id_issues_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_info_base_complete** | [**IssueInfoBaseComplete**](IssueInfoBaseComplete.md)|  | 

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

# **post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post**
> SuccessAndMessageResponse post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post(organization_id, project_id, issue_id)

Post Issue To Github

Post an existing issue to github

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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int | 

    try:
        # Post Issue To Github
        api_response = await api_instance.post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post(organization_id, project_id, issue_id)
        print("The response of IssuesApi->post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->post_issue_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_issue_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | 

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

# **post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post**
> SuccessAndMessageResponse post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post(organization_id, project_id, issue_id)

Post Security Advisory To Github

Post an existing issue to github

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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int | 

    try:
        # Post Security Advisory To Github
        api_response = await api_instance.post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post(organization_id, project_id, issue_id)
        print("The response of IssuesApi->post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->post_security_advisory_to_github_organizations_organization_id_projects_project_id_issues_issue_id_gh_security_advisory_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | 

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

# **put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put**
> IdAndMessageResponse put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put(organization_id, project_id, issue_id, issue_info_editable)

Put Issue

Put issue

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.issue_info_editable import IssueInfoEditable
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
    api_instance = audithub_sdk.IssuesApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 
    issue_id = 56 # int | 
    issue_info_editable = audithub_sdk.IssueInfoEditable() # IssueInfoEditable | 

    try:
        # Put Issue
        api_response = await api_instance.put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put(organization_id, project_id, issue_id, issue_info_editable)
        print("The response of IssuesApi->put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssuesApi->put_issue_organizations_organization_id_projects_project_id_issues_issue_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **project_id** | **int**|  | 
 **issue_id** | **int**|  | 
 **issue_info_editable** | [**IssueInfoEditable**](IssueInfoEditable.md)|  | 

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

