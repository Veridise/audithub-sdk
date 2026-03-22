# audithub_sdk.UsersApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_key_users_api_keys_post**](UsersApi.md#create_api_key_users_api_keys_post) | **POST** /users/api-keys | Create Api Key
[**get_api_keys_users_api_keys_get**](UsersApi.md#get_api_keys_users_api_keys_get) | **GET** /users/api-keys | Get Api Keys
[**get_arbitrary_user_info_users_user_id_get**](UsersApi.md#get_arbitrary_user_info_users_user_id_get) | **GET** /users/{user_id} | Get Arbitrary User Info
[**get_organizations_users_myorganizations_get**](UsersApi.md#get_organizations_users_myorganizations_get) | **GET** /users/myorganizations | Get Organizations
[**get_profile_users_myprofile_get**](UsersApi.md#get_profile_users_myprofile_get) | **GET** /users/myprofile | Get Profile
[**onboard_request_users_onboard_request_post**](UsersApi.md#onboard_request_users_onboard_request_post) | **POST** /users/onboard-request | Onboard Request
[**patch_profile_users_myprofile_patch**](UsersApi.md#patch_profile_users_myprofile_patch) | **PATCH** /users/myprofile | Patch Profile
[**put_profile_users_myprofile_put**](UsersApi.md#put_profile_users_myprofile_put) | **PUT** /users/myprofile | Put Profile
[**revoke_api_key_users_api_keys_client_id_delete**](UsersApi.md#revoke_api_key_users_api_keys_client_id_delete) | **DELETE** /users/api-keys/{client_id} | Revoke Api Key
[**self_onboard_users_self_onboard_post**](UsersApi.md#self_onboard_users_self_onboard_post) | **POST** /users/self-onboard | Self Onboard


# **create_api_key_users_api_keys_post**
> ApiKeyWithSecret create_api_key_users_api_keys_post(api_key_base)

Create Api Key

### Example


```python
import audithub_sdk
from audithub_sdk.models.api_key_base import ApiKeyBase
from audithub_sdk.models.api_key_with_secret import ApiKeyWithSecret
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
    api_instance = audithub_sdk.UsersApi(api_client)
    api_key_base = audithub_sdk.ApiKeyBase() # ApiKeyBase | 

    try:
        # Create Api Key
        api_response = await api_instance.create_api_key_users_api_keys_post(api_key_base)
        print("The response of UsersApi->create_api_key_users_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_api_key_users_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_base** | [**ApiKeyBase**](ApiKeyBase.md)|  | 

### Return type

[**ApiKeyWithSecret**](ApiKeyWithSecret.md)

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

# **get_api_keys_users_api_keys_get**
> List[ApiKey] get_api_keys_users_api_keys_get()

Get Api Keys

### Example


```python
import audithub_sdk
from audithub_sdk.models.api_key import ApiKey
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
    api_instance = audithub_sdk.UsersApi(api_client)

    try:
        # Get Api Keys
        api_response = await api_instance.get_api_keys_users_api_keys_get()
        print("The response of UsersApi->get_api_keys_users_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_api_keys_users_api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ApiKey]**](ApiKey.md)

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

# **get_arbitrary_user_info_users_user_id_get**
> UserInformation get_arbitrary_user_info_users_user_id_get(user_id)

Get Arbitrary User Info

Returns information for the user with the specified id

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
    api_instance = audithub_sdk.UsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get Arbitrary User Info
        api_response = await api_instance.get_arbitrary_user_info_users_user_id_get(user_id)
        print("The response of UsersApi->get_arbitrary_user_info_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_arbitrary_user_info_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

[**UserInformation**](UserInformation.md)

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

# **get_organizations_users_myorganizations_get**
> List[Organization] get_organizations_users_myorganizations_get()

Get Organizations

Returns the organizations the currently logged in user has access to

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
    api_instance = audithub_sdk.UsersApi(api_client)

    try:
        # Get Organizations
        api_response = await api_instance.get_organizations_users_myorganizations_get()
        print("The response of UsersApi->get_organizations_users_myorganizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_organizations_users_myorganizations_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Organization]**](Organization.md)

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

# **get_profile_users_myprofile_get**
> User get_profile_users_myprofile_get()

Get Profile

Returns the user's profile data

### Example


```python
import audithub_sdk
from audithub_sdk.models.user import User
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
    api_instance = audithub_sdk.UsersApi(api_client)

    try:
        # Get Profile
        api_response = await api_instance.get_profile_users_myprofile_get()
        print("The response of UsersApi->get_profile_users_myprofile_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_profile_users_myprofile_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**User**](User.md)

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

# **onboard_request_users_onboard_request_post**
> SuccessAndMessageResponse onboard_request_users_onboard_request_post()

Onboard Request

Returns access to the AuditHub platform for the currently logged-in user

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
    api_instance = audithub_sdk.UsersApi(api_client)

    try:
        # Onboard Request
        api_response = await api_instance.onboard_request_users_onboard_request_post()
        print("The response of UsersApi->onboard_request_users_onboard_request_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->onboard_request_users_onboard_request_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_profile_users_myprofile_patch**
> SuccessAndMessageResponse patch_profile_users_myprofile_patch(patch_user)

Patch Profile

Patches the adjustable parts of the user's profile

### Example


```python
import audithub_sdk
from audithub_sdk.models.patch_user import PatchUser
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
    api_instance = audithub_sdk.UsersApi(api_client)
    patch_user = audithub_sdk.PatchUser() # PatchUser | 

    try:
        # Patch Profile
        api_response = await api_instance.patch_profile_users_myprofile_patch(patch_user)
        print("The response of UsersApi->patch_profile_users_myprofile_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->patch_profile_users_myprofile_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **patch_user** | [**PatchUser**](PatchUser.md)|  | 

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

# **put_profile_users_myprofile_put**
> SuccessAndMessageResponse put_profile_users_myprofile_put(put_user)

Put Profile

Updates the adjustable parts of the user's profile

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
    api_instance = audithub_sdk.UsersApi(api_client)
    put_user = audithub_sdk.PutUser() # PutUser | 

    try:
        # Put Profile
        api_response = await api_instance.put_profile_users_myprofile_put(put_user)
        print("The response of UsersApi->put_profile_users_myprofile_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->put_profile_users_myprofile_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_user** | [**PutUser**](PutUser.md)|  | 

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

# **revoke_api_key_users_api_keys_client_id_delete**
> SuccessAndMessageResponse revoke_api_key_users_api_keys_client_id_delete(client_id)

Revoke Api Key

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
    api_instance = audithub_sdk.UsersApi(api_client)
    client_id = 'client_id_example' # str | 

    try:
        # Revoke Api Key
        api_response = await api_instance.revoke_api_key_users_api_keys_client_id_delete(client_id)
        print("The response of UsersApi->revoke_api_key_users_api_keys_client_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->revoke_api_key_users_api_keys_client_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | 

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

# **self_onboard_users_self_onboard_post**
> SuccessAndMessageResponse self_onboard_users_self_onboard_post(self_onboard_request)

Self Onboard

Executed automated onboarding

### Example


```python
import audithub_sdk
from audithub_sdk.models.self_onboard_request import SelfOnboardRequest
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
    api_instance = audithub_sdk.UsersApi(api_client)
    self_onboard_request = audithub_sdk.SelfOnboardRequest() # SelfOnboardRequest | 

    try:
        # Self Onboard
        api_response = await api_instance.self_onboard_users_self_onboard_post(self_onboard_request)
        print("The response of UsersApi->self_onboard_users_self_onboard_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->self_onboard_users_self_onboard_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_onboard_request** | [**SelfOnboardRequest**](SelfOnboardRequest.md)|  | 

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

