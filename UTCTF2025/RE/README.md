## Ostrich Algorithm

![alt text](OstrichAlgorithm.png)

Khá đơn giản chúng ta chỉ cần patch hoặc chỉnh cờ để đi được đến cuối chương trình và nhận được flag
<details>
  <summary>Click để nhìn flag mỗi file có thể có 1 file khác nhau</summary>
  utflag{d686e9b8f13bef2a3078c324ceafd25d}
</details>


## Retro Cookie Clicker

Chúng ta nhận được 1 file gb. Sau 1 lúc tìm hiểu tôi đã mở được nó bằng tool bgb đây là 1 file game boy.
![alt text](retro-cookie-clicker.png)

Qua một hồi tìm kiếm tôi đã tìm được offset lưu điểm mục đích của tôi là chỉnh tối đa điểm này và có được flag.
![alt text](retro-cookie-clicker_1.png)
Tôi thử sửa thành 7FFF max range của short.
![alt text](retro-cookie-clicker_2.png)
Sau đó ấn phím S một lần nữa chúng ta sẽ có được flag.
![alt text](retro-cookie-clicker_3.png)

