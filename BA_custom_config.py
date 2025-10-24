import os

import BA_incheck


def custom_config(configuration):

    def select_config(selected_setting = None):
        
        def print_config():
            os.system('cls')
            print(
                'Select a setting:\n',
                f'1. Resolution: {configuration["resolution"]}',
                f'2. Right and Bottom window margin: {configuration["window_margin"]}',
                f'3. Frame cleaning: {configuration["cleaning_mode"]}',
                f'4. Cleaning delay: {configuration["cleaning_delay"]}',
                f'5. Play music: {configuration["play_music"]}',
                f'6. Countdown before starting: {configuration["countdown"]}',
                f'7. Starting frame: {configuration["starting_frame"]}',
                f'8. Custom font: {configuration["custom_font"]}',
                f'0. Return\n',
                sep='\n')
        
        if selected_setting == None:
            while True:
                print_config()
                user_input = input('>> ')
                if (
                    BA_incheck.inputcheck(user_input, 'int')
                    #and 0 <= int(user_input)
                    #and int(user_input) <= 6
                    ): return int(user_input)

        print_config()
        print(f'>> {selected_setting}\n')
    

    def set_config(selected_setting):
        while True:
            select_config(selected_setting)
            print()
            try:
                match(selected_setting):
                    case 1:    
                        print('Insert resolution value:\n')
                        print('>> 60 45\t--> 60x45 mode')
                        print('>> 120 90\t--> 120x90 mode')
                        print('>> 160 120\t--> 160x120 mode\n')
                        
                        new_value = tuple(map(int, input('>> ').split()))
                        if len(new_value) != 2: raise ValueError

                        configuration['resolution'] = new_value

                    case 2:
                        print('Set right and bottom window margin:\n')
                        print('>> 3 3\t--> 3 right and 3 bottom margin space')
                        print('>> 4 5\t--> 4 right and 5 bottom margin space')
                        print('>> 3 0\t--> 3 right and 0 bottom margin space\n')
                        
                        new_value = tuple(map(int, input('>> ').split()))
                        if len(new_value) != 2: raise ValueError

                        configuration['window_margin'] = new_value

                    case 3:
                        print('Insert cleaning mode:\n')
                        print('>> winsetcursor\t--> set console cursor to start and print over old frame')
                        print('>> wincls\t--> use \'cls\' command to clear console and print')
                        print('>> newline 84\t--> print 84 newlines between each frame\n')
                        
                        new_value = tuple(input('>> ').split())
                        if new_value[0] == 'newline':
                            if int(new_value[1]) < 0: raise ValueError
                            new_value = (new_value[0], int(new_value[1]))
                        elif new_value[0] == 'wincls':
                            if len(new_value) != 1: raise ValueError
                            new_value = (new_value[0], )
                        elif new_value[0] == 'winsetcursor':
                            if len(new_value) != 1: raise ValueError
                            new_value = (new_value[0], )
                        else: raise ValueError
                        
                        configuration['cleaning_mode'] = new_value

                    case 4:
                        print('Insert delay between frames in milliseconds (ms):\n')
                        print('>> 0\t--> 0 ms delay')  
                        print('>> 33\t--> 1/30 ms delay')
                        print('>> 1000\t--> 1000 ms delay\n')
                        
                        new_value = input('>> ')             
                        if not BA_incheck.inputcheck(new_value, 'int') or int(new_value) < 0: raise ValueError
                        new_value = int(new_value)

                        configuration['cleaning_delay'] = new_value

                    case 5:
                        print('Play music:\n')
                        print('>> y\t--> set to \'yes\'')
                        print('>> n\t--> set to \'no\'\n')

                        new_value = input('>> ')
                        if new_value == 'y': configuration['play_music'] = True
                        elif new_value == 'n': configuration['play_music'] = False
                        else: raise ValueError

                    case 6:
                        print('Set countdown before starting in seconds (s):\n')
                        print('>> 0\t--> Start immediately')
                        print('>> 3\t--> 3 seconds before starting')
                        print('>> 5\t--> 5 seconds before starting\n')

                        new_value = input('>> ')             
                        if not BA_incheck.inputcheck(new_value, 'int') or int(new_value) < 0: raise ValueError
                        new_value = int(new_value)

                        configuration['countdown'] = new_value

                    case 7:
                        print('Starting frame (max: 6572):\n')
                        print('>> 0\t--> Start from beginning')
                        print('>> 824\t--> Start from frame n° 824')
                        print('>> 3323\t--> Start from frame n° 3323\n')

                        new_value = input('>> ')             
                        if not BA_incheck.inputcheck(new_value, 'int') or int(new_value) < 0: raise ValueError
                        new_value = int(new_value)

                        configuration['starting_frame'] = new_value

                    case 8:
                        print('Set custom font to be used, will be searched on C:\Windows\Fonts:\n')
                        print('>> none\t--> use current cmd font')
                        print('>> raster, 6\t--> set to windows raster font with size 6, font need to be installed or won\'t work')
                        print('>> [name of the font]\t--> set to custom installed font with default size 6')
                        print('>> [name of the font], [n°]\t--> set to custom installed font and size\n')
                        
                        new_value = tuple(input('>> ').split(','))
                        if len(new_value) == 2:
                            new_value = (new_value[0], int(new_value[1]))
                        elif len(new_value) == 1:
                            match(new_value[0]):
                                case 'none': new_value = None
                                case 'raster': new_value = ('Raster Fonts 8x8', 6)
                                case _: new_value = (new_value[0], 6)
                        else: raise ValueError
                        
                        configuration['custom_font'] = new_value
                        
                    case _: break
                break
            except: pass


    while True:
        selected_setting = select_config()
        if selected_setting == 0: return configuration
        set_config(selected_setting)