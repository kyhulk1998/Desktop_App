
from pyotp import HOTP
from base64 import b32encode
from datetime import datetime
from hashlib import sha256, blake2b, md5, sha512
# Static random (6 digits)

# Create combine hash


def hash_generator(var_1, var_2, var_3):
    var_1_hash = sha256(var_1.encode('ascii')).hexdigest()
    var_2_hash = blake2b(var_2.encode('ascii')).hexdigest()
    var_3_hash = md5(var_3.encode('ascii')).hexdigest()
    return sha512((var_1_hash + var_2_hash + var_3_hash).encode('ascii')).hexdigest()

# Create encryption key - server & desktop app


def key_generator(license_id, editable, printable, username, phone, owner):
    hash_value = hash_generator(
        str(editable + printable), username + phone, owner)
    return sha256((hash_value + license_id + ' ').encode('ascii')).hexdigest()


# Create OTP - server & desktop app


def OTP_generator(license_id, downloader, username, phone, expDate, random_code):
    timeNowCreate = datetime.now()
    time_create = timeNowCreate.minute
    hash_value = hash_generator(
        license_id + downloader, username + phone, expDate + "asfb86")
    hash_value_base32 = b32encode(hash_value.encode('ascii'))
    hotp = HOTP(hash_value_base32)
    return time_create, hotp


# Verify OTP - only desktop app

def OTP_verification(OTP_value, time_create, hotp, random_code):
    timeNowVerify = datetime.now()
    time_verify = timeNowVerify.minute
    if time_verify - time_create < 5:
        if hotp.verify(OTP_value, random_code):
            return True
        else:
            return "OTP is wrong!!"
    else:
        return "OTP expires!!!"
