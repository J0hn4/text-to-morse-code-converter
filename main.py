import pygame
import time
from tkinter import*
#todo make morse code library
from Morse_dictionary import MORSE_DICT

#Constants
TIME_BETWEEN = 0.5  # Time between sounds
PATH = "morse_code_audio(1)/morse_code_audio/" #Path to morse code audio files for letters and numbers


#Condition to keep program running inside of a while loop
run_program = True


"""Convert ogg files to mp3"""
def ogg2mp3(input_files, outputdir, lame_V):
    for ogg_file in input_files:
        #Convert ogg file to wav
        input_file_dir, input_file_name = os.path.split(ogg_file)
        if outputdir == None:
            mp3dir = input_file_dir
        else:
            mp3dir = outputdir
        input_file_base_name, _ = os.path.splitext(input_file_name)
        wav_file = os.path.join(tempfile.mkdtemp(), input_file_base_name+".wav")
        ogg2wav(ogg_file, wav_file)

#create a function to take a string and convert to morse code
def string_to_morse_code():
    #todo take input of text
    string_input = input("Please input your message that your would like convert to morse code: ").upper()
    #todo make a function that replaces each string with a morse code value
    # morse_code_string_list = [MORSE_DICT[letter] if MORSE_DICT[letter] else '*' for letter in string_input]
    morse_code_string_list = []
    for letter in string_input:
        try:
            [MORSE_DICT[letter]]
        except KeyError:
            morse_code_string_list.append('/**/')
        else:
            morse_code_string_list.append(MORSE_DICT[letter])

    morse_code_string = ""
    #convert list into a string
    for entry in morse_code_string_list:
        morse_code_string += entry
        morse_code_string += (" ")
    #todo print new string
    print(f"ORIGINAL STRING: {string_input} \nMORSE CODE: {morse_code_string} \n")

    #play audio for morse code
    pygame.init()

    #this plays the audio for the morse code
    for char in string_input:

        #creates a pause in between words if there is a space in the string
        if char == " ":
            time.sleep(7 * TIME_BETWEEN)

        #Plays the morse code audio for each letter in the string
        elif type(char) == str:

            #this function will play the ogg file once it is loaded
            def play_morse_ogg():
                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play()
                time.sleep(3 * TIME_BETWEEN)

            #Because the library of morse code audio files for strings and numbers has a different name format, this try/except/else
            # will check to see if it should load the audio file for a letter, number, or just skip it if no audio file is present
            try:
                pygame.mixer.music.load(PATH + char + '_morse_code.ogg')  # Loads the audio file
            except pygame.error:
                try:
                    pygame.mixer.music.load(PATH + char + '_number_morse_code.ogg')
                except pygame.error:
                    pass
                else:
                    play_morse_ogg()
            else:
                play_morse_ogg()

#starts the initial program
string_to_morse_code()

#this while loop keeps the program running until the user is ready to quit
while run_program:
    convert_again = input("Would you like to convert another string? Y or N : ").lower()
    if convert_again == 'y' or convert_again == 'yes':
        string_to_morse_code()
    else:
        run_program = False
        print("\nTHANK YOU FOR RUNNING THIS CONVERTER. THIS PROGRAM WILL NOW CLOSE.")

