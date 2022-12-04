import json
import urllib.request
import urllib
import uuid
import requests
import hmac
import hashlib


class Momo:
    def __init__(self, endpoint, partnerCode, accessKey, secretKey, orderInfo, redirectUrl, ipnUrl, amount, orderId, requestId, requestType, extraData):
        self.endpoint = endpoint
        self.partnerCode = partnerCode
        self.accessKey = accessKey
        self.secretKey = secretKey
        self.orderInfo = orderInfo
        self.redirectUrl = redirectUrl
        self.ipnUrl = ipnUrl
        self.amount = amount
        self.orderId = orderId
        self.requestId = requestId
        self.requestType = requestType
        self.extraData = extraData

    
    def sign(self):
        raw_signature = "accessKey=" + self.accessKey + "&amount=" + self.amount + "&extraData=" + self.extraData + "&ipnUrl=" + self.ipnUrl + "&orderId=" + self.orderId + "&orderInfo=" + self.orderInfo + "&partnerCode=" + self.partnerCode + "&redirectUrl=" + self.redirectUrl + "&requestId=" + self.requestId + "&requestType=" + self.requestType

        # Generate the Signature
        h = hmac.new(bytes(self.secretKey, 'ascii'), bytes(raw_signature, 'ascii'), hashlib.sha256)
        return h.hexdigest()


    def dump(self, data):
        # JSON Request
        data = json.dumps(data)
        clen = len(data)
        response = requests.post(self.endpoint, data=data, headers={'Content-Type': 'application/json', 'Content-Length': str(clen)})
        # Return the response JSON
        return response.json()


 