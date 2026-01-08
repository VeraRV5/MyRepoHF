import requests


def httpinfo (Link):
   L = Link
   r = requests.get(L)

   try:
      print ("Status Code: ", r.status_code)
      print ("Headers: ", r.headers)
      print ("Body:", r.text)
   except Exception as e:
      print ("Error:", e)




L = "https://httpbin.org/get"
httpinfo(L)

H = "https://httpbin.org/headers"
httpinfo(H)

C = "https://httpbin.org/get?navn=ditnavn&alder=20"
httpinfo(C)