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


<h1 id="openapi-definition-request-controller">Request (RM)</h1>

## Edit Request

<a id="opIdupdateRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/requests/request \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/request");
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
  'Accept': 'application/json',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/requests/request', headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/requests/request`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "description": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "createdDate": "2019-08-24T14:15:22Z",
  "createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "modifiedBy": "07ff0787-1af5-4fc4-9832-7aaeaa962a5e",
  "source": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "personAssignedTo": "string",
  "reasonCode": "string",
  "location": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "alternateId": "string",
    "serviceAddress": "string",
    "path": "string",
    "timeZone": "string"
  },
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "positionTypePath": "string",
    "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
    "assetName": "string"
  },
  "serviceClassification": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "description": "string",
    "aliasId": "string",
    "aliasDescription": "string"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "watcher": [
    {
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "fullName": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string"
    }
  ],
  "slaDate": [
    {
      "slaName": "string",
      "slaDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistory": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "extendedProperties": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "value": [
        "string"
      ],
      "translatedValue": [
        "string"
      ]
    }
  ],
  "workOrders": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "completionDescription": "string",
      "statusDescription": "string",
      "nte": 0,
      "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
      "assigneeName": "string",
      "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
      "dispatchSiteName": "string",
      "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
      "targetCompletionDate": "string",
      "targetResponseDate": "string",
      "targetAttendDate": "string",
      "targetDispatchDate": "string",
      "completionDescriptionDate": "2019-08-24T14:15:22Z"
    }
  ],
  "comments": [
    {
      "comment": "string",
      "type": "string",
      "addedDate": "string",
      "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
      "addedByName": "string",
      "source": "string"
    }
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}
```

<h3 id="edit-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[RequestDetailsDto](#schemarequestdetailsdto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "description": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "createdDate": "2019-08-24T14:15:22Z",
  "createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "modifiedBy": "07ff0787-1af5-4fc4-9832-7aaeaa962a5e",
  "source": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "personAssignedTo": "string",
  "reasonCode": "string",
  "location": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "alternateId": "string",
    "serviceAddress": "string",
    "path": "string",
    "timeZone": "string"
  },
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "positionTypePath": "string",
    "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
    "assetName": "string"
  },
  "serviceClassification": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "description": "string",
    "aliasId": "string",
    "aliasDescription": "string"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "watcher": [
    {
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "fullName": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string"
    }
  ],
  "slaDate": [
    {
      "slaName": "string",
      "slaDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistory": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "extendedProperties": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "value": [
        "string"
      ],
      "translatedValue": [
        "string"
      ]
    }
  ],
  "workOrders": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "completionDescription": "string",
      "statusDescription": "string",
      "nte": 0,
      "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
      "assigneeName": "string",
      "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
      "dispatchSiteName": "string",
      "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
      "targetCompletionDate": "string",
      "targetResponseDate": "string",
      "targetAttendDate": "string",
      "targetDispatchDate": "string",
      "completionDescriptionDate": "2019-08-24T14:15:22Z"
    }
  ],
  "comments": [
    {
      "comment": "string",
      "type": "string",
      "addedDate": "string",
      "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
      "addedByName": "string",
      "source": "string"
    }
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}
```

<h3 id="edit-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request updated successfully|[RequestDetailsDto](#schemarequestdetailsdto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create Request

<a id="opIdcreateRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/request \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/request");
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
  'Accept': 'application/json',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/request', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/request`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "description": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "createdDate": "2019-08-24T14:15:22Z",
  "createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "modifiedBy": "07ff0787-1af5-4fc4-9832-7aaeaa962a5e",
  "source": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "personAssignedTo": "string",
  "reasonCode": "string",
  "location": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "alternateId": "string",
    "serviceAddress": "string",
    "path": "string",
    "timeZone": "string"
  },
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "positionTypePath": "string",
    "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
    "assetName": "string"
  },
  "serviceClassification": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "description": "string",
    "aliasId": "string",
    "aliasDescription": "string"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "watcher": [
    {
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "fullName": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string"
    }
  ],
  "slaDate": [
    {
      "slaName": "string",
      "slaDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistory": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "extendedProperties": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "value": [
        "string"
      ],
      "translatedValue": [
        "string"
      ]
    }
  ],
  "workOrders": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "completionDescription": "string",
      "statusDescription": "string",
      "nte": 0,
      "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
      "assigneeName": "string",
      "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
      "dispatchSiteName": "string",
      "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
      "targetCompletionDate": "string",
      "targetResponseDate": "string",
      "targetAttendDate": "string",
      "targetDispatchDate": "string",
      "completionDescriptionDate": "2019-08-24T14:15:22Z"
    }
  ],
  "comments": [
    {
      "comment": "string",
      "type": "string",
      "addedDate": "string",
      "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
      "addedByName": "string",
      "source": "string"
    }
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}
```

<h3 id="create-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[RequestDetailsDto](#schemarequestdetailsdto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "description": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "createdDate": "2019-08-24T14:15:22Z",
  "createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "modifiedBy": "07ff0787-1af5-4fc4-9832-7aaeaa962a5e",
  "source": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "personAssignedTo": "string",
  "reasonCode": "string",
  "location": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "alternateId": "string",
    "serviceAddress": "string",
    "path": "string",
    "timeZone": "string"
  },
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "positionTypePath": "string",
    "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
    "assetName": "string"
  },
  "serviceClassification": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "description": "string",
    "aliasId": "string",
    "aliasDescription": "string"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "watcher": [
    {
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "fullName": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string"
    }
  ],
  "slaDate": [
    {
      "slaName": "string",
      "slaDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistory": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "extendedProperties": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "value": [
        "string"
      ],
      "translatedValue": [
        "string"
      ]
    }
  ],
  "workOrders": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "completionDescription": "string",
      "statusDescription": "string",
      "nte": 0,
      "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
      "assigneeName": "string",
      "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
      "dispatchSiteName": "string",
      "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
      "targetCompletionDate": "string",
      "targetResponseDate": "string",
      "targetAttendDate": "string",
      "targetDispatchDate": "string",
      "completionDescriptionDate": "2019-08-24T14:15:22Z"
    }
  ],
  "comments": [
    {
      "comment": "string",
      "type": "string",
      "addedDate": "string",
      "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
      "addedByName": "string",
      "source": "string"
    }
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}
```

<h3 id="create-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request created successfully|[RequestDetailsDto](#schemarequestdetailsdto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## To Configure Flag Settings

<a id="opIdupdateFlagTypeDescription"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/requests/flag-reasons/settings?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/flag-reasons/settings?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Accept': 'application/json',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/requests/flag-reasons/settings', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/requests/flag-reasons/settings`

> Body parameter

```json
{
  "manualFlag": true,
  "isFlaggedReason": true,
  "systemFlag": true,
  "locale": "string",
  "flagTypeList": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "manualFlag": true,
      "isFlaggedReason": true,
      "systemFlag": true,
      "locale": "string",
      "orderSeq": 0,
      "unflagManually": true
    }
  ]
}
```

<h3 id="to-configure-flag-settings-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|Array of Organization IDs.|
|body|body|[FlagTypeSettingsDTO](#schemaflagtypesettingsdto)|true|none|

> Example responses

<h3 id="to-configure-flag-settings-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-configure-flag-settings-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Create Draft Request

<a id="opIdcreateDraftRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests`

> Body parameter

```json
{
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "alternateId": "string",
  "requestedBy": "d834780c-1e92-44d4-9ca3-e84824c5c502",
  "requestedFor": "e12c6185-162f-439c-8c31-bd8ca5946d6b",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
  "serviceDescription": "string",
  "masterServiceClassification": "bfc9a520-fee4-4602-97f3-c501043add0f",
  "extendedProperties": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  }
}
```

<h3 id="create-draft-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[DraftRequestDto](#schemadraftrequestdto)|true|none|

> Example responses

> 200 Response

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "alternateId": "string",
  "requestedBy": "d834780c-1e92-44d4-9ca3-e84824c5c502",
  "requestedFor": "e12c6185-162f-439c-8c31-bd8ca5946d6b",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
  "serviceDescription": "string",
  "masterServiceClassification": "bfc9a520-fee4-4602-97f3-c501043add0f",
  "extendedProperties": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  }
}
```

<h3 id="create-draft-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Draft Request created successfully|[DraftRequestDto](#schemadraftrequestdto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## add to watchers requests.

<a id="opIdaddWatchersRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/{id}/watchers?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/{id}/watchers?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Accept': 'application/json',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/{id}/watchers', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/{id}/watchers`

> Body parameter

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "givenName": "string",
  "familyName": "string",
  "fullName": "string",
  "email": "string"
}
```

<h3 id="add-to-watchers-requests.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orgs|query|array[string]|true|none|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[WatcherDto](#schemawatcherdto)|true|none|

> Example responses

<h3 id="add-to-watchers-requests.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="add-to-watchers-requests.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## To Flag/unflag Requests.

<a id="opIdflagUnflagRequests"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/flag-request?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/flag-request?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Accept': 'application/json',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/flag-request', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/flag-request`

> Body parameter

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
  "isFlaggedRequest": true,
  "flagUnflagReason": "string",
  "assignedToPerson": "dc8f2d92-77bb-48e7-a8d3-93a89322684f",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "hideFromOrgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "unFlagId": "d3b1373b-579f-4af5-b421-a237523f5094"
}
```

<h3 id="to-flag/unflag-requests.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|Array of Organization IDs.|
|body|body|[FlagRequestDto](#schemaflagrequestdto)|true|none|

> Example responses

<h3 id="to-flag/unflag-requests.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-flag/unflag-requests.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Handover Work List to the given person.

<a id="opIdhandoverWorkList"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH http://localhost:8098/request-management/api/v1/requests/handover/{personId}?filterId=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/handover/{personId}?filterId=497f6eca-6276-4993-bfeb-53cbbbba6f08");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("PATCH");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.patch('http://localhost:8098/request-management/api/v1/requests/handover/{personId}', params={
  'filterId': '497f6eca-6276-4993-bfeb-53cbbbba6f08'
}, headers = headers)

print(r.json())

```

`PATCH /request-management/api/v1/requests/handover/{personId}`

> Body parameter

```json
{
  "workListIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="handover-work-list-to-the-given-person.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|personId|path|string(uuid)|true|none|
|filterId|query|string(uuid)|true|none|
|body|body|[WorkListHandoverDto](#schemaworklisthandoverdto)|true|none|

> Example responses

<h3 id="handover-work-list-to-the-given-person.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Handover completed successfully|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="handover-work-list-to-the-given-person.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## getAllRequestsByFilters

<a id="opIdgetAllRequestsByFilters"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/{filterId}?page=page,0,size,1,sort,string \
  -H 'Accept: */*' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/{filterId}?page=page,0,size,1,sort,string");
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
  'Accept': '*/*',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/{filterId}', params={
  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/{filterId}`

<h3 id="getallrequestsbyfilters-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|filterId|path|string(uuid)|true|none|
|orgs|query|array[string]|false|none|
|sort|query|string|false|none|
|filter|query|string|false|none|
|search|query|string|false|none|
|daterange|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

#### Enumerated Values

|Parameter|Value|
|---|---|
|daterange|LAST_30_DAYS|
|daterange|LAST_6_MONTHS|
|daterange|LAST_12_MONTHS|
|daterange|OVER_12_MONTHS|

> Example responses

> 200 Response

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "tenantId": "string",
      "reportedDate": "2019-08-24T14:15:22Z",
      "alternateId": "string",
      "requestDescription": "string",
      "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
      "locationPath": "string",
      "positionId": "da3402dc-13f8-45f9-83a6-bde06dd8eb35",
      "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
      "serviceClassificationDescription": "string",
      "serviceClassificationAliasId": "string",
      "serviceClassificationAliasDescription": "string",
      "flaggedReason": [
        "string"
      ],
      "flagType": "string",
      "flagId": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "flaggedDate": "2019-08-24T14:15:22Z",
      "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
      "priorityDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "statusDescription": "string",
      "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
      "subStatusDescription": "string",
      "requestCreateDate": "2019-08-24T14:15:22Z",
      "requestCreateBy": "5dec2599-4bc7-4639-baba-b0891f624f66",
      "requestModifiedBy": "f5218524-4ede-470a-b7e0-d13454567fb8",
      "requestModifiedDate": "2019-08-24T14:15:22Z",
      "requestLastViewedDate": "2019-08-24T14:15:22Z",
      "requestSource": "string",
      "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
      "teamName": "string",
      "watcherPersonId": "a068f962-505b-4529-928c-2558531c569e",
      "locationName": "string",
      "locationServiceAddress": "string",
      "locationTimezone": "string",
      "ownerPersonId": "bc1f5a42-194a-488a-9b0c-c0149abdaab0",
      "requestedBy": "string",
      "requestedFor": "string",
      "createdBy": "string",
      "requestAssignedToPersonId": "48a43ab1-c57f-4d99-818d-d3d65ddbcc7a",
      "handledBy": "string",
      "customer": "string",
      "country": "string",
      "sla": {
        "targetCompletion": "2019-08-24T14:15:22Z",
        "targetResponse": "2019-08-24T14:15:22Z",
        "targetAttend": "2019-08-24T14:15:22Z"
      },
      "creator": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "owner": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "requester": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "attachments": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "mimeType": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string"
      },
      "completionDate": "2019-08-24T14:15:22Z",
      "numberOfWorkOrders": 0,
      "workOrderId": "string",
      "requestFlagDto": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
          "flaggedBy": "fbe6f7bc-8b40-48d7-9978-e02d8e9c1194",
          "flaggedDate": "2019-08-24T14:15:22Z",
          "unflagId": "2154f209-e227-4c60-8d2b-682a485dd185",
          "unflaggedBy": "5e393d41-bbbd-446e-a1d6-1938deccfa87",
          "unflaggedDate": "2019-08-24T14:15:22Z"
        }
      ],
      "statusHistoryDto": [
        {
          "statusDescription": "string",
          "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
          "changeDate": "2019-08-24T14:15:22Z",
          "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
          "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
        }
      ],
      "isFlagged": true,
      "isPrivate": true,
      "isWatching": true
    }
  ],
  "number": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": {
      "empty": true,
      "unsorted": true,
      "sorted": true
    },
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "first": true,
  "last": true,
  "empty": true
}

```

<h3 id="getallrequestsbyfilters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PageRequestListDto](#schemapagerequestlistdto)|

<aside class="success">
This operation does not require authentication
</aside>

## To Get Similar Requests.

<a id="opIdgetAllSimilarRequests"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/similar-requests?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&locationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&serviceClassificationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/similar-requests?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&locationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&serviceClassificationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/similar-requests', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'locationId': '497f6eca-6276-4993-bfeb-53cbbbba6f08',  'serviceClassificationId': '497f6eca-6276-4993-bfeb-53cbbbba6f08',  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/similar-requests`

<h3 id="to-get-similar-requests.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|Array of Organization IDs.|
|locationId|query|string(uuid)|true|Location Id based on which Similar Request Check is Done.|
|serviceClassificationId|query|string(uuid)|true|ServiceClassification Id based on which Similar Request Check is Done.|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

<h3 id="to-get-similar-requests.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-similar-requests.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## getRequestDetailsById

<a id="opIdgetRequestDetailsById"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/request/{id} \
  -H 'Accept: */*' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/request/{id}");
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
  'Accept': '*/*',
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/request/{id}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/request/{id}`

<h3 id="getrequestdetailsbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|id|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="getrequestdetailsbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequestDetailsDto](#schemarequestdetailsdto)|

<aside class="success">
This operation does not require authentication
</aside>

## getExistingDraftRequestDetails

<a id="opIdgetExistingDraftRequestDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/request/draft \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/request/draft");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/request/draft', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/request/draft`

<h3 id="getexistingdraftrequestdetails-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|

> Example responses

> 200 Response

<h3 id="getexistingdraftrequestdetails-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequestDetailsDto](#schemarequestdetailsdto)|

<aside class="success">
This operation does not require authentication
</aside>

## getPresetFilters

<a id="opIdgetPresetFilters"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/preset-filters \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/preset-filters");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/preset-filters', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/preset-filters`

<h3 id="getpresetfilters-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|

> Example responses

> 200 Response

<h3 id="getpresetfilters-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="getpresetfilters-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[FilterDto](#schemafilterdto)]|false|none|none|
|» filterId|string(uuid)|false|none|none|
|» filterName|string|false|none|none|
|» recordCount|integer(int32)|false|none|none|
|» isOrgEnabled|boolean|false|none|none|
|» isTableFilterEnabled|boolean|false|none|none|
|» sequence|integer(int32)|false|none|none|
|» filterColumns|[[FilterColumnDto](#schemafiltercolumndto)]|false|none|none|
|»» filterColumnId|string(uuid)|false|none|none|
|»» dataAttribute|string|false|none|none|
|»» filterAttribute|string|false|none|none|
|»» labelAttribute|string|false|none|none|
|»» isHideable|boolean|false|none|none|
|»» isSortable|boolean|false|none|none|
|»» isFilterable|boolean|false|none|none|
|»» showOnMobile|boolean|false|none|none|
|»» defaultShow|boolean|false|none|none|
|»» sequence|integer(int32)|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## To Get Flag/unflag Reasons list

<a id="opIdgetFlagUnflagReasonList"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/flag-reasons?isManualFlag=true&isSystemFlag=true&isFlagReasons=true \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/flag-reasons?isManualFlag=true&isSystemFlag=true&isFlagReasons=true");
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
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/flag-reasons', params={
  'isManualFlag': 'true',  'isSystemFlag': 'true',  'isFlagReasons': 'true'
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/flag-reasons`

<h3 id="to-get-flag/unflag-reasons-list-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|false|Array of Organization IDs.|
|isManualFlag|query|boolean|true|isManualFlag - true if returning manual flag reasons list.|
|isSystemFlag|query|boolean|true|isSystemFlag - true if returning system flag reasons list.|
|isFlagReasons|query|boolean|true|isFlagReasons - true if returning flag reason list.|

> Example responses

<h3 id="to-get-flag/unflag-reasons-list-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|None|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-flag/unflag-reasons-list-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## delete from watchers Requests.

<a id="opIddeleteWatchersRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-management/api/v1/requests/{id}/watchers/{personId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/{id}/watchers/{personId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
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
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.delete('http://localhost:8098/request-management/api/v1/requests/{id}/watchers/{personId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`DELETE /request-management/api/v1/requests/{id}/watchers/{personId}`

<h3 id="delete-from-watchers-requests.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orgs|query|array[string]|true|none|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|personId|path|string(uuid)|true|none|

> Example responses

<h3 id="delete-from-watchers-requests.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="delete-from-watchers-requests.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## discardDraftRequest

<a id="opIddiscardDraftRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-management/api/v1/requests/request/draft/{requestId} \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/request/draft/{requestId}");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.delete('http://localhost:8098/request-management/api/v1/requests/request/draft/{requestId}', headers = headers)

print(r.json())

```

`DELETE /request-management/api/v1/requests/request/draft/{requestId}`

<h3 id="discarddraftrequest-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|requestId|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="discarddraftrequest-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|integer|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-profile-controller">Profile</h1>

## Get User-Profile by Person-Id And Identity-Id

<a id="opIdgetPersonProfile"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/profile/me \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me");
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

r = requests.get('http://localhost:8098/request-management/api/v1/profile/me', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/profile/me`

<h3 id="get-user-profile-by-person-id-and-identity-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}
```

<h3 id="get-user-profile-by-person-id-and-identity-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the User-Profile and associated preferences|[ProfileDTO](#schemaprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|User-Profile not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Update User-Profile

<a id="opIdupdatePersonProfile"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/profile/me \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/profile/me', headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/profile/me`

> Body parameter

```json
{
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string"
}
```

<h3 id="update-user-profile-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[UpdateProfileDTO](#schemaupdateprofiledto)|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}
```

<h3 id="update-user-profile-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Updated the User-Profile successfully|[ProfileDTO](#schemaprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|User-Profile not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Self-Register a User

<a id="opIdpostSelfRegisterUser"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/profile/me \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me");
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
  'Accept': 'application/json',
  'Authorization': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/profile/me', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/profile/me`

> Body parameter

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string"
}
```

<h3 id="self-register-a-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|body|body|[SelfRegisterUserProfileDTO](#schemaselfregisteruserprofiledto)|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}
```

<h3 id="self-register-a-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User is Self-Registered with default access and role|[ProfileDTO](#schemaprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden: User is ineligible for Self-Registration|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Update Profile-Preference by Id

<a id="opIdupdatePersonPreference"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/profile/me/preferences/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me/preferences/{id}");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/profile/me/preferences/{id}', headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/profile/me/preferences/{id}`

> Body parameter

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}
```

<h3 id="update-profile-preference-by-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|id|path|string|true|none|
|body|body|[ProfilePreferenceDTO](#schemaprofilepreferencedto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}
```

<h3 id="update-profile-preference-by-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Update the Profile-Preference for the given Id successfully|[ProfilePreferenceDTO](#schemaprofilepreferencedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Profile-Preference not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create Profile-Preference for a combination of Tenant-Id, Person-Id, App-Synonym and Configuration-Type

<a id="opIdcreatePersonPreference"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/profile/me/preferences \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me/preferences");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/profile/me/preferences', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/profile/me/preferences`

> Body parameter

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}
```

<h3 id="create-profile-preference-for-a-combination-of-tenant-id,-person-id,-app-synonym-and-configuration-type-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[ProfilePreferenceDTO](#schemaprofilepreferencedto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}
```

<h3 id="create-profile-preference-for-a-combination-of-tenant-id,-person-id,-app-synonym-and-configuration-type-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Profile Preference created successfully|[ProfilePreferenceDTO](#schemaprofilepreferencedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Tenant-Id or Person-Id or App-Synonym not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Bulk-Create Notification-Preference for a list of users

<a id="opIdcreateBulkNotificationPreferencesForUsers"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/profile/me/preferences/bulk \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me/preferences/bulk");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/profile/me/preferences/bulk', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/profile/me/preferences/bulk`

> Body parameter

```json
{
  "personIdList": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "requestAppSynonym": "string"
}
```

<h3 id="bulk-create-notification-preference-for-a-list-of-users-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[BulkCreateNotificationPreferenceDTO](#schemabulkcreatenotificationpreferencedto)|true|none|

> Example responses

> 200 Response

```json
"string"
```

<h3 id="bulk-create-notification-preference-for-a-list-of-users-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request for Bulk-Create Notification-Preference submitted successfully|string|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Tenant-Id or Person-Id or App-Synonym not found|None|
|409|[Conflict](https://tools.ietf.org/html/rfc7231#section-6.5.8)|Conflict|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Validate User for Self-Registration

<a id="opIdvalidateUserForSelfRegistration"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/profile/me/validate \
  -H 'Accept: application/json' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/me/validate");
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
  'Authorization': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/profile/me/validate', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/profile/me/validate`

<h3 id="validate-user-for-self-registration-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}
```

<h3 id="validate-user-for-self-registration-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User is eligible for Self-Registration|[ProfileDTO](#schemaprofiledto)|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|No Content|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden: User is ineligible for Self-Registration|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-caller-controller">Caller</h1>

## Update Caller-Profile by Call-Centre user

<a id="opIdupdateCallerProfileByCallCenterUser"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/profile/caller \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/caller");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/profile/caller', headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/profile/caller`

> Body parameter

```json
{
  "tenantId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "personId": "string",
  "identityId": "string",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string"
}
```

<h3 id="update-caller-profile-by-call-centre-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[UpdateCallerProfileDTO](#schemaupdatecallerprofiledto)|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}
```

<h3 id="update-caller-profile-by-call-centre-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Updated the Caller-Profile successfully|[ProfileDTO](#schemaprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Caller-Profile not found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create User-Profile for a Caller

<a id="opIdcreateCallerProfile"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/profile/caller \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/caller");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/profile/caller', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/profile/caller`

> Body parameter

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "personId": "string"
}
```

<h3 id="create-user-profile-for-a-caller-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[CallerProfileDTO](#schemacallerprofiledto)|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "personId": "string"
}
```

<h3 id="create-user-profile-for-a-caller-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Caller-Profile created successfully|[CallerProfileDTO](#schemacallerprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Preferences by Tenant-Id,Person-Id, App-Synonym and Configuration-Type for usage in Call-Center

<a id="opIdgetUserPreferencesForCaller"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/profile/caller/{personId}/preference?tenantId=string&orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&overrideAppSynonym=true&configurationType=string \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/caller/{personId}/preference?tenantId=string&orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&overrideAppSynonym=true&configurationType=string");
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

r = requests.get('http://localhost:8098/request-management/api/v1/profile/caller/{personId}/preference', params={
  'tenantId': 'string',  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'overrideAppSynonym': 'true',  'configurationType': 'string'
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/profile/caller/{personId}/preference`

<h3 id="get-preferences-by-tenant-id,person-id,-app-synonym-and-configuration-type-for-usage-in-call-center-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|tenantId|query|string|true|Tenant-Id|
|orgs|query|array[string]|true|Array of Organization-Ids|
|overrideAppSynonym|query|boolean|true|Override App-Synonym flag|
|configurationType|query|string|true|Configuration-Type for the Preference|
|personId|path|string|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}
```

<h3 id="get-preferences-by-tenant-id,person-id,-app-synonym-and-configuration-type-for-usage-in-call-center-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found the Preferences pertaining to the given inputs|[ProfilePreferenceDTO](#schemaprofilepreferencedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-attachment-controller">Attachment</h1>

## Updates attachment, DTO (Only attachment description update is allowed)

<a id="opIdupdateAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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

r = requests.put('http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/attachment/{objectId}/{attachmentId}`

> Body parameter

```json
{
  "description": "string"
}
```

<h3 id="updates-attachment,-dto-(only-attachment-description-update-is-allowed)-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|objectId|path|string(uuid)|true|none|
|attachmentId|path|string(uuid)|true|none|
|body|body|[AttachmentUpdateRequestDTO](#schemaattachmentupdaterequestdto)|true|none|

> Example responses

> 200 Response

<h3 id="updates-attachment,-dto-(only-attachment-description-update-is-allowed)-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|

<aside class="success">
This operation does not require authentication
</aside>

## Deletes an attachment

<a id="opIdremoveAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.delete('http://localhost:8098/request-management/api/v1/attachment/{objectId}/{attachmentId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`DELETE /request-management/api/v1/attachment/{objectId}/{attachmentId}`

<h3 id="deletes-an-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|objectId|path|string(uuid)|true|none|
|attachmentId|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="deletes-an-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|string|

<aside class="success">
This operation does not require authentication
</aside>

## Used to get attachments for an objectId

<a id="opIdgetAttachments"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/attachment/{objectId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/attachment/{objectId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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

r = requests.get('http://localhost:8098/request-management/api/v1/attachment/{objectId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/attachment/{objectId}`

<h3 id="used-to-get-attachments-for-an-objectid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|objectId|path|string(uuid)|true|none|

> Example responses

<h3 id="used-to-get-attachments-for-an-objectid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Response Accepted|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|

<h3 id="used-to-get-attachments-for-an-objectid-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Used to upload an attachment

<a id="opIduploadAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/attachment/{objectId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/attachment/{objectId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/attachment/{objectId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`POST /request-management/api/v1/attachment/{objectId}`

> Body parameter

```json
{
  "file": "string"
}
```

<h3 id="used-to-upload-an-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|objectId|path|string(uuid)|true|none|
|body|body|object|false|none|
|» file|body|string(binary)|true|none|

> Example responses

<h3 id="used-to-upload-an-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|202|[Accepted](https://tools.ietf.org/html/rfc7231#section-6.3.3)|Response Accepted|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|

<h3 id="used-to-upload-an-attachment-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Used to download attachment

<a id="opIddownloadAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/attachment/file/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/attachment/file/{attachmentId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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

r = requests.get('http://localhost:8098/request-management/api/v1/attachment/file/{attachmentId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/attachment/file/{attachmentId}`

<h3 id="used-to-download-attachment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|attachmentId|path|string(uuid)|true|none|

> Example responses

<h3 id="used-to-download-attachment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Response is Ok|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Attachment not found|None|

<h3 id="used-to-download-attachment-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-approval-controller">Approval</h1>

## Approval Process Decision

<a id="opIdprocessDecision"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-management/api/v1/approvals \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/approvals");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.put('http://localhost:8098/request-management/api/v1/approvals', headers = headers)

print(r.json())

```

`PUT /request-management/api/v1/approvals`

> Body parameter

```json
[
  {
    "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
    "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
    "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
    "generalizationId": "927aae38-0d16-4c6f-be55-722105ea93d7",
    "step": 0,
    "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
    "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
    "decision": "Approved",
    "decisionDate": "2019-08-24T14:15:22Z",
    "decisionNote": "string",
    "isDelegate": true
  }
]
```

<h3 id="approval-process-decision-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|false|none|
|body|body|[FactApprovalDecisionDTO](#schemafactapprovaldecisiondto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="approval-process-decision-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Approvals processed successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Approval List by Person ID

<a id="opIdgetApprovals"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/approvals/{personId}?page=page,0,size,1,sort,string \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/approvals/{personId}?page=page,0,size,1,sort,string");
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

r = requests.get('http://localhost:8098/request-management/api/v1/approvals/{personId}', params={
  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/approvals/{personId}`

<h3 id="get-approval-list-by-person-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|false|none|
|filter|query|string|false|none|
|personId|path|string(uuid)|true|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="get-approval-list-by-person-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Approvals returned successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Approval Request Chain Details

<a id="opIdgetRequestChainDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/approvals/{personId}/{factId} \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/approvals/{personId}/{factId}");
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

r = requests.get('http://localhost:8098/request-management/api/v1/approvals/{personId}/{factId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/approvals/{personId}/{factId}`

<h3 id="get-approval-request-chain-details-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|personId|path|string(uuid)|true|none|
|factId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="get-approval-request-chain-details-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Approvals returned successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Approval Request Chain Details History

<a id="opIdgetRequestChainDetailsHistory"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/approvals/history/{subStateId} \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/approvals/history/{subStateId}");
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

r = requests.get('http://localhost:8098/request-management/api/v1/approvals/history/{subStateId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/approvals/history/{subStateId}`

<h3 id="get-approval-request-chain-details-history-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|subStateId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="get-approval-request-chain-details-history-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Approvals chain details returned successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Get Approval Count by Person ID

<a id="opIdgetApprovalsCount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/approvals/count/{personId} \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/approvals/count/{personId}");
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

r = requests.get('http://localhost:8098/request-management/api/v1/approvals/count/{personId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/approvals/count/{personId}`

<h3 id="get-approval-count-by-person-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|personId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="get-approval-count-by-person-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Approvals count returned successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-user-search-controller">User Search</h1>

## Search a user based on firstName, lastName, fullName, email, Orgs and role-permissions

<a id="opIdsearchUsersByNameOrEmailAndOrgsAndRolePermissions"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/user-search \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/user-search");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/user-search', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/user-search`

> Body parameter

```json
{
  "searchStr": "string",
  "searchableOrgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "appSynonym": "string",
  "rolePermissions": [
    "string"
  ]
}
```

<h3 id="search-a-user-based-on-firstname,-lastname,-fullname,-email,-orgs-and-role-permissions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[UserSearchRequestDTO](#schemausersearchrequestdto)|true|none|

> Example responses

> 200 Response

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "personId": "string"
}
```

<h3 id="search-a-user-based-on-firstname,-lastname,-fullname,-email,-orgs-and-role-permissions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|User/s found successfully|[CallerProfileDTO](#schemacallerprofiledto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-feedback-controller">Feedback</h1>

## Fetch Feedback for a Request

<a id="opIdgetFeedbackForRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/{id}/feedback \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/{id}/feedback");
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

r = requests.get('http://localhost:8098/request-management/api/v1/requests/{id}/feedback', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/{id}/feedback`

<h3 id="fetch-feedback-for-a-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|id|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="fetch-feedback-for-a-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Feedback returned successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create Feedback for a Request

<a id="opIdcreateFeedbackForRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/{id}/feedback \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/{id}/feedback");
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
  'Accept': 'application/json',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/{id}/feedback', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/{id}/feedback`

> Body parameter

```json
{
  "rating": 0,
  "comment": "string"
}
```

<h3 id="create-feedback-for-a-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|id|path|string(uuid)|true|none|
|body|body|[FeedbackPostDTO](#schemafeedbackpostdto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}
```

<h3 id="create-feedback-for-a-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Feedback persisted successfully|[FeedbackResponseDTO](#schemafeedbackresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-request-comments-controller">Request Comments</h1>

## addComment

<a id="opIdaddComment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/comments \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/comments");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/comments', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/comments`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "comment": "string",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "commentType": "SUPPORTING_INFORMATION",
  "createdDate": "2019-08-24T14:15:22Z",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "authorName": "string",
  "authorInitials": "string",
  "authorType": "string",
  "sourceApp": "string",
  "organizationType": "string",
  "linkedWorkOrderComment": "097e27f3-3d11-4683-982f-92dbf558862a",
  "commentSource": "COMMENT"
}
```

<h3 id="addcomment-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[CommentDto](#schemacommentdto)|true|none|

> Example responses

> 200 Response

<h3 id="addcomment-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CommentDto](#schemacommentdto)|

<aside class="success">
This operation does not require authentication
</aside>

## addComment_deprecated

<a id="opIdaddComment_deprecated"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/requests/comments/add \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/comments/add");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/requests/comments/add', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/requests/comments/add`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "comment": "string",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "commentType": "SUPPORTING_INFORMATION",
  "createdDate": "2019-08-24T14:15:22Z",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "authorName": "string",
  "authorInitials": "string",
  "authorType": "string",
  "sourceApp": "string",
  "organizationType": "string",
  "linkedWorkOrderComment": "097e27f3-3d11-4683-982f-92dbf558862a",
  "commentSource": "COMMENT"
}
```

<h3 id="addcomment_deprecated-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[CommentDto](#schemacommentdto)|true|none|

> Example responses

> 200 Response

<h3 id="addcomment_deprecated-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[CommentDto](#schemacommentdto)|

<aside class="success">
This operation does not require authentication
</aside>

## getAllComments

<a id="opIdgetAllComments"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/requests/comments/{requestId} \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/requests/comments/{requestId}");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/requests/comments/{requestId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/requests/comments/{requestId}`

<h3 id="getallcomments-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|requestId|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="getallcomments-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[RequestCommentsDto](#schemarequestcommentsdto)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-quick-request-controller">Quick Request</h1>

## Get Quick Request to get Service Classifications

<a id="opIdgetQuickRequestServiceClassifications"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/profile/quickrequests?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/quickrequests?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/profile/quickrequests', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/profile/quickrequests`

<h3 id="get-quick-request-to-get-service-classifications-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|

> Example responses

> 200 Response

<h3 id="get-quick-request-to-get-service-classifications-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Quick Request Service Classification retrieved successfully|[QuickRequestResponseDTO](#schemaquickrequestresponsedto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Record Not Found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Create Quick Request to add Service Classification

<a id="opIdaddQuickRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-management/api/v1/profile/quickrequests \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/quickrequests");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.post('http://localhost:8098/request-management/api/v1/profile/quickrequests', headers = headers)

print(r.json())

```

`POST /request-management/api/v1/profile/quickrequests`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "configuration": [
    {
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "serviceClassifications": [
        {
          "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
          "sequence": 0
        }
      ]
    }
  ]
}
```

<h3 id="create-quick-request-to-add-service-classification-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|body|body|[QuickRequestDto](#schemaquickrequestdto)|true|none|

> Example responses

> 200 Response

<h3 id="create-quick-request-to-add-service-classification-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Quick Request Service Classification added successfully|[QuickRequestDto](#schemaquickrequestdto)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

## Delete Quick Request Add Service Classification

<a id="opIddeleteQuickRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-management/api/v1/profile/quickrequests/{serviceClassificationId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/profile/quickrequests/{serviceClassificationId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
HttpURLConnection con = (HttpURLConnection) obj.openConnection();
con.setRequestMethod("DELETE");
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
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.delete('http://localhost:8098/request-management/api/v1/profile/quickrequests/{serviceClassificationId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`DELETE /request-management/api/v1/profile/quickrequests/{serviceClassificationId}`

<h3 id="delete-quick-request-add-service-classification-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|serviceClassificationId|path|string(uuid)|true|none|
|orgs|query|array[string]|true|none|

<h3 id="delete-quick-request-add-service-classification-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Quick Request Service Classification Deleted successfully|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Runtime error|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-service-classification-controller">Service Classification</h1>

## getServiceClassifications

<a id="opIdgetServiceClassifications"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/serviceclassifications?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/serviceclassifications?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/serviceclassifications', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/serviceclassifications`

<h3 id="getserviceclassifications-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|search|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

<h3 id="getserviceclassifications-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PageClassificationResponseDTO](#schemapageclassificationresponsedto)|

<aside class="success">
This operation does not require authentication
</aside>

## To Get Service Classification Extended Question Set.

<a id="opIdgetSCQuestionSet"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/serviceclassifications/extended-questions/{serviceClassificationId} \
  -H 'Accept: application/json' \
  -H 'authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/serviceclassifications/extended-questions/{serviceClassificationId}");
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
  'authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/serviceclassifications/extended-questions/{serviceClassificationId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/serviceclassifications/extended-questions/{serviceClassificationId}`

<h3 id="to-get-service-classification-extended-question-set.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|serviceClassificationId|path|string(uuid)|true|none|

> Example responses

<h3 id="to-get-service-classification-extended-question-set.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-service-classification-extended-question-set.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-position-controller">Position</h1>

## getPositionsAndAssets

<a id="opIdgetPositionsAndAssets"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/positions?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&locationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/positions?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&locationId=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/positions', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'locationId': '497f6eca-6276-4993-bfeb-53cbbbba6f08',  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/positions`

<h3 id="getpositionsandassets-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|locationId|query|string(uuid)|true|none|
|search|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

<h3 id="getpositionsandassets-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PagePositionDTO](#schemapagepositiondto)|

<aside class="success">
This operation does not require authentication
</aside>

## getPositionById

<a id="opIdgetPositionById"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/positions/{positionId} \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/positions/{positionId}");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/positions/{positionId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/positions/{positionId}`

<h3 id="getpositionbyid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|positionId|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="getpositionbyid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PositionDTO](#schemapositiondto)|

<aside class="success">
This operation does not require authentication
</aside>

## getPositionsByLocationAndStatusId

<a id="opIdgetPositionsByLocationAndStatusId"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/positions/location/{locationId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/positions/location/{locationId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/positions/location/{locationId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/positions/location/{locationId}`

<h3 id="getpositionsbylocationandstatusid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|none|
|locationId|path|string(uuid)|true|none|
|filter|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

<h3 id="getpositionsbylocationandstatusid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PagePositionDTO](#schemapagepositiondto)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-location-controller">Location</h1>

## getLocations

<a id="opIdgetLocations"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/locations?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: */*' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/locations?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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
  'Accept': '*/*',
  'Authorization': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/locations', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/locations`

<h3 id="getlocations-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|orgs|query|array[string]|true|none|
|filter|query|string|false|none|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

> 200 Response

<h3 id="getlocations-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PageLocationDTO](#schemapagelocationdto)|

<aside class="success">
This operation does not require authentication
</aside>

## getLocation

<a id="opIdgetLocation"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/locations/{id} \
  -H 'Accept: */*' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/locations/{id}");
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
  'Accept': '*/*',
  'Authorization': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/locations/{id}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/locations/{id}`

<h3 id="getlocation-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|id|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="getlocation-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[LocationDTO](#schemalocationdto)|

<aside class="success">
This operation does not require authentication
</aside>

## To get Location by id, used to get default location.

<a id="opIdgetLocationById"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/locations/reduced/{locationId} \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/locations/reduced/{locationId}");
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

r = requests.get('http://localhost:8098/request-management/api/v1/locations/reduced/{locationId}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/locations/reduced/{locationId}`

<h3 id="to-get-location-by-id,-used-to-get-default-location.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|locationId|path|string(uuid)|true|To return locations based on id value.|

> Example responses

<h3 id="to-get-location-by-id,-used-to-get-default-location.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Not Found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-location-by-id,-used-to-get-default-location.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## getLocationForeignDomainValue

<a id="opIdgetLocationForeignDomainValue"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/locations/foreignDomainValues/{id} \
  -H 'Accept: */*' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/locations/foreignDomainValues/{id}");
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
  'Accept': '*/*',
  'Authorization': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/locations/foreignDomainValues/{id}', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/locations/foreignDomainValues/{id}`

<h3 id="getlocationforeigndomainvalue-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|source|query|string|false|none|
|id|path|string(uuid)|true|none|

> Example responses

> 200 Response

<h3 id="getlocationforeigndomainvalue-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[LocationForeignReferenceDTO](#schemalocationforeignreferencedto)|

<aside class="success">
This operation does not require authentication
</aside>

## To Get Active Locations.

<a id="opIdgetActiveLocations"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/locations/activelocations?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/locations/activelocations?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08&page=page,0,size,1,sort,string");
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

r = requests.get('http://localhost:8098/request-management/api/v1/locations/activelocations', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
],  'page': {
  "page": 0,
  "size": 1,
  "sort": [
    "string"
  ]
}
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/locations/activelocations`

<h3 id="to-get-active-locations.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|true|Array of Organization IDs.|
|filter|query|string|false|Search/filter locations based on String value.|
|parentId|query|string(uuid)|false|Return child locations using parentId.|
|page|query|[Pageable](#schemapageable)|true|none|

> Example responses

<h3 id="to-get-active-locations.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-active-locations.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-banner-message-controller">Banner Message</h1>

## To Get Latest Banner Message.

<a id="opIdgetLatestBannerMessage"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/banner-message/latest?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: application/json' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/banner-message/latest?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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

r = requests.get('http://localhost:8098/request-management/api/v1/banner-message/latest', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/banner-message/latest`

<h3 id="to-get-latest-banner-message.-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|orgs|query|array[string]|true|none|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|

> Example responses

<h3 id="to-get-latest-banner-message.-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Ok|None|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad request|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|None|

<h3 id="to-get-latest-banner-message.-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-asset-controller">Asset</h1>

## getAssetFDVByIdAndSource

<a id="opIdgetAssetFDVByIdAndSource"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/assets/asset-foreign-domain-value?assetForeignDomainId=497f6eca-6276-4993-bfeb-53cbbbba6f08&source=string \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/assets/asset-foreign-domain-value?assetForeignDomainId=497f6eca-6276-4993-bfeb-53cbbbba6f08&source=string");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/assets/asset-foreign-domain-value', params={
  'assetForeignDomainId': '497f6eca-6276-4993-bfeb-53cbbbba6f08',  'source': 'string'
}, headers = headers)

print(r.json())

```

`GET /request-management/api/v1/assets/asset-foreign-domain-value`

<h3 id="getassetfdvbyidandsource-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|assetForeignDomainId|query|string(uuid)|true|none|
|source|query|string|true|none|

> Example responses

> 200 Response

<h3 id="getassetfdvbyidandsource-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[AssetForeignDomainValueDTO](#schemaassetforeigndomainvaluedto)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-aggregation-controller">Aggregation</h1>

## getAggregatedData

<a id="opIdgetAggregatedData"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/aggregations \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/aggregations");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/aggregations', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/aggregations`

<h3 id="getaggregateddata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|false|none|

> Example responses

> 200 Response

<h3 id="getaggregateddata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[AggregatedDataResponseDTO](#schemaaggregateddataresponsedto)|

<aside class="success">
This operation does not require authentication
</aside>

## getOrgSpecificAggregatedData

<a id="opIdgetOrgSpecificAggregatedData"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/aggregations/orgSpecific \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/aggregations/orgSpecific");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/aggregations/orgSpecific', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/aggregations/orgSpecific`

<h3 id="getorgspecificaggregateddata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|
|orgs|query|array[string]|false|none|

> Example responses

> 200 Response

<h3 id="getorgspecificaggregateddata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[AggregatedDataOrgSpecificResponseDTO](#schemaaggregateddataorgspecificresponsedto)|

<aside class="success">
This operation does not require authentication
</aside>

## getAppAggregatedData

<a id="opIdgetAppAggregatedData"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-management/api/v1/aggregations/app \
  -H 'Accept: */*' \
  -H 'Authorization: string' \
  -H 'x-synonym: string'

```

```java
URL obj = new URL("http://localhost:8098/request-management/api/v1/aggregations/app");
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
  'Accept': '*/*',
  'Authorization': 'string',
  'x-synonym': 'string'
}

r = requests.get('http://localhost:8098/request-management/api/v1/aggregations/app', headers = headers)

print(r.json())

```

`GET /request-management/api/v1/aggregations/app`

<h3 id="getappaggregateddata-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|x-synonym|header|string|true|none|

> Example responses

> 200 Response

<h3 id="getappaggregateddata-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[AggregatedDataAppResponseDTO](#schemaaggregateddataappresponsedto)|

<aside class="success">
This operation does not require authentication
</aside>

# Request Management Schemas

<h2 id="tocS_CommentDetailsDto">CommentDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemacommentdetailsdto"></a>
<a id="schema_CommentDetailsDto"></a>
<a id="tocScommentdetailsdto"></a>
<a id="tocscommentdetailsdto"></a>

```json
{
  "comment": "string",
  "type": "string",
  "addedDate": "string",
  "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
  "addedByName": "string",
  "source": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comment|string|false|none|none|
|type|string|false|none|none|
|addedDate|string|false|none|none|
|addedBy|string(uuid)|false|none|none|
|addedByName|string|false|none|none|
|source|string|false|none|none|

<h2 id="tocS_CreatorDetailsDto">CreatorDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemacreatordetailsdto"></a>
<a id="schema_CreatorDetailsDto"></a>
<a id="tocScreatordetailsdto"></a>
<a id="tocscreatordetailsdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "phoneNumbers": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|email|string|false|none|none|
|phoneNumbers|[string]|false|none|none|

<h2 id="tocS_ExtendedPropertiesDetailsDTO">ExtendedPropertiesDetailsDTO</h2>
<!-- backwards compatibility -->
<a id="schemaextendedpropertiesdetailsdto"></a>
<a id="schema_ExtendedPropertiesDetailsDTO"></a>
<a id="tocSextendedpropertiesdetailsdto"></a>
<a id="tocsextendedpropertiesdetailsdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "value": [
    "string"
  ],
  "translatedValue": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|value|[string]|false|none|none|
|translatedValue|[string]|false|none|none|

<h2 id="tocS_LocationDto">LocationDto</h2>
<!-- backwards compatibility -->
<a id="schemalocationdto"></a>
<a id="schema_LocationDto"></a>
<a id="tocSlocationdto"></a>
<a id="tocslocationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "alternateId": "string",
  "serviceAddress": "string",
  "path": "string",
  "timeZone": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|alternateId|string|false|none|none|
|serviceAddress|string|false|none|none|
|path|string|false|none|none|
|timeZone|string|false|none|none|

<h2 id="tocS_OwnerDetailsDto">OwnerDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemaownerdetailsdto"></a>
<a id="schema_OwnerDetailsDto"></a>
<a id="tocSownerdetailsdto"></a>
<a id="tocsownerdetailsdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "phoneNumbers": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|email|string|false|none|none|
|phoneNumbers|[string]|false|none|none|

<h2 id="tocS_PositionDto">PositionDto</h2>
<!-- backwards compatibility -->
<a id="schemapositiondto"></a>
<a id="schema_PositionDto"></a>
<a id="tocSpositiondto"></a>
<a id="tocspositiondto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "positionTypePath": "string",
  "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
  "assetName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|positionTypePath|string|false|none|none|
|assetId|string(uuid)|false|none|none|
|assetName|string|false|none|none|

<h2 id="tocS_RequestDetailsDto">RequestDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemarequestdetailsdto"></a>
<a id="schema_RequestDetailsDto"></a>
<a id="tocSrequestdetailsdto"></a>
<a id="tocsrequestdetailsdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "description": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "createdDate": "2019-08-24T14:15:22Z",
  "createdBy": "25a02396-1048-48f9-bf93-102d2fb7895e",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "modifiedBy": "07ff0787-1af5-4fc4-9832-7aaeaa962a5e",
  "source": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "personAssignedTo": "string",
  "reasonCode": "string",
  "location": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "alternateId": "string",
    "serviceAddress": "string",
    "path": "string",
    "timeZone": "string"
  },
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "positionTypePath": "string",
    "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
    "assetName": "string"
  },
  "serviceClassification": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "description": "string",
    "aliasId": "string",
    "aliasDescription": "string"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "phoneNumbers": [
      "string"
    ]
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "watcher": [
    {
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "fullName": "string",
      "firstName": "string",
      "lastName": "string",
      "email": "string"
    }
  ],
  "slaDate": [
    {
      "slaName": "string",
      "slaDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistory": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "extendedProperties": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "value": [
        "string"
      ],
      "translatedValue": [
        "string"
      ]
    }
  ],
  "workOrders": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "completionDescription": "string",
      "statusDescription": "string",
      "nte": 0,
      "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
      "assigneeName": "string",
      "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
      "dispatchSiteName": "string",
      "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
      "targetCompletionDate": "string",
      "targetResponseDate": "string",
      "targetAttendDate": "string",
      "targetDispatchDate": "string",
      "completionDescriptionDate": "2019-08-24T14:15:22Z"
    }
  ],
  "comments": [
    {
      "comment": "string",
      "type": "string",
      "addedDate": "string",
      "addedBy": "e7b73b51-b147-4481-bcc4-0ec1394b652e",
      "addedByName": "string",
      "source": "string"
    }
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|reportedDate|string(date-time)|false|none|none|
|alternateId|string|false|none|none|
|description|string|false|none|none|
|flagId|[string]|false|none|none|
|priorityId|string(uuid)|false|none|none|
|priorityDescription|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|statusDescription|string|false|none|none|
|subStatusId|string(uuid)|false|none|none|
|subStatusDescription|string|false|none|none|
|createdDate|string(date-time)|false|none|none|
|createdBy|string(uuid)|false|none|none|
|modifiedDate|string(date-time)|false|none|none|
|modifiedBy|string(uuid)|false|none|none|
|source|string|false|none|none|
|teamId|string(uuid)|false|none|none|
|teamName|string|false|none|none|
|sessionId|string(uuid)|false|none|none|
|personAssignedTo|string|false|none|none|
|reasonCode|string|false|none|none|
|location|[LocationDto](#schemalocationdto)|false|none|none|
|position|[PositionDto](#schemapositiondto)|false|none|none|
|serviceClassification|[ServiceClassificationDto](#schemaserviceclassificationdto)|false|none|none|
|creator|[CreatorDetailsDto](#schemacreatordetailsdto)|false|none|none|
|owner|[OwnerDetailsDto](#schemaownerdetailsdto)|false|none|none|
|requester|[RequesterDetailsDto](#schemarequesterdetailsdto)|false|none|none|
|completionDate|string(date-time)|false|none|none|
|watcher|[[WatcherDetailsDto](#schemawatcherdetailsdto)]|false|none|none|
|slaDate|[[SLADetailsDto](#schemasladetailsdto)]|false|none|none|
|statusHistory|[[StatusHistoryDto](#schemastatushistorydto)]|false|none|none|
|extendedProperties|[[ExtendedPropertiesDetailsDTO](#schemaextendedpropertiesdetailsdto)]|false|none|none|
|workOrders|[[WorkOrderDetailsDto](#schemaworkorderdetailsdto)]|false|none|none|
|comments|[[CommentDetailsDto](#schemacommentdetailsdto)]|false|none|none|
|flaggedDate|string(date-time)|false|none|none|
|isFlagged|boolean|false|none|none|
|isPrivate|boolean|false|none|none|
|isWatching|boolean|false|none|none|

<h2 id="tocS_RequesterDetailsDto">RequesterDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemarequesterdetailsdto"></a>
<a id="schema_RequesterDetailsDto"></a>
<a id="tocSrequesterdetailsdto"></a>
<a id="tocsrequesterdetailsdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "phoneNumbers": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|email|string|false|none|none|
|phoneNumbers|[string]|false|none|none|

<h2 id="tocS_SLADetailsDto">SLADetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemasladetailsdto"></a>
<a id="schema_SLADetailsDto"></a>
<a id="tocSsladetailsdto"></a>
<a id="tocssladetailsdto"></a>

```json
{
  "slaName": "string",
  "slaDate": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|slaName|string|false|none|none|
|slaDate|string(date-time)|false|none|none|

<h2 id="tocS_ServiceClassificationDto">ServiceClassificationDto</h2>
<!-- backwards compatibility -->
<a id="schemaserviceclassificationdto"></a>
<a id="schema_ServiceClassificationDto"></a>
<a id="tocSserviceclassificationdto"></a>
<a id="tocsserviceclassificationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "description": "string",
  "aliasId": "string",
  "aliasDescription": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|description|string|false|none|none|
|aliasId|string|false|none|none|
|aliasDescription|string|false|none|none|

<h2 id="tocS_StatusHistoryDto">StatusHistoryDto</h2>
<!-- backwards compatibility -->
<a id="schemastatushistorydto"></a>
<a id="schema_StatusHistoryDto"></a>
<a id="tocSstatushistorydto"></a>
<a id="tocsstatushistorydto"></a>

```json
{
  "statusDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "changeDate": "2019-08-24T14:15:22Z",
  "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
  "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|statusDescription|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|changeDate|string(date-time)|false|none|none|
|changeBy|string(uuid)|false|none|none|
|changeByName|string(uuid)|false|none|none|

<h2 id="tocS_WatcherDetailsDto">WatcherDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemawatcherdetailsdto"></a>
<a id="schema_WatcherDetailsDto"></a>
<a id="tocSwatcherdetailsdto"></a>
<a id="tocswatcherdetailsdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string",
  "firstName": "string",
  "lastName": "string",
  "email": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|email|string|false|none|none|

<h2 id="tocS_WorkOrderDetailsDto">WorkOrderDetailsDto</h2>
<!-- backwards compatibility -->
<a id="schemaworkorderdetailsdto"></a>
<a id="schema_WorkOrderDetailsDto"></a>
<a id="tocSworkorderdetailsdto"></a>
<a id="tocsworkorderdetailsdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "description": "string",
  "completionDescription": "string",
  "statusDescription": "string",
  "nte": 0,
  "assigneeId": "665a9750-71bd-4b96-bacd-9efa4ae022dd",
  "assigneeName": "string",
  "dispatchSiteId": "5a635992-409d-46b2-9826-0e325ffa4dd9",
  "dispatchSiteName": "string",
  "legacyFacilityManageId": "7b2ba80f-4328-440f-8f91-7bab46b8107c",
  "targetCompletionDate": "string",
  "targetResponseDate": "string",
  "targetAttendDate": "string",
  "targetDispatchDate": "string",
  "completionDescriptionDate": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|description|string|false|none|none|
|completionDescription|string|false|none|none|
|statusDescription|string|false|none|none|
|nte|number|false|none|none|
|assigneeId|string(uuid)|false|none|none|
|assigneeName|string|false|none|none|
|dispatchSiteId|string(uuid)|false|none|none|
|dispatchSiteName|string|false|none|none|
|legacyFacilityManageId|string(uuid)|false|none|none|
|targetCompletionDate|string|false|none|none|
|targetResponseDate|string|false|none|none|
|targetAttendDate|string|false|none|none|
|targetDispatchDate|string|false|none|none|
|completionDescriptionDate|string(date-time)|false|none|none|

<h2 id="tocS_FlagTypeDTO">FlagTypeDTO</h2>
<!-- backwards compatibility -->
<a id="schemaflagtypedto"></a>
<a id="schema_FlagTypeDTO"></a>
<a id="tocSflagtypedto"></a>
<a id="tocsflagtypedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "description": "string",
  "manualFlag": true,
  "isFlaggedReason": true,
  "systemFlag": true,
  "locale": "string",
  "orderSeq": 0,
  "unflagManually": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|description|string|false|none|none|
|manualFlag|boolean|false|none|none|
|isFlaggedReason|boolean|false|none|none|
|systemFlag|boolean|false|none|none|
|locale|string|false|none|none|
|orderSeq|integer(int32)|false|none|none|
|unflagManually|boolean|false|none|none|

<h2 id="tocS_FlagTypeSettingsDTO">FlagTypeSettingsDTO</h2>
<!-- backwards compatibility -->
<a id="schemaflagtypesettingsdto"></a>
<a id="schema_FlagTypeSettingsDTO"></a>
<a id="tocSflagtypesettingsdto"></a>
<a id="tocsflagtypesettingsdto"></a>

```json
{
  "manualFlag": true,
  "isFlaggedReason": true,
  "systemFlag": true,
  "locale": "string",
  "flagTypeList": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "manualFlag": true,
      "isFlaggedReason": true,
      "systemFlag": true,
      "locale": "string",
      "orderSeq": 0,
      "unflagManually": true
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|manualFlag|boolean|false|none|none|
|isFlaggedReason|boolean|false|none|none|
|systemFlag|boolean|false|none|none|
|locale|string|false|none|none|
|flagTypeList|[[FlagTypeDTO](#schemaflagtypedto)]|false|none|none|

<h2 id="tocS_UpdateProfileDTO">UpdateProfileDTO</h2>
<!-- backwards compatibility -->
<a id="schemaupdateprofiledto"></a>
<a id="schema_UpdateProfileDTO"></a>
<a id="tocSupdateprofiledto"></a>
<a id="tocsupdateprofiledto"></a>

```json
{
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumber|string|false|none|none|
|locale|string|false|none|none|

<h2 id="tocS_ProfileDTO">ProfileDTO</h2>
<!-- backwards compatibility -->
<a id="schemaprofiledto"></a>
<a id="schema_ProfileDTO"></a>
<a id="tocSprofiledto"></a>
<a id="tocsprofiledto"></a>

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string",
  "applicationPreferences": [
    {
      "id": "string",
      "tenantId": "string",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "appSynonym": "string",
      "configurationName": "string",
      "configurationType": "string",
      "configuration": {
        "property1": {},
        "property2": {}
      }
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumber|string|false|none|none|
|locale|string|false|none|none|
|applicationPreferences|[[ProfilePreferenceDTO](#schemaprofilepreferencedto)]|false|none|none|

<h2 id="tocS_ProfilePreferenceDTO">ProfilePreferenceDTO</h2>
<!-- backwards compatibility -->
<a id="schemaprofilepreferencedto"></a>
<a id="schema_ProfilePreferenceDTO"></a>
<a id="tocSprofilepreferencedto"></a>
<a id="tocsprofilepreferencedto"></a>

```json
{
  "id": "string",
  "tenantId": "string",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": {
    "property1": {},
    "property2": {}
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|tenantId|string|false|none|none|
|personId|string(uuid)|false|none|none|
|appSynonym|string|false|none|none|
|configurationName|string|false|none|none|
|configurationType|string|false|none|none|
|configuration|object|false|none|none|
|» **additionalProperties**|object|false|none|none|

<h2 id="tocS_UpdateCallerProfileDTO">UpdateCallerProfileDTO</h2>
<!-- backwards compatibility -->
<a id="schemaupdatecallerprofiledto"></a>
<a id="schema_UpdateCallerProfileDTO"></a>
<a id="tocSupdatecallerprofiledto"></a>
<a id="tocsupdatecallerprofiledto"></a>

```json
{
  "tenantId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "personId": "string",
  "identityId": "string",
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|tenantId|string|false|none|none|
|orgs|[string]|false|none|none|
|personId|string|false|none|none|
|identityId|string|false|none|none|
|email|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumber|string|false|none|none|

<h2 id="tocS_AttachmentUpdateRequestDTO">AttachmentUpdateRequestDTO</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentupdaterequestdto"></a>
<a id="schema_AttachmentUpdateRequestDTO"></a>
<a id="tocSattachmentupdaterequestdto"></a>
<a id="tocsattachmentupdaterequestdto"></a>

```json
{
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|description|string|false|none|none|

<h2 id="tocS_FactApprovalDecisionDTO">FactApprovalDecisionDTO</h2>
<!-- backwards compatibility -->
<a id="schemafactapprovaldecisiondto"></a>
<a id="schema_FactApprovalDecisionDTO"></a>
<a id="tocSfactapprovaldecisiondto"></a>
<a id="tocsfactapprovaldecisiondto"></a>

```json
{
  "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
  "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
  "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
  "generalizationId": "927aae38-0d16-4c6f-be55-722105ea93d7",
  "step": 0,
  "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
  "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
  "decision": "Approved",
  "decisionDate": "2019-08-24T14:15:22Z",
  "decisionNote": "string",
  "isDelegate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|subStateId|string(uuid)|false|none|none|
|factId|string(uuid)|false|none|none|
|approverId|string(uuid)|false|none|none|
|generalizationId|string(uuid)|false|none|none|
|step|integer(int32)|false|none|none|
|chainId|string(uuid)|false|none|none|
|delegatorId|string(uuid)|false|none|none|
|decision|string|false|none|none|
|decisionDate|string(date-time)|false|none|none|
|decisionNote|string|false|none|none|
|isDelegate|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|decision|Approved|
|decision|Declined|

<h2 id="tocS_FeedbackResponseDTO">FeedbackResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemafeedbackresponsedto"></a>
<a id="schema_FeedbackResponseDTO"></a>
<a id="tocSfeedbackresponsedto"></a>
<a id="tocsfeedbackresponsedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "rating": 0,
  "comment": "string",
  "createDate": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|requestId|string(uuid)|false|none|none|
|author|string(uuid)|false|none|none|
|rating|integer(int32)|false|none|none|
|comment|string|false|none|none|
|createDate|string(date-time)|false|none|none|

<h2 id="tocS_UserSearchRequestDTO">UserSearchRequestDTO</h2>
<!-- backwards compatibility -->
<a id="schemausersearchrequestdto"></a>
<a id="schema_UserSearchRequestDTO"></a>
<a id="tocSusersearchrequestdto"></a>
<a id="tocsusersearchrequestdto"></a>

```json
{
  "searchStr": "string",
  "searchableOrgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "appSynonym": "string",
  "rolePermissions": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|searchStr|string|false|none|none|
|searchableOrgs|[string]|false|none|none|
|appSynonym|string|false|none|none|
|rolePermissions|[string]|false|none|none|

<h2 id="tocS_CallerProfileDTO">CallerProfileDTO</h2>
<!-- backwards compatibility -->
<a id="schemacallerprofiledto"></a>
<a id="schema_CallerProfileDTO"></a>
<a id="tocScallerprofiledto"></a>
<a id="tocscallerprofiledto"></a>

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "personId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumber|string|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|personId|string|false|none|none|

<h2 id="tocS_DraftRequestDto">DraftRequestDto</h2>
<!-- backwards compatibility -->
<a id="schemadraftrequestdto"></a>
<a id="schema_DraftRequestDto"></a>
<a id="tocSdraftrequestdto"></a>
<a id="tocsdraftrequestdto"></a>

```json
{
  "sessionId": "f6567dd8-e069-418e-8893-7d22fcf12459",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "alternateId": "string",
  "requestedBy": "d834780c-1e92-44d4-9ca3-e84824c5c502",
  "requestedFor": "e12c6185-162f-439c-8c31-bd8ca5946d6b",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
  "serviceDescription": "string",
  "masterServiceClassification": "bfc9a520-fee4-4602-97f3-c501043add0f",
  "extendedProperties": {
    "property1": [
      "string"
    ],
    "property2": [
      "string"
    ]
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sessionId|string(uuid)|false|write-only|none|
|requestId|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|alternateId|string|false|none|none|
|requestedBy|string(uuid)|false|none|none|
|requestedFor|string(uuid)|false|none|none|
|locationId|string(uuid)|false|none|none|
|assetId|string(uuid)|false|none|none|
|serviceDescription|string|false|none|none|
|masterServiceClassification|string(uuid)|false|none|none|
|extendedProperties|object|false|none|none|
|» **additionalProperties**|[string]|false|none|none|

<h2 id="tocS_WatcherDto">WatcherDto</h2>
<!-- backwards compatibility -->
<a id="schemawatcherdto"></a>
<a id="schema_WatcherDto"></a>
<a id="tocSwatcherdto"></a>
<a id="tocswatcherdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "givenName": "string",
  "familyName": "string",
  "fullName": "string",
  "email": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|true|none|none|
|givenName|string|false|none|none|
|familyName|string|false|none|none|
|fullName|string|false|none|none|
|email|string|false|none|none|

<h2 id="tocS_FeedbackPostDTO">FeedbackPostDTO</h2>
<!-- backwards compatibility -->
<a id="schemafeedbackpostdto"></a>
<a id="schema_FeedbackPostDTO"></a>
<a id="tocSfeedbackpostdto"></a>
<a id="tocsfeedbackpostdto"></a>

```json
{
  "rating": 0,
  "comment": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|rating|integer(int32)|false|none|none|
|comment|string|false|none|none|

<h2 id="tocS_FlagRequestDto">FlagRequestDto</h2>
<!-- backwards compatibility -->
<a id="schemaflagrequestdto"></a>
<a id="schema_FlagRequestDto"></a>
<a id="tocSflagrequestdto"></a>
<a id="tocsflagrequestdto"></a>

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
  "isFlaggedRequest": true,
  "flagUnflagReason": "string",
  "assignedToPerson": "dc8f2d92-77bb-48e7-a8d3-93a89322684f",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "hideFromOrgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "unFlagId": "d3b1373b-579f-4af5-b421-a237523f5094"
}

```

FlagRequestDto to have details to Flag/Unflag request.

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requestId|string(uuid)|true|none|none|
|flagId|string(uuid)|true|none|none|
|isFlaggedRequest|boolean|true|none|none|
|flagUnflagReason|string|false|none|none|
|assignedToPerson|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|hideFromOrgs|[string]|false|none|none|
|unFlagId|string(uuid)|false|none|none|

<h2 id="tocS_CommentDto">CommentDto</h2>
<!-- backwards compatibility -->
<a id="schemacommentdto"></a>
<a id="schema_CommentDto"></a>
<a id="tocScommentdto"></a>
<a id="tocscommentdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "comment": "string",
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "commentType": "SUPPORTING_INFORMATION",
  "createdDate": "2019-08-24T14:15:22Z",
  "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
  "authorName": "string",
  "authorInitials": "string",
  "authorType": "string",
  "sourceApp": "string",
  "organizationType": "string",
  "linkedWorkOrderComment": "097e27f3-3d11-4683-982f-92dbf558862a",
  "commentSource": "COMMENT"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|comment|string|false|none|none|
|requestId|string(uuid)|false|none|none|
|commentType|string|false|none|none|
|createdDate|string(date-time)|false|none|none|
|author|string(uuid)|false|none|none|
|authorName|string|false|none|none|
|authorInitials|string|false|none|none|
|authorType|string|false|none|none|
|sourceApp|string|false|none|none|
|organizationType|string|false|none|none|
|linkedWorkOrderComment|string(uuid)|false|none|none|
|commentSource|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|commentType|SUPPORTING_INFORMATION|
|commentType|REQUEST_UPDATE|
|commentType|FEEDBACK|
|commentType|REQUEST_DESCRIPTION|
|commentSource|COMMENT|
|commentSource|STATUS_CHANGE|
|commentSource|FEEDBACK|

<h2 id="tocS_ConfigurationDto">ConfigurationDto</h2>
<!-- backwards compatibility -->
<a id="schemaconfigurationdto"></a>
<a id="schema_ConfigurationDto"></a>
<a id="tocSconfigurationdto"></a>
<a id="tocsconfigurationdto"></a>

```json
{
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "serviceClassifications": [
    {
      "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
      "sequence": 0
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orgs|[string]|false|none|none|
|serviceClassifications|[[QuickRequestServiceClassificationDto](#schemaquickrequestserviceclassificationdto)]|false|none|none|

<h2 id="tocS_QuickRequestDto">QuickRequestDto</h2>
<!-- backwards compatibility -->
<a id="schemaquickrequestdto"></a>
<a id="schema_QuickRequestDto"></a>
<a id="tocSquickrequestdto"></a>
<a id="tocsquickrequestdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "configuration": [
    {
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "serviceClassifications": [
        {
          "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
          "sequence": 0
        }
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|configuration|[[ConfigurationDto](#schemaconfigurationdto)]|false|none|none|

<h2 id="tocS_QuickRequestServiceClassificationDto">QuickRequestServiceClassificationDto</h2>
<!-- backwards compatibility -->
<a id="schemaquickrequestserviceclassificationdto"></a>
<a id="schema_QuickRequestServiceClassificationDto"></a>
<a id="tocSquickrequestserviceclassificationdto"></a>
<a id="tocsquickrequestserviceclassificationdto"></a>

```json
{
  "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
  "sequence": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serviceClassificationId|string(uuid)|false|none|none|
|sequence|integer(int32)|false|none|none|

<h2 id="tocS_SelfRegisterUserProfileDTO">SelfRegisterUserProfileDTO</h2>
<!-- backwards compatibility -->
<a id="schemaselfregisteruserprofiledto"></a>
<a id="schema_SelfRegisterUserProfileDTO"></a>
<a id="tocSselfregisteruserprofiledto"></a>
<a id="tocsselfregisteruserprofiledto"></a>

```json
{
  "email": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "phoneNumber": "string",
  "locale": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|email|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|phoneNumber|string|false|none|none|
|locale|string|false|none|none|

<h2 id="tocS_BulkCreateNotificationPreferenceDTO">BulkCreateNotificationPreferenceDTO</h2>
<!-- backwards compatibility -->
<a id="schemabulkcreatenotificationpreferencedto"></a>
<a id="schema_BulkCreateNotificationPreferenceDTO"></a>
<a id="tocSbulkcreatenotificationpreferencedto"></a>
<a id="tocsbulkcreatenotificationpreferencedto"></a>

```json
{
  "personIdList": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "requestAppSynonym": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personIdList|[string]|false|none|none|
|tenantId|string|false|none|none|
|requestAppSynonym|string|false|none|none|

<h2 id="tocS_WorkListHandoverDto">WorkListHandoverDto</h2>
<!-- backwards compatibility -->
<a id="schemaworklisthandoverdto"></a>
<a id="schema_WorkListHandoverDto"></a>
<a id="tocSworklisthandoverdto"></a>
<a id="tocsworklisthandoverdto"></a>

```json
{
  "workListIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|workListIds|[string]|false|none|none|

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

<h2 id="tocS_ClassificationResponseDTO">ClassificationResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemaclassificationresponsedto"></a>
<a id="schema_ClassificationResponseDTO"></a>
<a id="tocSclassificationresponsedto"></a>
<a id="tocsclassificationresponsedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "catalogName": "string",
  "catalogId": "8c4666aa-d43d-4196-b78a-f94040b1db76",
  "path": "string",
  "synonyms": [
    "string"
  ],
  "relatedClassifications": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "catalogName": "string",
      "catalogId": "8c4666aa-d43d-4196-b78a-f94040b1db76",
      "path": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|catalogName|string|false|none|none|
|catalogId|string(uuid)|false|none|none|
|path|string|false|none|none|
|synonyms|[string]|false|none|none|
|relatedClassifications|[[RelatedClassifications](#schemarelatedclassifications)]|false|none|none|

<h2 id="tocS_PageClassificationResponseDTO">PageClassificationResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemapageclassificationresponsedto"></a>
<a id="schema_PageClassificationResponseDTO"></a>
<a id="tocSpageclassificationresponsedto"></a>
<a id="tocspageclassificationresponsedto"></a>

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "catalogName": "string",
      "catalogId": "8c4666aa-d43d-4196-b78a-f94040b1db76",
      "path": "string",
      "synonyms": [
        "string"
      ],
      "relatedClassifications": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "catalogName": "string",
          "catalogId": "8c4666aa-d43d-4196-b78a-f94040b1db76",
          "path": "string"
        }
      ]
    }
  ],
  "number": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": {
      "empty": true,
      "unsorted": true,
      "sorted": true
    },
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "first": true,
  "last": true,
  "empty": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalPages|integer(int32)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|size|integer(int32)|false|none|none|
|content|[[ClassificationResponseDTO](#schemaclassificationresponsedto)]|false|none|none|
|number|integer(int32)|false|none|none|
|sort|[SortObject](#schemasortobject)|false|none|none|
|numberOfElements|integer(int32)|false|none|none|
|pageable|[PageableObject](#schemapageableobject)|false|none|none|
|first|boolean|false|none|none|
|last|boolean|false|none|none|
|empty|boolean|false|none|none|

<h2 id="tocS_PageableObject">PageableObject</h2>
<!-- backwards compatibility -->
<a id="schemapageableobject"></a>
<a id="schema_PageableObject"></a>
<a id="tocSpageableobject"></a>
<a id="tocspageableobject"></a>

```json
{
  "offset": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "pageNumber": 0,
  "pageSize": 0,
  "paged": true,
  "unpaged": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|offset|integer(int64)|false|none|none|
|sort|[SortObject](#schemasortobject)|false|none|none|
|pageNumber|integer(int32)|false|none|none|
|pageSize|integer(int32)|false|none|none|
|paged|boolean|false|none|none|
|unpaged|boolean|false|none|none|

<h2 id="tocS_RelatedClassifications">RelatedClassifications</h2>
<!-- backwards compatibility -->
<a id="schemarelatedclassifications"></a>
<a id="schema_RelatedClassifications"></a>
<a id="tocSrelatedclassifications"></a>
<a id="tocsrelatedclassifications"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "catalogName": "string",
  "catalogId": "8c4666aa-d43d-4196-b78a-f94040b1db76",
  "path": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|catalogName|string|false|none|none|
|catalogId|string(uuid)|false|none|none|
|path|string|false|none|none|

<h2 id="tocS_SortObject">SortObject</h2>
<!-- backwards compatibility -->
<a id="schemasortobject"></a>
<a id="schema_SortObject"></a>
<a id="tocSsortobject"></a>
<a id="tocssortobject"></a>

```json
{
  "empty": true,
  "unsorted": true,
  "sorted": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|empty|boolean|false|none|none|
|unsorted|boolean|false|none|none|
|sorted|boolean|false|none|none|

<h2 id="tocS_AttachmentDto">AttachmentDto</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentdto"></a>
<a id="schema_AttachmentDto"></a>
<a id="tocSattachmentdto"></a>
<a id="tocsattachmentdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "mimeType": "string",
  "extension": "string",
  "type": "string",
  "status": "string",
  "storageAccount": "string",
  "container": "string",
  "fileMd5": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|mimeType|string|false|none|none|
|extension|string|false|none|none|
|type|string|false|none|none|
|status|string|false|none|none|
|storageAccount|string|false|none|none|
|container|string|false|none|none|
|fileMd5|string|false|none|none|

<h2 id="tocS_CreatorDto">CreatorDto</h2>
<!-- backwards compatibility -->
<a id="schemacreatordto"></a>
<a id="schema_CreatorDto"></a>
<a id="tocScreatordto"></a>
<a id="tocscreatordto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|

<h2 id="tocS_OwnerDto">OwnerDto</h2>
<!-- backwards compatibility -->
<a id="schemaownerdto"></a>
<a id="schema_OwnerDto"></a>
<a id="tocSownerdto"></a>
<a id="tocsownerdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|

<h2 id="tocS_PageRequestListDto">PageRequestListDto</h2>
<!-- backwards compatibility -->
<a id="schemapagerequestlistdto"></a>
<a id="schema_PageRequestListDto"></a>
<a id="tocSpagerequestlistdto"></a>
<a id="tocspagerequestlistdto"></a>

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "tenantId": "string",
      "reportedDate": "2019-08-24T14:15:22Z",
      "alternateId": "string",
      "requestDescription": "string",
      "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
      "locationPath": "string",
      "positionId": "da3402dc-13f8-45f9-83a6-bde06dd8eb35",
      "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
      "serviceClassificationDescription": "string",
      "serviceClassificationAliasId": "string",
      "serviceClassificationAliasDescription": "string",
      "flaggedReason": [
        "string"
      ],
      "flagType": "string",
      "flagId": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "flaggedDate": "2019-08-24T14:15:22Z",
      "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
      "priorityDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "statusDescription": "string",
      "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
      "subStatusDescription": "string",
      "requestCreateDate": "2019-08-24T14:15:22Z",
      "requestCreateBy": "5dec2599-4bc7-4639-baba-b0891f624f66",
      "requestModifiedBy": "f5218524-4ede-470a-b7e0-d13454567fb8",
      "requestModifiedDate": "2019-08-24T14:15:22Z",
      "requestLastViewedDate": "2019-08-24T14:15:22Z",
      "requestSource": "string",
      "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
      "teamName": "string",
      "watcherPersonId": "a068f962-505b-4529-928c-2558531c569e",
      "locationName": "string",
      "locationServiceAddress": "string",
      "locationTimezone": "string",
      "ownerPersonId": "bc1f5a42-194a-488a-9b0c-c0149abdaab0",
      "requestedBy": "string",
      "requestedFor": "string",
      "createdBy": "string",
      "requestAssignedToPersonId": "48a43ab1-c57f-4d99-818d-d3d65ddbcc7a",
      "handledBy": "string",
      "customer": "string",
      "country": "string",
      "sla": {
        "targetCompletion": "2019-08-24T14:15:22Z",
        "targetResponse": "2019-08-24T14:15:22Z",
        "targetAttend": "2019-08-24T14:15:22Z"
      },
      "creator": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "owner": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "requester": {
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "fullName": "string"
      },
      "attachments": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "mimeType": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string"
      },
      "completionDate": "2019-08-24T14:15:22Z",
      "numberOfWorkOrders": 0,
      "workOrderId": "string",
      "requestFlagDto": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
          "flaggedBy": "fbe6f7bc-8b40-48d7-9978-e02d8e9c1194",
          "flaggedDate": "2019-08-24T14:15:22Z",
          "unflagId": "2154f209-e227-4c60-8d2b-682a485dd185",
          "unflaggedBy": "5e393d41-bbbd-446e-a1d6-1938deccfa87",
          "unflaggedDate": "2019-08-24T14:15:22Z"
        }
      ],
      "statusHistoryDto": [
        {
          "statusDescription": "string",
          "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
          "changeDate": "2019-08-24T14:15:22Z",
          "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
          "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
        }
      ],
      "isFlagged": true,
      "isPrivate": true,
      "isWatching": true
    }
  ],
  "number": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": {
      "empty": true,
      "unsorted": true,
      "sorted": true
    },
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "first": true,
  "last": true,
  "empty": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalPages|integer(int32)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|size|integer(int32)|false|none|none|
|content|[[RequestListDto](#schemarequestlistdto)]|false|none|none|
|number|integer(int32)|false|none|none|
|sort|[SortObject](#schemasortobject)|false|none|none|
|numberOfElements|integer(int32)|false|none|none|
|pageable|[PageableObject](#schemapageableobject)|false|none|none|
|first|boolean|false|none|none|
|last|boolean|false|none|none|
|empty|boolean|false|none|none|

<h2 id="tocS_RequestFlagDto">RequestFlagDto</h2>
<!-- backwards compatibility -->
<a id="schemarequestflagdto"></a>
<a id="schema_RequestFlagDto"></a>
<a id="tocSrequestflagdto"></a>
<a id="tocsrequestflagdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
  "flaggedBy": "fbe6f7bc-8b40-48d7-9978-e02d8e9c1194",
  "flaggedDate": "2019-08-24T14:15:22Z",
  "unflagId": "2154f209-e227-4c60-8d2b-682a485dd185",
  "unflaggedBy": "5e393d41-bbbd-446e-a1d6-1938deccfa87",
  "unflaggedDate": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|flagId|string(uuid)|false|none|none|
|flaggedBy|string(uuid)|false|none|none|
|flaggedDate|string(date-time)|false|none|none|
|unflagId|string(uuid)|false|none|none|
|unflaggedBy|string(uuid)|false|none|none|
|unflaggedDate|string(date-time)|false|none|none|

<h2 id="tocS_RequestListDto">RequestListDto</h2>
<!-- backwards compatibility -->
<a id="schemarequestlistdto"></a>
<a id="schema_RequestListDto"></a>
<a id="tocSrequestlistdto"></a>
<a id="tocsrequestlistdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "reportedDate": "2019-08-24T14:15:22Z",
  "alternateId": "string",
  "requestDescription": "string",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "locationPath": "string",
  "positionId": "da3402dc-13f8-45f9-83a6-bde06dd8eb35",
  "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
  "serviceClassificationDescription": "string",
  "serviceClassificationAliasId": "string",
  "serviceClassificationAliasDescription": "string",
  "flaggedReason": [
    "string"
  ],
  "flagType": "string",
  "flagId": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "flaggedDate": "2019-08-24T14:15:22Z",
  "priorityId": "a57eab25-838b-40cc-a576-57e4056f1d6c",
  "priorityDescription": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusDescription": "string",
  "subStatusId": "c9b6af8c-39fe-4426-a105-7343d1ed54d3",
  "subStatusDescription": "string",
  "requestCreateDate": "2019-08-24T14:15:22Z",
  "requestCreateBy": "5dec2599-4bc7-4639-baba-b0891f624f66",
  "requestModifiedBy": "f5218524-4ede-470a-b7e0-d13454567fb8",
  "requestModifiedDate": "2019-08-24T14:15:22Z",
  "requestLastViewedDate": "2019-08-24T14:15:22Z",
  "requestSource": "string",
  "teamId": "a4ede8ba-7c0a-4485-8763-cbd9b282fbec",
  "teamName": "string",
  "watcherPersonId": "a068f962-505b-4529-928c-2558531c569e",
  "locationName": "string",
  "locationServiceAddress": "string",
  "locationTimezone": "string",
  "ownerPersonId": "bc1f5a42-194a-488a-9b0c-c0149abdaab0",
  "requestedBy": "string",
  "requestedFor": "string",
  "createdBy": "string",
  "requestAssignedToPersonId": "48a43ab1-c57f-4d99-818d-d3d65ddbcc7a",
  "handledBy": "string",
  "customer": "string",
  "country": "string",
  "sla": {
    "targetCompletion": "2019-08-24T14:15:22Z",
    "targetResponse": "2019-08-24T14:15:22Z",
    "targetAttend": "2019-08-24T14:15:22Z"
  },
  "creator": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string"
  },
  "owner": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string"
  },
  "requester": {
    "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
    "fullName": "string"
  },
  "attachments": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "mimeType": "string",
    "extension": "string",
    "type": "string",
    "status": "string",
    "storageAccount": "string",
    "container": "string",
    "fileMd5": "string"
  },
  "completionDate": "2019-08-24T14:15:22Z",
  "numberOfWorkOrders": 0,
  "workOrderId": "string",
  "requestFlagDto": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "flagId": "8872ed4e-aef3-4929-9fcf-2d71741365e7",
      "flaggedBy": "fbe6f7bc-8b40-48d7-9978-e02d8e9c1194",
      "flaggedDate": "2019-08-24T14:15:22Z",
      "unflagId": "2154f209-e227-4c60-8d2b-682a485dd185",
      "unflaggedBy": "5e393d41-bbbd-446e-a1d6-1938deccfa87",
      "unflaggedDate": "2019-08-24T14:15:22Z"
    }
  ],
  "statusHistoryDto": [
    {
      "statusDescription": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "changeDate": "2019-08-24T14:15:22Z",
      "changeBy": "c57f8a44-1f34-4bac-84ad-cdc85969102f",
      "changeByName": "84362505-2459-4705-b575-dc9c5f205c1c"
    }
  ],
  "isFlagged": true,
  "isPrivate": true,
  "isWatching": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|reportedDate|string(date-time)|false|none|none|
|alternateId|string|false|none|none|
|requestDescription|string|false|none|none|
|locationId|string(uuid)|false|none|none|
|locationPath|string|false|none|none|
|positionId|string(uuid)|false|none|none|
|serviceClassificationId|string(uuid)|false|none|none|
|serviceClassificationDescription|string|false|none|none|
|serviceClassificationAliasId|string|false|none|none|
|serviceClassificationAliasDescription|string|false|none|none|
|flaggedReason|[string]|false|none|none|
|flagType|string|false|none|none|
|flagId|[string]|false|none|none|
|flaggedDate|string(date-time)|false|none|none|
|priorityId|string(uuid)|false|none|none|
|priorityDescription|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|statusDescription|string|false|none|none|
|subStatusId|string(uuid)|false|none|none|
|subStatusDescription|string|false|none|none|
|requestCreateDate|string(date-time)|false|none|none|
|requestCreateBy|string(uuid)|false|none|none|
|requestModifiedBy|string(uuid)|false|none|none|
|requestModifiedDate|string(date-time)|false|none|none|
|requestLastViewedDate|string(date-time)|false|none|none|
|requestSource|string|false|none|none|
|teamId|string(uuid)|false|none|none|
|teamName|string|false|none|none|
|watcherPersonId|string(uuid)|false|none|none|
|locationName|string|false|none|none|
|locationServiceAddress|string|false|none|none|
|locationTimezone|string|false|none|none|
|ownerPersonId|string(uuid)|false|none|none|
|requestedBy|string|false|none|none|
|requestedFor|string|false|none|none|
|createdBy|string|false|none|none|
|requestAssignedToPersonId|string(uuid)|false|none|none|
|handledBy|string|false|none|none|
|customer|string|false|none|none|
|country|string|false|none|none|
|sla|[SLADto](#schemasladto)|false|none|none|
|creator|[CreatorDto](#schemacreatordto)|false|none|none|
|owner|[OwnerDto](#schemaownerdto)|false|none|none|
|requester|[RequesterDto](#schemarequesterdto)|false|none|none|
|attachments|[AttachmentDto](#schemaattachmentdto)|false|none|none|
|completionDate|string(date-time)|false|none|none|
|numberOfWorkOrders|integer(int64)|false|none|none|
|workOrderId|string|false|none|none|
|requestFlagDto|[[RequestFlagDto](#schemarequestflagdto)]|false|none|none|
|statusHistoryDto|[[StatusHistoryDto](#schemastatushistorydto)]|false|none|none|
|isFlagged|boolean|false|none|none|
|isPrivate|boolean|false|none|none|
|isWatching|boolean|false|none|none|

<h2 id="tocS_RequesterDto">RequesterDto</h2>
<!-- backwards compatibility -->
<a id="schemarequesterdto"></a>
<a id="schema_RequesterDto"></a>
<a id="tocSrequesterdto"></a>
<a id="tocsrequesterdto"></a>

```json
{
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "fullName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string(uuid)|false|none|none|
|fullName|string|false|none|none|

<h2 id="tocS_SLADto">SLADto</h2>
<!-- backwards compatibility -->
<a id="schemasladto"></a>
<a id="schema_SLADto"></a>
<a id="tocSsladto"></a>
<a id="tocssladto"></a>

```json
{
  "targetCompletion": "2019-08-24T14:15:22Z",
  "targetResponse": "2019-08-24T14:15:22Z",
  "targetAttend": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|targetCompletion|string(date-time)|false|none|none|
|targetResponse|string(date-time)|false|none|none|
|targetAttend|string(date-time)|false|none|none|

<h2 id="tocS_FilterColumnDto">FilterColumnDto</h2>
<!-- backwards compatibility -->
<a id="schemafiltercolumndto"></a>
<a id="schema_FilterColumnDto"></a>
<a id="tocSfiltercolumndto"></a>
<a id="tocsfiltercolumndto"></a>

```json
{
  "filterColumnId": "60d5eec6-7991-4b7b-b04f-5000b1a6fe0f",
  "dataAttribute": "string",
  "filterAttribute": "string",
  "labelAttribute": "string",
  "isHideable": true,
  "isSortable": true,
  "isFilterable": true,
  "showOnMobile": true,
  "defaultShow": true,
  "sequence": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|filterColumnId|string(uuid)|false|none|none|
|dataAttribute|string|false|none|none|
|filterAttribute|string|false|none|none|
|labelAttribute|string|false|none|none|
|isHideable|boolean|false|none|none|
|isSortable|boolean|false|none|none|
|isFilterable|boolean|false|none|none|
|showOnMobile|boolean|false|none|none|
|defaultShow|boolean|false|none|none|
|sequence|integer(int32)|false|none|none|

<h2 id="tocS_FilterDto">FilterDto</h2>
<!-- backwards compatibility -->
<a id="schemafilterdto"></a>
<a id="schema_FilterDto"></a>
<a id="tocSfilterdto"></a>
<a id="tocsfilterdto"></a>

```json
{
  "filterId": "aff0ee0f-f371-4b82-82c6-dc3b96f05c91",
  "filterName": "string",
  "recordCount": 0,
  "isOrgEnabled": true,
  "isTableFilterEnabled": true,
  "sequence": 0,
  "filterColumns": [
    {
      "filterColumnId": "60d5eec6-7991-4b7b-b04f-5000b1a6fe0f",
      "dataAttribute": "string",
      "filterAttribute": "string",
      "labelAttribute": "string",
      "isHideable": true,
      "isSortable": true,
      "isFilterable": true,
      "showOnMobile": true,
      "defaultShow": true,
      "sequence": 0
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|filterId|string(uuid)|false|none|none|
|filterName|string|false|none|none|
|recordCount|integer(int32)|false|none|none|
|isOrgEnabled|boolean|false|none|none|
|isTableFilterEnabled|boolean|false|none|none|
|sequence|integer(int32)|false|none|none|
|filterColumns|[[FilterColumnDto](#schemafiltercolumndto)]|false|none|none|

<h2 id="tocS_RequestCommentsDto">RequestCommentsDto</h2>
<!-- backwards compatibility -->
<a id="schemarequestcommentsdto"></a>
<a id="schema_RequestCommentsDto"></a>
<a id="tocSrequestcommentsdto"></a>
<a id="tocsrequestcommentsdto"></a>

```json
{
  "comments": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "comment": "string",
      "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
      "commentType": "SUPPORTING_INFORMATION",
      "createdDate": "2019-08-24T14:15:22Z",
      "author": "32ad2cdb-22a2-48aa-a42c-1c53a9afc4bd",
      "authorName": "string",
      "authorInitials": "string",
      "authorType": "string",
      "sourceApp": "string",
      "organizationType": "string",
      "linkedWorkOrderComment": "097e27f3-3d11-4683-982f-92dbf558862a",
      "commentSource": "COMMENT"
    }
  ],
  "userCanAddComment": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|comments|[[CommentDto](#schemacommentdto)]|false|none|none|
|userCanAddComment|boolean|false|none|none|

<h2 id="tocS_QuickRequestConfigurationDTO">QuickRequestConfigurationDTO</h2>
<!-- backwards compatibility -->
<a id="schemaquickrequestconfigurationdto"></a>
<a id="schema_QuickRequestConfigurationDTO"></a>
<a id="tocSquickrequestconfigurationdto"></a>
<a id="tocsquickrequestconfigurationdto"></a>

```json
{
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "serviceClassifications": [
    {
      "sequence": 0,
      "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
      "description": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|orgs|[string]|false|none|none|
|serviceClassifications|[[QuickRequestServiceClassifications](#schemaquickrequestserviceclassifications)]|false|none|none|

<h2 id="tocS_QuickRequestResponseDTO">QuickRequestResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemaquickrequestresponsedto"></a>
<a id="schema_QuickRequestResponseDTO"></a>
<a id="tocSquickrequestresponsedto"></a>
<a id="tocsquickrequestresponsedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "tenantId": "string",
  "personId": "string",
  "appSynonym": "string",
  "configurationName": "string",
  "configurationType": "string",
  "configuration": [
    {
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "serviceClassifications": [
        {
          "sequence": 0,
          "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
          "description": "string"
        }
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|tenantId|string|false|none|none|
|personId|string|false|none|none|
|appSynonym|string|false|none|none|
|configurationName|string|false|none|none|
|configurationType|string|false|none|none|
|configuration|[[QuickRequestConfigurationDTO](#schemaquickrequestconfigurationdto)]|false|none|none|

<h2 id="tocS_QuickRequestServiceClassifications">QuickRequestServiceClassifications</h2>
<!-- backwards compatibility -->
<a id="schemaquickrequestserviceclassifications"></a>
<a id="schema_QuickRequestServiceClassifications"></a>
<a id="tocSquickrequestserviceclassifications"></a>
<a id="tocsquickrequestserviceclassifications"></a>

```json
{
  "sequence": 0,
  "serviceClassificationId": "87fdd3ad-cc8e-45f0-a94e-ba1649898e16",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sequence|integer(int32)|false|none|none|
|serviceClassificationId|string(uuid)|false|none|none|
|description|string|false|none|none|

<h2 id="tocS_AssetDTO">AssetDTO</h2>
<!-- backwards compatibility -->
<a id="schemaassetdto"></a>
<a id="schema_AssetDTO"></a>
<a id="tocSassetdto"></a>
<a id="tocsassetdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "description": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusAlternateId": "string",
  "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
  "operatingStatusAlternateId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|description|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|statusAlternateId|string|false|none|none|
|operatingStatusId|string(uuid)|false|none|none|
|operatingStatusAlternateId|string|false|none|none|

<h2 id="tocS_AssetForeignDomainValueDTO">AssetForeignDomainValueDTO</h2>
<!-- backwards compatibility -->
<a id="schemaassetforeigndomainvaluedto"></a>
<a id="schema_AssetForeignDomainValueDTO"></a>
<a id="tocSassetforeigndomainvaluedto"></a>
<a id="tocsassetforeigndomainvaluedto"></a>

```json
{
  "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
  "position": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "alternateId": "string",
    "orgs": [
      "497f6eca-6276-4993-bfeb-53cbbbba6f08"
    ],
    "tenantId": "string",
    "name": "string",
    "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
    "statusAlternateId": "string",
    "inService": true,
    "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
    "operatingStatusAlternateId": "string",
    "positionTypeId": "28be1d2f-064d-4eda-835a-245a27f4958d",
    "positionTypeAlternateId": "string",
    "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
    "locationAlternateId": "string",
    "modifiedDate": "2019-08-24T14:15:22Z",
    "changeTag": "08e41d67-c4c4-44b2-9f35-2ff22bd5d23b",
    "attributes": [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "orgs": [
          "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        ],
        "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
        "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
        "classSpecStructureName": "string",
        "classSpecStructureType": "string",
        "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
        "attributeAlternateId": "string",
        "attributeName": "string",
        "attributeValue": "string",
        "useInCharts": true,
        "chartFieldName": "string",
        "isPrivate": true
      }
    ],
    "asset": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "tenantId": "string",
      "description": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "statusAlternateId": "string",
      "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
      "operatingStatusAlternateId": "string"
    },
    "assetForeignDomainValues": [
      {
        "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
        "position": {},
        "source": "string",
        "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
        "reference": "string",
        "name": "string",
        "useInCharts": true,
        "chartFieldName": "string"
      }
    ]
  },
  "source": "string",
  "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
  "reference": "string",
  "name": "string",
  "useInCharts": true,
  "chartFieldName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|assetId|string(uuid)|false|none|none|
|position|[PositionDTO](#schemapositiondto)|false|none|none|
|source|string|false|none|none|
|referenceId|string(uuid)|false|none|none|
|reference|string|false|none|none|
|name|string|false|none|none|
|useInCharts|boolean|false|none|none|
|chartFieldName|string|false|none|none|

<h2 id="tocS_PagePositionDTO">PagePositionDTO</h2>
<!-- backwards compatibility -->
<a id="schemapagepositiondto"></a>
<a id="schema_PagePositionDTO"></a>
<a id="tocSpagepositiondto"></a>
<a id="tocspagepositiondto"></a>

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "tenantId": "string",
      "name": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "statusAlternateId": "string",
      "inService": true,
      "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
      "operatingStatusAlternateId": "string",
      "positionTypeId": "28be1d2f-064d-4eda-835a-245a27f4958d",
      "positionTypeAlternateId": "string",
      "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
      "locationAlternateId": "string",
      "modifiedDate": "2019-08-24T14:15:22Z",
      "changeTag": "08e41d67-c4c4-44b2-9f35-2ff22bd5d23b",
      "attributes": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "orgs": [
            "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          ],
          "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
          "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
          "classSpecStructureName": "string",
          "classSpecStructureType": "string",
          "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
          "attributeAlternateId": "string",
          "attributeName": "string",
          "attributeValue": "string",
          "useInCharts": true,
          "chartFieldName": "string",
          "isPrivate": true
        }
      ],
      "asset": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "alternateId": "string",
        "orgs": [
          "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        ],
        "tenantId": "string",
        "description": "string",
        "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
        "statusAlternateId": "string",
        "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
        "operatingStatusAlternateId": "string"
      },
      "assetForeignDomainValues": [
        {
          "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
          "position": {},
          "source": "string",
          "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
          "reference": "string",
          "name": "string",
          "useInCharts": true,
          "chartFieldName": "string"
        }
      ]
    }
  ],
  "number": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": {
      "empty": true,
      "unsorted": true,
      "sorted": true
    },
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "first": true,
  "last": true,
  "empty": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalPages|integer(int32)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|size|integer(int32)|false|none|none|
|content|[[PositionDTO](#schemapositiondto)]|false|none|none|
|number|integer(int32)|false|none|none|
|sort|[SortObject](#schemasortobject)|false|none|none|
|numberOfElements|integer(int32)|false|none|none|
|pageable|[PageableObject](#schemapageableobject)|false|none|none|
|first|boolean|false|none|none|
|last|boolean|false|none|none|
|empty|boolean|false|none|none|

<h2 id="tocS_PositionAttributeDTO">PositionAttributeDTO</h2>
<!-- backwards compatibility -->
<a id="schemapositionattributedto"></a>
<a id="schema_PositionAttributeDTO"></a>
<a id="tocSpositionattributedto"></a>
<a id="tocspositionattributedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
  "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
  "classSpecStructureName": "string",
  "classSpecStructureType": "string",
  "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
  "attributeAlternateId": "string",
  "attributeName": "string",
  "attributeValue": "string",
  "useInCharts": true,
  "chartFieldName": "string",
  "isPrivate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|classSpecId|string(uuid)|false|none|none|
|classSpecStructureId|string(uuid)|false|none|none|
|classSpecStructureName|string|false|none|none|
|classSpecStructureType|string|false|none|none|
|attributeId|string(uuid)|false|none|none|
|attributeAlternateId|string|false|none|none|
|attributeName|string|false|none|none|
|attributeValue|string|false|none|none|
|useInCharts|boolean|false|none|none|
|chartFieldName|string|false|none|none|
|isPrivate|boolean|false|none|none|

<h2 id="tocS_PositionDTO">PositionDTO</h2>
<!-- backwards compatibility -->
<a id="schemapositiondto"></a>
<a id="schema_PositionDTO"></a>
<a id="tocSpositiondto"></a>
<a id="tocspositiondto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "name": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusAlternateId": "string",
  "inService": true,
  "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
  "operatingStatusAlternateId": "string",
  "positionTypeId": "28be1d2f-064d-4eda-835a-245a27f4958d",
  "positionTypeAlternateId": "string",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "locationAlternateId": "string",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "changeTag": "08e41d67-c4c4-44b2-9f35-2ff22bd5d23b",
  "attributes": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
      "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
      "classSpecStructureName": "string",
      "classSpecStructureType": "string",
      "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
      "attributeAlternateId": "string",
      "attributeName": "string",
      "attributeValue": "string",
      "useInCharts": true,
      "chartFieldName": "string",
      "isPrivate": true
    }
  ],
  "asset": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "alternateId": "string",
    "orgs": [
      "497f6eca-6276-4993-bfeb-53cbbbba6f08"
    ],
    "tenantId": "string",
    "description": "string",
    "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
    "statusAlternateId": "string",
    "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
    "operatingStatusAlternateId": "string"
  },
  "assetForeignDomainValues": [
    {
      "assetId": "9179b887-04ef-4ce5-ab3a-b5bbd39ea3c8",
      "position": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "alternateId": "string",
        "orgs": [
          "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        ],
        "tenantId": "string",
        "name": "string",
        "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
        "statusAlternateId": "string",
        "inService": true,
        "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
        "operatingStatusAlternateId": "string",
        "positionTypeId": "28be1d2f-064d-4eda-835a-245a27f4958d",
        "positionTypeAlternateId": "string",
        "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
        "locationAlternateId": "string",
        "modifiedDate": "2019-08-24T14:15:22Z",
        "changeTag": "08e41d67-c4c4-44b2-9f35-2ff22bd5d23b",
        "attributes": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "orgs": [
              "497f6eca-6276-4993-bfeb-53cbbbba6f08"
            ],
            "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
            "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
            "classSpecStructureName": "string",
            "classSpecStructureType": "string",
            "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
            "attributeAlternateId": "string",
            "attributeName": "string",
            "attributeValue": "string",
            "useInCharts": true,
            "chartFieldName": "string",
            "isPrivate": true
          }
        ],
        "asset": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "alternateId": "string",
          "orgs": [
            "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          ],
          "tenantId": "string",
          "description": "string",
          "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
          "statusAlternateId": "string",
          "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
          "operatingStatusAlternateId": "string"
        },
        "assetForeignDomainValues": []
      },
      "source": "string",
      "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
      "reference": "string",
      "name": "string",
      "useInCharts": true,
      "chartFieldName": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|name|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|statusAlternateId|string|false|none|none|
|inService|boolean|false|none|none|
|operatingStatusId|string(uuid)|false|none|none|
|operatingStatusAlternateId|string|false|none|none|
|positionTypeId|string(uuid)|false|none|none|
|positionTypeAlternateId|string|false|none|none|
|locationId|string(uuid)|false|none|none|
|locationAlternateId|string|false|none|none|
|modifiedDate|string(date-time)|false|none|none|
|changeTag|string(uuid)|false|none|none|
|attributes|[[PositionAttributeDTO](#schemapositionattributedto)]|false|none|none|
|asset|[AssetDTO](#schemaassetdto)|false|none|none|
|assetForeignDomainValues|[[AssetForeignDomainValueDTO](#schemaassetforeigndomainvaluedto)]|false|none|none|

<h2 id="tocS_LocationAddressDTO">LocationAddressDTO</h2>
<!-- backwards compatibility -->
<a id="schemalocationaddressdto"></a>
<a id="schema_LocationAddressDTO"></a>
<a id="tocSlocationaddressdto"></a>
<a id="tocslocationaddressdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "name": "string",
  "region": "string",
  "type": "string",
  "latitude": "string",
  "longitude": "string",
  "addressLine1": "string",
  "addressLine2": "string",
  "addressLine3": "string",
  "addressLine4": "string",
  "city": "string",
  "country": "string",
  "postalCode": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|name|string|false|none|none|
|region|string|false|none|none|
|type|string|false|none|none|
|latitude|string|false|none|none|
|longitude|string|false|none|none|
|addressLine1|string|false|none|none|
|addressLine2|string|false|none|none|
|addressLine3|string|false|none|none|
|addressLine4|string|false|none|none|
|city|string|false|none|none|
|country|string|false|none|none|
|postalCode|string|false|none|none|

<h2 id="tocS_LocationAttributeDTO">LocationAttributeDTO</h2>
<!-- backwards compatibility -->
<a id="schemalocationattributedto"></a>
<a id="schema_LocationAttributeDTO"></a>
<a id="tocSlocationattributedto"></a>
<a id="tocslocationattributedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
  "attributeAlternateId": "string",
  "attributeName": "string",
  "attributeValue": "string",
  "useInCharts": true,
  "chartFieldName": "string",
  "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
  "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
  "classSpecStructureName": "string",
  "domainId": "8a0b02c3-fdd8-452e-bc6e-ef07a335ec7e",
  "domainTranslation": "string",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "isPrivate": true,
  "isMandatory": true,
  "isReadOnly": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|attributeId|string(uuid)|false|none|none|
|attributeAlternateId|string|false|none|none|
|attributeName|string|false|none|none|
|attributeValue|string|false|none|none|
|useInCharts|boolean|false|none|none|
|chartFieldName|string|false|none|none|
|classSpecId|string(uuid)|false|none|none|
|classSpecStructureId|string(uuid)|false|none|none|
|classSpecStructureName|string|false|none|none|
|domainId|string(uuid)|false|none|none|
|domainTranslation|string|false|none|none|
|locationId|string(uuid)|false|none|none|
|isPrivate|boolean|false|none|none|
|isMandatory|boolean|false|none|none|
|isReadOnly|boolean|false|none|none|

<h2 id="tocS_LocationChartFieldDTO">LocationChartFieldDTO</h2>
<!-- backwards compatibility -->
<a id="schemalocationchartfielddto"></a>
<a id="schema_LocationChartFieldDTO"></a>
<a id="tocSlocationchartfielddto"></a>
<a id="tocslocationchartfielddto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "isInherited": true,
  "chartFieldName": "string",
  "chartType": "string",
  "value": "string",
  "isPrivate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|isInherited|boolean|false|none|none|
|chartFieldName|string|false|none|none|
|chartType|string|false|none|none|
|value|string|false|none|none|
|isPrivate|boolean|false|none|none|

<h2 id="tocS_LocationDTO">LocationDTO</h2>
<!-- backwards compatibility -->
<a id="schemalocationdto"></a>
<a id="schema_LocationDTO"></a>
<a id="tocSlocationdto"></a>
<a id="tocslocationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "alternateId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "tenantId": "string",
  "name": "string",
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "statusAlternateId": "string",
  "typeId": "caab7c42-4ce7-4bd5-bbab-6017cec730b7",
  "typeAlternateId": "string",
  "functionId": "88c30c0d-0919-4072-a552-9669be152724",
  "functionAlternateId": "string",
  "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
  "operatingStatusAlternateId": "string",
  "serviceStatus": true,
  "timeZone": "string",
  "parentId": "70850378-7d3c-4f45-91b7-942d4dfbbd43",
  "parentAlternateId": "string",
  "structureId": "0e8c4ba3-b757-4e4a-9e0e-448fab22d027",
  "structureRuleId": "9a1bb58f-c83b-4c6d-bc24-fceecef4d68c",
  "formattedAddress": "string",
  "locationPath": "string",
  "legacyLocationPath": "string",
  "modifiedDate": "2019-08-24T14:15:22Z",
  "changeTag": "string",
  "hasChildren": true,
  "hasParent": true,
  "childrenCount": 0,
  "serviceAddress": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "alternateId": "string",
    "name": "string",
    "region": "string",
    "type": "string",
    "latitude": "string",
    "longitude": "string",
    "addressLine1": "string",
    "addressLine2": "string",
    "addressLine3": "string",
    "addressLine4": "string",
    "city": "string",
    "country": "string",
    "postalCode": "string"
  },
  "attributes": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
      "attributeAlternateId": "string",
      "attributeName": "string",
      "attributeValue": "string",
      "useInCharts": true,
      "chartFieldName": "string",
      "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
      "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
      "classSpecStructureName": "string",
      "domainId": "8a0b02c3-fdd8-452e-bc6e-ef07a335ec7e",
      "domainTranslation": "string",
      "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
      "isPrivate": true,
      "isMandatory": true,
      "isReadOnly": true
    }
  ],
  "foreignReferences": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
      "source": "string",
      "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
      "reference": "string",
      "name": "string",
      "useInCharts": true,
      "chartFieldName": "string"
    }
  ],
  "chartFields": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "isInherited": true,
      "chartFieldName": "string",
      "chartType": "string",
      "value": "string",
      "isPrivate": true
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|orgs|[string]|false|none|none|
|tenantId|string|false|none|none|
|name|string|false|none|none|
|statusId|string(uuid)|false|none|none|
|statusAlternateId|string|false|none|none|
|typeId|string(uuid)|false|none|none|
|typeAlternateId|string|false|none|none|
|functionId|string(uuid)|false|none|none|
|functionAlternateId|string|false|none|none|
|operatingStatusId|string(uuid)|false|none|none|
|operatingStatusAlternateId|string|false|none|none|
|serviceStatus|boolean|false|none|none|
|timeZone|string|false|none|none|
|parentId|string(uuid)|false|none|none|
|parentAlternateId|string|false|none|none|
|structureId|string(uuid)|false|none|none|
|structureRuleId|string(uuid)|false|none|none|
|formattedAddress|string|false|none|none|
|locationPath|string|false|none|none|
|legacyLocationPath|string|false|none|none|
|modifiedDate|string(date-time)|false|none|none|
|changeTag|string|false|none|none|
|hasChildren|boolean|false|none|none|
|hasParent|boolean|false|write-only|none|
|childrenCount|integer(int32)|false|write-only|none|
|serviceAddress|[LocationAddressDTO](#schemalocationaddressdto)|false|none|none|
|attributes|[[LocationAttributeDTO](#schemalocationattributedto)]|false|none|none|
|foreignReferences|[[LocationForeignReferenceDTO](#schemalocationforeignreferencedto)]|false|none|none|
|chartFields|[[LocationChartFieldDTO](#schemalocationchartfielddto)]|false|none|none|

<h2 id="tocS_LocationForeignReferenceDTO">LocationForeignReferenceDTO</h2>
<!-- backwards compatibility -->
<a id="schemalocationforeignreferencedto"></a>
<a id="schema_LocationForeignReferenceDTO"></a>
<a id="tocSlocationforeignreferencedto"></a>
<a id="tocslocationforeignreferencedto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
  "source": "string",
  "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
  "reference": "string",
  "name": "string",
  "useInCharts": true,
  "chartFieldName": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|locationId|string(uuid)|false|none|none|
|source|string|false|none|none|
|referenceId|string(uuid)|false|none|none|
|reference|string|false|none|none|
|name|string|false|none|none|
|useInCharts|boolean|false|none|none|
|chartFieldName|string|false|none|none|

<h2 id="tocS_PageLocationDTO">PageLocationDTO</h2>
<!-- backwards compatibility -->
<a id="schemapagelocationdto"></a>
<a id="schema_PageLocationDTO"></a>
<a id="tocSpagelocationdto"></a>
<a id="tocspagelocationdto"></a>

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "tenantId": "string",
      "name": "string",
      "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
      "statusAlternateId": "string",
      "typeId": "caab7c42-4ce7-4bd5-bbab-6017cec730b7",
      "typeAlternateId": "string",
      "functionId": "88c30c0d-0919-4072-a552-9669be152724",
      "functionAlternateId": "string",
      "operatingStatusId": "a5a0bc31-892c-49de-b3a7-af1471f167e3",
      "operatingStatusAlternateId": "string",
      "serviceStatus": true,
      "timeZone": "string",
      "parentId": "70850378-7d3c-4f45-91b7-942d4dfbbd43",
      "parentAlternateId": "string",
      "structureId": "0e8c4ba3-b757-4e4a-9e0e-448fab22d027",
      "structureRuleId": "9a1bb58f-c83b-4c6d-bc24-fceecef4d68c",
      "formattedAddress": "string",
      "locationPath": "string",
      "legacyLocationPath": "string",
      "modifiedDate": "2019-08-24T14:15:22Z",
      "changeTag": "string",
      "hasChildren": true,
      "hasParent": true,
      "childrenCount": 0,
      "serviceAddress": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "alternateId": "string",
        "name": "string",
        "region": "string",
        "type": "string",
        "latitude": "string",
        "longitude": "string",
        "addressLine1": "string",
        "addressLine2": "string",
        "addressLine3": "string",
        "addressLine4": "string",
        "city": "string",
        "country": "string",
        "postalCode": "string"
      },
      "attributes": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "orgs": [
            "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          ],
          "attributeId": "4373db18-af63-40d4-ad40-80a2c734bfcf",
          "attributeAlternateId": "string",
          "attributeName": "string",
          "attributeValue": "string",
          "useInCharts": true,
          "chartFieldName": "string",
          "classSpecId": "31153590-236a-405c-a39b-44c7795d09a9",
          "classSpecStructureId": "9cf1a78e-d167-40fd-9f83-3c4f76637f29",
          "classSpecStructureName": "string",
          "domainId": "8a0b02c3-fdd8-452e-bc6e-ef07a335ec7e",
          "domainTranslation": "string",
          "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
          "isPrivate": true,
          "isMandatory": true,
          "isReadOnly": true
        }
      ],
      "foreignReferences": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "locationId": "1a5515a3-ba81-4a42-aee7-ad9ffc090a54",
          "source": "string",
          "referenceId": "8502eb05-558d-4480-8511-c1011710b340",
          "reference": "string",
          "name": "string",
          "useInCharts": true,
          "chartFieldName": "string"
        }
      ],
      "chartFields": [
        {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "orgs": [
            "497f6eca-6276-4993-bfeb-53cbbbba6f08"
          ],
          "isInherited": true,
          "chartFieldName": "string",
          "chartType": "string",
          "value": "string",
          "isPrivate": true
        }
      ]
    }
  ],
  "number": 0,
  "sort": {
    "empty": true,
    "unsorted": true,
    "sorted": true
  },
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": {
      "empty": true,
      "unsorted": true,
      "sorted": true
    },
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "first": true,
  "last": true,
  "empty": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalPages|integer(int32)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|size|integer(int32)|false|none|none|
|content|[[LocationDTO](#schemalocationdto)]|false|none|none|
|number|integer(int32)|false|none|none|
|sort|[SortObject](#schemasortobject)|false|none|none|
|numberOfElements|integer(int32)|false|none|none|
|pageable|[PageableObject](#schemapageableobject)|false|none|none|
|first|boolean|false|none|none|
|last|boolean|false|none|none|
|empty|boolean|false|none|none|

<h2 id="tocS_AggregatedDataDTORequestStatusExtendedPropertiesDTO">AggregatedDataDTORequestStatusExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemaaggregateddatadtorequeststatusextendedpropertiesdto"></a>
<a id="schema_AggregatedDataDTORequestStatusExtendedPropertiesDTO"></a>
<a id="tocSaggregateddatadtorequeststatusextendedpropertiesdto"></a>
<a id="tocsaggregateddatadtorequeststatusextendedpropertiesdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "description": "string",
  "extendedProperties": {
    "friendlyTitle": "string",
    "friendlySubtitle": "string",
    "alternateId": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|description|string|false|none|none|
|extendedProperties|[RequestStatusExtendedPropertiesDTO](#schemarequeststatusextendedpropertiesdto)|false|none|none|

<h2 id="tocS_AggregatedDataDTORequestSubStatusExtendedPropertiesDTO">AggregatedDataDTORequestSubStatusExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemaaggregateddatadtorequestsubstatusextendedpropertiesdto"></a>
<a id="schema_AggregatedDataDTORequestSubStatusExtendedPropertiesDTO"></a>
<a id="tocSaggregateddatadtorequestsubstatusextendedpropertiesdto"></a>
<a id="tocsaggregateddatadtorequestsubstatusextendedpropertiesdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "description": "string",
  "extendedProperties": {
    "friendlyTitle": "string",
    "friendlySubtitle": "string",
    "canTransitionTo": [
      "497f6eca-6276-4993-bfeb-53cbbbba6f08"
    ],
    "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
    "alternateId": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|description|string|false|none|none|
|extendedProperties|[RequestSubStatusExtendedPropertiesDTO](#schemarequestsubstatusextendedpropertiesdto)|false|none|none|

<h2 id="tocS_AggregatedDataResponseDTO">AggregatedDataResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemaaggregateddataresponsedto"></a>
<a id="schema_AggregatedDataResponseDTO"></a>
<a id="tocSaggregateddataresponsedto"></a>
<a id="tocsaggregateddataresponsedto"></a>

```json
{
  "locale": "string",
  "requestStatuses": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "description": "string",
      "extendedProperties": {
        "friendlyTitle": "string",
        "friendlySubtitle": "string",
        "alternateId": "string"
      }
    }
  ],
  "requestSubStatuses": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "description": "string",
      "extendedProperties": {
        "friendlyTitle": "string",
        "friendlySubtitle": "string",
        "canTransitionTo": [
          "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        ],
        "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
        "alternateId": "string"
      }
    }
  ],
  "flagTypes": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "manualFlag": true,
      "isFlaggedReason": true,
      "systemFlag": true,
      "locale": "string",
      "orderSeq": 0,
      "unflagManually": true
    }
  ],
  "commentReasons": [
    {
      "alternateId": "string",
      "description": "string"
    }
  ],
  "serviceDescriptionCharLimit": "string",
  "requestCommentCharLimit": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|locale|string|false|none|none|
|requestStatuses|[[AggregatedDataDTORequestStatusExtendedPropertiesDTO](#schemaaggregateddatadtorequeststatusextendedpropertiesdto)]|false|none|none|
|requestSubStatuses|[[AggregatedDataDTORequestSubStatusExtendedPropertiesDTO](#schemaaggregateddatadtorequestsubstatusextendedpropertiesdto)]|false|none|none|
|flagTypes|[[FlagTypeDTO](#schemaflagtypedto)]|false|none|none|
|commentReasons|[[CommentReasonDTO](#schemacommentreasondto)]|false|none|none|
|serviceDescriptionCharLimit|string|false|none|none|
|requestCommentCharLimit|string|false|none|none|

<h2 id="tocS_CommentReasonDTO">CommentReasonDTO</h2>
<!-- backwards compatibility -->
<a id="schemacommentreasondto"></a>
<a id="schema_CommentReasonDTO"></a>
<a id="tocScommentreasondto"></a>
<a id="tocscommentreasondto"></a>

```json
{
  "alternateId": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|alternateId|string|false|none|none|
|description|string|false|none|none|

<h2 id="tocS_RequestStatusExtendedPropertiesDTO">RequestStatusExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequeststatusextendedpropertiesdto"></a>
<a id="schema_RequestStatusExtendedPropertiesDTO"></a>
<a id="tocSrequeststatusextendedpropertiesdto"></a>
<a id="tocsrequeststatusextendedpropertiesdto"></a>

```json
{
  "friendlyTitle": "string",
  "friendlySubtitle": "string",
  "alternateId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|friendlyTitle|string|false|none|none|
|friendlySubtitle|string|false|none|none|
|alternateId|string|false|none|none|

<h2 id="tocS_RequestSubStatusExtendedPropertiesDTO">RequestSubStatusExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestsubstatusextendedpropertiesdto"></a>
<a id="schema_RequestSubStatusExtendedPropertiesDTO"></a>
<a id="tocSrequestsubstatusextendedpropertiesdto"></a>
<a id="tocsrequestsubstatusextendedpropertiesdto"></a>

```json
{
  "friendlyTitle": "string",
  "friendlySubtitle": "string",
  "canTransitionTo": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
  "alternateId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|friendlyTitle|string|false|none|none|
|friendlySubtitle|string|false|none|none|
|canTransitionTo|[string]|false|none|none|
|statusId|string(uuid)|false|none|none|
|alternateId|string|false|none|none|

<h2 id="tocS_AggregatedDataOrgSpecificResponseDTO">AggregatedDataOrgSpecificResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemaaggregateddataorgspecificresponsedto"></a>
<a id="schema_AggregatedDataOrgSpecificResponseDTO"></a>
<a id="tocSaggregateddataorgspecificresponsedto"></a>
<a id="tocsaggregateddataorgspecificresponsedto"></a>

```json
{
  "serviceDescriptionCharLimit": "string",
  "requestCommentCharLimit": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serviceDescriptionCharLimit|string|false|none|none|
|requestCommentCharLimit|string|false|none|none|

<h2 id="tocS_AggregatedDataAppResponseDTO">AggregatedDataAppResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemaaggregateddataappresponsedto"></a>
<a id="schema_AggregatedDataAppResponseDTO"></a>
<a id="tocSaggregateddataappresponsedto"></a>
<a id="tocsaggregateddataappresponsedto"></a>

```json
{
  "locale": "string",
  "requestStatuses": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "description": "string",
      "extendedProperties": {
        "friendlyTitle": "string",
        "friendlySubtitle": "string",
        "alternateId": "string"
      }
    }
  ],
  "requestSubStatuses": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "description": "string",
      "extendedProperties": {
        "friendlyTitle": "string",
        "friendlySubtitle": "string",
        "canTransitionTo": [
          "497f6eca-6276-4993-bfeb-53cbbbba6f08"
        ],
        "statusId": "e900225c-0629-4e96-be6e-86a17a309645",
        "alternateId": "string"
      }
    }
  ],
  "flagTypes": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "alternateId": "string",
      "description": "string",
      "manualFlag": true,
      "isFlaggedReason": true,
      "systemFlag": true,
      "locale": "string",
      "orderSeq": 0,
      "unflagManually": true
    }
  ],
  "commentReasons": [
    {
      "alternateId": "string",
      "description": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|locale|string|false|none|none|
|requestStatuses|[[AggregatedDataDTORequestStatusExtendedPropertiesDTO](#schemaaggregateddatadtorequeststatusextendedpropertiesdto)]|false|none|none|
|requestSubStatuses|[[AggregatedDataDTORequestSubStatusExtendedPropertiesDTO](#schemaaggregateddatadtorequestsubstatusextendedpropertiesdto)]|false|none|none|
|flagTypes|[[FlagTypeDTO](#schemaflagtypedto)]|false|none|none|
|commentReasons|[[CommentReasonDTO](#schemacommentreasondto)]|false|none|none|

