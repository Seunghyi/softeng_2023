import PySimpleGUI as sg

import base64
from io import BytesIO
from PIL import Image

from pygame import mixer, time
mixer.init()
clock = time.Clock()

# 음원 불러오기
path = sg.popup_get_file('Open', no_window = True) # ... softeng/homework15/음원.mp3
song_name = path.split('/')[-1].split('.')[0] # 파일 제목만
song = mixer.Sound(path)

# 타이머
song_length = int(song.get_length())
time_since_start = 0
pause_amount = 0
playing = False

def base64_image_import_resize(path, target_size=(50, 50)):
    image = Image.open(path)
    image = image.resize(target_size)
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64

sg.theme('reddit')

play_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Text(song_name, font = 'Arial 20'), sg.Push()],
    [sg.VPush()],
    [
        sg.Push(),
        sg.Button(image_data=base64_image_import_resize('rewind.png'), key='-REWIND-', button_color='white', border_width=0,
                  size=(50, 50)),
        sg.Text(' '),
        sg.Button(image_data=base64_image_import_resize('play.png'), key='-PLAY-', button_color='white', border_width=0, size=(50, 50)),
        sg.Text(' '),
        sg.Button(image_data=base64_image_import_resize('pause.png'), key='-PAUSE-', button_color='white', border_width=0, size=(50, 50)),
        sg.Text(' '),
        sg.Button(image_data=base64_image_import_resize('forward.png'), key='-FORWARD-', button_color='white', border_width=0,
                  size=(50, 50)),
        sg.Push(),
    ],
    [
        sg.Text('00:00', key='-CURRENT_TIME-', justification='left'),  # CURRENT_TIME을 좌측에 배치
        sg.Stretch(),  # 남은 공간을 채움
        sg.Text(f'{song_length // 60:02}:{song_length % 60:02}', key='-TOTAL_TIME-', justification='right'),

    ],
    [sg.ProgressBar(100, size=(100, 5), key='-PROGRESS-')],

]
volume_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Slider(range = (0,100), default_value = 50, orientation = 'h', key = '-VOLUME-'), sg.Push()], # default_value: 시작 값, orientation='h': 가로배치
    [sg.VPush()]
]
etc_layout = [
    [sg.Text('Detail', font='Arial 20')],
    [sg.Text("Title : ", font='Arial 10'), sg.Text(song_name, font='Arial 10')],
    [sg.Text("곡 재생시간 : ", font='Arial 10'), sg.Text(f'{song_length // 60:02}:{song_length % 60:02}', font='Arial 10')],
]

layout = [
    [sg.TabGroup([[sg.Tab('Play', play_layout), sg.Tab('Volume', volume_layout), sg.Tab('etc', etc_layout)]])]

          ]

window = sg.Window('Music Player', layout)
while True:
    event, values = window.read(timeout = 1)
    if event == sg.WIN_CLOSED:
        break

    if playing:
        time_since_start = time.get_ticks()
        current_time = (time_since_start - pause_amount) // 1000
        window['-CURRENT_TIME-'].update(f'{current_time // 60:02}:{current_time % 60:02}')

        progress_value = int((current_time / song_length) * 100)
        window['-PROGRESS-'].update(progress_value)

        if current_time == song_length:
            playing = False
            mixer.stop()


    if event == '-PLAY-':
        playing = True
        # 음악 재생 바 처음부터 시작
        pause_amount += time.get_ticks() - time_since_start
        # 중복 재생 방지
        if mixer.get_busy() == False:
            song.play()
        else:
            mixer.unpause()

    if event == '-PAUSE-':
        playing = False
        mixer.pause()

    # if event == '-REWIND-':
    #     if playing:
    #         new_position = max(0, time.get_ticks() - 10000)
    #         # mixer.music.set_pos(new_position / 1000)
    #         mixer.music.rewind()
    #         mixer.music.play(start=new_position // 1000)
    #
    # if event == '-FORWARD-':
    #     if playing:
    #         new_position = min(song_length * 1000, time.get_ticks() + 10000)
    #         mixer.music.set_pos(new_position / 1000)

    song.set_volume(values['-VOLUME-'] / 100)

window.close()

