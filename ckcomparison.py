import glob
import os

list_of_certificates = glob.glob("/config/filestore/files_d/*/certificate_d/*")
list_of_keys = glob.glob("/config/filestore/files_d/*/certificate_key_d/*")

cert_dict = {}
key_dict = {}
failed_certs = []

print '\n', ' CERTIFICATES FOUND '.center(125, '='), '\n'
for c in list_of_certificates:
    print c.rjust(125)
print '\n', ' KEYS FOUND '.center(125, '='), '\n'
for k in list_of_keys:
    print k.rjust(125)

for certificate in list_of_certificates:
    a = os.popen('openssl x509 -in %s -modulus -noout | openssl md5' % certificate)
    cert_hash = a.read()
    cert_dict[cert_hash] = certificate

for key in list_of_keys:
    b = os.popen('openssl rsa -in %s -modulus -noout | openssl md5' % key)
    key_hash = b.read()
    key_dict[key_hash] = key

print '\n', ' CERTS - KEYS MATCH '.center(125, '=')

for k in cert_dict.keys():
    if key_dict.has_key(k):
        print '\n', 'Cer: ', cert_dict[k].rjust(119), '\nKey: ', key_dict[k].rjust(119), '\n'
        print '-' * 125
    else:
        failed_certs.append(cert_dict[k])

print '\n', ' CERTS WITH NO MATCH '.center(125, '='), '\n'
for cert in failed_certs:
    print 'Cer: ', cert.rjust(119)
