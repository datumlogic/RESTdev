import json
import bottle
from bottle import route, run, request
import hmac
import hashlib
import base64

# REST Signature: VERB\nURI\nACTION/SRV_VERS (vX)/parameter/AuthID=[test]&AuthType=[SHA256]&AuthVers=[1]&TimeStamp=['YYYYMMDDT24h:MM:SS' in UDT]
# eg- GET\nlocalhost:8081\n/ipsum/v1/3\nAuthID=test&AuthType=SHA256&AuthVers=1&TimeStamp=2013-05-27T10:50:00"
host = ''

@route('/ipsum/:vers/:para', method='GET')
def get_ipsum(vers,para):
	newval = 'ERROR'
	#for key, value in request.headers.items():
	#	if key == 'Authorization': newval = value

	global host
	host = request.headers.get('Host')
	auth = request.headers.get('Authorization')
	authID = request.headers.get('AuthID')
	authType = request.headers.get('AuthType')
	authVers = request.headers.get('AuthVers')
	dateTime = request.headers.get('TimeStamp')
	byte_string = 'GET\n' + host + '\n/ipsum/' + vers + '/' + para + '\nAuthID=' + authID + '&AuthType=' +  authType + '&AuthVers=' + authVers + '&TimeStamp=' + dateTime
	
	#need to check dateTime to prevent Replay Attack
	
	#for protyping only- the shared secret should be looked up in a database? or derived using ECDH?
	sharedsecret = ''
	if authID == 'test':
		sharedsecret = '1234567890'
	
	#if AuthVers = 1 and SRV_VERS = v1- when implemented, the AuthVers would determine how the 
	#signature is formed, and the service version would determine how the returned data is derived and formated
	signature = (hmac.new(sharedsecret, msg=byte_string, digestmod=hashlib.sha256).digest())
	b64signature = (base64.b64encode(signature).decode())
	
	#for now just returning the signature, but need to return XML or JSON result (BuddhaIpsum)
	#at that point should incvlude param in URL for return type? xml or json?
	return byte_string + '\nSignature: ' + b64signature + '\nAuthorised: ' + str(b64signature == auth)

 
run(host=host, port=8081)