# 🧠 Pomodoro Timer - Boost Your Focus!
A simple and customizable Pomodoro timer app to help you stay productive and manage your time effectively. Perfect for work, study, or daily task management.

# 🌟 Features
1) 🕒 Customizable work/short break/long break durations 
2) 🔊 Sound alerts for transitions (e.g., atomic bomb explosion sound)
3) 🎛️ Intuitive GUI with Start/Pause/Reset controls
4) 📦 No Python installation required for end-users (create .exe with PyInstaller)
5) 💻 Cross-platform (Windows/macOS/Linux)
# 🛠️ Setup Instructions
For End Users (No Python Required)
1) 📦 Download and extract the archive
2) 🔊 Place the sound file (Atom.mp3) in the same directory as the app
3) 🚀 Double-click the executable file to run the timer
# For Developers (With Source Code)
1) 📥 Clone the repository
2) 🧬 Install dependencies: pip install playsound
3) 🔊 Replace Atom.mp3 with your preferred sound file (MP3 format)
4) 🏃 Run the app: python pomodoro_timer.py
5) 🎨 Customize Your Timer
6) 🕐 Set durations in minutes (work time, short break, long break)
7) 💾 Click "Save" to apply settings
8) ▶️ Use controls: Start, Pause, Reset
9) 🔁 Long break triggers every 4 completed work cycles
10) 🧱 Build Your Own Executable
11) 🔧 Install PyInstaller: pip install pyinstaller
12) 🔨 Create a single executable file: pyinstaller --onefile --windowed --add-data "Atom.mp3;." pomodoro_timer.py
13) 📁 Distribute the .exe file from the dist/ folder
# 📁 File Structure
pomodoro-timer/
1) pomodoro_timer.py      # Main application code
2) Atom.mp3               # Sound
3) Pomodorka.exe          # Exe-file for non-programmers
4) README.md              # This file
# 💡 Tips
1) 🔁 Different sounds can be added for work/break transitions
2) 📦 Share the app with friends without requiring Python installation
3) 🎯 Ideal for students, remote workers, and productivity enthusiasts


# Pomodoro-timer
Pomodoro-timer для фокусирования на делах
# Инструкция для пользователя
1) Скачать архив и распаковать
2) В одну директорию положить файл с кодом и звуком
3) Перед работой обязательно в терминале прописать pip install playsound
4) При желании изменить звук таймера нужно в папку с файлом кода загрузить желаемый звук в формате mp3 и в последних строчках изменить название файла(ну или же назвать
   свой звук "Atom" и удалить уже имеющийся
5) Всё готово к запуску! В приложении вы можете задать длину таймера  работы, перерыва и длинного перерыва (в минутах, целые числа). После выбранного времени нажать сохранить и запустить таймер. Имеются кнопку продолжения, паузы и остановки таймера 
6) При желании сделать exe файл пропишите в командной строке
   а) pip install pyinstaller (если еще не установлен)
   б) pyinstaller --onefile --windowed --add-data "Atom.mp3;." Pomodorka.py (названия файла меняются в зависимости от названий ваших файлов)
