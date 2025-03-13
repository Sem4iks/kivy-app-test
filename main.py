from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window

Window.size = (300,525)
# Определяем экраны в Python
class FirstScreen(Screen):
    def on_enter(self, *args):
        # Запускаем таймер для перехода на второй экран через 3 секунды
        Clock.schedule_once(self.switch_to_second, 3)

    def switch_to_second(self, dt):
        self.manager.current = 'second'  # Переключаемся на второй экран

class SecondScreen(Screen):
    pass

class ThirdScreen(Screen):
    pass

class FourthScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

# Основное приложение
class MyApp(App):
    def build(self):
        # Создаем ScreenManager и добавляем экраны
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(FourthScreen(name='fourth'))
        sm.add_widget(RegisterScreen(name='register'))
        return sm

if __name__ == '__main__':
    MyApp().run()