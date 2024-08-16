---
title: OpenAPI definition v0
language_tabs:
  - shell: Shell
  - java: Java
  - python: Python
language_clients:
  - shell: ""
  - java: ""
  - python: ""
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

<h1 id="openapi-definition-notification-controller">Notification</h1>

## Update Notification as Read

<a id="opIdupdateNotifications"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8085/notification/api/v1/user-notifications/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8085/notification/api/v1/user-notifications/{id}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PUT");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8085/notification/api/v1/user-notifications/{id}', headers = headers)

print(r.json())

```

`PUT /notification/api/v1/user-notifications/{id}`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "status": "READ",
  "message": "string",
  "url": "string",
  "createdDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="update-notification-as-read-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[UINotificationDTO](#schemauinotificationdto)|true|none|

> Example responses

> 200 Response

> 201 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "status": "READ",
    "message": "string",
    "url": "string",
    "createdDate": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="update-notification-as-read-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[UINotificationDTO](#schemauinotificationdto)|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Notification updated|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Notification not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="update-notification-as-read-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[UINotificationDTO](#schemauinotificationdto)]|false|none|none|
|» id|string(uuid)|true|none|none|
|» status|string|true|none|none|
|» message|string|true|none|none|
|» url|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|READ|
|status|UNREAD|
|status|DELETE|

<aside class="success">
This operation does not require authentication
</aside>

## Get Notifications

<a id="opIdgetOfflineNotifications"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8085/notification/api/v1/user-notifications/user/{userId} \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8085/notification/api/v1/user-notifications/user/{userId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("GET");
int responseCode = con.getResponseCode();
BufferedReader in = new BufferedReader(
    new InputStreamReader(con.getInputStream()));
String inputLine;
StringBuffer response = new StringBuffer();
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
in.close();
System.out.println(response.toString());

```

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8085/notification/api/v1/user-notifications/user/{userId}', headers = headers)

print(r.json())

```

`GET /notification/api/v1/user-notifications/user/{userId}`

<h3 id="get-notifications-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|userId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "status": "READ",
    "message": "string",
    "url": "string",
    "createdDate": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="get-notifications-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Notifications|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Notifications not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-notifications-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[UINotificationDTO](#schemauinotificationdto)]|false|none|none|
|» id|string(uuid)|true|none|none|
|» status|string|true|none|none|
|» message|string|true|none|none|
|» url|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|READ|
|status|UNREAD|
|status|DELETE|

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_UINotificationDTO">UINotificationDTO</h2>
<!-- backwards compatibility -->
<a id="schemauinotificationdto"></a>
<a id="schema_UINotificationDTO"></a>
<a id="tocSuinotificationdto"></a>
<a id="tocsuinotificationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "status": "READ",
  "message": "string",
  "url": "string",
  "createdDate": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|true|none|none|
|status|string|true|none|none|
|message|string|true|none|none|
|url|string|false|none|none|
|createdDate|string(date-time)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|READ|
|status|UNREAD|
|status|DELETE|

