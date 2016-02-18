import glob
import os

list_of_certificates = glob.glob("/config/filestore/files_d/*/certificate_d/*")
list_of_keys = glob.glob("/config/filestore/files_d/*/certificate_key_d/*")

cert_dict = {}
key_dict = {}
intersection = []

print '\n', ' CERTIFICATES FOUND '.center(100, '='), '\n\n', list_of_certificates
print '\n', ' KEYS FOUND '.center(100, '='), '\n\n', list_of_keys

for certificate in list_of_certificates:
    a = os.popen('openssl x509 -in %s -modulus -noout | openssl md5' % certificate)
    cert_hash = a.read()
    cert_dict[cert_hash] = certificate

for key in list_of_keys:
    b = os.popen('openssl rsa -in %s -modulus -noout | openssl md5' % key)
    key_hash = b.read()
    key_dict[key_hash] = key

for k in cert_dict.keys():
    if key_dict.has_key(k):
        intersection.append(k)

print '\n', ' CERTS - KEYS MATCH '.center(100, '=')
for i in intersection:
    if i in cert_dict:
        print '\n', 'Cer: ', cert_dict[i].rjust(94), '\nKey: ', key_dict[i].rjust(94)
        print '-' * 100
