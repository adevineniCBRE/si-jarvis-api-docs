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
includes:
  - errors
search: true
highlight_theme: darkula
headingLevel: 2

---

<!-- Generator: Widdershins v4.0.1 -->

Base URLs:

* <a href="http://localhost:8098">http://localhost:8098</a>

<h1 id="openapi-definition-request-core-controller">Request (Core)</h1>

## Update the Service Request

<a id="opIdupdateRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-core/api/v1/request/{requestId} \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{requestId}");
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
  'authorization': 'string'
}

r = requests.put('http://localhost:8098/request-core/api/v1/request/{requestId}', headers = headers)

print(r.json())

```

`PUT /request-core/api/v1/request/{requestId}`

Update the Service Request

> Body parameter

```json
{
  "id": "string",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "subStatusId": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "relatedServiceClassificationId": [
    "string"
  ],
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "startDate": "string",
  "modifiedDate": "string",
  "description": "string",
  "chart": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}
```

<h3 id="update-the-service-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|requestId|path|string|true|none|
|body|body|[RequestBodyDTO](#schemarequestbodydto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "statusCode": "string",
  "subStatusId": "string",
  "subStatusCode": "string",
  "materialsStatusId": "string",
  "materialsStatusCode": "string",
  "assignmentStatusId": "string",
  "assignmentStatusCode": "string",
  "disputeStatusId": "string",
  "disputeStatusCode": "string",
  "disputedDate": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "relatedServiceClassification": [
    "string"
  ],
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "spendLimit": 0,
  "estimatedServiceCost": 0,
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "modifiedDate": "string",
  "closedDate": "string",
  "description": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "watchLists": [
    {
      "id": "string",
      "requestId": "string",
      "user": "string",
      "createdBy": "string"
    }
  ],
  "triageStatus": "string",
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "reason": {
    "reasonCode": "string",
    "reasonDescription": "string"
  },
  "requestChain": [
    {
      "activeApprovers": [
        {
          "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
          "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
          "stepNumber": 0,
          "isDelegator": true
        }
      ],
      "chain": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "majorVersion": 0,
        "minorVersion": 0,
        "createdDate": "string",
        "updatedTime": "string",
        "source": "string",
        "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
        "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
        "capabilityTtl": "string",
        "capabilityName": "string",
        "capabilityLimit": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string",
          "unit": "string",
          "value": "string"
        },
        "chainDefinitionAlternateId": "string",
        "chainDefinitionVersion": 0,
        "orgs": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "type": "string"
          }
        ],
        "chainStatus": "InProgress",
        "approvers": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
            "personType": "string",
            "group": 0,
            "sequence": 0,
            "generalization": {
              "id": "string",
              "name": "string",
              "group": "string"
            },
            "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
            "when": "string",
            "responseCount": 0,
            "approvalRule": "string",
            "mandatory": true,
            "decision": {
              "status": "Approved",
              "decisionDate": "string",
              "madeByDelegate": true,
              "decisionNote": "string"
            },
            "personLimit": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "name": "string",
              "unit": "string",
              "value": "string"
            }
          }
        ],
        "delegates": [
          {
            "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
            "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
            "startDate": "2019-08-24T14:15:22Z",
            "endDate": "2019-08-24T14:15:22Z",
            "group": 0
          }
        ],
        "excluded": [
          {
            "excludedApprover": "string",
            "conflictCapability": {
              "id": "string",
              "name": "string"
            },
            "conflictObject": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "type": "string",
              "alternateId": "string"
            }
          }
        ],
        "isRecalculate": true
      },
      "subStateStatus": "ACTIVE",
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536"
    }
  ],
  "errorContainer": {
    "version": "string",
    "traceId": "string",
    "title": "string",
    "category": "INFO",
    "errors": [
      {
        "id": "string",
        "alternateId": "string",
        "description": "string",
        "domain": "string",
        "messages": [
          {
            "message": "string",
            "code": "string"
          }
        ]
      }
    ]
  },
  "workOwnerGroupValue": "string",
  "miscellaneous": {
    "statusChangeDate": "string",
    "slaAttendDate": "string",
    "slaCompleteDate": "string",
    "slaDispatchDate": "string",
    "slaResponseDate": "string",
    "isFlagged": true,
    "flaggedDate": "string"
  },
  "requestAuthActions": [
    {
      "name": "string",
      "additionalDetailsKey": "string",
      "additionalDetails": {
        "property1": "string",
        "property2": "string"
      }
    }
  ],
  "action": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}
```

<h3 id="update-the-service-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Service Request Updated|[RequestDTO](#schemarequestdto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[RequestDTO](#schemarequestdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[RequestDTO](#schemarequestdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[RequestDTO](#schemarequestdto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[RequestDTO](#schemarequestdto)|

<aside class="success">
This operation does not require authentication
</aside>

## Update the Extended Properties

<a id="opIdupdateExtendedProperties"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-core/api/v1/request/extendedProperties/{id} \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/extendedProperties/{id}");
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
  'authorization': 'string'
}

r = requests.put('http://localhost:8098/request-core/api/v1/request/extendedProperties/{id}', headers = headers)

print(r.json())

```

`PUT /request-core/api/v1/request/extendedProperties/{id}`

Update the Extended Properties

> Body parameter

```json
{
  "id": "string",
  "data": "string"
}
```

<h3 id="update-the-extended-properties-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|id|path|string|true|none|
|body|body|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "string",
  "data": "string"
}
```

<h3 id="update-the-extended-properties-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|

<aside class="success">
This operation does not require authentication
</aside>

## Get All Requests for given user

<a id="opIdgetRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/request?userId=string \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request?userId=string");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/request', params={
  'userId': 'string'
}, headers = headers)

print(r.json())

```

`GET /request-core/api/v1/request`

Get All Requests for given user.

<h3 id="get-all-requests-for-given-user-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|status|query|string|false|none|
|userId|query|string|true|none|
|tenantId|query|string|false|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "statusCode": "string",
  "subStatusId": "string",
  "subStatusCode": "string",
  "materialsStatusId": "string",
  "materialsStatusCode": "string",
  "assignmentStatusId": "string",
  "assignmentStatusCode": "string",
  "disputeStatusId": "string",
  "disputeStatusCode": "string",
  "disputedDate": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "relatedServiceClassification": [
    "string"
  ],
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "spendLimit": 0,
  "estimatedServiceCost": 0,
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "modifiedDate": "string",
  "closedDate": "string",
  "description": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "watchLists": [
    {
      "id": "string",
      "requestId": "string",
      "user": "string",
      "createdBy": "string"
    }
  ],
  "triageStatus": "string",
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "reason": {
    "reasonCode": "string",
    "reasonDescription": "string"
  },
  "requestChain": [
    {
      "activeApprovers": [
        {
          "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
          "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
          "stepNumber": 0,
          "isDelegator": true
        }
      ],
      "chain": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "majorVersion": 0,
        "minorVersion": 0,
        "createdDate": "string",
        "updatedTime": "string",
        "source": "string",
        "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
        "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
        "capabilityTtl": "string",
        "capabilityName": "string",
        "capabilityLimit": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string",
          "unit": "string",
          "value": "string"
        },
        "chainDefinitionAlternateId": "string",
        "chainDefinitionVersion": 0,
        "orgs": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "type": "string"
          }
        ],
        "chainStatus": "InProgress",
        "approvers": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
            "personType": "string",
            "group": 0,
            "sequence": 0,
            "generalization": {
              "id": "string",
              "name": "string",
              "group": "string"
            },
            "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
            "when": "string",
            "responseCount": 0,
            "approvalRule": "string",
            "mandatory": true,
            "decision": {
              "status": "Approved",
              "decisionDate": "string",
              "madeByDelegate": true,
              "decisionNote": "string"
            },
            "personLimit": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "name": "string",
              "unit": "string",
              "value": "string"
            }
          }
        ],
        "delegates": [
          {
            "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
            "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
            "startDate": "2019-08-24T14:15:22Z",
            "endDate": "2019-08-24T14:15:22Z",
            "group": 0
          }
        ],
        "excluded": [
          {
            "excludedApprover": "string",
            "conflictCapability": {
              "id": "string",
              "name": "string"
            },
            "conflictObject": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "type": "string",
              "alternateId": "string"
            }
          }
        ],
        "isRecalculate": true
      },
      "subStateStatus": "ACTIVE",
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536"
    }
  ],
  "errorContainer": {
    "version": "string",
    "traceId": "string",
    "title": "string",
    "category": "INFO",
    "errors": [
      {
        "id": "string",
        "alternateId": "string",
        "description": "string",
        "domain": "string",
        "messages": [
          {
            "message": "string",
            "code": "string"
          }
        ]
      }
    ]
  },
  "workOwnerGroupValue": "string",
  "miscellaneous": {
    "statusChangeDate": "string",
    "slaAttendDate": "string",
    "slaCompleteDate": "string",
    "slaDispatchDate": "string",
    "slaResponseDate": "string",
    "isFlagged": true,
    "flaggedDate": "string"
  },
  "requestAuthActions": [
    {
      "name": "string",
      "additionalDetailsKey": "string",
      "additionalDetails": {
        "property1": "string",
        "property2": "string"
      }
    }
  ],
  "action": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}
```

<h3 id="get-all-requests-for-given-user-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of Service Requests|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="get-all-requests-for-given-user-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestDTO](#schemarequestdto)]|false|none|none|
|» id|string(uuid)|false|none|none|
|» tenantId|string|false|none|none|
|» assetId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» alternateId|string|false|none|none|
|» statusId|string|false|none|none|
|» statusCode|string|false|none|none|
|» subStatusId|string|false|none|none|
|» subStatusCode|string|false|none|none|
|» materialsStatusId|string|false|none|none|
|» materialsStatusCode|string|false|none|none|
|» assignmentStatusId|string|false|none|none|
|» assignmentStatusCode|string|false|none|none|
|» disputeStatusId|string|false|none|none|
|» disputeStatusCode|string|false|none|none|
|» disputedDate|string|false|none|none|
|» createdBy|string|false|none|none|
|» modifiedBy|string|false|none|none|
|» requestorId|string|false|none|none|
|» ownerId|string|false|none|none|
|» locationId|string|false|none|none|
|» positionId|string|false|none|none|
|» serviceClassificationId|string|false|none|none|
|» relatedServiceClassification|[string]|false|none|none|
|» miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|»» serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» value|[string]|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedId|string|false|none|none|
|»» flagReason|string|false|none|none|
|» source|string|false|none|none|
|» isFlagged|boolean|false|none|none|
|» isPrivate|boolean|false|none|none|
|» priorityId|string|false|none|none|
|» watchers|[string]|false|none|none|
|» sourceApp|string|false|none|none|
|» spendLimit|number|false|none|none|
|» estimatedServiceCost|number|false|none|none|
|» lastAssessmentDate|string|false|none|none|
|» lastAssessmentTrigger|string|false|none|none|
|» createdDate|string|false|none|none|
|» reportedDate|string|false|none|none|
|» modifiedDate|string|false|none|none|
|» closedDate|string|false|none|none|
|» description|string|false|none|none|
|» charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|»» chartId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» version|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» chartName|string|false|none|none|
|»» dimensionName|string|false|none|none|
|»» dimensionPosition|string|false|none|none|
|»» dimensionValue|string|false|none|none|
|» comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|»» commentId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» addedByPersonId|string|false|none|none|
|»» source|string|false|none|none|
|»» comment|string|false|none|none|
|»» type|string|false|none|none|
|»» orgType|string|false|none|none|
|»» linkedWOCommentId|string|false|none|none|
|»» addedDate|string|false|none|none|
|»» linkedWorkOrderId|string|false|none|none|
|»» isClientViewable|boolean|false|none|none|
|» extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|»» id|string|false|none|none|
|»» data|string|false|none|none|
|» serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» name|string|false|none|none|
|»» timeAllotted|number|false|none|none|
|»» unit|string|false|none|none|
|»» targetTime|string|false|none|none|
|»» overriddenDate|string|false|none|none|
|»» overriddenReason|string|false|none|none|
|»» overriddenBy|string|false|none|none|
|»» slaMetDate|string|false|none|none|
|»» slaMetWO|string|false|none|none|
|»» slaMetDatet|string|false|write-only|none|
|» watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» user|string|false|none|none|
|»» createdBy|string|false|none|none|
|» triageStatus|string|false|none|none|
|» workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|»» id|string|false|none|none|
|»» description|string|false|none|none|
|»» alternateId|string|false|none|none|
|»» statusId|string|false|none|none|
|»» assigneeName|string|false|none|none|
|»» assignmentType|string|false|none|none|
|»» assigneeId|string|false|none|none|
|»» facilityManagerId|string|false|none|none|
|»» comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|»»» commentId|string|false|none|none|
|»»» workOrderCommentId|integer(int32)|false|none|none|
|»»» addedByPersonId|string|false|none|none|
|»»» comment|string|false|none|none|
|»»» commentType|string|false|none|none|
|»»» addedDate|string|false|none|none|
|»» slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» targetDate|string|false|none|none|
|»»» overrideDate|string|false|none|none|
|»»» overrideReason|string|false|none|none|
|»»» overrideBy|string|false|none|none|
|»»» slaMetDate|string|false|none|none|
|»»» slaMet|boolean|false|none|none|
|»» nte|number|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» dispatchSiteId|string|false|none|none|
|»» dispatchSiteName|string|false|none|none|
|»» completionDescription|string|false|none|none|
|»» requestedBy|string|false|none|none|
|»» serviceClassificationId|string|false|none|none|
|»» locationId|string|false|none|none|
|»» assetId|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» modifiedDate|string|false|none|none|
|»» assigneeIds|[string]|false|none|none|
|»» dispatchSiteIds|[string]|false|none|none|
|» statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|»» statusId|string|false|none|none|
|»» statusCode|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» updatedBy|string|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» reasonId|string|false|none|none|
|»» version|integer(int32)|false|none|none|
|» attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|»» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» mimetype|string|false|none|none|
|»»» extension|string|false|none|none|
|»»» type|string|false|none|none|
|»»» status|string|false|none|none|
|»»» tenantId|string|false|none|none|
|»»» storageAccount|string|false|none|none|
|»»» container|string|false|none|none|
|»»» fileMd5|string|false|none|none|
|»»» createdTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»»» id|string|false|none|none|
|»»» orgs|[string]|false|none|none|
|»»» objectId|string|false|none|none|
|»»» objectType|string|false|none|none|
|»»» createTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»»» description|string|false|none|none|
|» reason|[ReasonDTO](#schemareasondto)|false|none|none|
|»» reasonCode|string|false|none|none|
|»» reasonDescription|string|false|none|none|
|» requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|»» activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|»»» approverId|string(uuid)|false|none|none|
|»»» delegatorId|string(uuid)|false|none|none|
|»»» stepNumber|integer(int32)|false|none|none|
|»»» isDelegator|boolean|false|none|none|
|»» chain|[ChainDTO](#schemachaindto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» majorVersion|integer(int32)|false|none|none|
|»»» minorVersion|integer(int32)|false|none|none|
|»»» createdDate|string|false|none|none|
|»»» updatedTime|string|false|none|none|
|»»» source|string|false|none|none|
|»»» chainDefinitionId|string(uuid)|false|none|none|
|»»» capabilityId|string(uuid)|false|none|none|
|»»» capabilityTtl|string|false|none|none|
|»»» capabilityName|string|false|none|none|
|»»» capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»»» value|string|false|none|none|
|»»» chainDefinitionAlternateId|string|false|none|none|
|»»» chainDefinitionVersion|integer(int32)|false|none|none|
|»»» orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» type|string|false|none|none|
|»»» chainStatus|string|false|none|none|
|»»» approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» personId|string(uuid)|false|none|none|
|»»»» personType|string|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»»» sequence|integer(int32)|false|none|none|
|»»»» generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»»» group|string|false|none|none|
|»»»» authScopeId|string(uuid)|false|none|none|
|»»»» when|string|false|none|none|
|»»»» responseCount|integer(int32)|false|none|none|
|»»»» approvalRule|string|false|none|none|
|»»»» mandatory|boolean|false|none|none|
|»»»» decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|»»»»» status|string|false|none|none|
|»»»»» decisionDate|string|false|none|none|
|»»»»» madeByDelegate|boolean|false|none|none|
|»»»»» decisionNote|string|false|none|none|
|»»»» personLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»» delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|»»»» approver|string(uuid)|false|none|none|
|»»»» delegatedTo|string(uuid)|false|none|none|
|»»»» startDate|string(date-time)|false|none|none|
|»»»» endDate|string(date-time)|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»» excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|»»»» excludedApprover|string|false|none|none|
|»»»» conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»» conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|
|»»»»» id|string(uuid)|false|none|none|
|»»»»» type|string|false|none|none|
|»»»»» alternateId|string|false|none|none|
|»»» isRecalculate|boolean|false|none|none|
|»» subStateStatus|string|false|none|none|
|»» subStateId|string(uuid)|false|none|none|
|» errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|»» version|string|false|none|none|
|»» traceId|string|false|none|none|
|»» title|string|false|none|none|
|»» category|string|false|none|none|
|»» errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|
|»»» id|string|false|none|none|
|»»» alternateId|string|false|none|none|
|»»» description|string|false|none|none|
|»»» domain|string|false|none|none|
|»»» messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|
|»»»» message|string|false|none|none|
|»»»» code|string|false|none|none|
|» workOwnerGroupValue|string|false|none|none|
|» miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|»» statusChangeDate|string|false|none|none|
|»» slaAttendDate|string|false|none|none|
|»» slaCompleteDate|string|false|none|none|
|»» slaDispatchDate|string|false|none|none|
|»» slaResponseDate|string|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedDate|string|false|none|none|
|» requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|»» name|string|false|none|none|
|»» additionalDetailsKey|string|false|none|none|
|»» additionalDetails|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|» action|[string]|false|none|none|
|» pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|
|»» pmId|string|false|none|none|
|»» pmAlternateId|string|false|none|none|
|»» pmConfigUrl|string|false|none|none|
|»» planId|string|false|none|none|
|»» type|string|false|none|none|
|»» primaryLocationId|string|false|none|none|
|»» maintenanceFrequency|string|false|none|none|
|»» maintenanceFrequencyUnit|string|false|none|none|
|»» interval|string|false|none|none|
|»» totalSequences|string|false|none|none|
|»» sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|»»» sequence|integer(int32)|false|none|none|
|»»» locationId|string|false|none|none|
|»»» assetId|string|false|none|none|
|»»» positionId|string|false|none|none|
|»» providerId|string|false|none|none|
|»» providerType|string|false|none|none|
|»» providerReferenceId|string|false|none|none|
|»» assignmentOverride|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|
|status|Approved|
|status|Declined|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestDTO](#schemarequestdto)]|false|none|none|
|» id|string(uuid)|false|none|none|
|» tenantId|string|false|none|none|
|» assetId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» alternateId|string|false|none|none|
|» statusId|string|false|none|none|
|» statusCode|string|false|none|none|
|» subStatusId|string|false|none|none|
|» subStatusCode|string|false|none|none|
|» materialsStatusId|string|false|none|none|
|» materialsStatusCode|string|false|none|none|
|» assignmentStatusId|string|false|none|none|
|» assignmentStatusCode|string|false|none|none|
|» disputeStatusId|string|false|none|none|
|» disputeStatusCode|string|false|none|none|
|» disputedDate|string|false|none|none|
|» createdBy|string|false|none|none|
|» modifiedBy|string|false|none|none|
|» requestorId|string|false|none|none|
|» ownerId|string|false|none|none|
|» locationId|string|false|none|none|
|» positionId|string|false|none|none|
|» serviceClassificationId|string|false|none|none|
|» relatedServiceClassification|[string]|false|none|none|
|» miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|»» serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» value|[string]|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedId|string|false|none|none|
|»» flagReason|string|false|none|none|
|» source|string|false|none|none|
|» isFlagged|boolean|false|none|none|
|» isPrivate|boolean|false|none|none|
|» priorityId|string|false|none|none|
|» watchers|[string]|false|none|none|
|» sourceApp|string|false|none|none|
|» spendLimit|number|false|none|none|
|» estimatedServiceCost|number|false|none|none|
|» lastAssessmentDate|string|false|none|none|
|» lastAssessmentTrigger|string|false|none|none|
|» createdDate|string|false|none|none|
|» reportedDate|string|false|none|none|
|» modifiedDate|string|false|none|none|
|» closedDate|string|false|none|none|
|» description|string|false|none|none|
|» charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|»» chartId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» version|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» chartName|string|false|none|none|
|»» dimensionName|string|false|none|none|
|»» dimensionPosition|string|false|none|none|
|»» dimensionValue|string|false|none|none|
|» comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|»» commentId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» addedByPersonId|string|false|none|none|
|»» source|string|false|none|none|
|»» comment|string|false|none|none|
|»» type|string|false|none|none|
|»» orgType|string|false|none|none|
|»» linkedWOCommentId|string|false|none|none|
|»» addedDate|string|false|none|none|
|»» linkedWorkOrderId|string|false|none|none|
|»» isClientViewable|boolean|false|none|none|
|» extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|»» id|string|false|none|none|
|»» data|string|false|none|none|
|» serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» name|string|false|none|none|
|»» timeAllotted|number|false|none|none|
|»» unit|string|false|none|none|
|»» targetTime|string|false|none|none|
|»» overriddenDate|string|false|none|none|
|»» overriddenReason|string|false|none|none|
|»» overriddenBy|string|false|none|none|
|»» slaMetDate|string|false|none|none|
|»» slaMetWO|string|false|none|none|
|»» slaMetDatet|string|false|write-only|none|
|» watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» user|string|false|none|none|
|»» createdBy|string|false|none|none|
|» triageStatus|string|false|none|none|
|» workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|»» id|string|false|none|none|
|»» description|string|false|none|none|
|»» alternateId|string|false|none|none|
|»» statusId|string|false|none|none|
|»» assigneeName|string|false|none|none|
|»» assignmentType|string|false|none|none|
|»» assigneeId|string|false|none|none|
|»» facilityManagerId|string|false|none|none|
|»» comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|»»» commentId|string|false|none|none|
|»»» workOrderCommentId|integer(int32)|false|none|none|
|»»» addedByPersonId|string|false|none|none|
|»»» comment|string|false|none|none|
|»»» commentType|string|false|none|none|
|»»» addedDate|string|false|none|none|
|»» slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» targetDate|string|false|none|none|
|»»» overrideDate|string|false|none|none|
|»»» overrideReason|string|false|none|none|
|»»» overrideBy|string|false|none|none|
|»»» slaMetDate|string|false|none|none|
|»»» slaMet|boolean|false|none|none|
|»» nte|number|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» dispatchSiteId|string|false|none|none|
|»» dispatchSiteName|string|false|none|none|
|»» completionDescription|string|false|none|none|
|»» requestedBy|string|false|none|none|
|»» serviceClassificationId|string|false|none|none|
|»» locationId|string|false|none|none|
|»» assetId|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» modifiedDate|string|false|none|none|
|»» assigneeIds|[string]|false|none|none|
|»» dispatchSiteIds|[string]|false|none|none|
|» statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|»» statusId|string|false|none|none|
|»» statusCode|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» updatedBy|string|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» reasonId|string|false|none|none|
|»» version|integer(int32)|false|none|none|
|» attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|»» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» mimetype|string|false|none|none|
|»»» extension|string|false|none|none|
|»»» type|string|false|none|none|
|»»» status|string|false|none|none|
|»»» tenantId|string|false|none|none|
|»»» storageAccount|string|false|none|none|
|»»» container|string|false|none|none|
|»»» fileMd5|string|false|none|none|
|»»» createdTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»»» id|string|false|none|none|
|»»» orgs|[string]|false|none|none|
|»»» objectId|string|false|none|none|
|»»» objectType|string|false|none|none|
|»»» createTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»»» description|string|false|none|none|
|» reason|[ReasonDTO](#schemareasondto)|false|none|none|
|»» reasonCode|string|false|none|none|
|»» reasonDescription|string|false|none|none|
|» requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|»» activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|»»» approverId|string(uuid)|false|none|none|
|»»» delegatorId|string(uuid)|false|none|none|
|»»» stepNumber|integer(int32)|false|none|none|
|»»» isDelegator|boolean|false|none|none|
|»» chain|[ChainDTO](#schemachaindto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» majorVersion|integer(int32)|false|none|none|
|»»» minorVersion|integer(int32)|false|none|none|
|»»» createdDate|string|false|none|none|
|»»» updatedTime|string|false|none|none|
|»»» source|string|false|none|none|
|»»» chainDefinitionId|string(uuid)|false|none|none|
|»»» capabilityId|string(uuid)|false|none|none|
|»»» capabilityTtl|string|false|none|none|
|»»» capabilityName|string|false|none|none|
|»»» capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»»» value|string|false|none|none|
|»»» chainDefinitionAlternateId|string|false|none|none|
|»»» chainDefinitionVersion|integer(int32)|false|none|none|
|»»» orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» type|string|false|none|none|
|»»» chainStatus|string|false|none|none|
|»»» approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» personId|string(uuid)|false|none|none|
|»»»» personType|string|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»»» sequence|integer(int32)|false|none|none|
|»»»» generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»»» group|string|false|none|none|
|»»»» authScopeId|string(uuid)|false|none|none|
|»»»» when|string|false|none|none|
|»»»» responseCount|integer(int32)|false|none|none|
|»»»» approvalRule|string|false|none|none|
|»»»» mandatory|boolean|false|none|none|
|»»»» decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|»»»»» status|string|false|none|none|
|»»»»» decisionDate|string|false|none|none|
|»»»»» madeByDelegate|boolean|false|none|none|
|»»»»» decisionNote|string|false|none|none|
|»»»» personLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»» delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|»»»» approver|string(uuid)|false|none|none|
|»»»» delegatedTo|string(uuid)|false|none|none|
|»»»» startDate|string(date-time)|false|none|none|
|»»»» endDate|string(date-time)|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»» excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|»»»» excludedApprover|string|false|none|none|
|»»»» conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»» conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|
|»»»»» id|string(uuid)|false|none|none|
|»»»»» type|string|false|none|none|
|»»»»» alternateId|string|false|none|none|
|»»» isRecalculate|boolean|false|none|none|
|»» subStateStatus|string|false|none|none|
|»» subStateId|string(uuid)|false|none|none|
|» errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|»» version|string|false|none|none|
|»» traceId|string|false|none|none|
|»» title|string|false|none|none|
|»» category|string|false|none|none|
|»» errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|
|»»» id|string|false|none|none|
|»»» alternateId|string|false|none|none|
|»»» description|string|false|none|none|
|»»» domain|string|false|none|none|
|»»» messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|
|»»»» message|string|false|none|none|
|»»»» code|string|false|none|none|
|» workOwnerGroupValue|string|false|none|none|
|» miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|»» statusChangeDate|string|false|none|none|
|»» slaAttendDate|string|false|none|none|
|»» slaCompleteDate|string|false|none|none|
|»» slaDispatchDate|string|false|none|none|
|»» slaResponseDate|string|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedDate|string|false|none|none|
|» requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|»» name|string|false|none|none|
|»» additionalDetailsKey|string|false|none|none|
|»» additionalDetails|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|» action|[string]|false|none|none|
|» pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|
|»» pmId|string|false|none|none|
|»» pmAlternateId|string|false|none|none|
|»» pmConfigUrl|string|false|none|none|
|»» planId|string|false|none|none|
|»» type|string|false|none|none|
|»» primaryLocationId|string|false|none|none|
|»» maintenanceFrequency|string|false|none|none|
|»» maintenanceFrequencyUnit|string|false|none|none|
|»» interval|string|false|none|none|
|»» totalSequences|string|false|none|none|
|»» sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|»»» sequence|integer(int32)|false|none|none|
|»»» locationId|string|false|none|none|
|»»» assetId|string|false|none|none|
|»»» positionId|string|false|none|none|
|»» providerId|string|false|none|none|
|»» providerType|string|false|none|none|
|»» providerReferenceId|string|false|none|none|
|»» assignmentOverride|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|
|status|Approved|
|status|Declined|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestDTO](#schemarequestdto)]|false|none|none|
|» id|string(uuid)|false|none|none|
|» tenantId|string|false|none|none|
|» assetId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» alternateId|string|false|none|none|
|» statusId|string|false|none|none|
|» statusCode|string|false|none|none|
|» subStatusId|string|false|none|none|
|» subStatusCode|string|false|none|none|
|» materialsStatusId|string|false|none|none|
|» materialsStatusCode|string|false|none|none|
|» assignmentStatusId|string|false|none|none|
|» assignmentStatusCode|string|false|none|none|
|» disputeStatusId|string|false|none|none|
|» disputeStatusCode|string|false|none|none|
|» disputedDate|string|false|none|none|
|» createdBy|string|false|none|none|
|» modifiedBy|string|false|none|none|
|» requestorId|string|false|none|none|
|» ownerId|string|false|none|none|
|» locationId|string|false|none|none|
|» positionId|string|false|none|none|
|» serviceClassificationId|string|false|none|none|
|» relatedServiceClassification|[string]|false|none|none|
|» miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|»» serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» value|[string]|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedId|string|false|none|none|
|»» flagReason|string|false|none|none|
|» source|string|false|none|none|
|» isFlagged|boolean|false|none|none|
|» isPrivate|boolean|false|none|none|
|» priorityId|string|false|none|none|
|» watchers|[string]|false|none|none|
|» sourceApp|string|false|none|none|
|» spendLimit|number|false|none|none|
|» estimatedServiceCost|number|false|none|none|
|» lastAssessmentDate|string|false|none|none|
|» lastAssessmentTrigger|string|false|none|none|
|» createdDate|string|false|none|none|
|» reportedDate|string|false|none|none|
|» modifiedDate|string|false|none|none|
|» closedDate|string|false|none|none|
|» description|string|false|none|none|
|» charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|»» chartId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» version|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» chartName|string|false|none|none|
|»» dimensionName|string|false|none|none|
|»» dimensionPosition|string|false|none|none|
|»» dimensionValue|string|false|none|none|
|» comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|»» commentId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» addedByPersonId|string|false|none|none|
|»» source|string|false|none|none|
|»» comment|string|false|none|none|
|»» type|string|false|none|none|
|»» orgType|string|false|none|none|
|»» linkedWOCommentId|string|false|none|none|
|»» addedDate|string|false|none|none|
|»» linkedWorkOrderId|string|false|none|none|
|»» isClientViewable|boolean|false|none|none|
|» extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|»» id|string|false|none|none|
|»» data|string|false|none|none|
|» serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» name|string|false|none|none|
|»» timeAllotted|number|false|none|none|
|»» unit|string|false|none|none|
|»» targetTime|string|false|none|none|
|»» overriddenDate|string|false|none|none|
|»» overriddenReason|string|false|none|none|
|»» overriddenBy|string|false|none|none|
|»» slaMetDate|string|false|none|none|
|»» slaMetWO|string|false|none|none|
|»» slaMetDatet|string|false|write-only|none|
|» watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» user|string|false|none|none|
|»» createdBy|string|false|none|none|
|» triageStatus|string|false|none|none|
|» workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|»» id|string|false|none|none|
|»» description|string|false|none|none|
|»» alternateId|string|false|none|none|
|»» statusId|string|false|none|none|
|»» assigneeName|string|false|none|none|
|»» assignmentType|string|false|none|none|
|»» assigneeId|string|false|none|none|
|»» facilityManagerId|string|false|none|none|
|»» comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|»»» commentId|string|false|none|none|
|»»» workOrderCommentId|integer(int32)|false|none|none|
|»»» addedByPersonId|string|false|none|none|
|»»» comment|string|false|none|none|
|»»» commentType|string|false|none|none|
|»»» addedDate|string|false|none|none|
|»» slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» targetDate|string|false|none|none|
|»»» overrideDate|string|false|none|none|
|»»» overrideReason|string|false|none|none|
|»»» overrideBy|string|false|none|none|
|»»» slaMetDate|string|false|none|none|
|»»» slaMet|boolean|false|none|none|
|»» nte|number|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» dispatchSiteId|string|false|none|none|
|»» dispatchSiteName|string|false|none|none|
|»» completionDescription|string|false|none|none|
|»» requestedBy|string|false|none|none|
|»» serviceClassificationId|string|false|none|none|
|»» locationId|string|false|none|none|
|»» assetId|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» modifiedDate|string|false|none|none|
|»» assigneeIds|[string]|false|none|none|
|»» dispatchSiteIds|[string]|false|none|none|
|» statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|»» statusId|string|false|none|none|
|»» statusCode|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» updatedBy|string|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» reasonId|string|false|none|none|
|»» version|integer(int32)|false|none|none|
|» attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|»» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» mimetype|string|false|none|none|
|»»» extension|string|false|none|none|
|»»» type|string|false|none|none|
|»»» status|string|false|none|none|
|»»» tenantId|string|false|none|none|
|»»» storageAccount|string|false|none|none|
|»»» container|string|false|none|none|
|»»» fileMd5|string|false|none|none|
|»»» createdTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»»» id|string|false|none|none|
|»»» orgs|[string]|false|none|none|
|»»» objectId|string|false|none|none|
|»»» objectType|string|false|none|none|
|»»» createTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»»» description|string|false|none|none|
|» reason|[ReasonDTO](#schemareasondto)|false|none|none|
|»» reasonCode|string|false|none|none|
|»» reasonDescription|string|false|none|none|
|» requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|»» activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|»»» approverId|string(uuid)|false|none|none|
|»»» delegatorId|string(uuid)|false|none|none|
|»»» stepNumber|integer(int32)|false|none|none|
|»»» isDelegator|boolean|false|none|none|
|»» chain|[ChainDTO](#schemachaindto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» majorVersion|integer(int32)|false|none|none|
|»»» minorVersion|integer(int32)|false|none|none|
|»»» createdDate|string|false|none|none|
|»»» updatedTime|string|false|none|none|
|»»» source|string|false|none|none|
|»»» chainDefinitionId|string(uuid)|false|none|none|
|»»» capabilityId|string(uuid)|false|none|none|
|»»» capabilityTtl|string|false|none|none|
|»»» capabilityName|string|false|none|none|
|»»» capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»»» value|string|false|none|none|
|»»» chainDefinitionAlternateId|string|false|none|none|
|»»» chainDefinitionVersion|integer(int32)|false|none|none|
|»»» orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» type|string|false|none|none|
|»»» chainStatus|string|false|none|none|
|»»» approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» personId|string(uuid)|false|none|none|
|»»»» personType|string|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»»» sequence|integer(int32)|false|none|none|
|»»»» generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»»» group|string|false|none|none|
|»»»» authScopeId|string(uuid)|false|none|none|
|»»»» when|string|false|none|none|
|»»»» responseCount|integer(int32)|false|none|none|
|»»»» approvalRule|string|false|none|none|
|»»»» mandatory|boolean|false|none|none|
|»»»» decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|»»»»» status|string|false|none|none|
|»»»»» decisionDate|string|false|none|none|
|»»»»» madeByDelegate|boolean|false|none|none|
|»»»»» decisionNote|string|false|none|none|
|»»»» personLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»» delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|»»»» approver|string(uuid)|false|none|none|
|»»»» delegatedTo|string(uuid)|false|none|none|
|»»»» startDate|string(date-time)|false|none|none|
|»»»» endDate|string(date-time)|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»» excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|»»»» excludedApprover|string|false|none|none|
|»»»» conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»» conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|
|»»»»» id|string(uuid)|false|none|none|
|»»»»» type|string|false|none|none|
|»»»»» alternateId|string|false|none|none|
|»»» isRecalculate|boolean|false|none|none|
|»» subStateStatus|string|false|none|none|
|»» subStateId|string(uuid)|false|none|none|
|» errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|»» version|string|false|none|none|
|»» traceId|string|false|none|none|
|»» title|string|false|none|none|
|»» category|string|false|none|none|
|»» errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|
|»»» id|string|false|none|none|
|»»» alternateId|string|false|none|none|
|»»» description|string|false|none|none|
|»»» domain|string|false|none|none|
|»»» messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|
|»»»» message|string|false|none|none|
|»»»» code|string|false|none|none|
|» workOwnerGroupValue|string|false|none|none|
|» miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|»» statusChangeDate|string|false|none|none|
|»» slaAttendDate|string|false|none|none|
|»» slaCompleteDate|string|false|none|none|
|»» slaDispatchDate|string|false|none|none|
|»» slaResponseDate|string|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedDate|string|false|none|none|
|» requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|»» name|string|false|none|none|
|»» additionalDetailsKey|string|false|none|none|
|»» additionalDetails|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|» action|[string]|false|none|none|
|» pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|
|»» pmId|string|false|none|none|
|»» pmAlternateId|string|false|none|none|
|»» pmConfigUrl|string|false|none|none|
|»» planId|string|false|none|none|
|»» type|string|false|none|none|
|»» primaryLocationId|string|false|none|none|
|»» maintenanceFrequency|string|false|none|none|
|»» maintenanceFrequencyUnit|string|false|none|none|
|»» interval|string|false|none|none|
|»» totalSequences|string|false|none|none|
|»» sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|»»» sequence|integer(int32)|false|none|none|
|»»» locationId|string|false|none|none|
|»»» assetId|string|false|none|none|
|»»» positionId|string|false|none|none|
|»» providerId|string|false|none|none|
|»» providerType|string|false|none|none|
|»» providerReferenceId|string|false|none|none|
|»» assignmentOverride|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|
|status|Approved|
|status|Declined|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestDTO](#schemarequestdto)]|false|none|none|
|» id|string(uuid)|false|none|none|
|» tenantId|string|false|none|none|
|» assetId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» alternateId|string|false|none|none|
|» statusId|string|false|none|none|
|» statusCode|string|false|none|none|
|» subStatusId|string|false|none|none|
|» subStatusCode|string|false|none|none|
|» materialsStatusId|string|false|none|none|
|» materialsStatusCode|string|false|none|none|
|» assignmentStatusId|string|false|none|none|
|» assignmentStatusCode|string|false|none|none|
|» disputeStatusId|string|false|none|none|
|» disputeStatusCode|string|false|none|none|
|» disputedDate|string|false|none|none|
|» createdBy|string|false|none|none|
|» modifiedBy|string|false|none|none|
|» requestorId|string|false|none|none|
|» ownerId|string|false|none|none|
|» locationId|string|false|none|none|
|» positionId|string|false|none|none|
|» serviceClassificationId|string|false|none|none|
|» relatedServiceClassification|[string]|false|none|none|
|» miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|»» serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» value|[string]|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedId|string|false|none|none|
|»» flagReason|string|false|none|none|
|» source|string|false|none|none|
|» isFlagged|boolean|false|none|none|
|» isPrivate|boolean|false|none|none|
|» priorityId|string|false|none|none|
|» watchers|[string]|false|none|none|
|» sourceApp|string|false|none|none|
|» spendLimit|number|false|none|none|
|» estimatedServiceCost|number|false|none|none|
|» lastAssessmentDate|string|false|none|none|
|» lastAssessmentTrigger|string|false|none|none|
|» createdDate|string|false|none|none|
|» reportedDate|string|false|none|none|
|» modifiedDate|string|false|none|none|
|» closedDate|string|false|none|none|
|» description|string|false|none|none|
|» charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|»» chartId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» version|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» chartName|string|false|none|none|
|»» dimensionName|string|false|none|none|
|»» dimensionPosition|string|false|none|none|
|»» dimensionValue|string|false|none|none|
|» comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|»» commentId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» addedByPersonId|string|false|none|none|
|»» source|string|false|none|none|
|»» comment|string|false|none|none|
|»» type|string|false|none|none|
|»» orgType|string|false|none|none|
|»» linkedWOCommentId|string|false|none|none|
|»» addedDate|string|false|none|none|
|»» linkedWorkOrderId|string|false|none|none|
|»» isClientViewable|boolean|false|none|none|
|» extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|»» id|string|false|none|none|
|»» data|string|false|none|none|
|» serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» name|string|false|none|none|
|»» timeAllotted|number|false|none|none|
|»» unit|string|false|none|none|
|»» targetTime|string|false|none|none|
|»» overriddenDate|string|false|none|none|
|»» overriddenReason|string|false|none|none|
|»» overriddenBy|string|false|none|none|
|»» slaMetDate|string|false|none|none|
|»» slaMetWO|string|false|none|none|
|»» slaMetDatet|string|false|write-only|none|
|» watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» user|string|false|none|none|
|»» createdBy|string|false|none|none|
|» triageStatus|string|false|none|none|
|» workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|»» id|string|false|none|none|
|»» description|string|false|none|none|
|»» alternateId|string|false|none|none|
|»» statusId|string|false|none|none|
|»» assigneeName|string|false|none|none|
|»» assignmentType|string|false|none|none|
|»» assigneeId|string|false|none|none|
|»» facilityManagerId|string|false|none|none|
|»» comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|»»» commentId|string|false|none|none|
|»»» workOrderCommentId|integer(int32)|false|none|none|
|»»» addedByPersonId|string|false|none|none|
|»»» comment|string|false|none|none|
|»»» commentType|string|false|none|none|
|»»» addedDate|string|false|none|none|
|»» slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» targetDate|string|false|none|none|
|»»» overrideDate|string|false|none|none|
|»»» overrideReason|string|false|none|none|
|»»» overrideBy|string|false|none|none|
|»»» slaMetDate|string|false|none|none|
|»»» slaMet|boolean|false|none|none|
|»» nte|number|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» dispatchSiteId|string|false|none|none|
|»» dispatchSiteName|string|false|none|none|
|»» completionDescription|string|false|none|none|
|»» requestedBy|string|false|none|none|
|»» serviceClassificationId|string|false|none|none|
|»» locationId|string|false|none|none|
|»» assetId|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» modifiedDate|string|false|none|none|
|»» assigneeIds|[string]|false|none|none|
|»» dispatchSiteIds|[string]|false|none|none|
|» statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|»» statusId|string|false|none|none|
|»» statusCode|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» updatedBy|string|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» reasonId|string|false|none|none|
|»» version|integer(int32)|false|none|none|
|» attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|»» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» mimetype|string|false|none|none|
|»»» extension|string|false|none|none|
|»»» type|string|false|none|none|
|»»» status|string|false|none|none|
|»»» tenantId|string|false|none|none|
|»»» storageAccount|string|false|none|none|
|»»» container|string|false|none|none|
|»»» fileMd5|string|false|none|none|
|»»» createdTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»»» id|string|false|none|none|
|»»» orgs|[string]|false|none|none|
|»»» objectId|string|false|none|none|
|»»» objectType|string|false|none|none|
|»»» createTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»»» description|string|false|none|none|
|» reason|[ReasonDTO](#schemareasondto)|false|none|none|
|»» reasonCode|string|false|none|none|
|»» reasonDescription|string|false|none|none|
|» requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|»» activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|»»» approverId|string(uuid)|false|none|none|
|»»» delegatorId|string(uuid)|false|none|none|
|»»» stepNumber|integer(int32)|false|none|none|
|»»» isDelegator|boolean|false|none|none|
|»» chain|[ChainDTO](#schemachaindto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» majorVersion|integer(int32)|false|none|none|
|»»» minorVersion|integer(int32)|false|none|none|
|»»» createdDate|string|false|none|none|
|»»» updatedTime|string|false|none|none|
|»»» source|string|false|none|none|
|»»» chainDefinitionId|string(uuid)|false|none|none|
|»»» capabilityId|string(uuid)|false|none|none|
|»»» capabilityTtl|string|false|none|none|
|»»» capabilityName|string|false|none|none|
|»»» capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»»» value|string|false|none|none|
|»»» chainDefinitionAlternateId|string|false|none|none|
|»»» chainDefinitionVersion|integer(int32)|false|none|none|
|»»» orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» type|string|false|none|none|
|»»» chainStatus|string|false|none|none|
|»»» approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» personId|string(uuid)|false|none|none|
|»»»» personType|string|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»»» sequence|integer(int32)|false|none|none|
|»»»» generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»»» group|string|false|none|none|
|»»»» authScopeId|string(uuid)|false|none|none|
|»»»» when|string|false|none|none|
|»»»» responseCount|integer(int32)|false|none|none|
|»»»» approvalRule|string|false|none|none|
|»»»» mandatory|boolean|false|none|none|
|»»»» decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|»»»»» status|string|false|none|none|
|»»»»» decisionDate|string|false|none|none|
|»»»»» madeByDelegate|boolean|false|none|none|
|»»»»» decisionNote|string|false|none|none|
|»»»» personLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»» delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|»»»» approver|string(uuid)|false|none|none|
|»»»» delegatedTo|string(uuid)|false|none|none|
|»»»» startDate|string(date-time)|false|none|none|
|»»»» endDate|string(date-time)|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»» excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|»»»» excludedApprover|string|false|none|none|
|»»»» conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»» conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|
|»»»»» id|string(uuid)|false|none|none|
|»»»»» type|string|false|none|none|
|»»»»» alternateId|string|false|none|none|
|»»» isRecalculate|boolean|false|none|none|
|»» subStateStatus|string|false|none|none|
|»» subStateId|string(uuid)|false|none|none|
|» errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|»» version|string|false|none|none|
|»» traceId|string|false|none|none|
|»» title|string|false|none|none|
|»» category|string|false|none|none|
|»» errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|
|»»» id|string|false|none|none|
|»»» alternateId|string|false|none|none|
|»»» description|string|false|none|none|
|»»» domain|string|false|none|none|
|»»» messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|
|»»»» message|string|false|none|none|
|»»»» code|string|false|none|none|
|» workOwnerGroupValue|string|false|none|none|
|» miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|»» statusChangeDate|string|false|none|none|
|»» slaAttendDate|string|false|none|none|
|»» slaCompleteDate|string|false|none|none|
|»» slaDispatchDate|string|false|none|none|
|»» slaResponseDate|string|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedDate|string|false|none|none|
|» requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|»» name|string|false|none|none|
|»» additionalDetailsKey|string|false|none|none|
|»» additionalDetails|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|» action|[string]|false|none|none|
|» pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|
|»» pmId|string|false|none|none|
|»» pmAlternateId|string|false|none|none|
|»» pmConfigUrl|string|false|none|none|
|»» planId|string|false|none|none|
|»» type|string|false|none|none|
|»» primaryLocationId|string|false|none|none|
|»» maintenanceFrequency|string|false|none|none|
|»» maintenanceFrequencyUnit|string|false|none|none|
|»» interval|string|false|none|none|
|»» totalSequences|string|false|none|none|
|»» sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|»»» sequence|integer(int32)|false|none|none|
|»»» locationId|string|false|none|none|
|»»» assetId|string|false|none|none|
|»»» positionId|string|false|none|none|
|»» providerId|string|false|none|none|
|»» providerType|string|false|none|none|
|»» providerReferenceId|string|false|none|none|
|»» assignmentOverride|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|
|status|Approved|
|status|Declined|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestDTO](#schemarequestdto)]|false|none|none|
|» id|string(uuid)|false|none|none|
|» tenantId|string|false|none|none|
|» assetId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» alternateId|string|false|none|none|
|» statusId|string|false|none|none|
|» statusCode|string|false|none|none|
|» subStatusId|string|false|none|none|
|» subStatusCode|string|false|none|none|
|» materialsStatusId|string|false|none|none|
|» materialsStatusCode|string|false|none|none|
|» assignmentStatusId|string|false|none|none|
|» assignmentStatusCode|string|false|none|none|
|» disputeStatusId|string|false|none|none|
|» disputeStatusCode|string|false|none|none|
|» disputedDate|string|false|none|none|
|» createdBy|string|false|none|none|
|» modifiedBy|string|false|none|none|
|» requestorId|string|false|none|none|
|» ownerId|string|false|none|none|
|» locationId|string|false|none|none|
|» positionId|string|false|none|none|
|» serviceClassificationId|string|false|none|none|
|» relatedServiceClassification|[string]|false|none|none|
|» miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|»» serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» value|[string]|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedId|string|false|none|none|
|»» flagReason|string|false|none|none|
|» source|string|false|none|none|
|» isFlagged|boolean|false|none|none|
|» isPrivate|boolean|false|none|none|
|» priorityId|string|false|none|none|
|» watchers|[string]|false|none|none|
|» sourceApp|string|false|none|none|
|» spendLimit|number|false|none|none|
|» estimatedServiceCost|number|false|none|none|
|» lastAssessmentDate|string|false|none|none|
|» lastAssessmentTrigger|string|false|none|none|
|» createdDate|string|false|none|none|
|» reportedDate|string|false|none|none|
|» modifiedDate|string|false|none|none|
|» closedDate|string|false|none|none|
|» description|string|false|none|none|
|» charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|»» chartId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» version|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» chartName|string|false|none|none|
|»» dimensionName|string|false|none|none|
|»» dimensionPosition|string|false|none|none|
|»» dimensionValue|string|false|none|none|
|» comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|»» commentId|string|false|none|none|
|»» requestId|string|false|none|none|
|»» addedByPersonId|string|false|none|none|
|»» source|string|false|none|none|
|»» comment|string|false|none|none|
|»» type|string|false|none|none|
|»» orgType|string|false|none|none|
|»» linkedWOCommentId|string|false|none|none|
|»» addedDate|string|false|none|none|
|»» linkedWorkOrderId|string|false|none|none|
|»» isClientViewable|boolean|false|none|none|
|» extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|»» id|string|false|none|none|
|»» data|string|false|none|none|
|» serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» name|string|false|none|none|
|»» timeAllotted|number|false|none|none|
|»» unit|string|false|none|none|
|»» targetTime|string|false|none|none|
|»» overriddenDate|string|false|none|none|
|»» overriddenReason|string|false|none|none|
|»» overriddenBy|string|false|none|none|
|»» slaMetDate|string|false|none|none|
|»» slaMetWO|string|false|none|none|
|»» slaMetDatet|string|false|write-only|none|
|» watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|»» id|string|false|none|none|
|»» requestId|string|false|none|none|
|»» user|string|false|none|none|
|»» createdBy|string|false|none|none|
|» triageStatus|string|false|none|none|
|» workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|»» id|string|false|none|none|
|»» description|string|false|none|none|
|»» alternateId|string|false|none|none|
|»» statusId|string|false|none|none|
|»» assigneeName|string|false|none|none|
|»» assignmentType|string|false|none|none|
|»» assigneeId|string|false|none|none|
|»» facilityManagerId|string|false|none|none|
|»» comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|»»» commentId|string|false|none|none|
|»»» workOrderCommentId|integer(int32)|false|none|none|
|»»» addedByPersonId|string|false|none|none|
|»»» comment|string|false|none|none|
|»»» commentType|string|false|none|none|
|»»» addedDate|string|false|none|none|
|»» slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» targetDate|string|false|none|none|
|»»» overrideDate|string|false|none|none|
|»»» overrideReason|string|false|none|none|
|»»» overrideBy|string|false|none|none|
|»»» slaMetDate|string|false|none|none|
|»»» slaMet|boolean|false|none|none|
|»» nte|number|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» dispatchSiteId|string|false|none|none|
|»» dispatchSiteName|string|false|none|none|
|»» completionDescription|string|false|none|none|
|»» requestedBy|string|false|none|none|
|»» serviceClassificationId|string|false|none|none|
|»» locationId|string|false|none|none|
|»» assetId|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» modifiedDate|string|false|none|none|
|»» assigneeIds|[string]|false|none|none|
|»» dispatchSiteIds|[string]|false|none|none|
|» statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|»» statusId|string|false|none|none|
|»» statusCode|string|false|none|none|
|»» createdDate|string|false|none|none|
|»» updatedBy|string|false|none|none|
|»» subStatusId|string|false|none|none|
|»» subStatusCode|string|false|none|none|
|»» reasonId|string|false|none|none|
|»» version|integer(int32)|false|none|none|
|» attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|»» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»»» id|string|false|none|none|
|»»» name|string|false|none|none|
|»»» mimetype|string|false|none|none|
|»»» extension|string|false|none|none|
|»»» type|string|false|none|none|
|»»» status|string|false|none|none|
|»»» tenantId|string|false|none|none|
|»»» storageAccount|string|false|none|none|
|»»» container|string|false|none|none|
|»»» fileMd5|string|false|none|none|
|»»» createdTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»»» id|string|false|none|none|
|»»» orgs|[string]|false|none|none|
|»»» objectId|string|false|none|none|
|»»» objectType|string|false|none|none|
|»»» createTime|string|false|none|none|
|»»» createdBy|string|false|none|none|
|»»» description|string|false|none|none|
|» reason|[ReasonDTO](#schemareasondto)|false|none|none|
|»» reasonCode|string|false|none|none|
|»» reasonDescription|string|false|none|none|
|» requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|»» activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|»»» approverId|string(uuid)|false|none|none|
|»»» delegatorId|string(uuid)|false|none|none|
|»»» stepNumber|integer(int32)|false|none|none|
|»»» isDelegator|boolean|false|none|none|
|»» chain|[ChainDTO](#schemachaindto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» majorVersion|integer(int32)|false|none|none|
|»»» minorVersion|integer(int32)|false|none|none|
|»»» createdDate|string|false|none|none|
|»»» updatedTime|string|false|none|none|
|»»» source|string|false|none|none|
|»»» chainDefinitionId|string(uuid)|false|none|none|
|»»» capabilityId|string(uuid)|false|none|none|
|»»» capabilityTtl|string|false|none|none|
|»»» capabilityName|string|false|none|none|
|»»» capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»»» value|string|false|none|none|
|»»» chainDefinitionAlternateId|string|false|none|none|
|»»» chainDefinitionVersion|integer(int32)|false|none|none|
|»»» orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» type|string|false|none|none|
|»»» chainStatus|string|false|none|none|
|»»» approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» personId|string(uuid)|false|none|none|
|»»»» personType|string|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»»» sequence|integer(int32)|false|none|none|
|»»»» generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»»» group|string|false|none|none|
|»»»» authScopeId|string(uuid)|false|none|none|
|»»»» when|string|false|none|none|
|»»»» responseCount|integer(int32)|false|none|none|
|»»»» approvalRule|string|false|none|none|
|»»»» mandatory|boolean|false|none|none|
|»»»» decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|»»»»» status|string|false|none|none|
|»»»»» decisionDate|string|false|none|none|
|»»»»» madeByDelegate|boolean|false|none|none|
|»»»»» decisionNote|string|false|none|none|
|»»»» personLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|»»» delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|»»»» approver|string(uuid)|false|none|none|
|»»»» delegatedTo|string(uuid)|false|none|none|
|»»»» startDate|string(date-time)|false|none|none|
|»»»» endDate|string(date-time)|false|none|none|
|»»»» group|integer(int32)|false|none|none|
|»»» excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|»»»» excludedApprover|string|false|none|none|
|»»»» conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|»»»»» id|string|false|none|none|
|»»»»» name|string|false|none|none|
|»»»» conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|
|»»»»» id|string(uuid)|false|none|none|
|»»»»» type|string|false|none|none|
|»»»»» alternateId|string|false|none|none|
|»»» isRecalculate|boolean|false|none|none|
|»» subStateStatus|string|false|none|none|
|»» subStateId|string(uuid)|false|none|none|
|» errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|»» version|string|false|none|none|
|»» traceId|string|false|none|none|
|»» title|string|false|none|none|
|»» category|string|false|none|none|
|»» errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|
|»»» id|string|false|none|none|
|»»» alternateId|string|false|none|none|
|»»» description|string|false|none|none|
|»»» domain|string|false|none|none|
|»»» messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|
|»»»» message|string|false|none|none|
|»»»» code|string|false|none|none|
|» workOwnerGroupValue|string|false|none|none|
|» miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|»» statusChangeDate|string|false|none|none|
|»» slaAttendDate|string|false|none|none|
|»» slaCompleteDate|string|false|none|none|
|»» slaDispatchDate|string|false|none|none|
|»» slaResponseDate|string|false|none|none|
|»» isFlagged|boolean|false|none|none|
|»» flaggedDate|string|false|none|none|
|» requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|»» name|string|false|none|none|
|»» additionalDetailsKey|string|false|none|none|
|»» additionalDetails|object|false|none|none|
|»»» **additionalProperties**|string|false|none|none|
|» action|[string]|false|none|none|
|» pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|
|»» pmId|string|false|none|none|
|»» pmAlternateId|string|false|none|none|
|»» pmConfigUrl|string|false|none|none|
|»» planId|string|false|none|none|
|»» type|string|false|none|none|
|»» primaryLocationId|string|false|none|none|
|»» maintenanceFrequency|string|false|none|none|
|»» maintenanceFrequencyUnit|string|false|none|none|
|»» interval|string|false|none|none|
|»» totalSequences|string|false|none|none|
|»» sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|»»» sequence|integer(int32)|false|none|none|
|»»» locationId|string|false|none|none|
|»»» assetId|string|false|none|none|
|»»» positionId|string|false|none|none|
|»» providerId|string|false|none|none|
|»» providerType|string|false|none|none|
|»» providerReferenceId|string|false|none|none|
|»» assignmentOverride|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|
|status|Approved|
|status|Declined|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

<aside class="success">
This operation does not require authentication
</aside>

## Create a Service Request

<a id="opIdcreateRequest"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request`

Create a Service Request in Request Domain

> Body parameter

```json
{
  "id": "string",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "subStatusId": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "relatedServiceClassificationId": [
    "string"
  ],
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "startDate": "string",
  "modifiedDate": "string",
  "description": "string",
  "chart": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}
```

<h3 id="create-a-service-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|body|body|[RequestBodyDTO](#schemarequestbodydto)|true|none|

> Example responses

> 201 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "statusCode": "string",
  "subStatusId": "string",
  "subStatusCode": "string",
  "materialsStatusId": "string",
  "materialsStatusCode": "string",
  "assignmentStatusId": "string",
  "assignmentStatusCode": "string",
  "disputeStatusId": "string",
  "disputeStatusCode": "string",
  "disputedDate": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "relatedServiceClassification": [
    "string"
  ],
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "spendLimit": 0,
  "estimatedServiceCost": 0,
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "modifiedDate": "string",
  "closedDate": "string",
  "description": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "watchLists": [
    {
      "id": "string",
      "requestId": "string",
      "user": "string",
      "createdBy": "string"
    }
  ],
  "triageStatus": "string",
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "reason": {
    "reasonCode": "string",
    "reasonDescription": "string"
  },
  "requestChain": [
    {
      "activeApprovers": [
        {
          "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
          "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
          "stepNumber": 0,
          "isDelegator": true
        }
      ],
      "chain": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "majorVersion": 0,
        "minorVersion": 0,
        "createdDate": "string",
        "updatedTime": "string",
        "source": "string",
        "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
        "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
        "capabilityTtl": "string",
        "capabilityName": "string",
        "capabilityLimit": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string",
          "unit": "string",
          "value": "string"
        },
        "chainDefinitionAlternateId": "string",
        "chainDefinitionVersion": 0,
        "orgs": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "type": "string"
          }
        ],
        "chainStatus": "InProgress",
        "approvers": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
            "personType": "string",
            "group": 0,
            "sequence": 0,
            "generalization": {
              "id": "string",
              "name": "string",
              "group": "string"
            },
            "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
            "when": "string",
            "responseCount": 0,
            "approvalRule": "string",
            "mandatory": true,
            "decision": {
              "status": "Approved",
              "decisionDate": "string",
              "madeByDelegate": true,
              "decisionNote": "string"
            },
            "personLimit": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "name": "string",
              "unit": "string",
              "value": "string"
            }
          }
        ],
        "delegates": [
          {
            "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
            "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
            "startDate": "2019-08-24T14:15:22Z",
            "endDate": "2019-08-24T14:15:22Z",
            "group": 0
          }
        ],
        "excluded": [
          {
            "excludedApprover": "string",
            "conflictCapability": {
              "id": "string",
              "name": "string"
            },
            "conflictObject": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "type": "string",
              "alternateId": "string"
            }
          }
        ],
        "isRecalculate": true
      },
      "subStateStatus": "ACTIVE",
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536"
    }
  ],
  "errorContainer": {
    "version": "string",
    "traceId": "string",
    "title": "string",
    "category": "INFO",
    "errors": [
      {
        "id": "string",
        "alternateId": "string",
        "description": "string",
        "domain": "string",
        "messages": [
          {
            "message": "string",
            "code": "string"
          }
        ]
      }
    ]
  },
  "workOwnerGroupValue": "string",
  "miscellaneous": {
    "statusChangeDate": "string",
    "slaAttendDate": "string",
    "slaCompleteDate": "string",
    "slaDispatchDate": "string",
    "slaResponseDate": "string",
    "isFlagged": true,
    "flaggedDate": "string"
  },
  "requestAuthActions": [
    {
      "name": "string",
      "additionalDetailsKey": "string",
      "additionalDetails": {
        "property1": "string",
        "property2": "string"
      }
    }
  ],
  "action": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}
```

<h3 id="create-a-service-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Service Request Created|[RequestDTO](#schemarequestdto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[RequestDTO](#schemarequestdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[RequestDTO](#schemarequestdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[RequestDTO](#schemarequestdto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[RequestDTO](#schemarequestdto)|

<aside class="success">
This operation does not require authentication
</aside>

## Add New Watcher to Request WatchList

<a id="opIdaddWatcher"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request/{id}/watcher \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}/watcher");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request/{id}/watcher', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request/{id}/watcher`

Add New Watcher to Request WatchList in Request Domain

> Body parameter

```json
[
  "string"
]
```

<h3 id="add-new-watcher-to-request-watchlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|id|path|string|true|none|
|body|body|array[string]|true|none|

> Example responses

> 201 Response

```json
{
  "id": "string",
  "requestId": "string",
  "user": "string",
  "createdBy": "string"
}
```

<h3 id="add-new-watcher-to-request-watchlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="add-new-watcher-to-request-watchlist-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|» id|string|false|none|none|
|» requestId|string|false|none|none|
|» user|string|false|none|none|
|» createdBy|string|false|none|none|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|» id|string|false|none|none|
|» requestId|string|false|none|none|
|» user|string|false|none|none|
|» createdBy|string|false|none|none|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|» id|string|false|none|none|
|» requestId|string|false|none|none|
|» user|string|false|none|none|
|» createdBy|string|false|none|none|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|» id|string|false|none|none|
|» requestId|string|false|none|none|
|» user|string|false|none|none|
|» createdBy|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|» id|string|false|none|none|
|» requestId|string|false|none|none|
|» user|string|false|none|none|
|» createdBy|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Updates the request flag on RD

<a id="opIdupdateRequestFlag"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request/{id}/flag \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}/flag");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request/{id}/flag', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request/{id}/flag`

Updates the request flag on RD database and publish its to FD.

> Body parameter

```json
{
  "id": "string",
  "flagId": "string",
  "flaggedBy": "string",
  "flaggedDate": "string",
  "unflagId": "string",
  "unflaggedBy": "string",
  "unflaggedDate": "string",
  "status": "string",
  "isRequestFlagged": true,
  "requestFlaggedDate": "string"
}
```

<h3 id="updates-the-request-flag-on-rd-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|false|none|
|id|path|string|true|none|
|body|body|[RequestFlagDto](#schemarequestflagdto)|true|none|

> Example responses

> 204 Response

<h3 id="updates-the-request-flag-on-rd-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Deleted|string|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|string|

<aside class="success">
This operation does not require authentication
</aside>

## Add Comment to Request

<a id="opIdaddComment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request/{id}/comment \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}/comment");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request/{id}/comment', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request/{id}/comment`

Add Comment to Request in Request Domain

> Body parameter

```json
[
  {
    "commentId": "string",
    "requestId": "string",
    "addedByPersonId": "string",
    "source": "string",
    "comment": "string",
    "type": "string",
    "orgType": "string",
    "linkedWOCommentId": "string",
    "addedDate": "string",
    "linkedWorkOrderId": "string",
    "isClientViewable": true
  }
]
```

<h3 id="add-comment-to-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|id|path|string|true|none|
|body|body|[CommentDTO](#schemacommentdto)|true|none|

> Example responses

> 201 Response

```json
{
  "commentId": "string",
  "requestId": "string",
  "addedByPersonId": "string",
  "source": "string",
  "comment": "string",
  "type": "string",
  "orgType": "string",
  "linkedWOCommentId": "string",
  "addedDate": "string",
  "linkedWorkOrderId": "string",
  "isClientViewable": true
}
```

<h3 id="add-comment-to-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="add-comment-to-request-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CommentDTO](#schemacommentdto)]|false|none|none|
|» commentId|string|false|none|none|
|» requestId|string|false|none|none|
|» addedByPersonId|string|false|none|none|
|» source|string|false|none|none|
|» comment|string|false|none|none|
|» type|string|false|none|none|
|» orgType|string|false|none|none|
|» linkedWOCommentId|string|false|none|none|
|» addedDate|string|false|none|none|
|» linkedWorkOrderId|string|false|none|none|
|» isClientViewable|boolean|false|none|none|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CommentDTO](#schemacommentdto)]|false|none|none|
|» commentId|string|false|none|none|
|» requestId|string|false|none|none|
|» addedByPersonId|string|false|none|none|
|» source|string|false|none|none|
|» comment|string|false|none|none|
|» type|string|false|none|none|
|» orgType|string|false|none|none|
|» linkedWOCommentId|string|false|none|none|
|» addedDate|string|false|none|none|
|» linkedWorkOrderId|string|false|none|none|
|» isClientViewable|boolean|false|none|none|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CommentDTO](#schemacommentdto)]|false|none|none|
|» commentId|string|false|none|none|
|» requestId|string|false|none|none|
|» addedByPersonId|string|false|none|none|
|» source|string|false|none|none|
|» comment|string|false|none|none|
|» type|string|false|none|none|
|» orgType|string|false|none|none|
|» linkedWOCommentId|string|false|none|none|
|» addedDate|string|false|none|none|
|» linkedWorkOrderId|string|false|none|none|
|» isClientViewable|boolean|false|none|none|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CommentDTO](#schemacommentdto)]|false|none|none|
|» commentId|string|false|none|none|
|» requestId|string|false|none|none|
|» addedByPersonId|string|false|none|none|
|» source|string|false|none|none|
|» comment|string|false|none|none|
|» type|string|false|none|none|
|» orgType|string|false|none|none|
|» linkedWOCommentId|string|false|none|none|
|» addedDate|string|false|none|none|
|» linkedWorkOrderId|string|false|none|none|
|» isClientViewable|boolean|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[CommentDTO](#schemacommentdto)]|false|none|none|
|» commentId|string|false|none|none|
|» requestId|string|false|none|none|
|» addedByPersonId|string|false|none|none|
|» source|string|false|none|none|
|» comment|string|false|none|none|
|» type|string|false|none|none|
|» orgType|string|false|none|none|
|» linkedWOCommentId|string|false|none|none|
|» addedDate|string|false|none|none|
|» linkedWorkOrderId|string|false|none|none|
|» isClientViewable|boolean|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Add attachment to the Request

<a id="opIdaddAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request/{id}/attachment \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}/attachment");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request/{id}/attachment', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request/{id}/attachment`

Add attachment to the Request in Request Domain

> Body parameter

```json
[
  {
    "attachmentData": {
      "id": "string",
      "name": "string",
      "mimetype": "string",
      "extension": "string",
      "type": "string",
      "status": "string",
      "tenantId": "string",
      "storageAccount": "string",
      "container": "string",
      "fileMd5": "string",
      "createdTime": "string",
      "createdBy": "string"
    },
    "attachmentRelatedObjects": {
      "id": "string",
      "orgs": [
        "string"
      ],
      "objectId": "string",
      "objectType": "string",
      "createTime": "string",
      "createdBy": "string",
      "description": "string"
    }
  }
]
```

<h3 id="add-attachment-to-the-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|id|path|string|true|none|
|body|body|[AttachmentDTO](#schemaattachmentdto)|true|none|

> Example responses

> 201 Response

```json
{
  "attachmentData": {
    "id": "string",
    "name": "string",
    "mimetype": "string",
    "extension": "string",
    "type": "string",
    "status": "string",
    "tenantId": "string",
    "storageAccount": "string",
    "container": "string",
    "fileMd5": "string",
    "createdTime": "string",
    "createdBy": "string"
  },
  "attachmentRelatedObjects": {
    "id": "string",
    "orgs": [
      "string"
    ],
    "objectId": "string",
    "objectType": "string",
    "createTime": "string",
    "createdBy": "string",
    "description": "string"
  }
}
```

<h3 id="add-attachment-to-the-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Created|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="add-attachment-to-the-request-responseschema">Response Schema</h3>

Status Code **201**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» mimetype|string|false|none|none|
|»» extension|string|false|none|none|
|»» type|string|false|none|none|
|»» status|string|false|none|none|
|»» tenantId|string|false|none|none|
|»» storageAccount|string|false|none|none|
|»» container|string|false|none|none|
|»» fileMd5|string|false|none|none|
|»» createdTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»» id|string|false|none|none|
|»» orgs|[string]|false|none|none|
|»» objectId|string|false|none|none|
|»» objectType|string|false|none|none|
|»» createTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|»» description|string|false|none|none|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» mimetype|string|false|none|none|
|»» extension|string|false|none|none|
|»» type|string|false|none|none|
|»» status|string|false|none|none|
|»» tenantId|string|false|none|none|
|»» storageAccount|string|false|none|none|
|»» container|string|false|none|none|
|»» fileMd5|string|false|none|none|
|»» createdTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»» id|string|false|none|none|
|»» orgs|[string]|false|none|none|
|»» objectId|string|false|none|none|
|»» objectType|string|false|none|none|
|»» createTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|»» description|string|false|none|none|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» mimetype|string|false|none|none|
|»» extension|string|false|none|none|
|»» type|string|false|none|none|
|»» status|string|false|none|none|
|»» tenantId|string|false|none|none|
|»» storageAccount|string|false|none|none|
|»» container|string|false|none|none|
|»» fileMd5|string|false|none|none|
|»» createdTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»» id|string|false|none|none|
|»» orgs|[string]|false|none|none|
|»» objectId|string|false|none|none|
|»» objectType|string|false|none|none|
|»» createTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|»» description|string|false|none|none|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» mimetype|string|false|none|none|
|»» extension|string|false|none|none|
|»» type|string|false|none|none|
|»» status|string|false|none|none|
|»» tenantId|string|false|none|none|
|»» storageAccount|string|false|none|none|
|»» container|string|false|none|none|
|»» fileMd5|string|false|none|none|
|»» createdTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»» id|string|false|none|none|
|»» orgs|[string]|false|none|none|
|»» objectId|string|false|none|none|
|»» objectType|string|false|none|none|
|»» createTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|»» description|string|false|none|none|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|» attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|»» id|string|false|none|none|
|»» name|string|false|none|none|
|»» mimetype|string|false|none|none|
|»» extension|string|false|none|none|
|»» type|string|false|none|none|
|»» status|string|false|none|none|
|»» tenantId|string|false|none|none|
|»» storageAccount|string|false|none|none|
|»» container|string|false|none|none|
|»» fileMd5|string|false|none|none|
|»» createdTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|» attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|
|»» id|string|false|none|none|
|»» orgs|[string]|false|none|none|
|»» objectId|string|false|none|none|
|»» objectType|string|false|none|none|
|»» createTime|string|false|none|none|
|»» createdBy|string|false|none|none|
|»» description|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## Override Request Details for given request alternate id and customer org

<a id="opIdoverrideRequestDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/request/override?altId=string&action=Approve%20client%20limit \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/override?altId=string&action=Approve%20client%20limit");
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
  'authorization': 'string'
}

r = requests.post('http://localhost:8098/request-core/api/v1/request/override', params={
  'altId': 'string',  'action': 'Approve client limit'
}, headers = headers)

print(r.json())

```

`POST /request-core/api/v1/request/override`

Override Request Details for given request alternate id.

> Body parameter

```json
{
  "property1": {},
  "property2": {}
}
```

<h3 id="override-request-details-for-given-request-alternate-id-and-customer-org-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|altId|query|string|true|none|
|customerOrgId|query|string(uuid)|false|none|
|action|query|string|true|none|
|body|body|object|true|none|
|» **additionalProperties**|body|object|false|none|

> Example responses

> 201 Response

<h3 id="override-request-details-for-given-request-alternate-id-and-customer-org-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|Request overridden successfully|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="override-request-details-for-given-request-alternate-id-and-customer-org-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Get Request Details for given request id

<a id="opIdgetRequestDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/request/{id} \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/request/{id}', headers = headers)

print(r.json())

```

`GET /request-core/api/v1/request/{id}`

Get Request Details for given request id.

<h3 id="get-request-details-for-given-request-id-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|status|query|string|false|none|
|id|path|string|true|none|
|tenantId|query|string|false|none|

> Example responses

> 200 Response

<h3 id="get-request-details-for-given-request-id-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|List of Service Requests|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="get-request-details-for-given-request-id-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Get Request Details for given request alternate id and customer org

<a id="opIdgetRequestDetailsByAltIdAndOrg"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/request/override/details?altId=string \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/override/details?altId=string");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/request/override/details', params={
  'altId': 'string'
}, headers = headers)

print(r.json())

```

`GET /request-core/api/v1/request/override/details`

Get Request Details for given request alternate id.

<h3 id="get-request-details-for-given-request-alternate-id-and-customer-org-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|altId|query|string|true|none|
|customerOrgId|query|string(uuid)|false|none|

> Example responses

> 200 Response

<h3 id="get-request-details-for-given-request-alternate-id-and-customer-org-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Found request|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="get-request-details-for-given-request-alternate-id-and-customer-org-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## Delete Watcher(s) from Request WatchList

<a id="opIddeleteWatcher"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-core/api/v1/request/{requestId}/watcher/{watcherIds} \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{requestId}/watcher/{watcherIds}");
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
  'authorization': 'string'
}

r = requests.delete('http://localhost:8098/request-core/api/v1/request/{requestId}/watcher/{watcherIds}', headers = headers)

print(r.json())

```

`DELETE /request-core/api/v1/request/{requestId}/watcher/{watcherIds}`

Delete Watcher(s) from Request in Request Domain

<h3 id="delete-watcher(s)-from-request-watchlist-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|requestId|path|string(uuid)|true|none|
|watcherIds|path|string|true|none|

<h3 id="delete-watcher(s)-from-request-watchlist-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Deleted|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|None|

<aside class="success">
This operation does not require authentication
</aside>

## Delete an attachment from Request

<a id="opIddeleteAttachment"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-core/api/v1/request/{id}/attachment/{attachmentRelatedId} \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/request/{id}/attachment/{attachmentRelatedId}");
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
  'authorization': 'string'
}

r = requests.delete('http://localhost:8098/request-core/api/v1/request/{id}/attachment/{attachmentRelatedId}', headers = headers)

print(r.json())

```

`DELETE /request-core/api/v1/request/{id}/attachment/{attachmentRelatedId}`

Delete an attachment from Request in Request Domain

<h3 id="delete-an-attachment-from-request-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|id|path|string|true|none|
|attachmentRelatedId|path|string|true|none|

<h3 id="delete-an-attachment-from-request-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Deleted|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Service Requests Not Found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|None|

<aside class="success">
This operation does not require authentication
</aside>

## Deletes cache from the in-memory

<a id="opIddeleteCache"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE http://localhost:8098/request-core/api/v1/clearRefDataCache \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/clearRefDataCache");
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
  'authorization': 'string'
}

r = requests.delete('http://localhost:8098/request-core/api/v1/clearRefDataCache', headers = headers)

print(r.json())

```

`DELETE /request-core/api/v1/clearRefDataCache`

Evicts reference data cache from the in-memory

<h3 id="deletes-cache-from-the-in-memory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|

> Example responses

> 204 Response

<h3 id="deletes-cache-from-the-in-memory-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|Deleted|string|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|string|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|string|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|string|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|string|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-approvals-controller">Approvals</h1>

## processDecision

<a id="opIdprocessDecision"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT http://localhost:8098/request-core/api/v1/approvals?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Content-Type: application/json' \
  -H 'Authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/approvals?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'Authorization': 'string'
}

r = requests.put('http://localhost:8098/request-core/api/v1/approvals', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`PUT /request-core/api/v1/approvals`

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

<h3 id="processdecision-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|Authorization|header|string|true|none|
|orgs|query|array[string]|true|none|
|body|body|[FactApprovalDecisionDTO](#schemafactapprovaldecisiondto)|true|none|

<h3 id="processdecision-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|None|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|None|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|None|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|None|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|None|

<aside class="success">
This operation does not require authentication
</aside>

## getApprovals

<a id="opIdgetApprovals"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/approvals/{personId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08 \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/approvals/{personId}?orgs=497f6eca-6276-4993-bfeb-53cbbbba6f08");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/approvals/{personId}', params={
  'orgs': [
  "497f6eca-6276-4993-bfeb-53cbbbba6f08"
]
}, headers = headers)

print(r.json())

```

`GET /request-core/api/v1/approvals/{personId}`

<h3 id="getapprovals-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|
|authorization|header|string|true|none|
|orgs|query|array[string]|true|none|

> Example responses

> 200 Response

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
      "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
      "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
      "delegator": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "step": 0,
      "alternateId": "string",
      "tenantId": "string",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "orgName": "string",
      "capability": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "description": "string",
      "personLimit": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "value": "string",
        "unit": "string"
      },
      "createdDate": "2019-08-24T14:15:22Z",
      "requester": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "requesterId": "ba828041-f5bf-46f6-bf7c-22eccb01f2a4",
      "status": "ACTIVE",
      "delegate": true
    }
  ],
  "number": 0,
  "sort": [
    {
      "direction": "string",
      "nullHandling": "string",
      "ascending": true,
      "property": "string",
      "ignoreCase": true
    }
  ],
  "first": true,
  "last": true,
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": [
      {
        "direction": "string",
        "nullHandling": "string",
        "ascending": true,
        "property": "string",
        "ignoreCase": true
      }
    ],
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "empty": true
}
```

<h3 id="getapprovals-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[PageRequestChainListViewDTO](#schemapagerequestchainlistviewdto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[PageRequestChainListViewDTO](#schemapagerequestchainlistviewdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[PageRequestChainListViewDTO](#schemapagerequestchainlistviewdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[PageRequestChainListViewDTO](#schemapagerequestchainlistviewdto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[PageRequestChainListViewDTO](#schemapagerequestchainlistviewdto)|

<aside class="success">
This operation does not require authentication
</aside>

## Get Request chain Details for given factId and personId

<a id="opIdgetRequestChainDetails"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/approvals/{personId}/{factId} \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/approvals/{personId}/{factId}");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/approvals/{personId}/{factId}', headers = headers)

print(r.json())

```

`GET /request-core/api/v1/approvals/{personId}/{factId}`

Get Request chain Details for given factId and personId.

<h3 id="get-request-chain-details-for-given-factid-and-personid-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|factId|path|string(uuid)|true|none|
|personId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
  "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
  "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
  "alternateId": "string",
  "orgs": [
    "string"
  ],
  "capability": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string"
  },
  "description": "string",
  "decisionFlag": true,
  "requestRevisionFlag": true,
  "capabilityLimit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "value": "string",
    "unit": "string"
  },
  "createdDate": "2019-08-24T14:15:22Z",
  "requester": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "status": "ACTIVE",
  "approvalDeadline": "2019-08-24T14:15:22Z",
  "steps": [
    {
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "step": 0,
      "when": "string",
      "appoversCount": 0,
      "approvers": [
        {
          "approver": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "limit": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "name": "string",
            "value": "string",
            "unit": "string"
          },
          "delegator": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "decisionDate": "string",
          "status": "Approved",
          "delegate": true,
          "isDelegate": true
        }
      ],
      "approvalRule": "string",
      "activeStep": true,
      "isActiveStep": true
    }
  ],
  "comments": [
    {
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "decisionDate": "string",
      "comment": "string",
      "status": "Approved"
    }
  ]
}
```

<h3 id="get-request-chain-details-for-given-factid-and-personid-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Request chain details found|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Requests chain details Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="get-request-chain-details-for-given-factid-and-personid-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainViewDetailsDTO](#schemarequestchainviewdetailsdto)]|false|none|none|
|» chainId|string(uuid)|false|none|none|
|» subStateId|string(uuid)|false|none|none|
|» factId|string(uuid)|false|none|none|
|» alternateId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|» description|string|false|none|none|
|» decisionFlag|boolean|false|none|none|
|» requestRevisionFlag|boolean|false|none|none|
|» capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|»» value|string|false|none|none|
|»» unit|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» personId|string|false|none|none|
|»» firstName|string|false|none|none|
|»» lastName|string|false|none|none|
|»» fullName|string|false|none|none|
|»» locale|string|false|none|none|
|»» telephone|string|false|none|none|
|»» email|string|false|none|none|
|» status|string|false|none|none|
|» approvalDeadline|string(date-time)|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainViewDetailsDTO](#schemarequestchainviewdetailsdto)]|false|none|none|
|» chainId|string(uuid)|false|none|none|
|» subStateId|string(uuid)|false|none|none|
|» factId|string(uuid)|false|none|none|
|» alternateId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|» description|string|false|none|none|
|» decisionFlag|boolean|false|none|none|
|» requestRevisionFlag|boolean|false|none|none|
|» capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|»» value|string|false|none|none|
|»» unit|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» personId|string|false|none|none|
|»» firstName|string|false|none|none|
|»» lastName|string|false|none|none|
|»» fullName|string|false|none|none|
|»» locale|string|false|none|none|
|»» telephone|string|false|none|none|
|»» email|string|false|none|none|
|» status|string|false|none|none|
|» approvalDeadline|string(date-time)|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainViewDetailsDTO](#schemarequestchainviewdetailsdto)]|false|none|none|
|» chainId|string(uuid)|false|none|none|
|» subStateId|string(uuid)|false|none|none|
|» factId|string(uuid)|false|none|none|
|» alternateId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|» description|string|false|none|none|
|» decisionFlag|boolean|false|none|none|
|» requestRevisionFlag|boolean|false|none|none|
|» capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|»» value|string|false|none|none|
|»» unit|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» personId|string|false|none|none|
|»» firstName|string|false|none|none|
|»» lastName|string|false|none|none|
|»» fullName|string|false|none|none|
|»» locale|string|false|none|none|
|»» telephone|string|false|none|none|
|»» email|string|false|none|none|
|» status|string|false|none|none|
|» approvalDeadline|string(date-time)|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainViewDetailsDTO](#schemarequestchainviewdetailsdto)]|false|none|none|
|» chainId|string(uuid)|false|none|none|
|» subStateId|string(uuid)|false|none|none|
|» factId|string(uuid)|false|none|none|
|» alternateId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|» description|string|false|none|none|
|» decisionFlag|boolean|false|none|none|
|» requestRevisionFlag|boolean|false|none|none|
|» capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|»» value|string|false|none|none|
|»» unit|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» personId|string|false|none|none|
|»» firstName|string|false|none|none|
|»» lastName|string|false|none|none|
|»» fullName|string|false|none|none|
|»» locale|string|false|none|none|
|»» telephone|string|false|none|none|
|»» email|string|false|none|none|
|» status|string|false|none|none|
|» approvalDeadline|string(date-time)|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainViewDetailsDTO](#schemarequestchainviewdetailsdto)]|false|none|none|
|» chainId|string(uuid)|false|none|none|
|» subStateId|string(uuid)|false|none|none|
|» factId|string(uuid)|false|none|none|
|» alternateId|string|false|none|none|
|» orgs|[string]|false|none|none|
|» capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|» description|string|false|none|none|
|» decisionFlag|boolean|false|none|none|
|» requestRevisionFlag|boolean|false|none|none|
|» capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»» id|string(uuid)|false|none|none|
|»» name|string|false|none|none|
|»» value|string|false|none|none|
|»» unit|string|false|none|none|
|» createdDate|string(date-time)|false|none|none|
|» requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» personId|string|false|none|none|
|»» firstName|string|false|none|none|
|»» lastName|string|false|none|none|
|»» fullName|string|false|none|none|
|»» locale|string|false|none|none|
|»» telephone|string|false|none|none|
|»» email|string|false|none|none|
|» status|string|false|none|none|
|» approvalDeadline|string(date-time)|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

<aside class="success">
This operation does not require authentication
</aside>

## getApprovalChainDetailsHistory

<a id="opIdgetApprovalChainDetailsHistory"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/approvals/history/{subStateId} \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/approvals/history/{subStateId}");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/approvals/history/{subStateId}', headers = headers)

print(r.json())

```

`GET /request-core/api/v1/approvals/history/{subStateId}`

<h3 id="getapprovalchaindetailshistory-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|authorization|header|string|true|none|
|subStateId|path|string(uuid)|true|none|

> Example responses

> 200 Response

```json
{
  "steps": [
    {
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "step": 0,
      "when": "string",
      "appoversCount": 0,
      "approvers": [
        {
          "approver": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "limit": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "name": "string",
            "value": "string",
            "unit": "string"
          },
          "delegator": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "decisionDate": "string",
          "status": "Approved",
          "delegate": true,
          "isDelegate": true
        }
      ],
      "approvalRule": "string",
      "activeStep": true,
      "isActiveStep": true
    }
  ],
  "comments": [
    {
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "decisionDate": "string",
      "comment": "string",
      "status": "Approved"
    }
  ]
}
```

<h3 id="getapprovalchaindetailshistory-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|Inline|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|Inline|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|Inline|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|Inline|

<h3 id="getapprovalchaindetailshistory-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainDetailsHistoryDTO](#schemarequestchaindetailshistorydto)]|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»»» personId|string|false|none|none|
|»»»» firstName|string|false|none|none|
|»»»» lastName|string|false|none|none|
|»»»» fullName|string|false|none|none|
|»»»» locale|string|false|none|none|
|»»»» telephone|string|false|none|none|
|»»»» email|string|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» value|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **401**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainDetailsHistoryDTO](#schemarequestchaindetailshistorydto)]|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»»» personId|string|false|none|none|
|»»»» firstName|string|false|none|none|
|»»»» lastName|string|false|none|none|
|»»»» fullName|string|false|none|none|
|»»»» locale|string|false|none|none|
|»»»» telephone|string|false|none|none|
|»»»» email|string|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» value|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **403**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainDetailsHistoryDTO](#schemarequestchaindetailshistorydto)]|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»»» personId|string|false|none|none|
|»»»» firstName|string|false|none|none|
|»»»» lastName|string|false|none|none|
|»»»» fullName|string|false|none|none|
|»»»» locale|string|false|none|none|
|»»»» telephone|string|false|none|none|
|»»»» email|string|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» value|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **404**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainDetailsHistoryDTO](#schemarequestchaindetailshistorydto)]|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»»» personId|string|false|none|none|
|»»»» firstName|string|false|none|none|
|»»»» lastName|string|false|none|none|
|»»»» fullName|string|false|none|none|
|»»»» locale|string|false|none|none|
|»»»» telephone|string|false|none|none|
|»»»» email|string|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» value|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

Status Code **500**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[RequestChainDetailsHistoryDTO](#schemarequestchaindetailshistorydto)]|false|none|none|
|» steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|»» generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|»»» id|string(uuid)|false|none|none|
|»»» name|string|false|none|none|
|»» step|integer(int32)|false|none|none|
|»» when|string|false|none|none|
|»» appoversCount|integer(int32)|false|none|none|
|»» approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|»»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»»» personId|string|false|none|none|
|»»»» firstName|string|false|none|none|
|»»»» lastName|string|false|none|none|
|»»»» fullName|string|false|none|none|
|»»»» locale|string|false|none|none|
|»»»» telephone|string|false|none|none|
|»»»» email|string|false|none|none|
|»»» limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|»»»» id|string(uuid)|false|none|none|
|»»»» name|string|false|none|none|
|»»»» value|string|false|none|none|
|»»»» unit|string|false|none|none|
|»»» delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»»» decisionDate|string|false|none|none|
|»»» status|string|false|none|none|
|»»» delegate|boolean|false|none|none|
|»»» isDelegate|boolean|false|none|none|
|»» approvalRule|string|false|none|none|
|»» activeStep|boolean|false|none|none|
|»» isActiveStep|boolean|false|none|none|
|» comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|
|»» approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|»» decisionDate|string|false|none|none|
|»» comment|string|false|none|none|
|»» status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|
|status|Approved|
|status|Declined|

<aside class="success">
This operation does not require authentication
</aside>

## getApprovalsCount

<a id="opIdgetApprovalsCount"></a>

> Code samples

```shell
# You can also use wget
curl -X GET http://localhost:8098/request-core/api/v1/approvals/count/{personId} \
  -H 'Accept: */*' \
  -H 'authorization: string'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/approvals/count/{personId}");
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
  'authorization': 'string'
}

r = requests.get('http://localhost:8098/request-core/api/v1/approvals/count/{personId}', headers = headers)

print(r.json())

```

`GET /request-core/api/v1/approvals/count/{personId}`

<h3 id="getapprovalscount-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|personId|path|string|true|none|
|authorization|header|string|true|none|

> Example responses

> 200 Response

<h3 id="getapprovalscount-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|integer|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|integer|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|integer|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|integer|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|integer|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-migration-admin-controller">Migration Admin</h1>

## reprocessFailedMigratedWorkOrders

<a id="opIdreprocessFailedMigratedWorkOrders"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/migration/admin/api/v1/reprocess-failed-migrated-work-orders \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*'

```

```java
URL obj = new URL("http://localhost:8098/request-core/migration/admin/api/v1/reprocess-failed-migrated-work-orders");
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
  'Accept': '*/*'
}

r = requests.post('http://localhost:8098/request-core/migration/admin/api/v1/reprocess-failed-migrated-work-orders', headers = headers)

print(r.json())

```

`POST /request-core/migration/admin/api/v1/reprocess-failed-migrated-work-orders`

> Body parameter

```json
{
  "messageIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}
```

<h3 id="reprocessfailedmigratedworkorders-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[MessageIdsPayload](#schemamessageidspayload)|true|none|

> Example responses

> 200 Response

<h3 id="reprocessfailedmigratedworkorders-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|Inline|

<h3 id="reprocessfailedmigratedworkorders-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|» **additionalProperties**|string|false|none|none|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="openapi-definition-chart-controller">Chart</h1>

## createChart

<a id="opIdcreateChart"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/charts \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/charts");
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
  'Accept': '*/*'
}

r = requests.post('http://localhost:8098/request-core/api/v1/charts', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/charts`

> Body parameter

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "object": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "globalOrgId": "03378aa8-9494-48fd-a5c7-dd47fb2149d8",
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "existingCharts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ]
}
```

<h3 id="createchart-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ChartBuilderExtendedPropertiesDTO](#schemachartbuilderextendedpropertiesdto)|true|none|

> Example responses

> 200 Response

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "source": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ]
}
```

<h3 id="createchart-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ChartObjectDTO](#schemachartobjectdto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ChartObjectDTO](#schemachartobjectdto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ChartObjectDTO](#schemachartobjectdto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[ChartObjectDTO](#schemachartobjectdto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[ChartObjectDTO](#schemachartobjectdto)|

<aside class="success">
This operation does not require authentication
</aside>

## updateChartDefinition

<a id="opIdupdateChartDefinition"></a>

> Code samples

```shell
# You can also use wget
curl -X POST http://localhost:8098/request-core/api/v1/charts/chartDefinition \
  -H 'Content-Type: application/json' \
  -H 'Accept: */*'

```

```java
URL obj = new URL("http://localhost:8098/request-core/api/v1/charts/chartDefinition");
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
  'Accept': '*/*'
}

r = requests.post('http://localhost:8098/request-core/api/v1/charts/chartDefinition', headers = headers)

print(r.json())

```

`POST /request-core/api/v1/charts/chartDefinition`

> Body parameter

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "status": "ACTIVE",
  "orgs": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "structure": "string"
    }
  ],
  "version": 0,
  "object": "string",
  "dimensionDefinitions": [
    {
      "name": "string",
      "type": "string",
      "seqNo": 0,
      "regexExpression": "string",
      "defaultValue": "string",
      "sourceDefs": [
        {
          "buildOrder": 0,
          "components": [
            {
              "propertyPath": "string",
              "prefix": "string",
              "suffix": "string",
              "regexPattern": "string",
              "presentationPath": "string"
            }
          ]
        }
      ]
    }
  ]
}
```

<h3 id="updatechartdefinition-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[ChartDefinitionDTO](#schemachartdefinitiondto)|true|none|

> Example responses

> 200 Response

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "status": "ACTIVE",
  "orgs": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "structure": "string"
    }
  ],
  "version": 0,
  "object": "string",
  "dimensionDefinitions": [
    {
      "name": "string",
      "type": "string",
      "seqNo": 0,
      "regexExpression": "string",
      "defaultValue": "string",
      "sourceDefs": [
        {
          "buildOrder": 0,
          "components": [
            {
              "propertyPath": "string",
              "prefix": "string",
              "suffix": "string",
              "regexPattern": "string",
              "presentationPath": "string"
            }
          ]
        }
      ]
    }
  ]
}
```

<h3 id="updatechartdefinition-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|OK|[ChartDefinitionDTO](#schemachartdefinitiondto)|
|401|[Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1)|Unauthorized|[ChartDefinitionDTO](#schemachartdefinitiondto)|
|403|[Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)|Forbidden|[ChartDefinitionDTO](#schemachartdefinitiondto)|
|404|[Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)|Resource Not Found|[ChartDefinitionDTO](#schemachartdefinitiondto)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Custom runtime errors|[ChartDefinitionDTO](#schemachartdefinitiondto)|

<aside class="success">
This operation does not require authentication
</aside>

# Request Core Schemas

<h2 id="tocS_AttachmentDTO">AttachmentDTO</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentdto"></a>
<a id="schema_AttachmentDTO"></a>
<a id="tocSattachmentdto"></a>
<a id="tocsattachmentdto"></a>

```json
{
  "attachmentData": {
    "id": "string",
    "name": "string",
    "mimetype": "string",
    "extension": "string",
    "type": "string",
    "status": "string",
    "tenantId": "string",
    "storageAccount": "string",
    "container": "string",
    "fileMd5": "string",
    "createdTime": "string",
    "createdBy": "string"
  },
  "attachmentRelatedObjects": {
    "id": "string",
    "orgs": [
      "string"
    ],
    "objectId": "string",
    "objectType": "string",
    "createTime": "string",
    "createdBy": "string",
    "description": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|attachmentData|[AttachmentDataDTO](#schemaattachmentdatadto)|false|none|none|
|attachmentRelatedObjects|[AttachmentRelatedObjectsDTO](#schemaattachmentrelatedobjectsdto)|false|none|none|

<h2 id="tocS_AttachmentDataDTO">AttachmentDataDTO</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentdatadto"></a>
<a id="schema_AttachmentDataDTO"></a>
<a id="tocSattachmentdatadto"></a>
<a id="tocsattachmentdatadto"></a>

```json
{
  "id": "string",
  "name": "string",
  "mimetype": "string",
  "extension": "string",
  "type": "string",
  "status": "string",
  "tenantId": "string",
  "storageAccount": "string",
  "container": "string",
  "fileMd5": "string",
  "createdTime": "string",
  "createdBy": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|
|mimetype|string|false|none|none|
|extension|string|false|none|none|
|type|string|false|none|none|
|status|string|false|none|none|
|tenantId|string|false|none|none|
|storageAccount|string|false|none|none|
|container|string|false|none|none|
|fileMd5|string|false|none|none|
|createdTime|string|false|none|none|
|createdBy|string|false|none|none|

<h2 id="tocS_AttachmentRelatedObjectsDTO">AttachmentRelatedObjectsDTO</h2>
<!-- backwards compatibility -->
<a id="schemaattachmentrelatedobjectsdto"></a>
<a id="schema_AttachmentRelatedObjectsDTO"></a>
<a id="tocSattachmentrelatedobjectsdto"></a>
<a id="tocsattachmentrelatedobjectsdto"></a>

```json
{
  "id": "string",
  "orgs": [
    "string"
  ],
  "objectId": "string",
  "objectType": "string",
  "createTime": "string",
  "createdBy": "string",
  "description": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|orgs|[string]|false|none|none|
|objectId|string|false|none|none|
|objectType|string|false|none|none|
|createTime|string|false|none|none|
|createdBy|string|false|none|none|
|description|string|false|none|none|

<h2 id="tocS_ChartDTO">ChartDTO</h2>
<!-- backwards compatibility -->
<a id="schemachartdto"></a>
<a id="schema_ChartDTO"></a>
<a id="tocSchartdto"></a>
<a id="tocschartdto"></a>

```json
{
  "chartId": "string",
  "requestId": "string",
  "version": "string",
  "createdDate": "string",
  "chartName": "string",
  "dimensionName": "string",
  "dimensionPosition": "string",
  "dimensionValue": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|chartId|string|false|none|none|
|requestId|string|false|none|none|
|version|string|false|none|none|
|createdDate|string|false|none|none|
|chartName|string|false|none|none|
|dimensionName|string|false|none|none|
|dimensionPosition|string|false|none|none|
|dimensionValue|string|false|none|none|

<h2 id="tocS_CommentDTO">CommentDTO</h2>
<!-- backwards compatibility -->
<a id="schemacommentdto"></a>
<a id="schema_CommentDTO"></a>
<a id="tocScommentdto"></a>
<a id="tocscommentdto"></a>

```json
{
  "commentId": "string",
  "requestId": "string",
  "addedByPersonId": "string",
  "source": "string",
  "comment": "string",
  "type": "string",
  "orgType": "string",
  "linkedWOCommentId": "string",
  "addedDate": "string",
  "linkedWorkOrderId": "string",
  "isClientViewable": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|commentId|string|false|none|none|
|requestId|string|false|none|none|
|addedByPersonId|string|false|none|none|
|source|string|false|none|none|
|comment|string|false|none|none|
|type|string|false|none|none|
|orgType|string|false|none|none|
|linkedWOCommentId|string|false|none|none|
|addedDate|string|false|none|none|
|linkedWorkOrderId|string|false|none|none|
|isClientViewable|boolean|false|none|none|

<h2 id="tocS_MiscExtendedPropertiesDTO">MiscExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemamiscextendedpropertiesdto"></a>
<a id="schema_MiscExtendedPropertiesDTO"></a>
<a id="tocSmiscextendedpropertiesdto"></a>
<a id="tocsmiscextendedpropertiesdto"></a>

```json
{
  "serviceClassification": [
    {
      "id": "string",
      "value": [
        "string"
      ]
    }
  ],
  "isFlagged": true,
  "flaggedId": "string",
  "flagReason": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|serviceClassification|[[MiscServiceClassificationDTO](#schemamiscserviceclassificationdto)]|false|none|none|
|isFlagged|boolean|false|none|none|
|flaggedId|string|false|none|none|
|flagReason|string|false|none|none|

<h2 id="tocS_MiscServiceClassificationDTO">MiscServiceClassificationDTO</h2>
<!-- backwards compatibility -->
<a id="schemamiscserviceclassificationdto"></a>
<a id="schema_MiscServiceClassificationDTO"></a>
<a id="tocSmiscserviceclassificationdto"></a>
<a id="tocsmiscserviceclassificationdto"></a>

```json
{
  "id": "string",
  "value": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|value|[string]|false|none|none|

<h2 id="tocS_PMDetailsDTO">PMDetailsDTO</h2>
<!-- backwards compatibility -->
<a id="schemapmdetailsdto"></a>
<a id="schema_PMDetailsDTO"></a>
<a id="tocSpmdetailsdto"></a>
<a id="tocspmdetailsdto"></a>

```json
{
  "pmId": "string",
  "pmAlternateId": "string",
  "pmConfigUrl": "string",
  "planId": "string",
  "type": "string",
  "primaryLocationId": "string",
  "maintenanceFrequency": "string",
  "maintenanceFrequencyUnit": "string",
  "interval": "string",
  "totalSequences": "string",
  "sequences": [
    {
      "sequence": 0,
      "locationId": "string",
      "assetId": "string",
      "positionId": "string"
    }
  ],
  "providerId": "string",
  "providerType": "string",
  "providerReferenceId": "string",
  "assignmentOverride": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|pmId|string|false|none|none|
|pmAlternateId|string|false|none|none|
|pmConfigUrl|string|false|none|none|
|planId|string|false|none|none|
|type|string|false|none|none|
|primaryLocationId|string|false|none|none|
|maintenanceFrequency|string|false|none|none|
|maintenanceFrequencyUnit|string|false|none|none|
|interval|string|false|none|none|
|totalSequences|string|false|none|none|
|sequences|[[SequenceDTO](#schemasequencedto)]|false|none|none|
|providerId|string|false|none|none|
|providerType|string|false|none|none|
|providerReferenceId|string|false|none|none|
|assignmentOverride|boolean|false|none|none|

<h2 id="tocS_RequestBodyDTO">RequestBodyDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestbodydto"></a>
<a id="schema_RequestBodyDTO"></a>
<a id="tocSrequestbodydto"></a>
<a id="tocsrequestbodydto"></a>

```json
{
  "id": "string",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "subStatusId": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "relatedServiceClassificationId": [
    "string"
  ],
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "startDate": "string",
  "modifiedDate": "string",
  "description": "string",
  "chart": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|tenantId|string|false|none|none|
|assetId|string|false|none|none|
|orgs|[string]|false|none|none|
|alternateId|string|false|none|none|
|statusId|string|false|none|none|
|subStatusId|string|false|none|none|
|createdBy|string|false|none|none|
|modifiedBy|string|false|none|none|
|requestorId|string|false|none|none|
|ownerId|string|false|none|none|
|locationId|string|false|none|none|
|positionId|string|false|none|none|
|serviceClassificationId|string|false|none|none|
|miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|relatedServiceClassificationId|[string]|false|none|none|
|source|string|false|none|none|
|isFlagged|boolean|false|none|none|
|isPrivate|boolean|false|none|none|
|priorityId|string|false|none|none|
|watchers|[string]|false|none|none|
|sourceApp|string|false|none|none|
|lastAssessmentDate|string|false|none|none|
|lastAssessmentTrigger|string|false|none|none|
|createdDate|string|false|none|none|
|reportedDate|string|false|none|none|
|startDate|string|false|none|none|
|modifiedDate|string|false|none|none|
|description|string|false|none|none|
|chart|[[ChartDTO](#schemachartdto)]|false|none|none|
|comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|

<h2 id="tocS_SequenceDTO">SequenceDTO</h2>
<!-- backwards compatibility -->
<a id="schemasequencedto"></a>
<a id="schema_SequenceDTO"></a>
<a id="tocSsequencedto"></a>
<a id="tocssequencedto"></a>

```json
{
  "sequence": 0,
  "locationId": "string",
  "assetId": "string",
  "positionId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|sequence|integer(int32)|false|none|none|
|locationId|string|false|none|none|
|assetId|string|false|none|none|
|positionId|string|false|none|none|

<h2 id="tocS_ServiceLevelAgreementDTO">ServiceLevelAgreementDTO</h2>
<!-- backwards compatibility -->
<a id="schemaservicelevelagreementdto"></a>
<a id="schema_ServiceLevelAgreementDTO"></a>
<a id="tocSservicelevelagreementdto"></a>
<a id="tocsservicelevelagreementdto"></a>

```json
{
  "id": "string",
  "requestId": "string",
  "name": "string",
  "timeAllotted": 0,
  "unit": "string",
  "targetTime": "string",
  "overriddenDate": "string",
  "overriddenReason": "string",
  "overriddenBy": "string",
  "slaMetDate": "string",
  "slaMetWO": "string",
  "slaMetDatet": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|requestId|string|false|none|none|
|name|string|false|none|none|
|timeAllotted|number|false|none|none|
|unit|string|false|none|none|
|targetTime|string|false|none|none|
|overriddenDate|string|false|none|none|
|overriddenReason|string|false|none|none|
|overriddenBy|string|false|none|none|
|slaMetDate|string|false|none|none|
|slaMetWO|string|false|none|none|
|slaMetDatet|string|false|write-only|none|

<h2 id="tocS_SlaTypesDTO">SlaTypesDTO</h2>
<!-- backwards compatibility -->
<a id="schemaslatypesdto"></a>
<a id="schema_SlaTypesDTO"></a>
<a id="tocSslatypesdto"></a>
<a id="tocsslatypesdto"></a>

```json
{
  "id": "string",
  "name": "string",
  "targetDate": "string",
  "overrideDate": "string",
  "overrideReason": "string",
  "overrideBy": "string",
  "slaMetDate": "string",
  "slaMet": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|
|targetDate|string|false|none|none|
|overrideDate|string|false|none|none|
|overrideReason|string|false|none|none|
|overrideBy|string|false|none|none|
|slaMetDate|string|false|none|none|
|slaMet|boolean|false|none|none|

<h2 id="tocS_StatusHistoryDTO">StatusHistoryDTO</h2>
<!-- backwards compatibility -->
<a id="schemastatushistorydto"></a>
<a id="schema_StatusHistoryDTO"></a>
<a id="tocSstatushistorydto"></a>
<a id="tocsstatushistorydto"></a>

```json
{
  "statusId": "string",
  "statusCode": "string",
  "createdDate": "string",
  "updatedBy": "string",
  "subStatusId": "string",
  "subStatusCode": "string",
  "reasonId": "string",
  "version": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|statusId|string|false|none|none|
|statusCode|string|false|none|none|
|createdDate|string|false|none|none|
|updatedBy|string|false|none|none|
|subStatusId|string|false|none|none|
|subStatusCode|string|false|none|none|
|reasonId|string|false|none|none|
|version|integer(int32)|false|none|none|

<h2 id="tocS_WorkOrderCommentDTO">WorkOrderCommentDTO</h2>
<!-- backwards compatibility -->
<a id="schemaworkordercommentdto"></a>
<a id="schema_WorkOrderCommentDTO"></a>
<a id="tocSworkordercommentdto"></a>
<a id="tocsworkordercommentdto"></a>

```json
{
  "commentId": "string",
  "workOrderCommentId": 0,
  "addedByPersonId": "string",
  "comment": "string",
  "commentType": "string",
  "addedDate": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|commentId|string|false|none|none|
|workOrderCommentId|integer(int32)|false|none|none|
|addedByPersonId|string|false|none|none|
|comment|string|false|none|none|
|commentType|string|false|none|none|
|addedDate|string|false|none|none|

<h2 id="tocS_WorkOrderDTO">WorkOrderDTO</h2>
<!-- backwards compatibility -->
<a id="schemaworkorderdto"></a>
<a id="schema_WorkOrderDTO"></a>
<a id="tocSworkorderdto"></a>
<a id="tocsworkorderdto"></a>

```json
{
  "id": "string",
  "description": "string",
  "alternateId": "string",
  "statusId": "string",
  "assigneeName": "string",
  "assignmentType": "string",
  "assigneeId": "string",
  "facilityManagerId": "string",
  "comments": [
    {
      "commentId": "string",
      "workOrderCommentId": 0,
      "addedByPersonId": "string",
      "comment": "string",
      "commentType": "string",
      "addedDate": "string"
    }
  ],
  "slaTypes": [
    {
      "id": "string",
      "name": "string",
      "targetDate": "string",
      "overrideDate": "string",
      "overrideReason": "string",
      "overrideBy": "string",
      "slaMetDate": "string",
      "slaMet": true
    }
  ],
  "nte": 0,
  "subStatusId": "string",
  "subStatusCode": "string",
  "dispatchSiteId": "string",
  "dispatchSiteName": "string",
  "completionDescription": "string",
  "requestedBy": "string",
  "serviceClassificationId": "string",
  "locationId": "string",
  "assetId": "string",
  "createdDate": "string",
  "modifiedDate": "string",
  "assigneeIds": [
    "string"
  ],
  "dispatchSiteIds": [
    "string"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|description|string|false|none|none|
|alternateId|string|false|none|none|
|statusId|string|false|none|none|
|assigneeName|string|false|none|none|
|assignmentType|string|false|none|none|
|assigneeId|string|false|none|none|
|facilityManagerId|string|false|none|none|
|comments|[[WorkOrderCommentDTO](#schemaworkordercommentdto)]|false|none|none|
|slaTypes|[[SlaTypesDTO](#schemaslatypesdto)]|false|none|none|
|nte|number|false|none|none|
|subStatusId|string|false|none|none|
|subStatusCode|string|false|none|none|
|dispatchSiteId|string|false|none|none|
|dispatchSiteName|string|false|none|none|
|completionDescription|string|false|none|none|
|requestedBy|string|false|none|none|
|serviceClassificationId|string|false|none|none|
|locationId|string|false|none|none|
|assetId|string|false|none|none|
|createdDate|string|false|none|none|
|modifiedDate|string|false|none|none|
|assigneeIds|[string]|false|none|none|
|dispatchSiteIds|[string]|false|none|none|

<h2 id="tocS_ActiveStepApproversDTO">ActiveStepApproversDTO</h2>
<!-- backwards compatibility -->
<a id="schemaactivestepapproversdto"></a>
<a id="schema_ActiveStepApproversDTO"></a>
<a id="tocSactivestepapproversdto"></a>
<a id="tocsactivestepapproversdto"></a>

```json
{
  "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
  "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
  "stepNumber": 0,
  "isDelegator": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|approverId|string(uuid)|false|none|none|
|delegatorId|string(uuid)|false|none|none|
|stepNumber|integer(int32)|false|none|none|
|isDelegator|boolean|false|none|none|

<h2 id="tocS_ApproverDTO">ApproverDTO</h2>
<!-- backwards compatibility -->
<a id="schemaapproverdto"></a>
<a id="schema_ApproverDTO"></a>
<a id="tocSapproverdto"></a>
<a id="tocsapproverdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
  "personType": "string",
  "group": 0,
  "sequence": 0,
  "generalization": {
    "id": "string",
    "name": "string",
    "group": "string"
  },
  "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
  "when": "string",
  "responseCount": 0,
  "approvalRule": "string",
  "mandatory": true,
  "decision": {
    "status": "Approved",
    "decisionDate": "string",
    "madeByDelegate": true,
    "decisionNote": "string"
  },
  "personLimit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "unit": "string",
    "value": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|personId|string(uuid)|false|none|none|
|personType|string|false|none|none|
|group|integer(int32)|false|none|none|
|sequence|integer(int32)|false|none|none|
|generalization|[AuthResponseGeneralizationDTO](#schemaauthresponsegeneralizationdto)|false|none|none|
|authScopeId|string(uuid)|false|none|none|
|when|string|false|none|none|
|responseCount|integer(int32)|false|none|none|
|approvalRule|string|false|none|none|
|mandatory|boolean|false|none|none|
|decision|[DecisionDTO](#schemadecisiondto)|false|none|none|
|personLimit|[LimitDTO](#schemalimitdto)|false|none|none|

<h2 id="tocS_AuthResponseGeneralizationDTO">AuthResponseGeneralizationDTO</h2>
<!-- backwards compatibility -->
<a id="schemaauthresponsegeneralizationdto"></a>
<a id="schema_AuthResponseGeneralizationDTO"></a>
<a id="tocSauthresponsegeneralizationdto"></a>
<a id="tocsauthresponsegeneralizationdto"></a>

```json
{
  "id": "string",
  "name": "string",
  "group": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|
|group|string|false|none|none|

<h2 id="tocS_ChainDTO">ChainDTO</h2>
<!-- backwards compatibility -->
<a id="schemachaindto"></a>
<a id="schema_ChainDTO"></a>
<a id="tocSchaindto"></a>
<a id="tocschaindto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "majorVersion": 0,
  "minorVersion": 0,
  "createdDate": "string",
  "updatedTime": "string",
  "source": "string",
  "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
  "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
  "capabilityTtl": "string",
  "capabilityName": "string",
  "capabilityLimit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "unit": "string",
    "value": "string"
  },
  "chainDefinitionAlternateId": "string",
  "chainDefinitionVersion": 0,
  "orgs": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "type": "string"
    }
  ],
  "chainStatus": "InProgress",
  "approvers": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
      "personType": "string",
      "group": 0,
      "sequence": 0,
      "generalization": {
        "id": "string",
        "name": "string",
        "group": "string"
      },
      "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
      "when": "string",
      "responseCount": 0,
      "approvalRule": "string",
      "mandatory": true,
      "decision": {
        "status": "Approved",
        "decisionDate": "string",
        "madeByDelegate": true,
        "decisionNote": "string"
      },
      "personLimit": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "unit": "string",
        "value": "string"
      }
    }
  ],
  "delegates": [
    {
      "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
      "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
      "startDate": "2019-08-24T14:15:22Z",
      "endDate": "2019-08-24T14:15:22Z",
      "group": 0
    }
  ],
  "excluded": [
    {
      "excludedApprover": "string",
      "conflictCapability": {
        "id": "string",
        "name": "string"
      },
      "conflictObject": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "type": "string",
        "alternateId": "string"
      }
    }
  ],
  "isRecalculate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|majorVersion|integer(int32)|false|none|none|
|minorVersion|integer(int32)|false|none|none|
|createdDate|string|false|none|none|
|updatedTime|string|false|none|none|
|source|string|false|none|none|
|chainDefinitionId|string(uuid)|false|none|none|
|capabilityId|string(uuid)|false|none|none|
|capabilityTtl|string|false|none|none|
|capabilityName|string|false|none|none|
|capabilityLimit|[LimitDTO](#schemalimitdto)|false|none|none|
|chainDefinitionAlternateId|string|false|none|none|
|chainDefinitionVersion|integer(int32)|false|none|none|
|orgs|[[OrganizationDTO](#schemaorganizationdto)]|false|none|none|
|chainStatus|string|false|none|none|
|approvers|[[ApproverDTO](#schemaapproverdto)]|false|none|none|
|delegates|[[DelegateDTO](#schemadelegatedto)]|false|none|none|
|excluded|[[ExcludedDTO](#schemaexcludeddto)]|false|none|none|
|isRecalculate|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|chainStatus|InProgress|
|chainStatus|Passed|
|chainStatus|Failed|
|chainStatus|Superseded|
|chainStatus|Abandoned|
|chainStatus|Invalid|

<h2 id="tocS_ConflictCapabilityDTO">ConflictCapabilityDTO</h2>
<!-- backwards compatibility -->
<a id="schemaconflictcapabilitydto"></a>
<a id="schema_ConflictCapabilityDTO"></a>
<a id="tocSconflictcapabilitydto"></a>
<a id="tocsconflictcapabilitydto"></a>

```json
{
  "id": "string",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_ConflictObjectDTO">ConflictObjectDTO</h2>
<!-- backwards compatibility -->
<a id="schemaconflictobjectdto"></a>
<a id="schema_ConflictObjectDTO"></a>
<a id="tocSconflictobjectdto"></a>
<a id="tocsconflictobjectdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "type": "string",
  "alternateId": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|type|string|false|none|none|
|alternateId|string|false|none|none|

<h2 id="tocS_DecisionDTO">DecisionDTO</h2>
<!-- backwards compatibility -->
<a id="schemadecisiondto"></a>
<a id="schema_DecisionDTO"></a>
<a id="tocSdecisiondto"></a>
<a id="tocsdecisiondto"></a>

```json
{
  "status": "Approved",
  "decisionDate": "string",
  "madeByDelegate": true,
  "decisionNote": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|status|string|false|none|none|
|decisionDate|string|false|none|none|
|madeByDelegate|boolean|false|none|none|
|decisionNote|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|

<h2 id="tocS_DelegateDTO">DelegateDTO</h2>
<!-- backwards compatibility -->
<a id="schemadelegatedto"></a>
<a id="schema_DelegateDTO"></a>
<a id="tocSdelegatedto"></a>
<a id="tocsdelegatedto"></a>

```json
{
  "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
  "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
  "startDate": "2019-08-24T14:15:22Z",
  "endDate": "2019-08-24T14:15:22Z",
  "group": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|approver|string(uuid)|false|none|none|
|delegatedTo|string(uuid)|false|none|none|
|startDate|string(date-time)|false|none|none|
|endDate|string(date-time)|false|none|none|
|group|integer(int32)|false|none|none|

<h2 id="tocS_ErrorContainer">ErrorContainer</h2>
<!-- backwards compatibility -->
<a id="schemaerrorcontainer"></a>
<a id="schema_ErrorContainer"></a>
<a id="tocSerrorcontainer"></a>
<a id="tocserrorcontainer"></a>

```json
{
  "version": "string",
  "traceId": "string",
  "title": "string",
  "category": "INFO",
  "errors": [
    {
      "id": "string",
      "alternateId": "string",
      "description": "string",
      "domain": "string",
      "messages": [
        {
          "message": "string",
          "code": "string"
        }
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|version|string|false|none|none|
|traceId|string|false|none|none|
|title|string|false|none|none|
|category|string|false|none|none|
|errors|[[ErrorInfo](#schemaerrorinfo)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|category|INFO|
|category|CRITICAL|
|category|WARNING|
|category|BULK|

<h2 id="tocS_ErrorInfo">ErrorInfo</h2>
<!-- backwards compatibility -->
<a id="schemaerrorinfo"></a>
<a id="schema_ErrorInfo"></a>
<a id="tocSerrorinfo"></a>
<a id="tocserrorinfo"></a>

```json
{
  "id": "string",
  "alternateId": "string",
  "description": "string",
  "domain": "string",
  "messages": [
    {
      "message": "string",
      "code": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|alternateId|string|false|none|none|
|description|string|false|none|none|
|domain|string|false|none|none|
|messages|[[ErrorMessage](#schemaerrormessage)]|false|none|none|

<h2 id="tocS_ErrorMessage">ErrorMessage</h2>
<!-- backwards compatibility -->
<a id="schemaerrormessage"></a>
<a id="schema_ErrorMessage"></a>
<a id="tocSerrormessage"></a>
<a id="tocserrormessage"></a>

```json
{
  "message": "string",
  "code": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|message|string|false|none|none|
|code|string|false|none|none|

<h2 id="tocS_ExcludedDTO">ExcludedDTO</h2>
<!-- backwards compatibility -->
<a id="schemaexcludeddto"></a>
<a id="schema_ExcludedDTO"></a>
<a id="tocSexcludeddto"></a>
<a id="tocsexcludeddto"></a>

```json
{
  "excludedApprover": "string",
  "conflictCapability": {
    "id": "string",
    "name": "string"
  },
  "conflictObject": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "type": "string",
    "alternateId": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|excludedApprover|string|false|none|none|
|conflictCapability|[ConflictCapabilityDTO](#schemaconflictcapabilitydto)|false|none|none|
|conflictObject|[ConflictObjectDTO](#schemaconflictobjectdto)|false|none|none|

<h2 id="tocS_ExtendedPropertiesDTO">ExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemaextendedpropertiesdto"></a>
<a id="schema_ExtendedPropertiesDTO"></a>
<a id="tocSextendedpropertiesdto"></a>
<a id="tocsextendedpropertiesdto"></a>

```json
{
  "id": "string",
  "data": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|data|string|false|none|none|

<h2 id="tocS_LimitDTO">LimitDTO</h2>
<!-- backwards compatibility -->
<a id="schemalimitdto"></a>
<a id="schema_LimitDTO"></a>
<a id="tocSlimitdto"></a>
<a id="tocslimitdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "unit": "string",
  "value": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|unit|string|false|none|none|
|value|string|false|none|none|

<h2 id="tocS_MiscellaneousDTO">MiscellaneousDTO</h2>
<!-- backwards compatibility -->
<a id="schemamiscellaneousdto"></a>
<a id="schema_MiscellaneousDTO"></a>
<a id="tocSmiscellaneousdto"></a>
<a id="tocsmiscellaneousdto"></a>

```json
{
  "statusChangeDate": "string",
  "slaAttendDate": "string",
  "slaCompleteDate": "string",
  "slaDispatchDate": "string",
  "slaResponseDate": "string",
  "isFlagged": true,
  "flaggedDate": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|statusChangeDate|string|false|none|none|
|slaAttendDate|string|false|none|none|
|slaCompleteDate|string|false|none|none|
|slaDispatchDate|string|false|none|none|
|slaResponseDate|string|false|none|none|
|isFlagged|boolean|false|none|none|
|flaggedDate|string|false|none|none|

<h2 id="tocS_OrganizationDTO">OrganizationDTO</h2>
<!-- backwards compatibility -->
<a id="schemaorganizationdto"></a>
<a id="schema_OrganizationDTO"></a>
<a id="tocSorganizationdto"></a>
<a id="tocsorganizationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "type": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|type|string|false|none|none|

<h2 id="tocS_ReasonDTO">ReasonDTO</h2>
<!-- backwards compatibility -->
<a id="schemareasondto"></a>
<a id="schema_ReasonDTO"></a>
<a id="tocSreasondto"></a>
<a id="tocsreasondto"></a>

```json
{
  "reasonCode": "string",
  "reasonDescription": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|reasonCode|string|false|none|none|
|reasonDescription|string|false|none|none|

<h2 id="tocS_RequestAuthActionDTO">RequestAuthActionDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestauthactiondto"></a>
<a id="schema_RequestAuthActionDTO"></a>
<a id="tocSrequestauthactiondto"></a>
<a id="tocsrequestauthactiondto"></a>

```json
{
  "name": "string",
  "additionalDetailsKey": "string",
  "additionalDetails": {
    "property1": "string",
    "property2": "string"
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|additionalDetailsKey|string|false|none|none|
|additionalDetails|object|false|none|none|
|» **additionalProperties**|string|false|none|none|

<h2 id="tocS_RequestChainApprovalResponseDTO">RequestChainApprovalResponseDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestchainapprovalresponsedto"></a>
<a id="schema_RequestChainApprovalResponseDTO"></a>
<a id="tocSrequestchainapprovalresponsedto"></a>
<a id="tocsrequestchainapprovalresponsedto"></a>

```json
{
  "activeApprovers": [
    {
      "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
      "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
      "stepNumber": 0,
      "isDelegator": true
    }
  ],
  "chain": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "majorVersion": 0,
    "minorVersion": 0,
    "createdDate": "string",
    "updatedTime": "string",
    "source": "string",
    "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
    "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
    "capabilityTtl": "string",
    "capabilityName": "string",
    "capabilityLimit": {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "unit": "string",
      "value": "string"
    },
    "chainDefinitionAlternateId": "string",
    "chainDefinitionVersion": 0,
    "orgs": [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "type": "string"
      }
    ],
    "chainStatus": "InProgress",
    "approvers": [
      {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
        "personType": "string",
        "group": 0,
        "sequence": 0,
        "generalization": {
          "id": "string",
          "name": "string",
          "group": "string"
        },
        "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
        "when": "string",
        "responseCount": 0,
        "approvalRule": "string",
        "mandatory": true,
        "decision": {
          "status": "Approved",
          "decisionDate": "string",
          "madeByDelegate": true,
          "decisionNote": "string"
        },
        "personLimit": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string",
          "unit": "string",
          "value": "string"
        }
      }
    ],
    "delegates": [
      {
        "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
        "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
        "startDate": "2019-08-24T14:15:22Z",
        "endDate": "2019-08-24T14:15:22Z",
        "group": 0
      }
    ],
    "excluded": [
      {
        "excludedApprover": "string",
        "conflictCapability": {
          "id": "string",
          "name": "string"
        },
        "conflictObject": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "type": "string",
          "alternateId": "string"
        }
      }
    ],
    "isRecalculate": true
  },
  "subStateStatus": "ACTIVE",
  "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|activeApprovers|[[ActiveStepApproversDTO](#schemaactivestepapproversdto)]|false|none|none|
|chain|[ChainDTO](#schemachaindto)|false|none|none|
|subStateStatus|string|false|none|none|
|subStateId|string(uuid)|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|subStateStatus|ACTIVE|
|subStateStatus|DECLINED|
|subStateStatus|APPROVED|
|subStateStatus|RECALLED|
|subStateStatus|EXPIRED|

<h2 id="tocS_RequestDTO">RequestDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestdto"></a>
<a id="schema_RequestDTO"></a>
<a id="tocSrequestdto"></a>
<a id="tocsrequestdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "tenantId": "string",
  "assetId": "string",
  "orgs": [
    "string"
  ],
  "alternateId": "string",
  "statusId": "string",
  "statusCode": "string",
  "subStatusId": "string",
  "subStatusCode": "string",
  "materialsStatusId": "string",
  "materialsStatusCode": "string",
  "assignmentStatusId": "string",
  "assignmentStatusCode": "string",
  "disputeStatusId": "string",
  "disputeStatusCode": "string",
  "disputedDate": "string",
  "createdBy": "string",
  "modifiedBy": "string",
  "requestorId": "string",
  "ownerId": "string",
  "locationId": "string",
  "positionId": "string",
  "serviceClassificationId": "string",
  "relatedServiceClassification": [
    "string"
  ],
  "miscExtendedProperties": {
    "serviceClassification": [
      {
        "id": "string",
        "value": [
          "string"
        ]
      }
    ],
    "isFlagged": true,
    "flaggedId": "string",
    "flagReason": "string"
  },
  "source": "string",
  "isFlagged": true,
  "isPrivate": true,
  "priorityId": "string",
  "watchers": [
    "string"
  ],
  "sourceApp": "string",
  "spendLimit": 0,
  "estimatedServiceCost": 0,
  "lastAssessmentDate": "string",
  "lastAssessmentTrigger": "string",
  "createdDate": "string",
  "reportedDate": "string",
  "modifiedDate": "string",
  "closedDate": "string",
  "description": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ],
  "comments": [
    {
      "commentId": "string",
      "requestId": "string",
      "addedByPersonId": "string",
      "source": "string",
      "comment": "string",
      "type": "string",
      "orgType": "string",
      "linkedWOCommentId": "string",
      "addedDate": "string",
      "linkedWorkOrderId": "string",
      "isClientViewable": true
    }
  ],
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "serviceLevelAgreements": [
    {
      "id": "string",
      "requestId": "string",
      "name": "string",
      "timeAllotted": 0,
      "unit": "string",
      "targetTime": "string",
      "overriddenDate": "string",
      "overriddenReason": "string",
      "overriddenBy": "string",
      "slaMetDate": "string",
      "slaMetWO": "string",
      "slaMetDatet": "string"
    }
  ],
  "watchLists": [
    {
      "id": "string",
      "requestId": "string",
      "user": "string",
      "createdBy": "string"
    }
  ],
  "triageStatus": "string",
  "workOrders": [
    {
      "id": "string",
      "description": "string",
      "alternateId": "string",
      "statusId": "string",
      "assigneeName": "string",
      "assignmentType": "string",
      "assigneeId": "string",
      "facilityManagerId": "string",
      "comments": [
        {
          "commentId": "string",
          "workOrderCommentId": 0,
          "addedByPersonId": "string",
          "comment": "string",
          "commentType": "string",
          "addedDate": "string"
        }
      ],
      "slaTypes": [
        {
          "id": "string",
          "name": "string",
          "targetDate": "string",
          "overrideDate": "string",
          "overrideReason": "string",
          "overrideBy": "string",
          "slaMetDate": "string",
          "slaMet": true
        }
      ],
      "nte": 0,
      "subStatusId": "string",
      "subStatusCode": "string",
      "dispatchSiteId": "string",
      "dispatchSiteName": "string",
      "completionDescription": "string",
      "requestedBy": "string",
      "serviceClassificationId": "string",
      "locationId": "string",
      "assetId": "string",
      "createdDate": "string",
      "modifiedDate": "string",
      "assigneeIds": [
        "string"
      ],
      "dispatchSiteIds": [
        "string"
      ]
    }
  ],
  "statusHistory": [
    {
      "statusId": "string",
      "statusCode": "string",
      "createdDate": "string",
      "updatedBy": "string",
      "subStatusId": "string",
      "subStatusCode": "string",
      "reasonId": "string",
      "version": 0
    }
  ],
  "attachments": [
    {
      "attachmentData": {
        "id": "string",
        "name": "string",
        "mimetype": "string",
        "extension": "string",
        "type": "string",
        "status": "string",
        "tenantId": "string",
        "storageAccount": "string",
        "container": "string",
        "fileMd5": "string",
        "createdTime": "string",
        "createdBy": "string"
      },
      "attachmentRelatedObjects": {
        "id": "string",
        "orgs": [
          "string"
        ],
        "objectId": "string",
        "objectType": "string",
        "createTime": "string",
        "createdBy": "string",
        "description": "string"
      }
    }
  ],
  "reason": {
    "reasonCode": "string",
    "reasonDescription": "string"
  },
  "requestChain": [
    {
      "activeApprovers": [
        {
          "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
          "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
          "stepNumber": 0,
          "isDelegator": true
        }
      ],
      "chain": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "majorVersion": 0,
        "minorVersion": 0,
        "createdDate": "string",
        "updatedTime": "string",
        "source": "string",
        "chainDefinitionId": "33c41efb-d33e-4a9a-a870-d84c4191c4f8",
        "capabilityId": "486ae165-7fa3-4fe9-8d0b-0636c8459cb3",
        "capabilityTtl": "string",
        "capabilityName": "string",
        "capabilityLimit": {
          "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
          "name": "string",
          "unit": "string",
          "value": "string"
        },
        "chainDefinitionAlternateId": "string",
        "chainDefinitionVersion": 0,
        "orgs": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "type": "string"
          }
        ],
        "chainStatus": "InProgress",
        "approvers": [
          {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "personId": "f3e5ff26-28ff-4cd6-9b1b-e303a185a13a",
            "personType": "string",
            "group": 0,
            "sequence": 0,
            "generalization": {
              "id": "string",
              "name": "string",
              "group": "string"
            },
            "authScopeId": "6ec9200a-76f9-43d6-bfa3-7aab9173cb22",
            "when": "string",
            "responseCount": 0,
            "approvalRule": "string",
            "mandatory": true,
            "decision": {
              "status": "Approved",
              "decisionDate": "string",
              "madeByDelegate": true,
              "decisionNote": "string"
            },
            "personLimit": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "name": "string",
              "unit": "string",
              "value": "string"
            }
          }
        ],
        "delegates": [
          {
            "approver": "a0a63d7a-7a62-4e15-9ab9-49317f76d38f",
            "delegatedTo": "24f4958c-0bd4-4a45-a033-794ec7b5b1f6",
            "startDate": "2019-08-24T14:15:22Z",
            "endDate": "2019-08-24T14:15:22Z",
            "group": 0
          }
        ],
        "excluded": [
          {
            "excludedApprover": "string",
            "conflictCapability": {
              "id": "string",
              "name": "string"
            },
            "conflictObject": {
              "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
              "type": "string",
              "alternateId": "string"
            }
          }
        ],
        "isRecalculate": true
      },
      "subStateStatus": "ACTIVE",
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536"
    }
  ],
  "errorContainer": {
    "version": "string",
    "traceId": "string",
    "title": "string",
    "category": "INFO",
    "errors": [
      {
        "id": "string",
        "alternateId": "string",
        "description": "string",
        "domain": "string",
        "messages": [
          {
            "message": "string",
            "code": "string"
          }
        ]
      }
    ]
  },
  "workOwnerGroupValue": "string",
  "miscellaneous": {
    "statusChangeDate": "string",
    "slaAttendDate": "string",
    "slaCompleteDate": "string",
    "slaDispatchDate": "string",
    "slaResponseDate": "string",
    "isFlagged": true,
    "flaggedDate": "string"
  },
  "requestAuthActions": [
    {
      "name": "string",
      "additionalDetailsKey": "string",
      "additionalDetails": {
        "property1": "string",
        "property2": "string"
      }
    }
  ],
  "action": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "pmDetails": {
    "pmId": "string",
    "pmAlternateId": "string",
    "pmConfigUrl": "string",
    "planId": "string",
    "type": "string",
    "primaryLocationId": "string",
    "maintenanceFrequency": "string",
    "maintenanceFrequencyUnit": "string",
    "interval": "string",
    "totalSequences": "string",
    "sequences": [
      {
        "sequence": 0,
        "locationId": "string",
        "assetId": "string",
        "positionId": "string"
      }
    ],
    "providerId": "string",
    "providerType": "string",
    "providerReferenceId": "string",
    "assignmentOverride": true
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|tenantId|string|false|none|none|
|assetId|string|false|none|none|
|orgs|[string]|false|none|none|
|alternateId|string|false|none|none|
|statusId|string|false|none|none|
|statusCode|string|false|none|none|
|subStatusId|string|false|none|none|
|subStatusCode|string|false|none|none|
|materialsStatusId|string|false|none|none|
|materialsStatusCode|string|false|none|none|
|assignmentStatusId|string|false|none|none|
|assignmentStatusCode|string|false|none|none|
|disputeStatusId|string|false|none|none|
|disputeStatusCode|string|false|none|none|
|disputedDate|string|false|none|none|
|createdBy|string|false|none|none|
|modifiedBy|string|false|none|none|
|requestorId|string|false|none|none|
|ownerId|string|false|none|none|
|locationId|string|false|none|none|
|positionId|string|false|none|none|
|serviceClassificationId|string|false|none|none|
|relatedServiceClassification|[string]|false|none|none|
|miscExtendedProperties|[MiscExtendedPropertiesDTO](#schemamiscextendedpropertiesdto)|false|none|none|
|source|string|false|none|none|
|isFlagged|boolean|false|none|none|
|isPrivate|boolean|false|none|none|
|priorityId|string|false|none|none|
|watchers|[string]|false|none|none|
|sourceApp|string|false|none|none|
|spendLimit|number|false|none|none|
|estimatedServiceCost|number|false|none|none|
|lastAssessmentDate|string|false|none|none|
|lastAssessmentTrigger|string|false|none|none|
|createdDate|string|false|none|none|
|reportedDate|string|false|none|none|
|modifiedDate|string|false|none|none|
|closedDate|string|false|none|none|
|description|string|false|none|none|
|charts|[[ChartDTO](#schemachartdto)]|false|none|none|
|comments|[[CommentDTO](#schemacommentdto)]|false|none|none|
|extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|serviceLevelAgreements|[[ServiceLevelAgreementDTO](#schemaservicelevelagreementdto)]|false|none|none|
|watchLists|[[WatchListDTO](#schemawatchlistdto)]|false|none|none|
|triageStatus|string|false|none|none|
|workOrders|[[WorkOrderDTO](#schemaworkorderdto)]|false|none|none|
|statusHistory|[[StatusHistoryDTO](#schemastatushistorydto)]|false|none|none|
|attachments|[[AttachmentDTO](#schemaattachmentdto)]|false|none|none|
|reason|[ReasonDTO](#schemareasondto)|false|none|none|
|requestChain|[[RequestChainApprovalResponseDTO](#schemarequestchainapprovalresponsedto)]|false|none|none|
|errorContainer|[ErrorContainer](#schemaerrorcontainer)|false|none|none|
|workOwnerGroupValue|string|false|none|none|
|miscellaneous|[MiscellaneousDTO](#schemamiscellaneousdto)|false|none|none|
|requestAuthActions|[[RequestAuthActionDTO](#schemarequestauthactiondto)]|false|none|none|
|action|[string]|false|none|none|
|pmDetails|[PMDetailsDTO](#schemapmdetailsdto)|false|none|none|

<h2 id="tocS_WatchListDTO">WatchListDTO</h2>
<!-- backwards compatibility -->
<a id="schemawatchlistdto"></a>
<a id="schema_WatchListDTO"></a>
<a id="tocSwatchlistdto"></a>
<a id="tocswatchlistdto"></a>

```json
{
  "id": "string",
  "requestId": "string",
  "user": "string",
  "createdBy": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|requestId|string|false|none|none|
|user|string|false|none|none|
|createdBy|string|false|none|none|

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

<h2 id="tocS_MessageIdsPayload">MessageIdsPayload</h2>
<!-- backwards compatibility -->
<a id="schemamessageidspayload"></a>
<a id="schema_MessageIdsPayload"></a>
<a id="tocSmessageidspayload"></a>
<a id="tocsmessageidspayload"></a>

```json
{
  "messageIds": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|messageIds|[string]|true|none|none|

<h2 id="tocS_RequestFlagDto">RequestFlagDto</h2>
<!-- backwards compatibility -->
<a id="schemarequestflagdto"></a>
<a id="schema_RequestFlagDto"></a>
<a id="tocSrequestflagdto"></a>
<a id="tocsrequestflagdto"></a>

```json
{
  "id": "string",
  "flagId": "string",
  "flaggedBy": "string",
  "flaggedDate": "string",
  "unflagId": "string",
  "unflaggedBy": "string",
  "unflaggedDate": "string",
  "status": "string",
  "isRequestFlagged": true,
  "requestFlaggedDate": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string|false|none|none|
|flagId|string|false|none|none|
|flaggedBy|string|false|none|none|
|flaggedDate|string|false|none|none|
|unflagId|string|false|none|none|
|unflaggedBy|string|false|none|none|
|unflaggedDate|string|false|none|none|
|status|string|false|none|none|
|isRequestFlagged|boolean|false|none|none|
|requestFlaggedDate|string|false|none|none|

<h2 id="tocS_ChartBuilderExtendedPropertiesDTO">ChartBuilderExtendedPropertiesDTO</h2>
<!-- backwards compatibility -->
<a id="schemachartbuilderextendedpropertiesdto"></a>
<a id="schema_ChartBuilderExtendedPropertiesDTO"></a>
<a id="tocSchartbuilderextendedpropertiesdto"></a>
<a id="tocschartbuilderextendedpropertiesdto"></a>

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "object": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "globalOrgId": "03378aa8-9494-48fd-a5c7-dd47fb2149d8",
  "extendedProperties": {
    "id": "string",
    "data": "string"
  },
  "existingCharts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requestId|string(uuid)|false|none|none|
|object|string|false|none|none|
|orgs|[string]|false|none|none|
|globalOrgId|string(uuid)|false|none|none|
|extendedProperties|[ExtendedPropertiesDTO](#schemaextendedpropertiesdto)|false|none|none|
|existingCharts|[[ChartDTO](#schemachartdto)]|false|none|none|

<h2 id="tocS_ChartObjectDTO">ChartObjectDTO</h2>
<!-- backwards compatibility -->
<a id="schemachartobjectdto"></a>
<a id="schema_ChartObjectDTO"></a>
<a id="tocSchartobjectdto"></a>
<a id="tocschartobjectdto"></a>

```json
{
  "requestId": "d385ab22-0f51-4b97-9ecd-b8ff3fd4fcb6",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "source": "string",
  "charts": [
    {
      "chartId": "string",
      "requestId": "string",
      "version": "string",
      "createdDate": "string",
      "chartName": "string",
      "dimensionName": "string",
      "dimensionPosition": "string",
      "dimensionValue": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|requestId|string(uuid)|false|none|none|
|orgs|[string]|false|none|none|
|source|string|false|none|none|
|charts|[[ChartDTO](#schemachartdto)]|false|none|none|

<h2 id="tocS_ChartDefinitionDTO">ChartDefinitionDTO</h2>
<!-- backwards compatibility -->
<a id="schemachartdefinitiondto"></a>
<a id="schema_ChartDefinitionDTO"></a>
<a id="tocSchartdefinitiondto"></a>
<a id="tocschartdefinitiondto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "status": "ACTIVE",
  "orgs": [
    {
      "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
      "name": "string",
      "structure": "string"
    }
  ],
  "version": 0,
  "object": "string",
  "dimensionDefinitions": [
    {
      "name": "string",
      "type": "string",
      "seqNo": 0,
      "regexExpression": "string",
      "defaultValue": "string",
      "sourceDefs": [
        {
          "buildOrder": 0,
          "components": [
            {
              "propertyPath": "string",
              "prefix": "string",
              "suffix": "string",
              "regexPattern": "string",
              "presentationPath": "string"
            }
          ]
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
|name|string|false|none|none|
|status|string|false|none|none|
|orgs|[[OrgDTO](#schemaorgdto)]|false|none|none|
|version|integer(int32)|false|none|none|
|object|string|false|none|none|
|dimensionDefinitions|[[DimensionDefinitionDTO](#schemadimensiondefinitiondto)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|INACTIVE|

<h2 id="tocS_ComponentsDto">ComponentsDto</h2>
<!-- backwards compatibility -->
<a id="schemacomponentsdto"></a>
<a id="schema_ComponentsDto"></a>
<a id="tocScomponentsdto"></a>
<a id="tocscomponentsdto"></a>

```json
{
  "propertyPath": "string",
  "prefix": "string",
  "suffix": "string",
  "regexPattern": "string",
  "presentationPath": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|propertyPath|string|false|none|none|
|prefix|string|false|none|none|
|suffix|string|false|none|none|
|regexPattern|string|false|none|none|
|presentationPath|string|false|none|none|

<h2 id="tocS_DimensionDefinitionDTO">DimensionDefinitionDTO</h2>
<!-- backwards compatibility -->
<a id="schemadimensiondefinitiondto"></a>
<a id="schema_DimensionDefinitionDTO"></a>
<a id="tocSdimensiondefinitiondto"></a>
<a id="tocsdimensiondefinitiondto"></a>

```json
{
  "name": "string",
  "type": "string",
  "seqNo": 0,
  "regexExpression": "string",
  "defaultValue": "string",
  "sourceDefs": [
    {
      "buildOrder": 0,
      "components": [
        {
          "propertyPath": "string",
          "prefix": "string",
          "suffix": "string",
          "regexPattern": "string",
          "presentationPath": "string"
        }
      ]
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|false|none|none|
|type|string|false|none|none|
|seqNo|integer(int32)|false|none|none|
|regexExpression|string|false|none|none|
|defaultValue|string|false|none|none|
|sourceDefs|[[SourceDefinitionsDTO](#schemasourcedefinitionsdto)]|false|none|none|

<h2 id="tocS_OrgDTO">OrgDTO</h2>
<!-- backwards compatibility -->
<a id="schemaorgdto"></a>
<a id="schema_OrgDTO"></a>
<a id="tocSorgdto"></a>
<a id="tocsorgdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "structure": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|structure|string|false|none|none|

<h2 id="tocS_SourceDefinitionsDTO">SourceDefinitionsDTO</h2>
<!-- backwards compatibility -->
<a id="schemasourcedefinitionsdto"></a>
<a id="schema_SourceDefinitionsDTO"></a>
<a id="tocSsourcedefinitionsdto"></a>
<a id="tocssourcedefinitionsdto"></a>

```json
{
  "buildOrder": 0,
  "components": [
    {
      "propertyPath": "string",
      "prefix": "string",
      "suffix": "string",
      "regexPattern": "string",
      "presentationPath": "string"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|buildOrder|integer(int32)|false|none|none|
|components|[[ComponentsDto](#schemacomponentsdto)]|false|none|none|

<h2 id="tocS_CapabilityDTO">CapabilityDTO</h2>
<!-- backwards compatibility -->
<a id="schemacapabilitydto"></a>
<a id="schema_CapabilityDTO"></a>
<a id="tocScapabilitydto"></a>
<a id="tocscapabilitydto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_ChainViewLimitDTO">ChainViewLimitDTO</h2>
<!-- backwards compatibility -->
<a id="schemachainviewlimitdto"></a>
<a id="schema_ChainViewLimitDTO"></a>
<a id="tocSchainviewlimitdto"></a>
<a id="tocschainviewlimitdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string",
  "value": "string",
  "unit": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|
|value|string|false|none|none|
|unit|string|false|none|none|

<h2 id="tocS_GeneralizationDTO">GeneralizationDTO</h2>
<!-- backwards compatibility -->
<a id="schemageneralizationdto"></a>
<a id="schema_GeneralizationDTO"></a>
<a id="tocSgeneralizationdto"></a>
<a id="tocsgeneralizationdto"></a>

```json
{
  "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
  "name": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|string(uuid)|false|none|none|
|name|string|false|none|none|

<h2 id="tocS_PageRequestChainListViewDTO">PageRequestChainListViewDTO</h2>
<!-- backwards compatibility -->
<a id="schemapagerequestchainlistviewdto"></a>
<a id="schema_PageRequestChainListViewDTO"></a>
<a id="tocSpagerequestchainlistviewdto"></a>
<a id="tocspagerequestchainlistviewdto"></a>

```json
{
  "totalPages": 0,
  "totalElements": 0,
  "size": 0,
  "content": [
    {
      "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
      "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
      "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
      "delegator": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "step": 0,
      "alternateId": "string",
      "tenantId": "string",
      "orgs": [
        "497f6eca-6276-4993-bfeb-53cbbbba6f08"
      ],
      "orgName": "string",
      "capability": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "description": "string",
      "personLimit": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "value": "string",
        "unit": "string"
      },
      "createdDate": "2019-08-24T14:15:22Z",
      "requester": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "requesterId": "ba828041-f5bf-46f6-bf7c-22eccb01f2a4",
      "status": "ACTIVE",
      "delegate": true
    }
  ],
  "number": 0,
  "sort": [
    {
      "direction": "string",
      "nullHandling": "string",
      "ascending": true,
      "property": "string",
      "ignoreCase": true
    }
  ],
  "first": true,
  "last": true,
  "numberOfElements": 0,
  "pageable": {
    "offset": 0,
    "sort": [
      {
        "direction": "string",
        "nullHandling": "string",
        "ascending": true,
        "property": "string",
        "ignoreCase": true
      }
    ],
    "pageNumber": 0,
    "pageSize": 0,
    "paged": true,
    "unpaged": true
  },
  "empty": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|totalPages|integer(int32)|false|none|none|
|totalElements|integer(int64)|false|none|none|
|size|integer(int32)|false|none|none|
|content|[[RequestChainListViewDTO](#schemarequestchainlistviewdto)]|false|none|none|
|number|integer(int32)|false|none|none|
|sort|[[SortObject](#schemasortobject)]|false|none|none|
|first|boolean|false|none|none|
|last|boolean|false|none|none|
|numberOfElements|integer(int32)|false|none|none|
|pageable|[PageableObject](#schemapageableobject)|false|none|none|
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
  "sort": [
    {
      "direction": "string",
      "nullHandling": "string",
      "ascending": true,
      "property": "string",
      "ignoreCase": true
    }
  ],
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
|sort|[[SortObject](#schemasortobject)]|false|none|none|
|pageNumber|integer(int32)|false|none|none|
|pageSize|integer(int32)|false|none|none|
|paged|boolean|false|none|none|
|unpaged|boolean|false|none|none|

<h2 id="tocS_PersonIdentityDTO">PersonIdentityDTO</h2>
<!-- backwards compatibility -->
<a id="schemapersonidentitydto"></a>
<a id="schema_PersonIdentityDTO"></a>
<a id="tocSpersonidentitydto"></a>
<a id="tocspersonidentitydto"></a>

```json
{
  "personId": "string",
  "firstName": "string",
  "lastName": "string",
  "fullName": "string",
  "locale": "string",
  "telephone": "string",
  "email": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|personId|string|false|none|none|
|firstName|string|false|none|none|
|lastName|string|false|none|none|
|fullName|string|false|none|none|
|locale|string|false|none|none|
|telephone|string|false|none|none|
|email|string|false|none|none|

<h2 id="tocS_RequestChainListViewDTO">RequestChainListViewDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestchainlistviewdto"></a>
<a id="schema_RequestChainListViewDTO"></a>
<a id="tocSrequestchainlistviewdto"></a>
<a id="tocsrequestchainlistviewdto"></a>

```json
{
  "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
  "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
  "generalization": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string"
  },
  "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
  "approver": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "approverId": "c4cb1502-f1f4-43be-8940-63247031d1fd",
  "delegatorId": "83c58675-1390-4726-803a-ede36a95b5e7",
  "delegator": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "step": 0,
  "alternateId": "string",
  "tenantId": "string",
  "orgs": [
    "497f6eca-6276-4993-bfeb-53cbbbba6f08"
  ],
  "orgName": "string",
  "capability": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string"
  },
  "description": "string",
  "personLimit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "value": "string",
    "unit": "string"
  },
  "createdDate": "2019-08-24T14:15:22Z",
  "requester": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "requesterId": "ba828041-f5bf-46f6-bf7c-22eccb01f2a4",
  "status": "ACTIVE",
  "delegate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|factId|string(uuid)|false|none|none|
|chainId|string(uuid)|false|none|none|
|generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|subStateId|string(uuid)|false|none|none|
|approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|approverId|string(uuid)|false|none|none|
|delegatorId|string(uuid)|false|none|none|
|delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|step|integer(int32)|false|none|none|
|alternateId|string|false|none|none|
|tenantId|string|false|none|none|
|orgs|[string]|false|none|none|
|orgName|string|false|none|none|
|capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|description|string|false|none|none|
|personLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|createdDate|string(date-time)|false|none|none|
|requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|requesterId|string(uuid)|false|none|none|
|status|string|false|none|none|
|delegate|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|

<h2 id="tocS_SortObject">SortObject</h2>
<!-- backwards compatibility -->
<a id="schemasortobject"></a>
<a id="schema_SortObject"></a>
<a id="tocSsortobject"></a>
<a id="tocssortobject"></a>

```json
{
  "direction": "string",
  "nullHandling": "string",
  "ascending": true,
  "property": "string",
  "ignoreCase": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|direction|string|false|none|none|
|nullHandling|string|false|none|none|
|ascending|boolean|false|none|none|
|property|string|false|none|none|
|ignoreCase|boolean|false|none|none|

<h2 id="tocS_ChainDetailsCommentsDTO">ChainDetailsCommentsDTO</h2>
<!-- backwards compatibility -->
<a id="schemachaindetailscommentsdto"></a>
<a id="schema_ChainDetailsCommentsDTO"></a>
<a id="tocSchaindetailscommentsdto"></a>
<a id="tocschaindetailscommentsdto"></a>

```json
{
  "approver": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "decisionDate": "string",
  "comment": "string",
  "status": "Approved"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|decisionDate|string|false|none|none|
|comment|string|false|none|none|
|status|string|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|

<h2 id="tocS_ChainViewApproverDTO">ChainViewApproverDTO</h2>
<!-- backwards compatibility -->
<a id="schemachainviewapproverdto"></a>
<a id="schema_ChainViewApproverDTO"></a>
<a id="tocSchainviewapproverdto"></a>
<a id="tocschainviewapproverdto"></a>

```json
{
  "approver": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "limit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "value": "string",
    "unit": "string"
  },
  "delegator": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "decisionDate": "string",
  "status": "Approved",
  "delegate": true,
  "isDelegate": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|approver|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|limit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|delegator|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|decisionDate|string|false|none|none|
|status|string|false|none|none|
|delegate|boolean|false|none|none|
|isDelegate|boolean|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|Approved|
|status|Declined|

<h2 id="tocS_ChainViewStepDTO">ChainViewStepDTO</h2>
<!-- backwards compatibility -->
<a id="schemachainviewstepdto"></a>
<a id="schema_ChainViewStepDTO"></a>
<a id="tocSchainviewstepdto"></a>
<a id="tocschainviewstepdto"></a>

```json
{
  "generalization": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string"
  },
  "step": 0,
  "when": "string",
  "appoversCount": 0,
  "approvers": [
    {
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "limit": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string",
        "value": "string",
        "unit": "string"
      },
      "delegator": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "decisionDate": "string",
      "status": "Approved",
      "delegate": true,
      "isDelegate": true
    }
  ],
  "approvalRule": "string",
  "activeStep": true,
  "isActiveStep": true
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|generalization|[GeneralizationDTO](#schemageneralizationdto)|false|none|none|
|step|integer(int32)|false|none|none|
|when|string|false|none|none|
|appoversCount|integer(int32)|false|none|none|
|approvers|[[ChainViewApproverDTO](#schemachainviewapproverdto)]|false|none|none|
|approvalRule|string|false|none|none|
|activeStep|boolean|false|none|none|
|isActiveStep|boolean|false|none|none|

<h2 id="tocS_RequestChainViewDetailsDTO">RequestChainViewDetailsDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestchainviewdetailsdto"></a>
<a id="schema_RequestChainViewDetailsDTO"></a>
<a id="tocSrequestchainviewdetailsdto"></a>
<a id="tocsrequestchainviewdetailsdto"></a>

```json
{
  "chainId": "9e7fb22a-9e5b-420e-8fd7-e3454fcfd5fd",
  "subStateId": "1d7b00df-3c29-4fa9-8140-09640f95e536",
  "factId": "dd15052b-d60e-4f1c-ae27-912075e27fd7",
  "alternateId": "string",
  "orgs": [
    "string"
  ],
  "capability": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string"
  },
  "description": "string",
  "decisionFlag": true,
  "requestRevisionFlag": true,
  "capabilityLimit": {
    "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
    "name": "string",
    "value": "string",
    "unit": "string"
  },
  "createdDate": "2019-08-24T14:15:22Z",
  "requester": {
    "personId": "string",
    "firstName": "string",
    "lastName": "string",
    "fullName": "string",
    "locale": "string",
    "telephone": "string",
    "email": "string"
  },
  "status": "ACTIVE",
  "approvalDeadline": "2019-08-24T14:15:22Z",
  "steps": [
    {
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "step": 0,
      "when": "string",
      "appoversCount": 0,
      "approvers": [
        {
          "approver": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "limit": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "name": "string",
            "value": "string",
            "unit": "string"
          },
          "delegator": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "decisionDate": "string",
          "status": "Approved",
          "delegate": true,
          "isDelegate": true
        }
      ],
      "approvalRule": "string",
      "activeStep": true,
      "isActiveStep": true
    }
  ],
  "comments": [
    {
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "decisionDate": "string",
      "comment": "string",
      "status": "Approved"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|chainId|string(uuid)|false|none|none|
|subStateId|string(uuid)|false|none|none|
|factId|string(uuid)|false|none|none|
|alternateId|string|false|none|none|
|orgs|[string]|false|none|none|
|capability|[CapabilityDTO](#schemacapabilitydto)|false|none|none|
|description|string|false|none|none|
|decisionFlag|boolean|false|none|none|
|requestRevisionFlag|boolean|false|none|none|
|capabilityLimit|[ChainViewLimitDTO](#schemachainviewlimitdto)|false|none|none|
|createdDate|string(date-time)|false|none|none|
|requester|[PersonIdentityDTO](#schemapersonidentitydto)|false|none|none|
|status|string|false|none|none|
|approvalDeadline|string(date-time)|false|none|none|
|steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|

#### Enumerated Values

|Property|Value|
|---|---|
|status|ACTIVE|
|status|DECLINED|
|status|APPROVED|
|status|RECALLED|
|status|EXPIRED|

<h2 id="tocS_RequestChainDetailsHistoryDTO">RequestChainDetailsHistoryDTO</h2>
<!-- backwards compatibility -->
<a id="schemarequestchaindetailshistorydto"></a>
<a id="schema_RequestChainDetailsHistoryDTO"></a>
<a id="tocSrequestchaindetailshistorydto"></a>
<a id="tocsrequestchaindetailshistorydto"></a>

```json
{
  "steps": [
    {
      "generalization": {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "string"
      },
      "step": 0,
      "when": "string",
      "appoversCount": 0,
      "approvers": [
        {
          "approver": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "limit": {
            "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
            "name": "string",
            "value": "string",
            "unit": "string"
          },
          "delegator": {
            "personId": "string",
            "firstName": "string",
            "lastName": "string",
            "fullName": "string",
            "locale": "string",
            "telephone": "string",
            "email": "string"
          },
          "decisionDate": "string",
          "status": "Approved",
          "delegate": true,
          "isDelegate": true
        }
      ],
      "approvalRule": "string",
      "activeStep": true,
      "isActiveStep": true
    }
  ],
  "comments": [
    {
      "approver": {
        "personId": "string",
        "firstName": "string",
        "lastName": "string",
        "fullName": "string",
        "locale": "string",
        "telephone": "string",
        "email": "string"
      },
      "decisionDate": "string",
      "comment": "string",
      "status": "Approved"
    }
  ]
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|steps|[[ChainViewStepDTO](#schemachainviewstepdto)]|false|none|none|
|comments|[[ChainDetailsCommentsDTO](#schemachaindetailscommentsdto)]|false|none|none|

