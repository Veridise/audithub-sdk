# audithub_sdk.InvitationsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_invitation_organizations_organization_id_invitations_invitation_id_delete**](InvitationsApi.md#delete_invitation_organizations_organization_id_invitations_invitation_id_delete) | **DELETE** /organizations/{organization_id}/invitations/{invitation_id} | Delete Invitation
[**get_invitation_organizations_organization_id_invitations_invitation_id_get**](InvitationsApi.md#get_invitation_organizations_organization_id_invitations_invitation_id_get) | **GET** /organizations/{organization_id}/invitations/{invitation_id} | Get Invitation
[**patch_invitation_organizations_organization_id_invitations_invitation_id_patch**](InvitationsApi.md#patch_invitation_organizations_organization_id_invitations_invitation_id_patch) | **PATCH** /organizations/{organization_id}/invitations/{invitation_id} | Patch Invitation
[**post_invitation_organizations_organization_id_invitations_post**](InvitationsApi.md#post_invitation_organizations_organization_id_invitations_post) | **POST** /organizations/{organization_id}/invitations | Post Invitation


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
    api_instance = audithub_sdk.InvitationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 

    try:
        # Delete Invitation
        api_response = await api_instance.delete_invitation_organizations_organization_id_invitations_invitation_id_delete(organization_id, invitation_id)
        print("The response of InvitationsApi->delete_invitation_organizations_organization_id_invitations_invitation_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->delete_invitation_organizations_organization_id_invitations_invitation_id_delete: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

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
    api_instance = audithub_sdk.InvitationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 

    try:
        # Get Invitation
        api_response = await api_instance.get_invitation_organizations_organization_id_invitations_invitation_id_get(organization_id, invitation_id)
        print("The response of InvitationsApi->get_invitation_organizations_organization_id_invitations_invitation_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->get_invitation_organizations_organization_id_invitations_invitation_id_get: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

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
    api_instance = audithub_sdk.InvitationsApi(api_client)
    organization_id = 56 # int | 
    invitation_id = 56 # int | 
    invitation_patch = audithub_sdk.InvitationPatch() # InvitationPatch | 

    try:
        # Patch Invitation
        api_response = await api_instance.patch_invitation_organizations_organization_id_invitations_invitation_id_patch(organization_id, invitation_id, invitation_patch)
        print("The response of InvitationsApi->patch_invitation_organizations_organization_id_invitations_invitation_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->patch_invitation_organizations_organization_id_invitations_invitation_id_patch: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

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
    api_instance = audithub_sdk.InvitationsApi(api_client)
    organization_id = 56 # int | 
    new_invitation = audithub_sdk.NewInvitation() # NewInvitation | 

    try:
        # Post Invitation
        api_response = await api_instance.post_invitation_organizations_organization_id_invitations_post(organization_id, new_invitation)
        print("The response of InvitationsApi->post_invitation_organizations_organization_id_invitations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvitationsApi->post_invitation_organizations_organization_id_invitations_post: %s\n" % e)
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
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**4XX** | Client Error |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

