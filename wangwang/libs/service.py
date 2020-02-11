import json

from utils.exceptions import OCRServiceUnavailable

from .hw_cloud_ocr_sdk_1_0_4.HWOcrClientToken import HWOcrClientToken

username = "hw08547655"
password = "fk2Qfj5KkbsadNj"
domain_name = "hw08547655"  # If the current user is not an IAM user, the domain_name is the same as the username.
region = "cn-north-4"  # cn-north-1,cn-east-2 etc.

img_path = "data/book.jpg"  # File path or URL of the image to be recognized.

OCR_Client = HWOcrClientToken(domain_name, username, password, region)


def HW_invoice_OCR(img_path):
    try:
        option = {}
        req_uri = "/v1.0/ocr/vat-invoice"
        response = OCR_Client.request_ocr_service_base64(req_uri, img_path, option)
        if response is None:
            raise OCRServiceUnavailable
        return json.loads(response.text)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    HW_invoice_OCR(img_path)
