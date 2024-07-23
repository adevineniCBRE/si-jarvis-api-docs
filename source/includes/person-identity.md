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

<h1 id="openapi-definition-identity-controller">Identity</h1>

## Get Identity by id

<a id="opIdfindByIdentityId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/identity/{identityId} \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identity/{identityId}");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/identity/{identityId}', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/identity/{identityId}`

<h3 id="get-identity-by-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|identityId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="get-identity-by-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identity|[IdentityDTO](#schemaidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Update Identity

<a id="opIdupdateIdentity"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8090/person-identity/api/v1/identity/{identityId} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identity/{identityId}");
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
  'Accept': 'application/json'
}

r = requests.put('http://localhost:8090/person-identity/api/v1/identity/{identityId}', headers = headers)

print(r.json())

```

`PUT /person-identity/api/v1/identity/{identityId}`

> Body parameter

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="update-identity-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|identityId|path|string|true|none|
|body|body|[IdentityDTO](#schemaidentitydto)|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="update-identity-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identity Created|[IdentityDTO](#schemaidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid id supplied|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Foo not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create Identity

<a id="opIdcreateIdentity"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8090/person-identity/api/v1/identity \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identity");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
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
  'Accept': 'application/json'
}

r = requests.post('http://localhost:8090/person-identity/api/v1/identity', headers = headers)

print(r.json())

```

`POST /person-identity/api/v1/identity`

> Body parameter

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="create-identity-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[IdentityDTO](#schemaidentitydto)|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="create-identity-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Identity Created|[IdentityDTO](#schemaidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Invalid id supplied|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Foo not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Search Person-Identity by First-Name, Last-Name, Full-Name or Email

<a id="opIdgetUsersByNameOrEmailAndRolePermissions"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8090/person-identity/api/v1/identity-role-search \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identity-role-search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
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
  'Accept': 'application/json'
}

r = requests.post('http://localhost:8090/person-identity/api/v1/identity-role-search', headers = headers)

print(r.json())

```

`POST /person-identity/api/v1/identity-role-search`

> Body parameter

```json
{
  "searchStr": "string",
  "searchableOrgs": [
    "string"
  ],
  "appSynonym": "string",
  "rolePermissions": [
    "string"
  ],
  "page": 0,
  "size": 0,
  "sort": "string",
  "sortOrder": "string"
}
```

<h3 id="search-person-identity-by-first-name,-last-name,-full-name-or-email-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[SearchPersonIdentityRequestDTO](#schemasearchpersonidentityrequestdto)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "registeredOrgs": [
      "string"
    ],
    "searchableOrgs": [
      "string"
    ],
    "rolePermissionEnabled": true,
    "dataAccessEnabled": true
  }
]
```

<h3 id="search-person-identity-by-first-name,-last-name,-full-name-or-email-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Person-Identity satisfying the criteria|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|No records found for the input search-criteria|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="search-person-identity-by-first-name,-last-name,-full-name-or-email-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[SearchPersonIdentityResponseDTO](#schemasearchpersonidentityresponsedto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|
|» searchableOrgs|[string]|false|none|none|
|» rolePermissionEnabled|boolean|false|none|none|
|» dataAccessEnabled|boolean|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identities by PersonIds

<a id="opIdfindByPersonIds_1"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8090/person-identity/api/v1/identities/search \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identities/search");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
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
  'Accept': 'application/json'
}

r = requests.post('http://localhost:8090/person-identity/api/v1/identities/search', headers = headers)

print(r.json())

```

`POST /person-identity/api/v1/identities/search`

> Body parameter

```json
{
  "personIds": [
    "string"
  ],
  "query": "string",
  "page": 0,
  "size": 0,
  "sort": "string",
  "sortOrder": "string"
}
```

<h3 id="get-identities-by-personids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[IdentitiesSearchRequestDTO](#schemaidentitiessearchrequestdto)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identities-by-personids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identities-by-personids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identity by PersonId

<a id="opIdfindByPersonId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/personId/{personId} \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/personId/{personId}");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/personId/{personId}', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/personId/{personId}`

<h3 id="get-identity-by-personid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identity-by-personid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identity-by-personid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Default Identity by PersonId

<a id="opIdgetDefaultIdentityByPersonId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/personId/{personId}/default \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/personId/{personId}/default");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/personId/{personId}/default', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/personId/{personId}/default`

<h3 id="get-default-identity-by-personid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="get-default-identity-by-personid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Returns Default-Identity|[IdentityDTO](#schemaidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get JWT Identity by Email and Tenant

<a id="opIdgetJWTIdentityByEmailAndTenant"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/jwtidentity?email=string&tenantId=string \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/jwtidentity?email=string&tenantId=string");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/jwtidentity', params={
  'email': 'string',  'tenantId': 'string'
}, headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/jwtidentity`

<h3 id="get-jwt-identity-by-email-and-tenant-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|email|query|string|true|none|
|tenantId|query|string|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "tenantId": "string",
  "synonymRolePermissions": [
    {
      "appSynonym": "string",
      "applicationName": "string",
      "permissions": [
        "string"
      ]
    }
  ]
}
```

<h3 id="get-jwt-identity-by-email-and-tenant-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identity|[JWTIdentityDTO](#schemajwtidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identity by mail

<a id="opIdfindByEmail"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/identity/email/{email} \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identity/email/{email}");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/identity/email/{email}', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/identity/email/{email}`

<h3 id="get-identity-by-mail-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|email|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}
```

<h3 id="get-identity-by-mail-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identity|[IdentityDTO](#schemaidentitydto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identity by First Name and Last Name

<a id="opIdfindIdentitiesByNames"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/identities \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/identities");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/identities', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/identities`

<h3 id="get-identity-by-first-name-and-last-name-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|firstName|query|string|false|none|
|lastName|query|string|false|none|
|fullName|query|string|false|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identity-by-first-name-and-last-name-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identity-by-first-name-and-last-name-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Search Consolidated Person Identity by Person Id

<a id="opIdfindConsolidatedPersonIdentityByPersonId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v1/consolidated-person/{personId} \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v1/consolidated-person/{personId}");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v1/consolidated-person/{personId}', headers = headers)

print(r.json())

```

`GET /person-identity/api/v1/consolidated-person/{personId}`

<h3 id="search-consolidated-person-identity-by-person-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "registeredOrgs": [
    "string"
  ],
  "searchableOrgs": [
    "string"
  ],
  "rolePermissionEnabled": true,
  "dataAccessEnabled": true
}
```

<h3 id="search-consolidated-person-identity-by-person-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Consolidated Person Identity by Person Id|[SearchPersonIdentityResponseDTO](#schemasearchpersonidentityresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-identity-controller-v-2">Identity (V2)</h1>

## Get Identity by personIds

<a id="opIdfindByPersonIds"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8090/person-identity/api/v2/identities/all-person/{tenantId} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v2/identities/all-person/{tenantId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("POST");
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
  'Accept': 'application/json'
}

r = requests.post('http://localhost:8090/person-identity/api/v2/identities/all-person/{tenantId}', headers = headers)

print(r.json())

```

`POST /person-identity/api/v2/identities/all-person/{tenantId}`

> Body parameter

```json
{
  "personIds": [
    "string"
  ]
}
```

<h3 id="get-identity-by-personids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tenantId|path|string|true|none|
|body|body|[PersonIdRequest](#schemapersonidrequest)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identity-by-personids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identity-by-personids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identity by First Name and Last Name

<a id="opIdfindByAll"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v2/identities?tenantId=string&page=page,0,size,1,sort,string \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v2/identities?tenantId=string&page=page,0,size,1,sort,string");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v2/identities', params={
  'tenantId': 'string',  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /person-identity/api/v2/identities`

<h3 id="get-identity-by-first-name-and-last-name-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|filter|query|string|false|none|
|tenantId|query|string|true|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identity-by-first-name-and-last-name-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identity-by-first-name-and-last-name-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identities by Rolegroup

<a id="opIdfindByAll_1"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v2/identities/roleGroup?tenantId=string&workspaceId=string&roleGroupId=string&page=page,0,size,1,sort,string \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v2/identities/roleGroup?tenantId=string&workspaceId=string&roleGroupId=string&page=page,0,size,1,sort,string");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v2/identities/roleGroup', params={
  'tenantId': 'string',  'workspaceId': 'string',  'roleGroupId': 'string',  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /person-identity/api/v2/identities/roleGroup`

<h3 id="get-identities-by-rolegroup-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tenantId|query|string|true|none|
|workspaceId|query|string|true|none|
|roleGroupId|query|string|true|none|
|filter|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identities-by-rolegroup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities by Rolegroup|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identities-by-rolegroup-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Get Identities by DataGroup

<a id="opIdfindByAllDataGroup"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/person-identity/api/v2/identities/dataGroup?tenantId=string&workspaceId=string&dataGroupId=string&page=page,0,size,1,sort,string \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/person-identity/api/v2/identities/dataGroup?tenantId=string&workspaceId=string&dataGroupId=string&page=page,0,size,1,sort,string");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/person-identity/api/v2/identities/dataGroup', params={
  'tenantId': 'string',  'workspaceId': 'string',  'dataGroupId': 'string',  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /person-identity/api/v2/identities/dataGroup`

<h3 id="get-identities-by-datagroup-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|tenantId|query|string|true|none|
|workspaceId|query|string|true|none|
|dataGroupId|query|string|true|none|
|filter|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-identities-by-datagroup-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities by Rolegroup|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-identities-by-datagroup-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-identity-internal-controller">Identity Internal</h1>

## Get Internal Identity by PersonId

<a id="opIdfindByPersonIdWithPhoneNumber"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8090/internal/person-identity/api/v1/personId/{personId} \
  -H 'Accept: application/json'

```

```java
URL obj = new URL("http://localhost:8090/internal/person-identity/api/v1/personId/{personId}");
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
  'Accept': 'application/json'
}

r = requests.get('http://localhost:8090/internal/person-identity/api/v1/personId/{personId}', headers = headers)

print(r.json())

```

`GET /internal/person-identity/api/v1/personId/{personId}`

<h3 id="get-internal-identity-by-personid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|

> Example responses

> 200 Response

```json
[
  {
    "identityId": "string",
    "personId": "string",
    "email": "string",
    "sourceIdentifier": "string",
    "type": "string",
    "regionId": "string",
    "defaultIdent": true,
    "firstName": "string",
    "lastName": "string",
    "init": "string",
    "fullName": "string",
    "phoneNumbers": [
      {
        "number": "string",
        "type": "string"
      }
    ],
    "createdDate": "2019-08-24T14:15:22Z",
    "lastModifiedBy": "string",
    "lastModifiedDate": "2019-08-24T14:15:22Z",
    "tenantId": "string",
    "registeredOrgs": [
      "string"
    ]
  }
]
```

<h3 id="get-internal-identity-by-personid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Identities|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Identity not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<h3 id="get-internal-identity-by-personid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[IdentityDTO](#schemaidentitydto)]|false|none|none|
|» identityId|string|false|none|none|
|» personId|string|false|none|none|
|» email|string|false|none|none|
|» sourceIdentifier|string|false|none|none|
|» type|string|false|none|none|
|» regionId|string|false|none|none|
|» defaultIdent|boolean|false|none|none|
|» firstName|string|false|none|none|
|» lastName|string|false|none|none|
|» init|string|false|none|none|
|» fullName|string|false|none|none|
|» phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|»» number|string|false|none|none|
|»» type|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» lastModifiedBy|string|false|none|none|
|» lastModifiedDate|string(date-time)|false|none|none|
|» tenantId|string|false|none|none|
|» registeredOrgs|[string]|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

# Person Identity Schemas

<h2 id="tocS_IdentityDTO">IdentityDTO</h2>
<!-- backwards compatibility -->
<a id="schemaidentitydto"></a>
<a id="schema_IdentityDTO"></a>
<a id="tocSidentitydto"></a>
<a id="tocsidentitydto"></a>

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "sourceIdentifier": "string",
  "type": "string",
  "regionId": "string",
  "defaultIdent": true,
  "firstName": "string",
  "lastName": "string",
  "init": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "createdDate": "2019-08-24T14:15:22Z",
  "lastModifiedBy": "string",
  "lastModifiedDate": "2019-08-24T14:15:22Z",
  "tenantId": "string",
  "registeredOrgs": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identityId|string|false|none|none|
|personId|string|false|none|none|
|email|string|false|none|none|
|sourceIdentifier|string|false|none|none|
|type|string|false|none|none|
|regionId|string|false|none|none|
|defaultIdent|boolean|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|init|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|createdDate|string(date-time)|false|none|none|
|lastModifiedBy|string|false|none|none|
|lastModifiedDate|string(date-time)|false|none|none|
|tenantId|string|false|none|none|
|registeredOrgs|[string]|false|none|none|

<h2 id="tocS_PhoneNumberDTO">PhoneNumberDTO</h2>
<!-- backwards compatibility -->
<a id="schemaphonenumberdto"></a>
<a id="schema_PhoneNumberDTO"></a>
<a id="tocSphonenumberdto"></a>
<a id="tocsphonenumberdto"></a>

```json
{
  "number": "string",
  "type": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|number|string|false|none|none|
|type|string|false|none|none|

<h2 id="tocS_PersonIdRequest">PersonIdRequest</h2>
<!-- backwards compatibility -->
<a id="schemapersonidrequest"></a>
<a id="schema_PersonIdRequest"></a>
<a id="tocSpersonidrequest"></a>
<a id="tocspersonidrequest"></a>

```json
{
  "personIds": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personIds|[string]|false|none|none|

<h2 id="tocS_SearchPersonIdentityRequestDTO">SearchPersonIdentityRequestDTO</h2>
<!-- backwards compatibility -->
<a id="schemasearchpersonidentityrequestdto"></a>
<a id="schema_SearchPersonIdentityRequestDTO"></a>
<a id="tocSsearchpersonidentityrequestdto"></a>
<a id="tocssearchpersonidentityrequestdto"></a>

```json
{
  "searchStr": "string",
  "searchableOrgs": [
    "string"
  ],
  "appSynonym": "string",
  "rolePermissions": [
    "string"
  ],
  "page": 0,
  "size": 0,
  "sort": "string",
  "sortOrder": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|searchStr|string|false|none|none|
|searchableOrgs|[string]|false|none|none|
|appSynonym|string|false|none|none|
|rolePermissions|[string]|false|none|none|
|page|integer(int32)|false|none|none|
|size|integer(int32)|false|none|none|
|sort|string|false|none|none|
|sortOrder|string|false|none|none|

<h2 id="tocS_SearchPersonIdentityResponseDTO">SearchPersonIdentityResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemasearchpersonidentityresponsedto"></a>
<a id="schema_SearchPersonIdentityResponseDTO"></a>
<a id="tocSsearchpersonidentityresponsedto"></a>
<a id="tocssearchpersonidentityresponsedto"></a>

```json
{
  "identityId": "string",
  "personId": "string",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumbers": [
    {
      "number": "string",
      "type": "string"
    }
  ],
  "registeredOrgs": [
    "string"
  ],
  "searchableOrgs": [
    "string"
  ],
  "rolePermissionEnabled": true,
  "dataAccessEnabled": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identityId|string|false|none|none|
|personId|string|false|none|none|
|email|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumbers|[[PhoneNumberDTO](#schemaphonenumberdto)]|false|none|none|
|registeredOrgs|[string]|false|none|none|
|searchableOrgs|[string]|false|none|none|
|rolePermissionEnabled|boolean|false|none|none|
|dataAccessEnabled|boolean|false|none|none|

<h2 id="tocS_IdentitiesSearchRequestDTO">IdentitiesSearchRequestDTO</h2>
<!-- backwards compatibility -->
<a id="schemaidentitiessearchrequestdto"></a>
<a id="schema_IdentitiesSearchRequestDTO"></a>
<a id="tocSidentitiessearchrequestdto"></a>
<a id="tocsidentitiessearchrequestdto"></a>

```json
{
  "personIds": [
    "string"
  ],
  "query": "string",
  "page": 0,
  "size": 0,
  "sort": "string",
  "sortOrder": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personIds|[string]|false|none|none|
|query|string|false|none|none|
|page|integer(int32)|false|none|none|
|size|integer(int32)|false|none|none|
|sort|string|false|none|none|
|sortOrder|string|false|none|none|

<h2 id="tocS_Pageable">Pageable</h2>
<!-- backwards compatibility -->
<a id="schemapageable"></a>
<a id="schema_Pageable"></a>
<a id="tocSpageable"></a>
<a id="tocspageable"></a>

```json
{
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|page|integer(int32)|false|none|none|
|size|integer(int32)|false|none|none|
|sort|[string]|false|none|none|

<h2 id="tocS_JWTIdentityDTO">JWTIdentityDTO</h2>
<!-- backwards compatibility -->
<a id="schemajwtidentitydto"></a>
<a id="schema_JWTIdentityDTO"></a>
<a id="tocSjwtidentitydto"></a>
<a id="tocsjwtidentitydto"></a>

```json
{
  "identityId": "string",
  "personId": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "tenantId": "string",
  "synonymRolePermissions": [
    {
      "appSynonym": "string",
      "applicationName": "string",
      "permissions": [
        "string"
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|identityId|string|false|none|none|
|personId|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|email|string|false|none|none|
|tenantId|string|false|none|none|
|synonymRolePermissions|[[SynonymRolePermissionsDTO](#schemasynonymrolepermissionsdto)]|false|none|none|

<h2 id="tocS_SynonymRolePermissionsDTO">SynonymRolePermissionsDTO</h2>
<!-- backwards compatibility -->
<a id="schemasynonymrolepermissionsdto"></a>
<a id="schema_SynonymRolePermissionsDTO"></a>
<a id="tocSsynonymrolepermissionsdto"></a>
<a id="tocssynonymrolepermissionsdto"></a>

```json
{
  "appSynonym": "string",
  "applicationName": "string",
  "permissions": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|appSynonym|string|false|none|none|
|applicationName|string|false|none|none|
|permissions|[string]|false|none|none|

