import cv2
import pygame
import threading
import requests
import http.client
import time
import numpy as np

# Configuration

speed = int(input("Enter speed limit between (150-250): "))
stream_url = f'http://192.168.{bot_num}.14:81/stream'
host_bot_bot = input("Enter brain block ip address : ")
port = 80
us_path = "/?cmd=US"

# Initialize Pygame
pygame.init()

# Screen dimensions for Pygame
screen_width = 641
screen_height = 482
info_width = 310  # Width of the information panel

# Pygame setup
screen = pygame.display.set_mode((screen_width + info_width, screen_height))
pygame.display.set_caption("AiLite Surveillance Bot")

# Font settings
title_font = pygame.font.Font(None, 48)  # Default font and size 48 for title
font = pygame.font.Font(None, 36)        # Default font and size 36 for instructions

# Load the image
instructions_image = pygame.image.load('2.png')
image_rect = instructions_image.get_rect()
image_rect.topleft = (screen_width + 10, 10)

additional_instruction_image = pygame.image.load('inst3.png')  # Change this to the path of your additional instruction image
additional_image_rect = additional_instruction_image.get_rect()
additional_image_rect.topleft = (screen_width + 10, image_rect.bottom + 20)


# Function to stream video
def stream_video():
    global running
    session = requests.Session()
    while running:  # Use global 'running' to control the loop
        try:
            response = session.get(stream_url, stream=True)
            if response.status_code == 200:
                bytes_data = bytes()
                for chunk in response.iter_content(chunk_size=1024):
                    if not running:
                        break
                    bytes_data += chunk
                    a = bytes_data.find(b'\xff\xd8')
                    b = bytes_data.find(b'\xff\xd9')
                    if a != -1 and b != -1:
                        jpg = bytes_data[a:b+2]
                        bytes_data = bytes_data[b+2:]
                        img = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        img = np.rot90(img)
                        img = pygame.surfarray.make_surface(img)
                        screen.blit(img, (0, 0))
                        display_instructions()
                        pygame.display.update()
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)  # Wait before retrying
            continue

# Function to send HTTP request with retries
def send_request(host_bot, port, path):
    retries = 10
    for _ in range(retries):
        conn = None
        try:
            conn = http.client.HTTPConnection(host_bot, port)
            conn.request("GET", path)
            response = conn.getresponse()
            data = response.read().decode("utf-8")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            if _ < retries - 1:
                time.sleep(1)
        finally:
            if conn:
                conn.close()
    return None

# Function to control the bot
def control_bot():
    global running
    requests.get(f"http://{host_bot_bot}/?cmd=left_speed={speed}")
    requests.get(f"http://{host_bot_bot}/?cmd=right_speed={speed}")
    while running:  # Use global 'running' to control the loop
        left_data = int(send_request(host_bot, port, us_path))
        if left_data < 10:
            send_request(host_bot, port, "/?cmd=s")
            requests.get(f"http://{host_bot_bot}/?cmd=b(100)")
        elif pygame.key.get_pressed()[pygame.K_UP]:
            requests.get(f"http://{host_bot_bot}/?cmd=f")
            print("up")
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            requests.get(f"http://{host_bot_bot}/?cmd=b")
            print("down")
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            requests.get(f"http://{host_bot_bot}/?cmd=l")
            print("left")
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            requests.get(f"http://{host_bot_bot}/?cmd=r")
            print("right")
        elif pygame.key.get_pressed()[pygame.K_SPACE]:
            requests.get(f"http://{host_bot_bot}/?cmd=s")
            print("stop")
        elif pygame.key.get_pressed()[pygame.K_ESCAPE]:
            requests.get(f"http://{host_bot_bot}/?cmd=s")
            print("Exiting...")
            running = False
            break
        else:
            requests.get(f"http://{host_bot_bot}/?cmd=s")
        time.sleep(0.1)  # Small delay to prevent overwhelming the CPU

# Function to display instructions
def display_instructions():
    # Draw background for instructions
    pygame.draw.rect(screen, (255, 255, 255), (screen_width, 0, info_width, screen_height))

    # Blit the main instruction image
    screen.blit(instructions_image, image_rect)

    # Blit the additional instruction image
    screen.blit(additional_instruction_image, additional_image_rect)

# Creating threads for video streaming and bot control
video_thread = threading.Thread(target=stream_video)
bot_thread = threading.Thread(target=control_bot)

# Start threads
running = True
video_thread.start()
bot_thread.start()

# Run the Pygame main loop
try:
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
finally:
    # Join threads to main thread
    video_thread.join()
    bot_thread.join()

    # Quit Pygame when done
    pygame.quit()
