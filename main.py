from kivymd.app import MDApp
from kivy.lang import Builder
from kivmob import KivMob, TestIds
from kivymd.toast import toast
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
class BotBuild(MDApp):
	#anti vpn and installing modules
	import requests 
	import webbrowser
	import json 
	import time
	ch = requests.get("http://ip-api.com/json/?fields=33292287")
	ip = ch.json()["query"]
	if ch.json()["proxy"] == True:
		toast("Sorry! this app cant run with proxys it may lead to problems, leaving in process")
		time.sleep(3)
		exit()
		
	toast("connected to "+ch.json()["country"])
	#bot functions 
	def bot(self):
		try:
			toast("running the bot")
			import discord 
			import time
			from discord.ext import commands
			client = commands.Bot(command_prefix=self.root.ids.prefix.text)
			@client.event
			async def on_ready():
				activity = discord.Game(name=f"being hosted by slicycord client | prefix: {self.root.ids.prefix.text}", type=3)
				await client.change_presence(status=discord.Status.dnd, activity=activity)
				toast("bot is online and ready")		
			
			client.run(self.root.ids.token.text)
	#error handler 
		except Exception as e:
			toast(str(e))
	
	#creators of app
	def credits(self):
		import webbrowser
		webbrowser.open("https://youtube.com/channel/UCqwE6vaLW1eVX6L3msbvTzw?sub_confirmation=1")
		#app building 
	def build(self):
		screen = """
Screen:
		MDTextField:
				hint_text:"bot token"
				mode: "rectangle"
				size_hint:.9,.1
				pos_hint:{"center_x":.5,"center_y":.7}
				id: token
		MDTextField:
				hint_text:"bot prefix"
				mode: "rectangle"
				size_hint:.9,.1
				pos_hint:{"center_x":.5,"center_y":.6}
				id: prefix 
		Button:
				text:"run bot"
				size_hint:.5,.1
				pos_hint:{"center_x":.5,"center_y":.3}
				on_press: app.bot()	
	
		Screen:
				MDNavigationLayout:
						
						ScreenManager:
								Screen:
										BoxLayout:
												orientation: "vertical"
												MDToolbar:
														title: "more"
														pos_hint:{"center_x":.5,"center_y":.8}
														elevation: 10
														left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
														
														Widget:
																
						MDNavigationDrawer:
								id: nav_drawer
						        BoxLayout:
						        		orientation: "vertical"
						        		MDRectangleFlatButton:
						        				text: "creators yt"
						        				pos_hint:{"center_x":.5,"center_y":.8}
						        				on_press: app.credits()			
						        		MDRectangleFlatButton:
						        				text: "discord server"
						        				pos_hint:{"center_x":.5,"center_y":.5}
						        				on_press: app.webbrowser.open("https://discord.gg/msUfWvBsyQ")
		"""
		self.title = "SlicyCordClient Android"
		self.theme_cls.primary_platte = "DarkPurple"
		self.ads = KivMob(TestIds.APP)
		self.ads.new_banner(TestIds.BANNER, top_pos=True)
		self.ads.request_banner()
		self.ads.show_banner()
		return Builder.load_string(screen)
#starting the app
BotBuild().run()
