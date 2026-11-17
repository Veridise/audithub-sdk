# audithub_sdk.CreditsApi

All URIs are relative to *https://audithub.dev.veridise.tools/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_credit_summary_organizations_organization_id_credits_summary_get**](CreditsApi.md#get_credit_summary_organizations_organization_id_credits_summary_get) | **GET** /organizations/{organization_id}/credits/summary | Get organization credit summary
[**get_credits_organizations_organization_id_credits_get**](CreditsApi.md#get_credits_organizations_organization_id_credits_get) | **GET** /organizations/{organization_id}/credits | Get organization credit accounting


# **get_credit_summary_organizations_organization_id_credits_summary_get**
> OrganizationCreditSummary get_credit_summary_organizations_organization_id_credits_summary_get(organization_id, current_only=current_only)

Get organization credit summary

Return total, consumed, and available credits across all credit periods by default. Set current_only=true to include only currently active periods. Consumption includes task reservations. Total and available are -1 for organizations with unlimited credits.

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_credit_summary import OrganizationCreditSummary
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
    api_instance = audithub_sdk.CreditsApi(api_client)
    organization_id = 56 # int | 
    current_only = False # bool | Include only currently usable credit periods. (optional) (default to False)

    try:
        # Get organization credit summary
        api_response = await api_instance.get_credit_summary_organizations_organization_id_credits_summary_get(organization_id, current_only=current_only)
        print("The response of CreditsApi->get_credit_summary_organizations_organization_id_credits_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_credit_summary_organizations_organization_id_credits_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 
 **current_only** | **bool**| Include only currently usable credit periods. | [optional] [default to False]

### Return type

[**OrganizationCreditSummary**](OrganizationCreditSummary.md)

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

# **get_credits_organizations_organization_id_credits_get**
> OrganizationCredits get_credits_organizations_organization_id_credits_get(organization_id)

Get organization credit accounting

Return subscriptions, extras, credit periods with task allocations, and the referenced tasks for an organization.

### Example


```python
import audithub_sdk
from audithub_sdk.models.organization_credits import OrganizationCredits
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
    api_instance = audithub_sdk.CreditsApi(api_client)
    organization_id = 56 # int | 

    try:
        # Get organization credit accounting
        api_response = await api_instance.get_credits_organizations_organization_id_credits_get(organization_id)
        print("The response of CreditsApi->get_credits_organizations_organization_id_credits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CreditsApi->get_credits_organizations_organization_id_credits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **int**|  | 

### Return type

[**OrganizationCredits**](OrganizationCredits.md)

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

