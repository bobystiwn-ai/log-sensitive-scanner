import json
import sys
import requests

def send_report(endpoint, file):
    try:
        response = requests.post(endpoint, json=file)
        print(f"server response {response.status_code}")
        if(response.status_code >= 200 & response.status_code < 300 ):
            print("report succes")

        else:
            print("report failed")
    except Exception as e:
        print(f"server error {str(e)}")


if __name__ == "__main__":

    if len(sys.argv) != 2 :
        print("proses usage: python3 reporter.py <log_path>")
        sys.exit(1)


    try:

        file_json = json.loads(sys.argv[1])
        endpoint = "https://httpbin.org/post"
        send_report(endpoint, file_json)

    except Exception as e:
        print(f"error {str(e)}")