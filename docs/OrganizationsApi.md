# audithub_sdk.OrganizationsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_project_to_favorites_organizations_organization_id_favorite_projects_post**](OrganizationsApi.md#add_project_to_favorites_organizations_organization_id_favorite_projects_post) | **POST** /organizations/{organization_id}/favorite-projects | Add Project To Favorites
[**create_missing_environment_organizations_organization_id_environment_get**](OrganizationsApi.md#create_missing_environment_organizations_organization_id_environment_get) | **GET** /organizations/{organization_id}/environment | Create Missing Environment
[**create_missing_organization_namespaces_organizations_namespace_get**](OrganizationsApi.md#create_missing_organization_namespaces_organizations_namespace_get) | **GET** /organizations/namespace | Create Missing Organization Namespaces
[**delete_github_connect_organizations_organization_id_github_connect_delete**](OrganizationsApi.md#delete_github_connect_organizations_organization_id_github_connect_delete) | **DELETE** /organizations/{organization_id}/github-connect | Delete Github Connect
[**delete_invitation_organizations_organization_id_invitations_invitation_id_delete**](OrganizationsApi.md#delete_invitation_organizations_organization_id_invitations_invitation_id_delete) | **DELETE** /organizations/{organization_id}/invitations/{invitation_id} | Delete Invitation
[**delete_issue_type_organizations_organization_id_issue_types_type_id_delete**](OrganizationsApi.md#delete_issue_type_organizations_organization_id_issue_types_type_id_delete) | **DELETE** /organizations/{organization_id}/issue_types/{type_id} | Delete Issue Type
[**delete_organization_organizations_organization_id_delete**](OrganizationsApi.md#delete_organization_organizations_organization_id_delete) | **DELETE** /organizations/{organization_id} | Delete Organization
[**delete_organization_user_organizations_organization_id_users_user_id_delete**](OrganizationsApi.md#delete_organization_user_organizations_organization_id_users_user_id_delete) | **DELETE** /organizations/{organization_id}/users/{user_id} | Delete Organization User
[**export_onboarding_package_organizations_organization_id_create_package_post**](OrganizationsApi.md#export_onboarding_package_organizations_organization_id_create_package_post) | **POST** /organizations/{organization_id}/create-package | Export Onboarding Package
[**get_active_organization_users_organizations_organization_id_active_users_get**](OrganizationsApi.md#get_active_organization_users_organizations_organization_id_active_users_get) | **GET** /organizations/{organization_id}/active-users | Get Active Organization Users
[**get_favorite_projects_organizations_organization_id_favorite_projects_get**](OrganizationsApi.md#get_favorite_projects_organizations_organization_id_favorite_projects_get) | **GET** /organizations/{organization_id}/favorite-projects | Get Favorite Projects
[**get_gh_repos_organizations_organization_id_gh_repos_get**](OrganizationsApi.md#get_gh_repos_organizations_organization_id_gh_repos_get) | **GET** /organizations/{organization_id}/gh-repos | Get Gh Repos
[**get_github_connect_info_organizations_github_connect_commit_get**](OrganizationsApi.md#get_github_connect_info_organizations_github_connect_commit_get) | **GET** /organizations/github-connect-commit | Get Github Connect Info
[**get_github_connect_url_organizations_organization_id_github_connect_get**](OrganizationsApi.md#get_github_connect_url_organizations_organization_id_github_connect_get) | **GET** /organizations/{organization_id}/github-connect | Get Github Connect Url
[**get_invitation_organizations_organization_id_invitations_invitation_id_get**](OrganizationsApi.md#get_invitation_organizations_organization_id_invitations_invitation_id_get) | **GET** /organizations/{organization_id}/invitations/{invitation_id} | Get Invitation
[**get_issue_type_organizations_organization_id_issue_types_type_id_get**](OrganizationsApi.md#get_issue_type_organizations_organization_id_issue_types_type_id_get) | **GET** /organizations/{organization_id}/issue_types/{type_id} | Get Issue Type
[**get_organization_issue_types_organizations_organization_id_issue_types_get**](OrganizationsApi.md#get_organization_issue_types_organizations_organization_id_issue_types_get) | **GET** /organizations/{organization_id}/issue_types | Get Organization Issue Types
[**get_organization_organizations_organization_id_get**](OrganizationsApi.md#get_organization_organizations_organization_id_get) | **GET** /organizations/{organization_id} | Get Organization
[**get_organization_quota_organizations_organization_id_quota_get**](OrganizationsApi.md#get_organization_quota_organizations_organization_id_quota_get) | **GET** /organizations/{organization_id}/quota | Get Organization Quota
[**get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get**](OrganizationsApi.md#get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get) | **GET** /organizations/{organization_id}/resource-consumption-detailed | Get Organization Resource Detailed
[**get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get**](OrganizationsApi.md#get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get) | **GET** /organizations/{organization_id}/resource-consumption-total | Get Organization Resource Usage
[**get_organization_restrictions_organizations_organization_id_restrictions_get**](OrganizationsApi.md#get_organization_restrictions_organizations_organization_id_restrictions_get) | **GET** /organizations/{organization_id}/restrictions | Get Organization Restrictions
[**get_organization_usage_organizations_organization_id_usage_get**](OrganizationsApi.md#get_organization_usage_organizations_organization_id_usage_get) | **GET** /organizations/{organization_id}/usage | Get Organization Usage
[**get_organization_user_groups_organizations_organization_id_user_groups_get**](OrganizationsApi.md#get_organization_user_groups_organizations_organization_id_user_groups_get) | **GET** /organizations/{organization_id}/user-groups | Get Organization User Groups
[**get_organization_users_organizations_organization_id_users_get**](OrganizationsApi.md#get_organization_users_organizations_organization_id_users_get) | **GET** /organizations/{organization_id}/users | Get Organization Users
[**get_organizations_organizations_get**](OrganizationsApi.md#get_organizations_organizations_get) | **GET** /organizations | Get Organizations
[**get_pending_invitations_organizations_organization_id_pending_invitations_get**](OrganizationsApi.md#get_pending_invitations_organizations_organization_id_pending_invitations_get) | **GET** /organizations/{organization_id}/pending-invitations | Get Pending Invitations
[**get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get**](OrganizationsApi.md#get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get) | **GET** /organizations/{organization_id}/users/{user_id}/effective-restrictions | Get User Effective Restrictions
[**get_user_organization_settings_organizations_organization_id_user_settings_get**](OrganizationsApi.md#get_user_organization_settings_organizations_organization_id_user_settings_get) | **GET** /organizations/{organization_id}/user-settings | Get User Organization Settings
[**get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get**](OrganizationsApi.md#get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get) | **GET** /organizations/{organization_id}/users/{user_id}/restrictions | Get User Restrictions
[**patch_invitation_organizations_organization_id_invitations_invitation_id_patch**](OrganizationsApi.md#patch_invitation_organizations_organization_id_invitations_invitation_id_patch) | **PATCH** /organizations/{organization_id}/invitations/{invitation_id} | Patch Invitation
[**patch_organization_organizations_organization_id_patch**](OrganizationsApi.md#patch_organization_organizations_organization_id_patch) | **PATCH** /organizations/{organization_id} | Patch Organization
[**patch_user_organizations_organization_id_users_patch**](OrganizationsApi.md#patch_user_organizations_organization_id_users_patch) | **PATCH** /organizations/{organization_id}/users | Patch User
[**post_invitation_organizations_organization_id_invitations_post**](OrganizationsApi.md#post_invitation_organizations_organization_id_invitations_post) | **POST** /organizations/{organization_id}/invitations | Post Invitation
[**post_issue_type_organizations_organization_id_issue_types_post**](OrganizationsApi.md#post_issue_type_organizations_organization_id_issue_types_post) | **POST** /organizations/{organization_id}/issue_types | Post Issue Type
[**post_organization_organizations_post**](OrganizationsApi.md#post_organization_organizations_post) | **POST** /organizations | Post Organization
[**post_organization_user_organizations_organization_id_users_post**](OrganizationsApi.md#post_organization_user_organizations_organization_id_users_post) | **POST** /organizations/{organization_id}/users | Post Organization User
[**put_issue_type_organizations_organization_id_issue_types_type_id_put**](OrganizationsApi.md#put_issue_type_organizations_organization_id_issue_types_type_id_put) | **PUT** /organizations/{organization_id}/issue_types/{type_id} | Put Issue Type
[**put_organization_organizations_organization_id_put**](OrganizationsApi.md#put_organization_organizations_organization_id_put) | **PUT** /organizations/{organization_id} | Put Organization
[**put_organization_restrictions_organizations_organization_id_restrictions_put**](OrganizationsApi.md#put_organization_restrictions_organizations_organization_id_restrictions_put) | **PUT** /organizations/{organization_id}/restrictions | Put Organization Restrictions
[**put_user_organization_settings_organizations_organization_id_user_settings_put**](OrganizationsApi.md#put_user_organization_settings_organizations_organization_id_user_settings_put) | **PUT** /organizations/{organization_id}/user-settings | Put User Organization Settings
[**put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put**](OrganizationsApi.md#put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put) | **PUT** /organizations/{organization_id}/users/{user_id}/restrictions | Put User Restrictions
[**remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete**](OrganizationsApi.md#remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete) | **DELETE** /organizations/{organization_id}/favorite-projects/{project_id} | Remove Project From Favorites


# **add_project_to_favorites_organizations_organization_id_favorite_projects_post**
> IdAndMessageResponse add_project_to_favorites_organizations_organization_id_favorite_projects_post(organization_id, favorite_project_assignment)

Add Project To Favorites

Adds a project to the user's favorite ones

### Example


```python
import audithub_sdk
from audithub_sdk.models.favorite_project_assignment import FavoriteProjectAssignment
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    favorite_project_assignment = audithub_sdk.FavoriteProjectAssignment() # FavoriteProjectAssignment | 

    try:
        # Add Project To Favorites
        api_response = await api_instance.add_project_to_favorites_organizations_organization_id_favorite_projects_post(organization_id, favorite_project_assignment)
        print("The response of OrganizationsApi->add_project_to_favorites_organizations_organization_id_favorite_projects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->add_project_to_favorites_organizations_organization_id_favorite_projects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **favorite_project_assignment** | [**FavoriteProjectAssignment**](FavoriteProjectAssignment.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

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

# **create_missing_environment_organizations_organization_id_environment_get**
> SuccessAndMessageResponse create_missing_environment_organizations_organization_id_environment_get(organization_id)

Create Missing Environment

Creates missing organization environment

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Create Missing Environment
        api_response = await api_instance.create_missing_environment_organizations_organization_id_environment_get(organization_id)
        print("The response of OrganizationsApi->create_missing_environment_organizations_organization_id_environment_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_missing_environment_organizations_organization_id_environment_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

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

# **create_missing_organization_namespaces_organizations_namespace_get**
> List[OrganizationAdmin] create_missing_organization_namespaces_organizations_namespace_get()

Create Missing Organization Namespaces

Returns all active organizations for which a namespace was missing and created.

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_admin import OrganizationAdmin
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)

    try:
        # Create Missing Organization Namespaces
        api_response = await api_instance.create_missing_organization_namespaces_organizations_namespace_get()
        print("The response of OrganizationsApi->create_missing_organization_namespaces_organizations_namespace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->create_missing_organization_namespaces_organizations_namespace_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrganizationAdmin]**](OrganizationAdmin.md)

### Authorization

[OpenIdConnect](../README.md#OpenIdConnect)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_github_connect_organizations_organization_id_github_connect_delete**
> SuccessAndMessageResponse delete_github_connect_organizations_organization_id_github_connect_delete(organization_id)

Delete Github Connect

Delete GitHub connection

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Delete Github Connect
        api_response = await api_instance.delete_github_connect_organizations_organization_id_github_connect_delete(organization_id)
        print("The response of OrganizationsApi->delete_github_connect_organizations_organization_id_github_connect_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_github_connect_organizations_organization_id_github_connect_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

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

# **delete_invitation_organizations_organization_id_invitations_invitation_id_delete**
> SuccessAndMessageResponse delete_invitation_organizations_organization_id_invitations_invitation_id_delete(organization_id, invitation_id)

Delete Invitation

Delete an invitation by id

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 

    try:
        # Delete Invitation
        api_response = await api_instance.delete_invitation_organizations_organization_id_invitations_invitation_id_delete(organization_id, invitation_id)
        print("The response of OrganizationsApi->delete_invitation_organizations_organization_id_invitations_invitation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_invitation_organizations_organization_id_invitations_invitation_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **invitation_id** | **int**|  | 

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

# **delete_issue_type_organizations_organization_id_issue_types_type_id_delete**
> SuccessAndMessageResponse delete_issue_type_organizations_organization_id_issue_types_type_id_delete(organization_id, type_id)

Delete Issue Type

Delete an issue type by id

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 

    try:
        # Delete Issue Type
        api_response = await api_instance.delete_issue_type_organizations_organization_id_issue_types_type_id_delete(organization_id, type_id)
        print("The response of OrganizationsApi->delete_issue_type_organizations_organization_id_issue_types_type_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_issue_type_organizations_organization_id_issue_types_type_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 

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

# **delete_organization_organizations_organization_id_delete**
> object delete_organization_organizations_organization_id_delete(organization_id)

Delete Organization

Permanently delete an organization

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Delete Organization
        api_response = await api_instance.delete_organization_organizations_organization_id_delete(organization_id)
        print("The response of OrganizationsApi->delete_organization_organizations_organization_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_organizations_organization_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

**object**

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

# **delete_organization_user_organizations_organization_id_users_user_id_delete**
> SuccessAndMessageResponse delete_organization_user_organizations_organization_id_users_user_id_delete(organization_id, user_id)

Delete Organization User

Remove user's access from organization

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_id = 'user_id_example' # str | 

    try:
        # Delete Organization User
        api_response = await api_instance.delete_organization_user_organizations_organization_id_users_user_id_delete(organization_id, user_id)
        print("The response of OrganizationsApi->delete_organization_user_organizations_organization_id_users_user_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->delete_organization_user_organizations_organization_id_users_user_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_id** | **str**|  | 

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

# **export_onboarding_package_organizations_organization_id_create_package_post**
> PackageData export_onboarding_package_organizations_organization_id_create_package_post(organization_id, new_organization_package)

Export Onboarding Package

Create an onboarding package using organization data

### Example


```python
import audithub_sdk
from audithub_sdk.models.new_organization_package import NewOrganizationPackage
from audithub_sdk.models.package_data import PackageData
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    new_organization_package = audithub_sdk.NewOrganizationPackage() # NewOrganizationPackage | 

    try:
        # Export Onboarding Package
        api_response = await api_instance.export_onboarding_package_organizations_organization_id_create_package_post(organization_id, new_organization_package)
        print("The response of OrganizationsApi->export_onboarding_package_organizations_organization_id_create_package_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->export_onboarding_package_organizations_organization_id_create_package_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **new_organization_package** | [**NewOrganizationPackage**](NewOrganizationPackage.md)|  | 

### Return type

[**PackageData**](PackageData.md)

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

# **get_active_organization_users_organizations_organization_id_active_users_get**
> ActiveOrganizationUsers get_active_organization_users_organizations_organization_id_active_users_get(organization_id)

Get Active Organization Users

Get all users with access to the specific organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.active_organization_users import ActiveOrganizationUsers
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Active Organization Users
        api_response = await api_instance.get_active_organization_users_organizations_organization_id_active_users_get(organization_id)
        print("The response of OrganizationsApi->get_active_organization_users_organizations_organization_id_active_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_active_organization_users_organizations_organization_id_active_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**ActiveOrganizationUsers**](ActiveOrganizationUsers.md)

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

# **get_favorite_projects_organizations_organization_id_favorite_projects_get**
> List[Optional[int]] get_favorite_projects_organizations_organization_id_favorite_projects_get(organization_id)

Get Favorite Projects

Get the user's favorite projects

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Favorite Projects
        api_response = await api_instance.get_favorite_projects_organizations_organization_id_favorite_projects_get(organization_id)
        print("The response of OrganizationsApi->get_favorite_projects_organizations_organization_id_favorite_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_favorite_projects_organizations_organization_id_favorite_projects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

**List[Optional[int]]**

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

# **get_gh_repos_organizations_organization_id_gh_repos_get**
> object get_gh_repos_organizations_organization_id_gh_repos_get(organization_id)

Get Gh Repos

Get github organization repos

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Gh Repos
        api_response = await api_instance.get_gh_repos_organizations_organization_id_gh_repos_get(organization_id)
        print("The response of OrganizationsApi->get_gh_repos_organizations_organization_id_gh_repos_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_gh_repos_organizations_organization_id_gh_repos_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

**object**

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

# **get_github_connect_info_organizations_github_connect_commit_get**
> object get_github_connect_info_organizations_github_connect_commit_get(setup_action, installation_id, state)

Get Github Connect Info

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    setup_action = 'setup_action_example' # str | 
    installation_id = 'installation_id_example' # str | 
    state = 'state_example' # str | 

    try:
        # Get Github Connect Info
        api_response = await api_instance.get_github_connect_info_organizations_github_connect_commit_get(setup_action, installation_id, state)
        print("The response of OrganizationsApi->get_github_connect_info_organizations_github_connect_commit_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_github_connect_info_organizations_github_connect_commit_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_action** | **str**|  | 
 **installation_id** | **str**|  | 
 **state** | **str**|  | 

### Return type

**object**

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

# **get_github_connect_url_organizations_organization_id_github_connect_get**
> str get_github_connect_url_organizations_organization_id_github_connect_get(organization_id, fe_state)

Get Github Connect Url

Get github connection url

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    fe_state = 'fe_state_example' # str | 

    try:
        # Get Github Connect Url
        api_response = await api_instance.get_github_connect_url_organizations_organization_id_github_connect_get(organization_id, fe_state)
        print("The response of OrganizationsApi->get_github_connect_url_organizations_organization_id_github_connect_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_github_connect_url_organizations_organization_id_github_connect_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **fe_state** | **str**|  | 

### Return type

**str**

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

# **get_invitation_organizations_organization_id_invitations_invitation_id_get**
> Invitation get_invitation_organizations_organization_id_invitations_invitation_id_get(organization_id, invitation_id)

Get Invitation

Get an invitation by id

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 

    try:
        # Get Invitation
        api_response = await api_instance.get_invitation_organizations_organization_id_invitations_invitation_id_get(organization_id, invitation_id)
        print("The response of OrganizationsApi->get_invitation_organizations_organization_id_invitations_invitation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_invitation_organizations_organization_id_invitations_invitation_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **invitation_id** | **int**|  | 

### Return type

[**Invitation**](Invitation.md)

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

# **get_issue_type_organizations_organization_id_issue_types_type_id_get**
> IssueType get_issue_type_organizations_organization_id_issue_types_type_id_get(organization_id, type_id)

Get Issue Type

Get an issue type by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type import IssueType
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 

    try:
        # Get Issue Type
        api_response = await api_instance.get_issue_type_organizations_organization_id_issue_types_type_id_get(organization_id, type_id)
        print("The response of OrganizationsApi->get_issue_type_organizations_organization_id_issue_types_type_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_issue_type_organizations_organization_id_issue_types_type_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 

### Return type

[**IssueType**](IssueType.md)

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

# **get_organization_issue_types_organizations_organization_id_issue_types_get**
> List[IssueType] get_organization_issue_types_organizations_organization_id_issue_types_get(organization_id)

Get Organization Issue Types

Get the available issue types for an organization.

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type import IssueType
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Issue Types
        api_response = await api_instance.get_organization_issue_types_organizations_organization_id_issue_types_get(organization_id)
        print("The response of OrganizationsApi->get_organization_issue_types_organizations_organization_id_issue_types_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_issue_types_organizations_organization_id_issue_types_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[IssueType]**](IssueType.md)

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

# **get_organization_organizations_organization_id_get**
> Organization get_organization_organizations_organization_id_get(organization_id)

Get Organization

Get the metadata of an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization import Organization
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization
        api_response = await api_instance.get_organization_organizations_organization_id_get(organization_id)
        print("The response of OrganizationsApi->get_organization_organizations_organization_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_organizations_organization_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**Organization**](Organization.md)

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

# **get_organization_quota_organizations_organization_id_quota_get**
> OrganizationQuota get_organization_quota_organizations_organization_id_quota_get(organization_id)

Get Organization Quota

Get current organization quota

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_quota import OrganizationQuota
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Quota
        api_response = await api_instance.get_organization_quota_organizations_organization_id_quota_get(organization_id)
        print("The response of OrganizationsApi->get_organization_quota_organizations_organization_id_quota_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_quota_organizations_organization_id_quota_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**OrganizationQuota**](OrganizationQuota.md)

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

# **get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get**
> List[VersionResources] get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get(organization_id, months=months)

Get Organization Resource Detailed

consumption

### Example


```python
import audithub_sdk
from audithub_sdk.models.version_resources import VersionResources
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    months = 3 # int | Fallback date interval in months when the organization has no active subscriptions. (optional) (default to 3)

    try:
        # Get Organization Resource Detailed
        api_response = await api_instance.get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get(organization_id, months=months)
        print("The response of OrganizationsApi->get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_resource_detailed_organizations_organization_id_resource_consumption_detailed_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **months** | **int**| Fallback date interval in months when the organization has no active subscriptions. | [optional] [default to 3]

### Return type

[**List[VersionResources]**](VersionResources.md)

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

# **get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get**
> OrganizationConsumption get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get(organization_id, months=months)

Get Organization Resource Usage

consumption

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    months = 3 # int | Fallback date interval in months when the organization has no active subscriptions. (optional) (default to 3)

    try:
        # Get Organization Resource Usage
        api_response = await api_instance.get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get(organization_id, months=months)
        print("The response of OrganizationsApi->get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_resource_usage_organizations_organization_id_resource_consumption_total_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **months** | **int**| Fallback date interval in months when the organization has no active subscriptions. | [optional] [default to 3]

### Return type

[**OrganizationConsumption**](OrganizationConsumption.md)

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

# **get_organization_restrictions_organizations_organization_id_restrictions_get**
> List[OrganizationAccessRestriction] get_organization_restrictions_organizations_organization_id_restrictions_get(organization_id)

Get Organization Restrictions

Get the access restrictions for an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_access_restriction import OrganizationAccessRestriction
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Restrictions
        api_response = await api_instance.get_organization_restrictions_organizations_organization_id_restrictions_get(organization_id)
        print("The response of OrganizationsApi->get_organization_restrictions_organizations_organization_id_restrictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_restrictions_organizations_organization_id_restrictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md)

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

# **get_organization_usage_organizations_organization_id_usage_get**
> object get_organization_usage_organizations_organization_id_usage_get(organization_id, from_date=from_date, to_date=to_date)

Get Organization Usage

Get organization usage

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    from_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    to_date = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

    try:
        # Get Organization Usage
        api_response = await api_instance.get_organization_usage_organizations_organization_id_usage_get(organization_id, from_date=from_date, to_date=to_date)
        print("The response of OrganizationsApi->get_organization_usage_organizations_organization_id_usage_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_usage_organizations_organization_id_usage_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **from_date** | **datetime**|  | [optional] 
 **to_date** | **datetime**|  | [optional] 

### Return type

**object**

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

# **get_organization_user_groups_organizations_organization_id_user_groups_get**
> List[UserGroup] get_organization_user_groups_organizations_organization_id_user_groups_get(organization_id)

Get Organization User Groups

Get the available groups of an organization.

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_group import UserGroup
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization User Groups
        api_response = await api_instance.get_organization_user_groups_organizations_organization_id_user_groups_get(organization_id)
        print("The response of OrganizationsApi->get_organization_user_groups_organizations_organization_id_user_groups_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_user_groups_organizations_organization_id_user_groups_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[UserGroup]**](UserGroup.md)

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

# **get_organization_users_organizations_organization_id_users_get**
> object get_organization_users_organizations_organization_id_users_get(organization_id)

Get Organization Users

Get all users with access to the specific organization

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Organization Users
        api_response = await api_instance.get_organization_users_organizations_organization_id_users_get(organization_id)
        print("The response of OrganizationsApi->get_organization_users_organizations_organization_id_users_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organization_users_organizations_organization_id_users_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

**object**

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

# **get_organizations_organizations_get**
> List[OrganizationAdmin] get_organizations_organizations_get(created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted)

Get Organizations

Returns all organizations

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_admin import OrganizationAdmin
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    created_by = 'created_by_example' # str | Created by user. If specified, limits the results to the organizations created by this user. (optional)
    from_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to organizations created on or after (>=) this time. (optional)
    to_created_at = '2013-10-20T19:20:30+01:00' # datetime | Timestamp in UTC. If specified, limits results to organizations created before (<) this time. (optional)
    include_deleted = True # bool | Also list soft-deleted organizations.  By default only active organizations are retrieved. (optional)

    try:
        # Get Organizations
        api_response = await api_instance.get_organizations_organizations_get(created_by=created_by, from_created_at=from_created_at, to_created_at=to_created_at, include_deleted=include_deleted)
        print("The response of OrganizationsApi->get_organizations_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_organizations_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **created_by** | **str**| Created by user. If specified, limits the results to the organizations created by this user. | [optional] 
 **from_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to organizations created on or after (&gt;&#x3D;) this time. | [optional] 
 **to_created_at** | **datetime**| Timestamp in UTC. If specified, limits results to organizations created before (&lt;) this time. | [optional] 
 **include_deleted** | **bool**| Also list soft-deleted organizations.  By default only active organizations are retrieved. | [optional] 

### Return type

[**List[OrganizationAdmin]**](OrganizationAdmin.md)

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

# **get_pending_invitations_organizations_organization_id_pending_invitations_get**
> List[Invitation] get_pending_invitations_organizations_organization_id_pending_invitations_get(organization_id)

Get Pending Invitations

Get all pending organization invitations

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get Pending Invitations
        api_response = await api_instance.get_pending_invitations_organizations_organization_id_pending_invitations_get(organization_id)
        print("The response of OrganizationsApi->get_pending_invitations_organizations_organization_id_pending_invitations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_pending_invitations_organizations_organization_id_pending_invitations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**List[Invitation]**](Invitation.md)

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

# **get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get**
> List[EffectiveUserAccessRestriction] get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get(organization_id, user_id)

Get User Effective Restrictions

Get the effective access restrictions for a user inside a organization, i.e., the aggregated organization and user ones

### Example


```python
import audithub_sdk
from audithub_sdk.models.effective_user_access_restriction import EffectiveUserAccessRestriction
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_id = 'user_id_example' # str | 

    try:
        # Get User Effective Restrictions
        api_response = await api_instance.get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get(organization_id, user_id)
        print("The response of OrganizationsApi->get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_user_effective_restrictions_organizations_organization_id_users_user_id_effective_restrictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[EffectiveUserAccessRestriction]**](EffectiveUserAccessRestriction.md)

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

# **get_user_organization_settings_organizations_organization_id_user_settings_get**
> UserOrganizationSetting get_user_organization_settings_organizations_organization_id_user_settings_get(organization_id)

Get User Organization Settings

Get the user's organization settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.user_organization_setting import UserOrganizationSetting
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get User Organization Settings
        api_response = await api_instance.get_user_organization_settings_organizations_organization_id_user_settings_get(organization_id)
        print("The response of OrganizationsApi->get_user_organization_settings_organizations_organization_id_user_settings_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_user_organization_settings_organizations_organization_id_user_settings_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**UserOrganizationSetting**](UserOrganizationSetting.md)

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

# **get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get**
> List[OrganizationAccessRestriction] get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get(organization_id, user_id)

Get User Restrictions

Get the access restrictions for a user inside an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_access_restriction import OrganizationAccessRestriction
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_id = 'user_id_example' # str | 

    try:
        # Get User Restrictions
        api_response = await api_instance.get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get(organization_id, user_id)
        print("The response of OrganizationsApi->get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->get_user_restrictions_organizations_organization_id_users_user_id_restrictions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_id** | **str**|  | 

### Return type

[**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md)

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

# **patch_invitation_organizations_organization_id_invitations_invitation_id_patch**
> SuccessAndMessageResponse patch_invitation_organizations_organization_id_invitations_invitation_id_patch(organization_id, invitation_id, invitation_patch)

Patch Invitation

Patch an invitation

### Example


```python
import audithub_sdk
from audithub_sdk.models.invitation_patch import InvitationPatch
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 
    invitation_patch = audithub_sdk.InvitationPatch() # InvitationPatch | 

    try:
        # Patch Invitation
        api_response = await api_instance.patch_invitation_organizations_organization_id_invitations_invitation_id_patch(organization_id, invitation_id, invitation_patch)
        print("The response of OrganizationsApi->patch_invitation_organizations_organization_id_invitations_invitation_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->patch_invitation_organizations_organization_id_invitations_invitation_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **invitation_id** | **int**|  | 
 **invitation_patch** | [**InvitationPatch**](InvitationPatch.md)|  | 

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

# **patch_organization_organizations_organization_id_patch**
> SuccessAndMessageResponse patch_organization_organizations_organization_id_patch(organization_id, resource_patch)

Patch Organization

Patch organization

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    resource_patch = audithub_sdk.ResourcePatch() # ResourcePatch | 

    try:
        # Patch Organization
        api_response = await api_instance.patch_organization_organizations_organization_id_patch(organization_id, resource_patch)
        print("The response of OrganizationsApi->patch_organization_organizations_organization_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->patch_organization_organizations_organization_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **resource_patch** | [**ResourcePatch**](ResourcePatch.md)|  | 

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

# **patch_user_organizations_organization_id_users_patch**
> SuccessAndMessageResponse patch_user_organizations_organization_id_users_patch(organization_id, user_patch)

Patch User

Patch user

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.user_patch import UserPatch
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_patch = audithub_sdk.UserPatch() # UserPatch | 

    try:
        # Patch User
        api_response = await api_instance.patch_user_organizations_organization_id_users_patch(organization_id, user_patch)
        print("The response of OrganizationsApi->patch_user_organizations_organization_id_users_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->patch_user_organizations_organization_id_users_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_patch** | [**UserPatch**](UserPatch.md)|  | 

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

# **post_invitation_organizations_organization_id_invitations_post**
> SuccessAndMessageResponse post_invitation_organizations_organization_id_invitations_post(organization_id, new_invitation)

Post Invitation

Create a user invitation for an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.new_invitation import NewInvitation
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    new_invitation = audithub_sdk.NewInvitation() # NewInvitation | 

    try:
        # Post Invitation
        api_response = await api_instance.post_invitation_organizations_organization_id_invitations_post(organization_id, new_invitation)
        print("The response of OrganizationsApi->post_invitation_organizations_organization_id_invitations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->post_invitation_organizations_organization_id_invitations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **new_invitation** | [**NewInvitation**](NewInvitation.md)|  | 

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

# **post_issue_type_organizations_organization_id_issue_types_post**
> IdAndMessageResponse post_issue_type_organizations_organization_id_issue_types_post(organization_id, issue_type_info)

Post Issue Type

Create new organization issue type

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.issue_type_info import IssueTypeInfo
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    issue_type_info = audithub_sdk.IssueTypeInfo() # IssueTypeInfo | 

    try:
        # Post Issue Type
        api_response = await api_instance.post_issue_type_organizations_organization_id_issue_types_post(organization_id, issue_type_info)
        print("The response of OrganizationsApi->post_issue_type_organizations_organization_id_issue_types_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->post_issue_type_organizations_organization_id_issue_types_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **issue_type_info** | [**IssueTypeInfo**](IssueTypeInfo.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

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

# **post_organization_organizations_post**
> IdAndMessageResponse post_organization_organizations_post(new_organization)

Post Organization

Post Organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.id_and_message_response import IdAndMessageResponse
from audithub_sdk.models.new_organization import NewOrganization
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    new_organization = audithub_sdk.NewOrganization() # NewOrganization | 

    try:
        # Post Organization
        api_response = await api_instance.post_organization_organizations_post(new_organization)
        print("The response of OrganizationsApi->post_organization_organizations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->post_organization_organizations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_organization** | [**NewOrganization**](NewOrganization.md)|  | 

### Return type

[**IdAndMessageResponse**](IdAndMessageResponse.md)

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

# **post_organization_user_organizations_organization_id_users_post**
> SuccessAndMessageResponse post_organization_user_organizations_organization_id_users_post(organization_id, user_to_organization_assignment)

Post Organization User

Allow user to access the specific organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.user_to_organization_assignment import UserToOrganizationAssignment
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_to_organization_assignment = audithub_sdk.UserToOrganizationAssignment() # UserToOrganizationAssignment | 

    try:
        # Post Organization User
        api_response = await api_instance.post_organization_user_organizations_organization_id_users_post(organization_id, user_to_organization_assignment)
        print("The response of OrganizationsApi->post_organization_user_organizations_organization_id_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->post_organization_user_organizations_organization_id_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_to_organization_assignment** | [**UserToOrganizationAssignment**](UserToOrganizationAssignment.md)|  | 

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

# **put_issue_type_organizations_organization_id_issue_types_type_id_put**
> SuccessAndMessageResponse put_issue_type_organizations_organization_id_issue_types_type_id_put(organization_id, type_id, issue_type_info)

Put Issue Type

Put an issue type by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.issue_type_info import IssueTypeInfo
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    type_id = 56 # int | 
    issue_type_info = audithub_sdk.IssueTypeInfo() # IssueTypeInfo | 

    try:
        # Put Issue Type
        api_response = await api_instance.put_issue_type_organizations_organization_id_issue_types_type_id_put(organization_id, type_id, issue_type_info)
        print("The response of OrganizationsApi->put_issue_type_organizations_organization_id_issue_types_type_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->put_issue_type_organizations_organization_id_issue_types_type_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **type_id** | **int**|  | 
 **issue_type_info** | [**IssueTypeInfo**](IssueTypeInfo.md)|  | 

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

# **put_organization_organizations_organization_id_put**
> SuccessAndMessageResponse put_organization_organizations_organization_id_put(organization_id, new_organization)

Put Organization

Put organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.new_organization import NewOrganization
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    new_organization = audithub_sdk.NewOrganization() # NewOrganization | 

    try:
        # Put Organization
        api_response = await api_instance.put_organization_organizations_organization_id_put(organization_id, new_organization)
        print("The response of OrganizationsApi->put_organization_organizations_organization_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->put_organization_organizations_organization_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **new_organization** | [**NewOrganization**](NewOrganization.md)|  | 

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

# **put_organization_restrictions_organizations_organization_id_restrictions_put**
> SuccessAndMessageResponse put_organization_restrictions_organizations_organization_id_restrictions_put(organization_id, organization_access_restriction)

Put Organization Restrictions

Set the access restrictions for an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_access_restriction import OrganizationAccessRestriction
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    organization_access_restriction = [audithub_sdk.OrganizationAccessRestriction()] # List[OrganizationAccessRestriction] | 

    try:
        # Put Organization Restrictions
        api_response = await api_instance.put_organization_restrictions_organizations_organization_id_restrictions_put(organization_id, organization_access_restriction)
        print("The response of OrganizationsApi->put_organization_restrictions_organizations_organization_id_restrictions_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->put_organization_restrictions_organizations_organization_id_restrictions_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **organization_access_restriction** | [**List[OrganizationAccessRestriction]**](OrganizationAccessRestriction.md)|  | 

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

# **put_user_organization_settings_organizations_organization_id_user_settings_put**
> SuccessAndMessageResponse put_user_organization_settings_organizations_organization_id_user_settings_put(organization_id, user_organization_setting)

Put User Organization Settings

Updates the user's project settings

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.user_organization_setting import UserOrganizationSetting
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_organization_setting = audithub_sdk.UserOrganizationSetting() # UserOrganizationSetting | 

    try:
        # Put User Organization Settings
        api_response = await api_instance.put_user_organization_settings_organizations_organization_id_user_settings_put(organization_id, user_organization_setting)
        print("The response of OrganizationsApi->put_user_organization_settings_organizations_organization_id_user_settings_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->put_user_organization_settings_organizations_organization_id_user_settings_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_organization_setting** | [**UserOrganizationSetting**](UserOrganizationSetting.md)|  | 

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

# **put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put**
> SuccessAndMessageResponse put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put(organization_id, user_id, user_access_restriction)

Put User Restrictions

Set the access restrictions for a user inside an organization

### Example


```python
import audithub_sdk
from audithub_sdk.models.success_and_message_response import SuccessAndMessageResponse
from audithub_sdk.models.user_access_restriction import UserAccessRestriction
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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    user_id = 'user_id_example' # str | 
    user_access_restriction = [audithub_sdk.UserAccessRestriction()] # List[UserAccessRestriction] | 

    try:
        # Put User Restrictions
        api_response = await api_instance.put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put(organization_id, user_id, user_access_restriction)
        print("The response of OrganizationsApi->put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->put_user_restrictions_organizations_organization_id_users_user_id_restrictions_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **user_id** | **str**|  | 
 **user_access_restriction** | [**List[UserAccessRestriction]**](UserAccessRestriction.md)|  | 

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

# **remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete**
> SuccessAndMessageResponse remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete(organization_id, project_id)

Remove Project From Favorites

Remove a project from the user's favorite ones

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
    api_instance = audithub_sdk.OrganizationsApi(api_client)
    organization_id = 56 # int | 
    project_id = 56 # int | 

    try:
        # Remove Project From Favorites
        api_response = await api_instance.remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete(organization_id, project_id)
        print("The response of OrganizationsApi->remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationsApi->remove_project_from_favorites_organizations_organization_id_favorite_projects_project_id_delete: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

