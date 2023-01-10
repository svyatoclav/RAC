
# RAC 
## Random Auto Cut 

RAC (Random Auto Cut) for Premiere Pro, DaVinci Resolve and other editing software. Generates .edl files of random moments in random videos in specific directory.

Рандомная Авто Нарезка. Создаёт файлы типа .edl со случайными отрезками случайных видео из выбранной папки. EDL импортируются в видеоредакторы как таймлайны. 

Параметры регулируются в самом файле. Перед использованием установите opencv-python `pip install opencv-python` 

`
cuts # number of cuts (clips) (количество склеек (клипов)) 
minl # min length of cut in frames (in 30 fps 1 frame = 33 milsec) (минимальная длина клипа в кадрах (в 30-и FPS 1 кадр = 33 миллисекунды)) 
maxl # max length of cut in frames (in 30 fps 60 frames = 2 sec) (максимальная длина клипа в кадрах (в 30-и FPS 60 кадров = 2 секунды)) 
rdml # max random length of cut (максимальная длина "суперрандомного" клипа) 
rdmlprob # random length probability (вероятность "суперрандомного" клипа) 
realfps # frames per second (set when need REAL FPS, than also swap "videoFPS[rdmboth]" to "realfps" in line 78)  (реальный ФПС, выставлять для РЕАЛЬНОГО FPS видоса, после этого поменять значение "videoFPS[rdmboth]" на "realfps" в строке 78) 
`

Запускается из терминала или даблкликом по файлу. 

### Политика лицензирования 
Мне пофиг кто это вообще юзать будет лол 

