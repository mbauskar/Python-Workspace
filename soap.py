def pass_request_to_client_esb():
    from suds.client import Client
    url = "file:///home/makarand/Desktop/Projects/CRM_ACCEPTANCE_MSGService.wsdl"
    client = Client(url, cache=None)

    # Request and response data
    # logged_request = json.loads(doc.request_parameters)
    # logged_response = json.loads(doc.response)

    P_CRM_ID = 123
    P_CIRCUIT_NO = "17XXXXXX"
    P_SERVICE_TYPE = "SaaS"
    P_ACTION_TYPE = "ROS"
    P_RETURN_CODE = "02"
    P_RETURN_MESG = "S"
    P_ATTRIBUTE1 = None
    P_ATTRIBUTE2 = None
    P_ATTRIBUTE3 = None

    try:
        response = client.service.AcceptRequest(P_CRM_ID=P_CRM_ID,P_SERVICE_TYPE=P_SERVICE_TYPE,
                                                P_CIRCUIT_NO=P_CIRCUIT_NO,P_ACTION_TYPE=P_ACTION_TYPE,
                                                P_RETURN_CODE=P_RETURN_CODE,P_RETURN_MESG=P_RETURN_MESG,
                                                P_ATTRIBUTE1=P_ATTRIBUTE1,P_ATTRIBUTE2=P_ATTRIBUTE2,
                                                P_ATTRIBUTE3=P_ATTRIBUTE3)
        # TODO check response
        print "response", response
    except Exception, e:
        import traceback
        print traceback.format_exc()
        print "%s"%(client.last_sent().str())
        print str(e)

pass_request_to_client_esb()
