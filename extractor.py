import sys # for import system library
import json # change file.log to json
import subprocess # to start command shell in file extractor

sensitive_keyword = ["password", "username", "API", "token"]
# fungtion extract and save file_log to json
def extract_file_log(path):
    findings = {}
    try:
        # read and open file.log
        with open(path, "r") as file:
            line = file.readlines()
        # find keyword and save result to 
            for keyword in sensitive_keyword:
                findings[keyword] = []
                for lines in line:
                    if keyword in lines:
                        findings[keyword].append(lines.strip())
        # export log to json
       
        return json.dumps(findings)
    except Exception as e:
        print(f"error {str(e)}")


#extract json to reporter
def extract_to_reporter(file_path):
    subprocess.run(["python3", "reporter.py", file_path])

# program utama
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("program usage python3, extractor.py, <log_path>")
        sys.exit(1)

    log_path = sys.argv[1]
    json_extract = extract_file_log(log_path)
    extract_to_reporter(json_extract)
