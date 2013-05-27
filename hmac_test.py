import hmac
import hashlib
import base64

#hmac uses the provided key to generate a salt and make the hash more strong, while hashlib only hashes the provided message.

#your_bytes_string1 = "GET\nwebservices.amazon.com\n/onca/xml\nAWSAccessKeyId=00000000000000000000&ItemId=0679722769&Operation=ItemLookup&ResponseGroup=ItemAttributes%2COffers%2CImages%2CReviews&Service=AWSECommerceService&Timestamp=2009-01-01T12%3A00%3A00Z&Version=2009-01-06"
your_bytes_string2 = "GET\nlocalhost:8081\n/ipsum/v1/3\nAuthID=test&AuthType=SHA256&AuthVers=1&TimeStamp=2013-05-27T10:50:00"
dig = hmac.new(b'1234567890', msg=your_bytes_string2, digestmod=hashlib.sha256).digest()
print(base64.b64encode(dig).decode())
#expected result 'your_bytes_string1' : Nace+U3Az4OhN7tISqgs1vdLBHBEijWcBeCqL5xN9xg=
#expected result 'your_bytes_string2' : E2UoCsLVP2XUGueDlW15Ghnh2Dr1/+66uvdwCtrAcq0=




#http://localhost:8081/ipsum/v1/3

#Authorization: E2UoCsLVP2XUGueDlW15Ghnh2Dr1/+66uvdwCtrAcq0=
#AuthID: test
#AuthType: SHA256
#AuthVers: 1
#TimeStamp: 2013-05-27T10:50:00