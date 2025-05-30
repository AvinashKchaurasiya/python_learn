{
	"info": {
		"_postman_id": "b9fe5a49-ddfd-470c-921c-af9c30c7c12f",
		"name": "UAT",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "33040731"
	},
	"item": [
		{
			"name": "Web to Lead",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\r\n    \"parentName\": \"Test\",\r\n    \"email\": \"test@test.com.invalid\",\r\n    \"countryCode\": \"+971\",\r\n    \"mobileNo\": \"1234567890\",\r\n    \"childName\": \"Test\",\r\n    \"childDOB\": \"2022-01-01\",\r\n    \"branch\": \"Maple Bear Yangi\", //Fixed Value for Uzbekistan\r\n    \"areaOfLiving\": \"XYZ\",\r\n    // \"batch\": \"\", // Ignore if do not have value\r\n    \"inquiryDate\": \"2024-09-17\", // Today Date - Only this Format (YYYY-MM-DD)\r\n    \"preferredTimeToCallBack\": \"\", // Ignore if do not have value\r\n    \"leadSource\": \"Website\" //Fixed Value\r\n    // \"requirement\": \"\" // Ignore if do not have value\r\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "{{end_point_URL}}/CreateLead",
					"host": [
						"{{end_point_URL}}"
					],
					"path": [
						"CreateLead"
					]
				}
			},
			"response": [
				{
					"name": "Web to Lead - success",
					"originalRequest": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"parentName\": \"Test\",\r\n    \"email\": \"test@test.com.invalid\",\r\n    \"countryCode\": \"+971\",\r\n    \"mobileNo\": \"1234567890\",\r\n    \"childName\": \"Test\",\r\n    \"childDOB\": \"2022-01-01\",\r\n    \"branch\": \"Maple Bear Yangi\", //Fixed Value for Uzbekistan\r\n    \"areaOfLiving\": \"XYZ\",\r\n    \"inquiryDate\": \"2024-09-17\", // Today Date - Only this Format (YYYY-MM-DD)\r\n    \"batch\": \"\", // Ignore if do not have value\r\n    \"preferredTimeToCallBack\": \"\", // Ignore if do not have value\r\n    \"requirement\": \"\", // Ignore if do not have value\r\n    \"leadSource\": \"Website\" //Fixed Value\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{end_point_URL}}/CreateLead",
							"host": [
								"{{end_point_URL}}"
							],
							"path": [
								"CreateLead"
							]
						}
					},
					"status": "OK",
					"code": 200,
					"_postman_previewlanguage": "json",
					"header": [
						{
							"key": "Content-Type",
							"value": "application/json;charset=UTF-8"
						},
						{
							"key": "Cache-Control",
							"value": "no-cache,must-revalidate,max-age=0,no-store,private"
						},
						{
							"key": "X-Content-Type-Options",
							"value": "nosniff"
						},
						{
							"key": "Vary",
							"value": "Accept-Encoding"
						},
						{
							"key": "Strict-Transport-Security",
							"value": "max-age=63072000; includeSubDomains"
						},
						{
							"key": "Content-Encoding",
							"value": "gzip"
						},
						{
							"key": "Server",
							"value": "sfdcedge"
						},
						{
							"key": "X-SFDC-Request-Id",
							"value": "f9f732fa2b9a3c13723957874d3f5907"
						},
						{
							"key": "Content-Length",
							"value": "80"
						},
						{
							"key": "Date",
							"value": "Tue, 17 Sep 2024 03:58:26 GMT"
						},
						{
							"key": "Connection",
							"value": "keep-alive"
						},
						{
							"key": "x-origin-cache-control",
							"value": "no-cache,must-revalidate,max-age=0,no-store,private"
						},
						{
							"key": "Akamai-GRN",
							"value": "0.1dadce17.1726545502.38f0ef22"
						}
					],
					"cookie": [],
					"body": "{\n    \"status\": true,\n    \"response\": \"Lead created successfully!!!\"\n}"
				},
				{
					"name": "Web to Lead - error",
					"originalRequest": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\r\n    \"parentName\": \"Test\",\r\n    \"email\": \"test@test.com.invalid\",\r\n    \"countryCode\": \"+971\",\r\n    \"mobileNo\": \"1234567890\",\r\n    \"childName\": \"Test\",\r\n    \"childDOB\": \"2022-01-01\",\r\n    \"branch\": \"Maple Bear Yangi-1\", //Fixed Value for Uzbekistan\r\n    \"areaOfLiving\": \"XYZ\",\r\n    \"inquiryDate\": \"2024-09-17\", // Today Date - Only this Format (YYYY-MM-DD)\r\n    \"batch\": \"\", // Ignore if do not have value\r\n    \"preferredTimeToCallBack\": \"\", // Ignore if do not have value\r\n    \"requirement\": \"\", // Ignore if do not have value\r\n    \"leadSource\": \"Website\" //Fixed Value\r\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "{{end_point_URL}}/CreateLead",
							"host": [
								"{{end_point_URL}}"
							],
							"path": [
								"CreateLead"
							]
						}
					},
					"status": "Bad Request",
					"code": 400,
					"_postman_previewlanguage": "raw",
					"header": [
						{
							"key": "Content-Type",
							"value": "application/octetstream"
						},
						{
							"key": "Strict-Transport-Security",
							"value": "max-age=63072000; includeSubDomains"
						},
						{
							"key": "X-Content-Type-Options",
							"value": "nosniff"
						},
						{
							"key": "Cache-Control",
							"value": "no-cache,must-revalidate,max-age=0,no-store,private"
						},
						{
							"key": "Server",
							"value": "sfdcedge"
						},
						{
							"key": "X-SFDC-Request-Id",
							"value": "5f77018cf5de2424e5b28d1812ce3df1"
						},
						{
							"key": "Date",
							"value": "Tue, 17 Sep 2024 03:59:03 GMT"
						},
						{
							"key": "Connection",
							"value": "close"
						},
						{
							"key": "X-DataStream-Origin-HTTP-Status",
							"value": "400"
						},
						{
							"key": "x-origin-cache-control",
							"value": "no-cache,must-revalidate,max-age=0,no-store,private"
						},
						{
							"key": "Akamai-GRN",
							"value": "0.16adce17.1726545542.1fe7a6b7"
						}
					],
					"cookie": [],
					"body": "{\"status\" : false, \"response\" : \"Bad request, Insert failed. First exception on row 0; first error: INVALID_OR_NULL_FOR_RESTRICTED_PICKLIST, Branch: bad value for restricted picklist field: Yangi-1: [Branch__c]\"}"
				}
			]
		}
	],
	"event": [
		{
			"listen": "prerequest",
			"script": {
				"type": "text/javascript",
				"packages": {},
				"exec": [
					""
				]
			}
		},
		{
			"listen": "test",
			"script": {
				"type": "text/javascript",
				"packages": {},
				"exec": [
					""
				]
			}
		}
	],
	"variable": [
		{
			"key": "instance_url",
			"value": "",
			"type": "string"
		},
		{
			"key": "end_point_URL",
			"value": "",
			"type": "string"
		}
	]
}