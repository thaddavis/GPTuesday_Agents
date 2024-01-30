from langchain.tools import StructuredTool
import requests
import json


def call_docket_api(params):
    print("Enter the DocketApiTool...")
    return {}


DocketApiTool = StructuredTool.from_function(
    name="DocketApiTool",
    func=call_docket_api,
    description="""Use the DocketApiTool to fetch information about dockets.
The call_docket_api function takes 2 params: { countyName: string, caseNumber: string }

ie: Example #1
ie: Example #2
""",
    return_direct=True,
)
