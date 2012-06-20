# This file is autogenerated from test_rparser.py
# It contains the translation of r expressions into their 
# (network-) serialized representation.

binaryRExpressions = {
    '"abc"': b'\x01\x00\x01\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x08\x00\x00\x22\x04\x00\x00\x61\x62\x63\x00',
    '1': b'\x01\x00\x01\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x0c\x00\x00\x21\x08\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x3f',
    'as.integer(c(1))': b'\x01\x00\x01\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x08\x00\x00\x20\x04\x00\x00\x01\x00\x00\x00',
    'c(1)': b'\x01\x00\x01\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x0c\x00\x00\x21\x08\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x3f',
    'c(1, 2)': b'\x01\x00\x01\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x14\x00\x00\x21\x10\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x3f\x00\x00\x00\x00\x00\x00\x00\x40',
    'as.integer(c(1, 2))': b'\x01\x00\x01\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x0c\x00\x00\x20\x08\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00',
    'TRUE': b'\x01\x00\x01\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x0c\x00\x00\x24\x08\x00\x00\x01\x00\x00\x00\x01\xff\xff\xff',
    'c(TRUE, FALSE, TRUE)': b'\x01\x00\x01\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x0c\x00\x00\x24\x08\x00\x00\x03\x00\x00\x00\x01\x00\x01\xff',
    'c("abc", "defghi")': b'\x01\x00\x01\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x10\x00\x00\x22\x0c\x00\x00\x61\x62\x63\x00\x64\x65\x66\x67\x68\x69\x00\x01',
    'seq(1, 5)': b'\x01\x00\x01\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x18\x00\x00\x20\x14\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00',
    'polyroot(c(-39.141,151.469,401.045))': b'\x01\x00\x01\x00\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x24\x00\x00\x26\x20\x00\x00\xc2\xec\x7f\x77\xd9\x8d\xc6\x3f\x00\x00\x00\x00\x00\x00\xf0\x39\xf8\xfc\x8b\xe3\x76\xb9\xe1\xbf\x00\x00\x00\x00\x00\x00\xf0\xb9',
    'list("otto")': b'\x01\x00\x01\x00\x14\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x10\x00\x00\x10\x0c\x00\x00\x22\x08\x00\x00\x6f\x74\x74\x6f\x00\x01\x01\x01',
    'list("otto", "gustav")': b'\x01\x00\x01\x00\x20\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x1c\x00\x00\x10\x18\x00\x00\x22\x08\x00\x00\x6f\x74\x74\x6f\x00\x01\x01\x01\x22\x08\x00\x00\x67\x75\x73\x74\x61\x76\x00\x01',
    'list(husband="otto")': b'\x01\x00\x01\x00\x30\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x2c\x00\x00\x90\x28\x00\x00\x15\x18\x00\x00\x22\x08\x00\x00\x68\x75\x73\x62\x61\x6e\x64\x00\x13\x08\x00\x00\x6e\x61\x6d\x65\x73\x00\x00\x00\x22\x08\x00\x00\x6f\x74\x74\x6f\x00\x01\x01\x01',
    'list(husband="otto", wife="erna")': b'\x01\x00\x01\x00\x44\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x40\x00\x00\x90\x3c\x00\x00\x15\x20\x00\x00\x22\x10\x00\x00\x68\x75\x73\x62\x61\x6e\x64\x00\x77\x69\x66\x65\x00\x01\x01\x01\x13\x08\x00\x00\x6e\x61\x6d\x65\x73\x00\x00\x00\x22\x08\x00\x00\x6f\x74\x74\x6f\x00\x01\x01\x01\x22\x08\x00\x00\x65\x72\x6e\x61\x00\x01\x01\x01',
    'list(n="Fred", no_c=2, c_ages=c(4,7))': b'\x01\x00\x01\x00\x58\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x54\x00\x00\x90\x50\x00\x00\x15\x20\x00\x00\x22\x10\x00\x00\x6e\x00\x6e\x6f\x5f\x63\x00\x63\x5f\x61\x67\x65\x73\x00\x01\x01\x13\x08\x00\x00\x6e\x61\x6d\x65\x73\x00\x00\x00\x22\x08\x00\x00\x46\x72\x65\x64\x00\x01\x01\x01\x21\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x21\x10\x00\x00\x00\x00\x00\x00\x00\x00\x10\x40\x00\x00\x00\x00\x00\x00\x1c\x40',
    'c(a=1.,b=2.,c=3.)': b'\x01\x00\x01\x00\x3c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x38\x00\x00\xa1\x34\x00\x00\x15\x18\x00\x00\x22\x08\x00\x00\x61\x00\x62\x00\x63\x00\x01\x01\x13\x08\x00\x00\x6e\x61\x6d\x65\x73\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x3f\x00\x00\x00\x00\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x08\x40',
    'c(a=1)': b'\x01\x00\x01\x00\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x24\x00\x00\xa1\x20\x00\x00\x15\x14\x00\x00\x22\x04\x00\x00\x61\x00\x01\x01\x13\x08\x00\x00\x6e\x61\x6d\x65\x73\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x3f',
    'array(1:20, dim=c(4, 5))': b'\x01\x00\x01\x00\x70\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0a\x6c\x00\x00\xa0\x68\x00\x00\x15\x14\x00\x00\x20\x08\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x13\x04\x00\x00\x64\x69\x6d\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00\x05\x00\x00\x00\x06\x00\x00\x00\x07\x00\x00\x00\x08\x00\x00\x00\x09\x00\x00\x00\x0a\x00\x00\x00\x0b\x00\x00\x00\x0c\x00\x00\x00\x0d\x00\x00\x00\x0e\x00\x00\x00\x0f\x00\x00\x00\x10\x00\x00\x00\x11\x00\x00\x00\x12\x00\x00\x00\x13\x00\x00\x00\x14\x00\x00\x00',
    }
