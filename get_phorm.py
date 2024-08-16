import requests
import json
from dataclasses import dataclass

from typing import List


@dataclass
class RetrievedNode:
    uri: str
    source_code: str
    start_line: int
    end_line: int


@dataclass
class PhormResult:
    answer: str
    query: str
    retrieved_nodes: List[RetrievedNode]


def query_phorm(query):
    url = "https://www.phorm.ai/api/db/generate_answer"

    headers = {
        "Host": "www.phorm.ai",
        "Sec-Ch-Ua": '"Chromium";v="125", "Not.A/Brand";v="24"',
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Ch-Ua-Mobile": "?0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Origin": "https://www.phorm.ai",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.phorm.ai/query?projectId=3e83d206-4b71-4888-bd68-7a9c55f791d2",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Priority": "u=1, i",
    }

    data = {
        "query": query,
        "project": "3e83d206-4b71-4888-bd68-7a9c55f791d2",
        "repos": [
            "https://github.com/aorwall/moatless-tools/tree/main/",
        ],
    }

    cookies = {
        "appSession": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIiwidWF0IjoxNzIzNzcwMzMyLCJpYXQiOjE3MjM2OTQwNzUsImV4cCI6MTcyMzg1NjczMn0..H8mpMgl4BaclvAPI.RtgwLztop4o-PsFZTTWp7ED2mrvKM476yHYk4h9QGHCq4d71y-kIPXbW5eo7Kcfuc1ck2f1c9x7NV0Dqkz-TV-H08hQOlnn5hCN4nd7iMrjZgDWeLpkA4mB3dGglZcZsgwULTK8f3RsGpieROvyhUaf1aMsdh00lv28UcRmp5_JggrSeF1Py9PH6-VcNPmb-0ulMe3osGWpXnUBFSy-CzJQeK5nIew0KfHgzYR-EgDIFGgMRBJ1zrveAhNSBN-1_eTEps7jPYJsNjOuHBRn9eVn_yxK_q1xRrq6KVbh0Qy0cyB7VYIITfpehzjjAOYcmct7sa7O5_sfZKAkUbJjn70CBQKD7hd6QQowwH1pj6N518HCOl4DR5YurxRtLjtCLTYH8S-99cf6-7Povi39zE6j8N7ipQgZt8Qolin6x0C7iQAVP1QOA3SlVZoymAxfsJ_G3TJh4Dhq4XpxyV3pNvZz91aQb1wbMyyjuJ6QGcM65LLRdfgoUnaM06rzdCWX-Vb9LygvHdT_gPyM8hBwE7FRGSpLY-LR7m6Jiq71ATl7WDE958I2mk97av09bDnbskbciVrJsmaj7sBa4VcjDHVjQDzRmXPxWmjfSZ2IifY4hdQbdQIBxTR9ZUv-ukuhFhvGeqnGclAuB32LRfbLGikShnsAx47emrUfkajs2vWlb7hZDSseN6DYENlarIpo5Cks_I6k4i8XMs6vik_VAJNxmnuZ-cI-FIVv66xqGwTXPRG7MMVJSsEnGXFdpKPI_casNK3cVeDr60d_RZwD70WJq-V5-oPj8VCkcj1B7g76DjvT-TQZ6aCliOdTwYRKCP6JcsAWCj-8FLtf2fI24nTpArw-ohjqmr6c8ZA8F_9b_fuUGvidvdz_rN0zwthCaPQ_XGniNRk7jy-MhpXTRUtNHVs_svVIeZv0MNiGIUsHWGQtj-EKw9dC1wlOM2IVcKYHdpr-Nv7VLPYmiaoQtkvPHuKYJPBqcQANViHT_u4_asSZJrk6h8Gs2L28JijBAEGKenOAZZW35-TOxzxfP_4bw0DYaMGt04edTtc6ml9LI0-D5xI49EcYDgvt-G8A59rTIAm16-uekOI4YUja95Py9i9HtGXNJ9TNKERRCBvvhf_w9TprxT3wdo75kFSA30MrYuDI9YZIe1yk84sso8yvwWhx5nKLsfQ64makniS0KOXfzi7z-GF6iXiYGFMHh-NTPUu2bqXeGLPDTbClgJ5wIGfvnq29iM2N4e7ZJ-2JY0LXk6bGluPAfkyM6ZEJj56ycDG37nTCoyMV6X8TPUUqVS3Rin4XQyiCL58aCrgnIcUgrqGd0tSh0rR_6kYAorAjOoUd23r4_26LF2xt7KLBJlGW8gLeI7l4y4npXgc9l98pTiQl4zKse_gKKqECl4rlCSIpSKuB5ZwRbpe7qqvqWmdjxXYtWiMlIJTRq3K-VWR_7vX8lkqtZnadJdTC6Jc5RR5dNsjgoPdsi7sg5oK82byFOfRT7HHQKUlcRNDGEeo6NuwfwkqvzfkoK9ZiIJd3rMrM2ZWwXC_Wkl-6VzD1Yo4HHqfx0y5Op_HnkVHDom-ITCg_qW5GFCpnnAiV7-eHHP9Qmf3wFgn73MvpYahbs67VQmguadIX_mEz8XYQcgW7BHIAJAIbfaqM5TjOCtpInVpvzZyTycfDST7dlJfjzpFJ6wpytYh2tN8xY8m-gWBwv3KP0s33oUsbPzlLVuJv6lZgOqFMKnCVAF4NZ6FJAqquQWRyNOUAOnjlhUsOVxtYexWvpaoZ1DjGJUXt3Fe8ejC8zyPxD23JLsYwnZNsdtPUwyBjYSvbKa2-mQZdvS0LvGnb5is9YLXON_oJiZYC-birevo_LlbwUNWI5bEPxdy44j7rVy9OALb41H-NSIEhXp2LAR464qdLzTWxYFgAKbbx3v-rRROa_2JBEqdwP8AfmuTjpcaBV2S3Oqu37Kk2YTec7kjwZh_AIkRRAd7f-MxhkVl0R7Zzm5J8CGVA4EEfgXNPMa-a0G4pbTgv4kW6ltMWwfY5-JdWRDZzbi9HVesZVJZVqhU1yb3kaaWkXlkK5FWxdI7ZYz8-swtUEJDiprmC0gSB0PmIBzxPC9_Ej20uC_U6jQV0Kkr5JE0pL5swVwTtAiAMhcYglZq7Jm4egLBEHE3tHKk_Hifw82xnJNNHC7G-RBgL-Hy92l3ZashEbOG7eyhiSzQOdH1-_AdPpZPUl0CP5qFBSZ9YRUy3QDR_2JrkCPoKPshX5mwPtiO-hRY88hnIKoyCh4SFiVXBv0Qzdks_u9ZrQNevrIlUHODwHKsAh1O3EHdGQMR_LjEREmJnQ7AbLsn7ykfMfkIOqFIacb7N7T1KniW1bn56dnwOwJ7aZT2DTVGEDrHYa6XaTDCHvk_7EzDxVu92_QAVpzZJ-NG6kVeZL41LBHCy82m1txUIJY_XN4i3ethnMmIEm8GvnX8MVYeJNFxsB3RaZm5cyM26hP5eI8Uen-3K7B08p0TaqLInl4xABxBeJnhcF_umYAVZVpqZE5OH6CM-o6vwjpW1txP3NDI_FcSZ1b88G38WGbLcyM5yvah91v4N00M4uf4ndIeJvIjGq3heOvejxa3aAIqokkcA5NIpmvX8FWB9zOAxPTVFmK4l2KGXmrrnP84QUgMCa1nSt2g_I1QO-SJnxvI3g0qooTAooKyK6APet1VDZ3wq_gALL3XKsmVvjDIyXuA283kAZjYYXumU5-ug28o8n8QiHziWxVYDOtQ1uTKSf_m350IbzsVjFobDBzexD5XrI3R5hhNPKPaCSRX6HwP_TC7JLmocCjIAVAbqNLCPmEJfBLBsxRcltKhFGMTv_A_Qch319NSqXPL9p1gkb.1_zikLm343UXEcdFHdvZLQ"
    }

    response = requests.post(
        url, headers=headers, json=data, verify=False, cookies=cookies
    )

    data = json.loads(response.text)

    retrieved_nodes = []
    print(data)
    for node in data["retrieved_nodes"]:
        line_range = node.split("#")[1]
        start_line, end_line = map(int, line_range.lstrip("L").split("L"))

        retrieved_nodes.append(
            RetrievedNode(
                uri=node["uri"],
                source_code=node["source_code"],
                start_line=start_line,
                end_line=end_line,
            )
        )

    return PhormResult(
        answer=data["answer"],
        query=data["query"],
        retrieved_nodes=retrieved_nodes,
    )


print(query_phorm("Show me all the places where repomap is used in the code?"))
