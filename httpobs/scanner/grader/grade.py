GRADE_CHART = {
    100: 'A+',
    95: 'A',
    90: 'A',
    85: 'A-',
    80: 'B+',
    75: 'B',
    70: 'B',
    65: 'B-',
    60: 'C+',
    55: 'C',
    50: 'C-',
    45: 'D+',
    40: 'D',
    35: 'D-',
    30: 'E',
    25: 'E',
    20: 'F',
    15: 'F',
    10: 'F',
    5: 'F',
    0: 'F'
}

GRADES = set(GRADE_CHART.values())

SCORE_TABLE = {
    # contribute.json
    'contribute-json-with-required-keys': {
        'description': 'Contribute.json implemented with the required contact information',
        'modifier': 0,
    },
    'contribute-json-only-required-on-mozilla-properties': {
        'description': 'Contribute.json isn\'t required on websites that don\'t belong to Mozilla',
        'modifier': 0,
    },
    'contribute-json-missing-required-keys': {
        'description': 'Contribute.json exists, but is missing some of the required keys',
        'modifier': -5,
    },
    'contribute-json-not-implemented': {
        'description': 'Contribute.json file missing from root of website',
        'modifier': -10,
    },
    'contribute-json-invalid-json': {
        'description': 'Contribute.json file cannot be parsed',
        'modifier': -10,
    },

    # CSP
    'csp-implemented-with-no-unsafe': {
        'description': 'Content Security Policy (CSP) implemented without unsafe-inline or unsafe-eval',
        'modifier': 0,
    },
    'csp-implemented-with-unsafe-inline-in-style-src-only': {
        'description': 'Content Security Policy (CSP) implemented with unsafe-inline inside style-src directive',
        'modifier': -5,
    },
    'csp-implemented-with-unsafe-eval': {
        'description': 'Content Security Policy (CSP) implemented, but allows unsafe-eval',
        'modifier': -10,
    },
    'csp-implemented-with-unsafe-inline': {
        'description': 'Content Security Policy (CSP) implemented, but allows unsafe-inline',
        'modifier': -20,
    },
    'csp-implemented-with-insecure-scheme': {
        'description': 'Content Security Policy (CSP) implemented, but allows resources to be loaded from http',
        'modifier': -20,
    },
    'csp-header-invalid': {
        'description': 'Content Security Policy (CSP) header cannot be parsed successfully',
        'modifier': -25,
    },
    'csp-not-implemented': {
        'description': 'Content Security Policy (CSP) header not implemented',
        'modifier': -25,
    },

    # Cookies
    'cookies-secure-with-httponly-sessions': {
        'description': 'All cookies use the Secure flag and all session cookies use the HttpOnly flag',
        'modifier': 0,
    },
    'cookies-not-found': {
        'description': 'No cookies detected',
        'modifier': 0,
    },
    'cookies-without-secure-flag-but-protected-by-hsts': {
        'description': 'Cookies set without using the Secure flag, but transmission over HTTP prevented by HSTS',
        'modifier': -5,
    },
    'cookies-session-without-secure-flag-but-protected-by-hsts': {
        'description': 'Session cookie set without the Secure flag, but transmission over HTTP prevented by HSTS',
        'modifier': -10,
    },
    'cookies-without-secure-flag': {
        'description': 'Cookies set without using the Secure flag or set over http',
        'modifier': -20,
    },
    'cookies-session-without-httponly-flag': {
        'description': 'Session cookie set without using the HttpOnly flag',
        'modifier': -30,
    },
    'cookies-session-without-secure-flag': {
        'description': 'Session cookie set without using the Secure flag or set over http',
        'modifier': -40,
    },

    # Cross-origin resource sharing
    'cross-origin-resource-sharing-not-implemented': {
        'description': 'Content is not visible via cross-origin resource sharing (CORS) files or headers',
        'modifier': 0,
    },
    'cross-origin-resource-sharing-implemented-with-public-access': {
        'description': ('Public content is visible via cross-origin resource sharing (CORS) '
                        'Access-Control-Allow-Origin header'),
        'modifier': 0,
    },
    'cross-origin-resource-sharing-implemented-with-restricted-access': {
        'description': ('Content is visible via cross-origin resource sharing (CORS) files or headers, '
                        'but is restricted to specific domains'),
        'modifier': 0,
    },
    'cross-origin-resource-sharing-implemented-with-universal-access': {
        'description': 'Content is visible via cross-origin resource sharing (CORS) file or headers',
        'modifier': -50,
    },

    # Public Key Pinning
    'hpkp-preloaded': {
        'description': 'Preloaded via the HTTP Public Key Pinning (HPKP) preloading process',
        'modifier': 5,
    },
    'hpkp-implemented-max-age-at-least-fifteen-days': {
        'description': 'HTTP Public Key Pinning (HPKP) header set to a minimum of 15 days (1296000)',
        'modifier': 5,
    },
    'hpkp-implemented-max-age-less-than-fifteen-days': {
        'description': 'HTTP Public Key Pinning (HPKP) header set to less than 15 days (1296000)',
        'modifier': 1,
    },
    'hpkp-not-implemented': {
        'description': 'HTTP Public Key Pinning (HPKP) header not implemented',
        'modifier': 0,
    },
    'hpkp-not-implemented-no-https': {
        'description': 'HTTP Public Key Pinning (HPKP) header can\'t be implemented without https',
        'modifier': 0,
    },
    'hpkp-header-invalid': {
        'description': 'HTTP Public Key Pinning (HPKP) header cannot be recognized',
        'modifier': -5,
    },

    # Redirection
    'redirection-to-https': {
        'description': 'Initial redirection is to https on same host, final destination is https',
        'modifier': 0,
    },
    'redirection-not-needed-no-http': {
        'description': 'Not able to connect via http, so no redirection necessary',
        'modifier': 0,
    },
    'redirection-off-host-from-http': {
        'description': 'Initial redirection from http to https is to a different host, preventing HSTS',
        'modifier': -5,
    },
    'redirection-not-to-https-on-initial-redirection': {
        'description': 'Redirects to https eventually, but initial redirection is to another http URL',
        'modifier': -10,
    },
    'redirection-not-to-https': {
        'description': 'Redirects, but final destination is not an https URL',
        'modifier': -20,
    },
    'redirection-missing': {
        'description': 'Does not redirect to an https site',  # if there's no HTTPS at all, other tests will score -100
        'modifier': -20,
    },

    # Strict Transport Security (HSTS)
    'hsts-preloaded': {
        'description': 'Preloaded via the HTTP Strict Transport Security (HSTS) preloading process',
        'modifier': 5,
    },
    'hsts-implemented-max-age-at-least-six-months': {
        'description': 'HTTP Strict Transport Security (HSTS) header set to a minimum of six months (15768000)',
        'modifier': 0,
    },
    'hsts-implemented-max-age-less-than-six-months': {
        'description': 'HTTP Strict Transport Security (HSTS) header set to less than six months (15768000)',
        'modifier': -10,
    },
    'hsts-not-implemented': {
        'description': 'HTTP Strict Transport Security (HSTS) header not implemented',
        'modifier': -20,
    },
    'hsts-header-invalid': {
        'description': 'HTTP Strict Transport Security (HSTS) header cannot be recognized',
        'modifier': -20,
    },
    'hsts-not-implemented-no-https': {
        'description': 'HTTP Strict Transport Security (HSTS) header cannot be set for sites not available over https',
        'modifier': -20,
    },

    # Subresource Integrity (SRI)
    'sri-implemented-and-all-scripts-loaded-securely': {
        'description': 'Subresource Integrity (SRI) is implemented and all scripts are loaded from a similar origin',
        'modifier': 5,
    },
    'sri-implemented-and-external-scripts-loaded-securely': {
        'description': 'Subresource Integrity (SRI) is implemented and all scripts are loaded securely',
        'modifier': 5,
    },
    'sri-not-implemented-response-not-html': {
        'description': 'Subresource Integrity (SRI) is only needed for html resources',
        'modifier': 0,
    },
    'sri-not-implemented-but-no-scripts-loaded': {
        'description': 'Subresource Integrity (SRI) is not needed since site contains no script tags',
        'modifier': 0,
    },
    'sri-not-implemented-but-all-scripts-loaded-from-secure-origin': {
        'description': 'Subresource Integrity (SRI) not implemented as all scripts are loaded from a similar origin',
        'modifier': 0,
    },
    'sri-not-implemented-but-external-scripts-loaded-securely': {
        'description': 'Subresource Integrity (SRI) not implemented, but all external scripts are loaded over https',
        'modifier': -5,
    },
    'sri-implemented-but-external-scripts-not-loaded-securely': {
        'description': 'Subresource Integrity (SRI) implemented, but external scripts are loaded over http',
        'modifier': -20,
    },
    'sri-not-implemented-and-external-scripts-not-loaded-securely': {
        'description': 'Subresource Integrity (SRI) is not implemented, and external scripts are loaded over http',
        'modifier': -50,
    },

    # X-Content-Type-Options
    'x-content-type-options-nosniff': {
        'description': 'X-Content-Type-Options header set to "nosniff"',
        'modifier': 0,
    },
    'x-content-type-options-not-implemented': {
        'description': 'X-Content-Type-Options header not implemented',
        'modifier': -5,
    },
    'x-content-type-options-header-invalid': {
        'description': 'X-Content-Type-Options header cannot be recognized',
        'modifier': -5,
    },

    # X-Frame-Options
    'x-frame-options-implemented-via-csp': {
        'description': 'X-Frame-Options (XFO) implemented via the CSP frame-ancestors directive',
        'modifier': 5,
    },
    'x-frame-options-sameorigin-or-deny': {
        'description': 'X-Frame-Options (XFO) header set to SAMEORIGIN or DENY',
        'modifier': 0,
    },
    'x-frame-options-allow-from-origin': {
        'description': 'X-Frame-Options (XFO) header uses ALLOW-FROM uri directive',
        'modifier': 0,
    },
    'x-frame-options-not-implemented': {
        'description': 'X-Frame-Options (XFO) header not implemented',
        'modifier': -20,
    },
    'x-frame-options-header-invalid': {
        'description': 'X-Frame-Options (XFO) header cannot be recognized',
        'modifier': -20,
    },

    # X-XSS-Protection
    'x-xss-protection-enabled-mode-block': {
        'description': 'X-XSS-Protection header set to "1; mode=block"',
        'modifier': 0,
    },
    'x-xss-protection-enabled': {
        'description': 'X-XSS-Protection header set to "1"',
        'modifier': 0,
    },
    'x-xss-protection-not-needed-due-to-csp': {
        'description': 'X-XSS-Protection header not needed due to strong Content Security Policy (CSP) header',
        'modifier': 0,
    },
    'x-xss-protection-disabled': {
        'description': 'X-XSS-Protection header set to "0" (disabled)',
        'modifier': -10,
    },
    'x-xss-protection-not-implemented': {
        'description': 'X-XSS-Protection header not implemented',
        'modifier': -10,
    },
    'x-xss-protection-header-invalid': {
        'description': 'X-XSS-Protection header cannot be recognized',
        'modifier': -10,
    },

    # Generic results
    'html-not-parsable': {
        'description': 'Claims to be html, but cannot be parsed',
        'modifier': -20,  # can't run an SRI check if the HTML isn't parsable
    },
    'request-did-not-return-status-code-200': {
        'description': '/ did not return a status code of 200',
        'modifier': -5,  # can't run an SRI check on pages that don't return a 200
    },
    'xml-not-parsable': {
        'description': 'Claims to be xml, but cannot be parsed',
        'modifier': -20,  # can't run an ACAO check if the xml files can't be parsed
    }
}


def get_grade_for_score(score: int) -> tuple:
    """
    :param scan_id: the scan_id belonging to the tests to grade
    :return: the overall test score and grade
    """

    score = max(score, 0)  # can't have scores below 0

    # If it's >100, just use the grade for 100, otherwise round down to the nearest multiple of 5
    grade = GRADE_CHART[min(score - score % 5, 100)]

    return score, grade


def get_score_description(result) -> str:
    return SCORE_TABLE[result]['description']


def get_score_modifier(result) -> int:
    return SCORE_TABLE[result]['modifier']
