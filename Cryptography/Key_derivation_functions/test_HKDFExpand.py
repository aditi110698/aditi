import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDFExpand

info = b"hkdf-example"
key_material = os.urandom(16)
hkdf = HKDFExpand(
    algorithm=hashes.SHA256(),
    length=32,
    info=info,
)
key = hkdf.derive(key_material)
hkdf = HKDFExpand(
    algorithm=hashes.SHA256(),
    length=32,
    info=info,
)
hkdf.verify(key_material, key)