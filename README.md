🧠 Pomodoro Timer - Boost Your Focus!
A simple and customizable Pomodoro timer app to help you stay productive and manage your time effectively. Perfect for work, study, or daily task management.

🌟 Features
🕒 Customizable work/short break/long break durations
🔊 Sound alerts for transitions (e.g., atomic bomb explosion sound)
🎛️ Intuitive GUI with Start/Pause/Reset controls
📦 No Python installation required for end-users (create .exe with PyInstaller)
💻 Cross-platform (Windows/macOS/Linux)
🛠️ Setup Instructions
For End Users (No Python Required)
📦 Download and extract the archive
🔊 Place the sound file (Atom.mp3) in the same directory as the app
🚀 Double-click the executable file to run the timer
For Developers (With Source Code)
📥 Clone the repository
🧬 Install dependencies:
bash
pip install playsound
🔊 Replace Atom.mp3 with your preferred sound file (MP3 format)
🏃 Run the app:
bash
python pomodoro_timer.py
🎨 Customize Your Timer
🕐 Set durations in minutes (work time, short break, long break)
💾 Click "Save" to apply settings
▶️ Use controls: Start, Pause, Reset
🔁 Long break triggers every 4 completed work cycles
🧱 Build Your Own Executable
🔧 Install PyInstaller:
bash
pip install pyinstaller
🔨 Create a single executable file:
bash
pyinstaller --onefile --windowed --add-data "Atom.mp3;." pomodoro_timer.py
📁 Distribute the .exe file from the dist/ folder
📁 File Structure
pomodoro-timer/
├── pomodoro_timer.py      # Main application code
├── Atom.mp3               # Alert sound (replace with your own)
└── README.md              # This file
💡 Tips
🔁 Different sounds can be added for work/break transitions
📦 Share the app with friends without requiring Python installation
🎯 Ideal for students, remote workers, and productivity enthusiasts


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
