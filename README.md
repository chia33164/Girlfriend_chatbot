# Girlfriend Chatbot

A Facebook messenger bot based on a finite state machine

粉絲團名稱 : Hi Sandy


## Setup

### Prerequisite
* Python 3
* Facebook Page and App
* HTTPS Server

#### Install Dependency
```sh
pip3 install -r requirements.txt
```

#### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
./ngrok http 5000
```

After that, `ngrok` would generate a https URL.

#### Run on google cloud platform

* Use GCP implement deploy

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](https://i.imgur.com/6k0MHTz.png)

## Usage
The initial state is set to `user`.

* state:user

	* Input: "start"
	  * state:choose
	  * Reply: "你女朋友怎麼了嗎?"
	  * Reply: 三個按鈕 1. 她生日到了該送什麼禮物 2. 她月經來了，我該怎麼辦 3. 她正在生氣...，我該怎麼辦

		* Input: 選擇按鈕"她生日到了該送什麼禮物"
		  * state: birthday
		  * Reply: "網路推薦禮物前三名"
		  * Reply: 一張爬蟲後畫出來的圓餅圖
		  * Reply: 三個按鈕 1.鞋子 2.手錶 3.卡片

		* Input: 選擇按鈕"她月經來了，我該怎麼辦"
		  * state: month
		  * Reply: "網路推薦方式前三名"
		  * Reply: 一張爬蟲後畫出來的圓餅圖
		  * Reply: 三個按鈕 1.巧克力 2.不理 3.黑糖

		* Input: 選擇按鈕"她正在生氣...，我該怎麼辦"
		  * state: angry
		  * Reply: "網路推薦方式前三名"
		  * Reply: 一張爬蟲後畫出來的圓餅圖
		  * Reply: 三個按鈕 1.放生 2.道歉 3.禮物

			* Input: 選擇按鈕 巧克力 黑糖 卡片 鞋子 手錶 禮物 道歉
	  		  * state:happy
	  		  * Reply: "恭喜你度過這次難關" (回到 user state)

			* Input: 選擇按鈕 不理 放生
	  		  * state:bad
	  		  * Reply: "你女友：我們分手吧"
			  * Reply: "你想分手嗎？"
			  * Reply: 兩個按紐: 1.分手吧  2.不要拜託

			  	* Input: 選擇按鈕 分手吧
	  		  	  * state:breakup
	  		  	  * Reply: "水啦恭喜你恢復單身！！" (回到 user state)

			  	* Input: 選擇按鈕 不要拜託
	  		  	  * state:unbreakup
	  		  	  * Reply: "你女友：看在你這麼有誠意的份上，我提示你，我現在正在生氣歐！！"
				  * Reply: "她正在生氣嗎？"
				  * Reply: 一個按鈕 1.超氣

					* Input: "超氣"
	  		  	  	  * state:reangry
	  		  	  	  * Reply: "你女友：給我好好選歐"
					  * Reply: 3個按鈕 1.親親 2.道歉 3.禮物

						* Input: 選擇按鈕 親親 道歉 禮物
	  		  	  		  * state:happy
	  		  	  		  * Reply: "恭喜你度過這次難關"  (回到 user state)

