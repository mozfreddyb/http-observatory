from database import get_cursor, insert_test_result
from scanner import STATE_FAILED
from scanner.retriever import retrieve_all

from celery import Celery
from os import environ

import scanner.analyzer
import sys

app = Celery('http_observatory_scanner', broker=environ['BROKER_URL'])


# TODO: make this into a Celery task
def scan(hostname: str, site_id: int, scan_id: int):
    # Attempt to retrieve all the resources
    try:
        reqs = retrieve_all(hostname)
    except:
        # TODO: have more specific error messages
        e = sys.exc_info()[1]  # get the error message

        # If we are unsuccessful in close out the scan in the database if it failed
        with get_cursor() as cur:
            cur.execute("""UPDATE scans
                             SET (status, end_time, error) = (%s, NOW(), %s)
                             WHERE id = %s
                             RETURNING *""",
                        (STATE_FAILED, repr(e), scan_id))
            return

    # Get all the tests
    tests = [f for _, f in scanner.analyzer.__dict__.items() if callable(f)]

    for test in tests:
        # TODO: Get overridden expectation
        test_name = test.__name__.replace('_', '-')
        insert_test_result(site_id, scan_id, test_name, test(reqs))
