__author__ = 'Raul'

ParamHeaderRequest = ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Accept-Datetime',
                      'Authorization', 'Cache-Control', 'Cache-Control', 'Connection', 'Cookie', 'Content-Length',
                      'Content-MD5', 'Content-Type', 'Date', 'DNT', 'Expect', 'From', 'Host', 'If-Match',
                      'If-Modified-Since', 'If-None-Match', 'If-Range', 'If-Unmodified-Since', 'Max-Forwards', 'Origin',
                      'Pragma', 'Proxy-Authorization', 'Range', 'Referer', 'TE', 'User-Agent', 'Upgrade', 'Via',
                      'Warning']

ParamHeaderResponse = ['Access-Control-Allow-Origin', 'Accept-Patch', 'Accept-Ranges', 'Age', 'Allow', 'Cache-Control',
                       'Connection', 'Content-Disposition', 'Content-Encoding', 'Content-Language', 'Content-Length',
                       'Content-Location', 'Content-MD5', 'Content-Range', 'Content-Type', 'Date', 'ETag', 'Expires',
                       'Last-Modified', 'Link', 'Location', 'P3P', 'Pragma', 'Proxy-Authenticate', 'Refresh',
                       'Retry-After', 'Server', 'Set-Cookie', 'Status', 'Strict-Transport-Security', 'Trailer',
                       'Transfer-Encoding', 'Upgrade', 'Vary', 'Via', 'Warning', 'WWW-Authenticate', 'X-Frame-Options']

DictReqRes = {'Request': ParamHeaderRequest, 'Response': ParamHeaderResponse}

TAGSHTTP = ['GET', 'POST', 'HEAD', 'PUT', 'DELETE', 'TRACE', 'OPTIONS', 'CONNECT']

ParametersAllPages = {}