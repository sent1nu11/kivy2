import kivy
kivy.require('1.9.0') # Kivy ver where the code has been tested
from kivy.app import App
from kivy.uix.label import Label

class e4App(App):
	def build(self):
		return Label()

if __name__ == '__main__':
	e4App().run()
