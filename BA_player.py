from PIL import Image
import time
import winsound
import os
import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p


def play_BA(configuration):
    
    # Font setup
    if configuration['custom_font'] != None:
        LF_FACESIZE = 32
        STD_OUTPUT_HANDLE = -11

        class COORD(ctypes.Structure):
            _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

        class CONSOLE_FONT_INFOEX(ctypes.Structure):
            _fields_ = [("cbSize", ctypes.c_ulong),
                        ("nFont", ctypes.c_ulong),
                        ("dwFontSize", COORD),
                        ("FontFamily", ctypes.c_uint),
                        ("FontWeight", ctypes.c_uint),
                        ("FaceName", ctypes.c_wchar * LF_FACESIZE)]
            
        font = CONSOLE_FONT_INFOEX()
        font.cbSize = ctypes.sizeof(CONSOLE_FONT_INFOEX)
        font.nFont = configuration['custom_font'][1]
        font.dwFontSize.X = configuration['custom_font'][1]
        font.dwFontSize.Y = configuration['custom_font'][1]
        font.FontFamily = 54
        font.FontWeight = 400
        font.FaceName = f'{configuration["custom_font"][0]}'

        handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
        ctypes.windll.kernel32.SetCurrentConsoleFontEx(handle, ctypes.c_long(False), ctypes.pointer(font))

    os.system('color 0f')


    # Window setup
    max_resolution = (480, 360)
    resolution = configuration['resolution']
    if all(resolution): coefficient = (max_resolution[0] // resolution[0], max_resolution[1] // resolution[1])
    else: coefficient = (0, 0)

    os.system(f'mode {resolution[0] + configuration["window_margin"][0]}, {resolution[1] + configuration["window_margin"][1]}')
    white, gray, gray2, black = 'o', 'x', '+', ' '


    # Countdown
    for seconds in range(configuration['countdown'], 0, -1):
        os.system('cls')
        print(seconds)
        time.sleep(1)


    # Music setup
    if configuration['play_music']: winsound.PlaySound('Bad Apple!!.wav', winsound.SND_ASYNC)


    # Play video
    starttime = time.time()
    while True:
        # Get frame
        playtime = time.time()

        frame = int(30 * (playtime - starttime)) + configuration['starting_frame']
        
        try: frame_img = Image.open(f"frames/BA-{frame:0>5}.jpg")   
        except FileNotFoundError:
            if frame < 6572:
                winsound.PlaySound('Bad Apple!!.wav', winsound.SND_PURGE)
                print('\n' * 84, 'Error, file "frames/BA-{frame:0>5}.jpg" not found.')
                input('Press ENTER to close\n')
                return 1
            else: return 0


        # Print frame
        screen = []
        for y in range(resolution[1]):
            for x in range(resolution[0]):
                pixel = frame_img.getpixel((x*coefficient[0], y*coefficient[1]))[0]
                screen.append(white if pixel >= 235
                              else gray if pixel < 235 and pixel >= 157
                              else gray2 if pixel < 157 and pixel > 80
                              else black)
            screen.append('\n')
        print(*screen, sep='', end='')


        frame_img.close()


        # Cleaning
        time.sleep(configuration['cleaning_delay'] / 1000)

        match(configuration['cleaning_mode'][0]):
            case 'winsetcursor':
                ctypes.windll.kernel32.SetConsoleCursorPosition(ctypes.windll.kernel32.GetStdHandle(c_long(-11)), c_ulong(0))
            case 'newline': print('\n' * configuration['cleaning_mode'][1])
            case 'wincls': os.system('cls')