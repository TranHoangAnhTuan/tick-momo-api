from .MomoResponse import Momo
import uuid

# endpoint = "https://test-payment.momo.vn/v2/gateway/api/create"
# partnerCode = "MOMO"
# accessKey = "F8BBA842ECF85"
# secretKey = "K951B6PE1waDMi640xX08PD3vg6EkVlz"
# orderInfo = "pay with MoMo"
# redirectUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
# ipnUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
# amount = "50000"
# orderId = '123'
# requestId = '123'
# requestType = "captureWallet"
# extraData = ""  # pass empty value or Encode base64 JsonString



def MomoResponse(amount):
    endpoint = "https://payment.momo.vn/v2/gateway/api/create"
    partnerCode = "MOMO0DDM20220908"
    accessKey = "eGeQE9L8ub8tM1G4"
    secretKey = "p7EObsGMJIEQkZgAms5uh8bUg8pBXcQ7"
    orderInfo = "pay with MoMo"
    redirectUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
    ipnUrl = "https://webhook.site/b3088a6a-2d17-4f8d-a383-71389a6c600b"
    orderId = str(uuid.uuid4())
    requestId = str(uuid.uuid4())
    requestType = "captureWallet"
    extraData = ""  # pass empty value or Encode base64 JsonString
    payment = Momo(endpoint, partnerCode, accessKey, secretKey, orderInfo, redirectUrl, ipnUrl, amount, orderId, requestId, requestType, extraData)
    signature = payment.sign()
    # print(signature)
    data = {
        'partnerCode': partnerCode,
        'partnerName': "Test",
        'storeId': "MomoTestStore",
        'requestId': requestId,
        'amount': amount,
        'orderId': orderId,
        'orderInfo': orderInfo,
        'redirectUrl': redirectUrl,
        'ipnUrl': ipnUrl,
        'lang': "vi",
        'extraData': extraData,
        'requestType': requestType,
        'signature': signature
    }
    # print(payment)
    return payment.dump(data)