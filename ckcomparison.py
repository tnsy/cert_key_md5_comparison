import glob
import os

list_of_certificates = glob.glob("/config/filestore/files_d/Common_d/certificate_d/*")
list_of_keys = glob.glob("/config/filestore/files_d/Common_d/certificate_key_d/*")

cert_dict = {}
key_dict = {}
intersection = []

print 'CERTS: %r\n\n' % list_of_certificates
print 'KEYS: %r\n\n' % list_of_keys

for certificate in list_of_certificates:
    a = os.popen('openssl x509 -in %s -modulus -noout | openssl md5' % certificate)
    cert_hash = a.read()
    cert_dict[cert_hash] = certificate
    print 'CERT HASH: %r\n\n' % cert_hash

for key in list_of_keys:
    b = os.popen('openssl rsa -in %s -modulus -noout | openssl md5' % key)
    key_hash = b.read()
    key_dict[key_hash] = key
    print 'KEY HASH: %r\n\n' % key_hash


for k in cert_dict.keys():
    if key_dict.has_key(k):
        intersection.append(k)

#print 'AFTER ADDING TO INTERSECTION LIST: %r\n\n' % intersection

for i in intersection:
    if i in cert_dict:
        print 'Following pairs match - ', cert_dict[i], key_dict[i]
