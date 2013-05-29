import hmac
import hashlib
import base64

#hmac uses the provided key to generate a salt and make the hash more strong, while hashlib only hashes the provided message.

dig = hmac.new(b'1234567890', msg=your_bytes_string2, digestmod=hashlib.sha256).digest()
print(base64.b64encode(dig).decode())

#=================================================================================

#http://localhost:8081/ipsum/v1/3

#Authorization: E2UoCsLVP2XUGueDlW15Ghnh2Dr1/+66uvdwCtrAcq0=
#AuthID: test
#AuthType: SHA256
#AuthVers: 1
#TimeStamp: 2013-05-27T10:50:00


#http://webdev.datumlogic.com:8081/ipsum/v1/3

#Authorization: JrDV4pH1bw41B2kyUPRTrDa5v9/blsSHJngte+fHbJs=
#AuthID: test
#AuthType: SHA256
#AuthVers: 1
#TimeStamp: 2013-05-27T10:50:00


