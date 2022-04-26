import time
import hmac
from requests import Request, Session

API = "API_KEY"
API_secret = "API_SECRET"

string = "https://ftx.com/api/wallet/withdrawals"
ts = int(time.time() * 1000)

payload = {
  "coin": "BTC",
  "size": input.get("amount"),
  "address": input.get("wallet"),
  "tag": None,
}

request = Request('POST', string, json=payload)
prepared = request.prepare()

signature_payload = f'{ts}{prepared.method}{prepared.path_url}'.encode()
if prepared.body:
    signature_payload += prepared.body

signature_payload = signature_payload
signature = hmac.new(API_secret.encode(),
                     signature_payload, 'sha256').hexdigest()

prepared.headers['FTX-KEY'] = API
prepared.headers['FTX-SIGN'] = signature
prepared.headers['FTX-TS'] = str(ts)
prepared.headers['FTX-SUBACCOUNT'] = "SUBACCOUNT"
session = Session()
resp = session.send(prepared)

output = { "Success": False, "JSON Response": "No Error"}

if resp.json()["success"] == True:
  output["Success"] = resp.json()["success"]
else:
  output["Success"] = resp.json()["success"]
  output["JSON Response"] = resp.json()['error']

print("Status Code", resp.status_code)
print("JSON Response", resp.json())