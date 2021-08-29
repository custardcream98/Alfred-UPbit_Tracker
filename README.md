# Alfred-UPbit_Tracker
This Workflow is for Korean UPbit users.  
[업비트](https://upbit.com/home)에서 가상화폐의 가격을 불러오는 풀 한국어 워크플로우입니다. 실시간 가격이며, 아직 원화마켓만 지원합니다.  
티커를 입력하면 해당 가상화폐의 실시간 가격, 일봉 기준 고가/저가 등을 보여주며, Keyword만 입력하면 미리 정해진 10개의 가상화폐 가격을 보여줍니다. [원하신다면 직접 이 리스트를 변경할 수 있습니다.](https://github.com/custardcream98/Alfred-UPbit_Tracker#%EA%B0%80%EC%83%81%ED%99%94%ED%8F%90-%EC%95%84%EC%9D%B4%EC%BD%98-%EC%B6%94%EA%B0%80%ED%95%98%EA%B8%B0)  
[rhlsthrm/alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker)를 참고하여 만들었습니다.<br/><br/>
  
This workflow was created with reference to: [rhlsthrm/alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker)<br/><br/><br/>
  
-------------------
## 설치 방법
* "[UPbit Tracker.alfredworkflow](https://github.com/custardcream98/Alfred-UPbit_Tracker/raw/main/UPbit%20Tracker.alfredworkflow)"를 다운로드합니다.
* 다운로드한 파일을 더블클릭합니다.
* [Releases](https://github.com/custardcream98/Alfred-UPbit_Tracker/releases)에서도 다운받을 수 있습니다.<br/><br/><br/><br/>


## 사용법
* `가격 기준 시각`은 불러오는 일봉의 기준이 되는 시각을 발합니다.
### 미리 정의된 10개의 가상화폐 가격 불러오기
![image](https://user-images.githubusercontent.com/87423085/131241334-9eff3a89-c103-4dee-9d77-efcdaba12ad0.png)
* `upbit` + Enter : 미리 정의된 10개의 가상화폐(BTC, ETH, ADA, XRP, DOGE, DOT, BCH, LINK, LTC, XLM) 가격을 불러옵니다.
* 정의 리스트를 바꾸고싶다면 다음의 방법을 따라해주세요.
>1. Alfred Preferences -> Workflows -> UPbit Tracker 우클릭 -> Open in finder
>2. UPbit-tracker.py 우클릭 -> 다음으로 열기 -> 텍스트 편집기
>3. command ⌘ + F -> 'coinlist' 입력
>4. `['BTC','ETH','ADA','XRP','DOGE','DOT','BCH','LINK','LTC','XLM']`의 형식을 지켜서 바꿔주시면 됩니다. (저장 잊지 마세요!)

<br/><br/>
### 티커를 이용해 특정 가상화폐의 가격 불러오기
![image](https://user-images.githubusercontent.com/87423085/131241677-ced95757-1fbc-4307-9bca-210de75a2558.png)
* `upbit {Ticker}` : 입력된 티커를 이용해 해당 가상화폐의 가격을 불러옵니다. (자동완성 기능은 없으니, 꼭 티커를 끝까지 다 써주세요)
<br/><br/>
### UPbit로 이동하기
모든 과정에서 해당 가상화폐를 누르면 업비트의 해당 가상화폐 차트로 이동합니다.
<br/><br/>
### 가상화폐 아이콘 추가하기
* Alfred Preferences -> Workflows -> UPbit Tracker 우클릭 -> Open in finder 내의 icon 폴더에 `가상화폐 이름(소문자).png`의 형식으로 아이콘을 추가해주세요.
* 아이콘이 없는 가상화폐 검색 시에는 아이콘이 표시되지 않습니다.
<br/><br/><br/><br/>
## 주의사항
업비트 정책으로 인해 *지나치게 자주 사용하시면 일시적으로 사용이 불가*하니, 너무 자주 사용하지는 말아주세요. (v0.0.4에서 해당 부분 해결한것으로 생각하나, 혹시 문제가 발생한다면 피드백 부탁드립니다.)<br/><br/><br/>  

--------------------
## Credits
* [Alfred-Workflow](https://github.com/deanishe/alfred-workflow) by denishe
* [alfred-crypto-tracker](https://github.com/rhlsthrm/alfred-crypto-tracker) by rhlsthrm
* [UPbit](https://upbit.com/home)
* 'clock.png' icon made by <a href="https://www.flaticon.com/authors/those-icons" title="Those Icons">Those Icons</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
