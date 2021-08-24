# Alfred-UPbit_Tracker
This Workflow is for Korean UPbit users.
[업비트](https://upbit.com/home)에서 가상화폐의 가격을 불러오는 워크플로우입니다.  
티커를 입력하면 해당 가상화폐의 가격, 24시간 고가/저가 등을 보여주며, Keyword만 입력하면 미리 정해진 10개의 가상화폐 가격을 보여줍니다.    
원하신다면 직접 이 리스트를 변경할 수 있습니다. [rhlsthrm/alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker)를 참고하여 만들었습니다.  
  
This workflow was created with reference to: [rhlsthrm/alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker)
  
-------------------
## 설치 방법
* "[UPbit Tracker.alfredworkflow](https://github.com/custardcream98/Alfred-UPbit_Tracker/raw/main/UPbit%20Tracker.alfredworkflow)"를 다운로드합니다.
* 다운로드한 파일을 더블클릭합니다.

## 사용법
### 미리 정의된 10개의 가상화폐 가격 불러오기
* ```upbit``` + Enter : 미리 정의된 10개의 가상화폐(BTC, ETH, ADA, XRP, DOGE, DOT, BCH, LINK, LTC, XLM) 가격을 불러옵니다.
* 정의 리스트를 바꾸고싶다면 다음의 방법을 따라해주세요.
1. Alfred Preferences -> Workflows -> UPbit Tracker 우클릭 -> Open in finder
2. UPbit-tracker.py 우클릭 -> 다음으로 열기 -> 텍스트 편집기
3. command ⌘ + F -> 'coinlist' 입력
4. ```['KRW-BTC','KRW-ETH','KRW-ADA','KRW-XRP','KRW-DOGE','KRW-DOT','KRW-BCH','KRW-LINK','KRW-LTC','KRW-XLM']```의 형식을 지켜서 바꿔주시면 됩니다. (저장 잊지 마세요!)
5. 추가로, 1번 과정에서 열었던 폴더 내의 'icon' 폴더에 가상화폐의 아이콘을 ```가상화폐 이름(소문자).png```로 넣어주시면 리스트를 불러올 때 아이콘이 제대로 뜹니다.

### 티커를 이용해 특정 가상화폐의 가격 불러오기
* ```upbit {Ticker}``` : 입력된 티커를 이용해 해당 가상화폐의 가격을 불러옵니다. (자동완성 기능은 없으니, 꼭 티커를 끝까지 다 써주세요)

### UPbit로 이동하기
모든 과정에서 해당 가상화폐를 누르면 업비트의 해강 가상화폐 가격 페이지로 이동합니다.

## 주의사항
업비트 정책으로 인해 지나치게 자주 사용하시면 일시적으로 사용이 불가하니, 너무 자주 사용하지는 말아주세요. (시간이 지나면 다시 사용 가능해집니다.)
  
--------------------
## Credits
* [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) by denishe
* [alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker) by rhlsthrm
* [UPbit](https://upbit.com/home)
