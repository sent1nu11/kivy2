import kivy
kivy.require('1.9.0') # Kivy ver where the code has been tested
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
	def build(self):
		return Label(ext="Hello World")

if __name__ == '__main__':
	MainApp().run()
