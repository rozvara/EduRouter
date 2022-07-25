# This file is part of `EduRouter tools'

# This is intended for educational purposes

# Seeing is believing:
# demonstration of intercepted/modified content

from mitmproxy import http
from io import BytesIO
from PIL import Image

def response(flow):

    # if content is an image, flip it upside down
    if flow.response.headers.get("content-type", "") in ("image/jpeg", "image/png",  "image/gif"):
        image = Image.open(BytesIO(flow.response.content))
        image = image.rotate(180)
        memfile = BytesIO()
        image.save(memfile, format="png")
        flow.response.content = memfile.getvalue()
        flow.response.headers["content-type"] = "image/png"

