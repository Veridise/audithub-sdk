# audithub_sdk.EditorLanguagesApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_language_editor_languages_language_id_delete**](EditorLanguagesApi.md#delete_language_editor_languages_language_id_delete) | **DELETE** /editor-languages/{language_id} | Delete Language
[**get_language_editor_languages_language_id_get**](EditorLanguagesApi.md#get_language_editor_languages_language_id_get) | **GET** /editor-languages/{language_id} | Get Language
[**get_languages_editor_languages_get**](EditorLanguagesApi.md#get_languages_editor_languages_get) | **GET** /editor-languages | Get Languages
[**post_language_editor_languages_post**](EditorLanguagesApi.md#post_language_editor_languages_post) | **POST** /editor-languages | Post Language
[**put_language_editor_languages_language_id_put**](EditorLanguagesApi.md#put_language_editor_languages_language_id_put) | **PUT** /editor-languages/{language_id} | Put Language


# **delete_language_editor_languages_language_id_delete**
> SuccessAndMessageResponse delete_language_editor_languages_language_id_delete(language_id)

Delete Language

Permanently delete a language

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
    api_instance = audithub_sdk.EditorLanguagesApi(api_client)
    language_id = 56 # int | 

    try:
        # Delete Language
        api_response = await api_instance.delete_language_editor_languages_language_id_delete(language_id)
        print("The response of EditorLanguagesApi->delete_language_editor_languages_language_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditorLanguagesApi->delete_language_editor_languages_language_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **int**|  | 

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

# **get_language_editor_languages_language_id_get**
> EditorLanguageWithId get_language_editor_languages_language_id_get(language_id)

Get Language

Returns language by id

### Example


```python
import audithub_sdk
from audithub_sdk.models.editor_language_with_id import EditorLanguageWithId
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
    api_instance = audithub_sdk.EditorLanguagesApi(api_client)
    language_id = 56 # int | 

    try:
        # Get Language
        api_response = await api_instance.get_language_editor_languages_language_id_get(language_id)
        print("The response of EditorLanguagesApi->get_language_editor_languages_language_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditorLanguagesApi->get_language_editor_languages_language_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **int**|  | 

### Return type

[**EditorLanguageWithId**](EditorLanguageWithId.md)

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

# **get_languages_editor_languages_get**
> List[EditorLanguageWithId] get_languages_editor_languages_get()

Get Languages

Returns all languages

### Example


```python
import audithub_sdk
from audithub_sdk.models.editor_language_with_id import EditorLanguageWithId
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
    api_instance = audithub_sdk.EditorLanguagesApi(api_client)

    try:
        # Get Languages
        api_response = await api_instance.get_languages_editor_languages_get()
        print("The response of EditorLanguagesApi->get_languages_editor_languages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditorLanguagesApi->get_languages_editor_languages_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EditorLanguageWithId]**](EditorLanguageWithId.md)

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

# **post_language_editor_languages_post**
> IdAndMessageResponse post_language_editor_languages_post(editor_language)

Post Language

Post language

### Example


```python
import audithub_sdk
from audithub_sdk.models.editor_language import EditorLanguage
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
    api_instance = audithub_sdk.EditorLanguagesApi(api_client)
    editor_language = audithub_sdk.EditorLanguage() # EditorLanguage | 

    try:
        # Post Language
        api_response = await api_instance.post_language_editor_languages_post(editor_language)
        print("The response of EditorLanguagesApi->post_language_editor_languages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditorLanguagesApi->post_language_editor_languages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **editor_language** | [**EditorLanguage**](EditorLanguage.md)|  | 

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

# **put_language_editor_languages_language_id_put**
> SuccessAndMessageResponse put_language_editor_languages_language_id_put(language_id, editor_language)

Put Language

Update language attributes

### Example


```python
import audithub_sdk
from audithub_sdk.models.editor_language import EditorLanguage
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
    api_instance = audithub_sdk.EditorLanguagesApi(api_client)
    language_id = 56 # int | 
    editor_language = audithub_sdk.EditorLanguage() # EditorLanguage | 

    try:
        # Put Language
        api_response = await api_instance.put_language_editor_languages_language_id_put(language_id, editor_language)
        print("The response of EditorLanguagesApi->put_language_editor_languages_language_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EditorLanguagesApi->put_language_editor_languages_language_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language_id** | **int**|  | 
 **editor_language** | [**EditorLanguage**](EditorLanguage.md)|  | 

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

