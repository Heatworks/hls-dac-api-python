# swagger_client.DefaultApi

All URIs are relative to *https://gtxrcsoql2.execute-api.us-east-1.amazonaws.com/pre_alpha*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_get**](DefaultApi.md#data_get) | **GET** /Data | 
[**data_put**](DefaultApi.md#data_put) | **PUT** /Data | 
[**device_delete**](DefaultApi.md#device_delete) | **DELETE** /Device | 
[**device_get**](DefaultApi.md#device_get) | **GET** /Device | 
[**device_post**](DefaultApi.md#device_post) | **POST** /Device | 
[**device_put**](DefaultApi.md#device_put) | **PUT** /Device | 
[**devices_get**](DefaultApi.md#devices_get) | **GET** /Devices | 


# **data_get**
> Data data_get(channel=channel, end_time=end_time, start_time=start_time)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
channel = 'channel_example' # str |  (optional)
end_time = 'end_time_example' # str |  (optional)
start_time = 'start_time_example' # str |  (optional)

try: 
    api_response = api_instance.data_get(channel=channel, end_time=end_time, start_time=start_time)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->data_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel** | **str**|  | [optional] 
 **end_time** | **str**|  | [optional] 
 **start_time** | **str**|  | [optional] 

### Return type

[**Data**](Data.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_put**
> Empty data_put(empty, content_type=content_type, organization_id=organization_id, file=file)



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
empty = swagger_client.Empty() # Empty | 
content_type = 'content_type_example' # str |  (optional)
organization_id = 'organization_id_example' # str |  (optional)
file = 'file_example' # str |  (optional)

try: 
    api_response = api_instance.data_put(empty, content_type=content_type, organization_id=organization_id, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->data_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **empty** | [**Empty**](Empty.md)|  | 
 **content_type** | **str**|  | [optional] 
 **organization_id** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: text/csv
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_delete**
> Empty device_delete()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.device_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_get**
> Empty device_get()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.device_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_post**
> Empty device_post()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.device_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_put**
> Empty device_put()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.device_put()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->device_put: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **devices_get**
> Empty devices_get()



### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: oAuth_2_0
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try: 
    api_response = api_instance.devices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->devices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Empty**](Empty.md)

### Authorization

[oAuth_2_0](../README.md#oAuth_2_0)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

