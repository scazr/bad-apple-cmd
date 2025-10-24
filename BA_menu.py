import os

import BA_incheck
import BA_custom_config


def menu():
    os.system('cls')
    print(
        '--== Bad Apple!! ==--',
        'Please install the font located in this directory to make sure that the player will run on recommended font,',
        'alternatively change the used font on settings or disable font change to use default cmd settings.',
        sep='\n')
    
    if input('Press ENTER to continue, or 0 to exit.\n\n>> ') == '0': exit()


def config_menu():
    
    configuration = {
        'resolution': (160, 120),
        'window_margin':(3, 3),
        'cleaning_mode': ('winsetcursor', ),
        'cleaning_delay': 0,
        'play_music': True,
        'countdown': 0,
        'starting_frame': 0,
        'custom_font': ('Raster Fonts 8x8', 6)
    }

    while True:
        os.system('cls')
        print(
            'Select preset:\n',
            '1. Recommended: 160x120, winsetcursor, countdown 0, Raster Font size 6',
            '2. Reduced Size: 120x90, winsetcursor, countdown 0, Raster Font size 6',
            '3. Miniplayer: 60x45, winsetcursor, countdown 0, Raster Font size 6\n\n',
            'Configure preset:\n',
            '4. Edit custom configuration',
            '5. Play custom configuration\n\n',
            '0. Exit\n',
            sep='\n')

        user_input = input('>> ')
        if not(BA_incheck.inputcheck(user_input, 'int')): continue

        match (int(user_input)):
            case 1:
                configuration = {
                    'resolution': (160, 120),
                    'window_margin':(3, 3),
                    'cleaning_mode': ('winsetcursor', ),
                    'cleaning_delay': 0,
                    'play_original': True,
                    'play_music': True,
                    'countdown': 0,
                    'starting_frame': 0,
                    'custom_font': ('Raster Fonts 8x8', 6)
                }
            case 2:
                configuration = {
                    'resolution': (120, 90),
                    'window_margin':(3, 3),
                    'cleaning_mode': ('winsetcursor', ),
                    'cleaning_delay': 0,
                    'play_original': True,
                    'play_music': True,
                    'countdown': 0,
                    'starting_frame': 0,
                    'custom_font': ('Raster Fonts 8x8', 6)
                }
            case 3:
                configuration = {
                    'resolution': (60, 45),
                    'window_margin':(3, 3),
                    'cleaning_mode': ('winsetcursor', ),
                    'cleaning_delay': 0,
                    'play_original': True,
                    'play_music': True,
                    'countdown': 0,
                    'starting_frame': 0,
                    'custom_font': ('Raster Fonts 8x8', 6)
                }
            case 4: BA_custom_config.custom_config(configuration); continue
            case 5: return configuration
            case 0: exit()
            case _: continue
        return configuration