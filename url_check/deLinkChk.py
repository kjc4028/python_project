import urllib
import urllib.request as req
from urllib.error import URLError, HTTPError
import time
from tqdm import tqdm

result = open('url_check/url_list_rs.txt','w',encoding='UTF-8')
# url_list.txt ANSI로 저장하기
with open('url_check/url_list.txt','rt') as f:
    lines = f.read().splitlines()

    for i, url in tqdm(enumerate(lines)):
        try:
            response=req.urlopen(url,timeout=10)
            contents=response.read()
        except HTTPError as e:
            errCode = ""
            if e.code is not None:
                errCode = e.code
            print(url,"|실패|",errCode, file=result)
        except URLError as e:
            errCode = ""
            if e.reason is not None:
                errCode = e.reason
            print(url,"|실패|",errCode, file=result)
        except ConnectionResetError as e:
            print(url,"|강제연결종료|", file=result)
        except TimeoutError as e:
            print(url,"|타임아웃|", file=result)
        except Exception as e:
            print(url,"|알수없음|", file=result)
        else:
            print(url,"|성공|", file=result)
f.close()
result.close()