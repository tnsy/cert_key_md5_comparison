import glob
import os

list_of_certificates = glob.glob("/config/filestore/files_d/Common_d/certificate_d/*")
list_of_keys = glob.glob("/config/filestore/files_d/Common_d/certificate_key_d/*")

cert_dict = {}
key_dict = {}

#print list_of_certificates
#print list_of_keys

for certificate in list_of_certificates:
    a = os.popen('openssl x509 -in %s -modulus -noout | openssl md5' % certificate)
    cert_hash = a.read()
    cert_dict[certificate] = cert_hash   
    #print cert_hash

for key in list_of_keys:
    b = os.popen('openssl rsa -in %s -modulus -noout | openssl md5' % key)
    key_hash = b.read()
    key_dict[key] = key_hash
    #print key_hash

print '\nCERT DICT:',cert_dict, '\n'
print 'KEY DICT:', key_dict

x = set(cert_dict.values())
y = set(key_dict.values())

z = x.intersection(y)
z = str(z)
print '\n\n\nZ =' , z
cut = z[6:-5]
print '\n\n\nCUT = ', cut, '\n\n'

for key, value in cert_dict.iteritems():
    value = str(value)
    print value
    if value == cut:
        print YEA 
    else:
        print 'Nothing found'
