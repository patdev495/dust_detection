from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional
from typing import Dict
app = FastAPI()


# Định nghĩa schema cho dữ liệu POST
# Route POST test
@app.post("/api/echo")
def echo(item: dict):
    print(item)
    data = {
    "Status":"fail",
    "Message": "ATE ?",
    "MessageCode": "",
    "Data":{
        "RES":"OK",
        "COMMAND1":"SN=PT53SH04520602GS,TRAY=YO250414AA22LA09,EMP=CYLOPS05,PASSED=1,PASS\r\n",
        "COMMAND2":"",
        "COMMAND3":"",
        "COMMAND4":"",
        "COMMAND5":""
        }
    }
    return data
