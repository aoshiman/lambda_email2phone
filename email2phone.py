# -*- coding: utf-8 -*-

from __future__ import print_function
from twilio.rest import TwilioRestClient
from twilio import TwilioRestException
from setting import SID, SECRET, TARGET, FROM, URL


def makecall(sid, secret, target, from_, url, timeout=10):
    try:
        client = TwilioRestClient(sid, secret)
        call = client.calls.create(
                to=target,
                from_=from_,
                url=url,
                timeout=timeout
                )

    except TwilioRestException as e:
        print(e)


def lambda_handler(event, context):
    try:
        makecall(SID, SECRET, TARGET, FROM, URL)

    except Exception as e:
        print(e)
