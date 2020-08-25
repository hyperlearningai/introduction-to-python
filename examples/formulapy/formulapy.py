#!/usr/bin/env python3
"""Car racing game written in Python.

This module implements a simple car driving game in Python using object
oriented programming principles and the Pygame engine. The aim of the game is
to overtake other cars without colliding with them. If you do collide with
either the other cars or the screen boundary, then it is game over.

Attribution:
    Splash Screen Image:
        <a href='https://www.freepik.com/vectors/background'>
            Background vector created by macrovector - www.freepik.com
        </a>
    Human Player Car Image:
        <a href="https://www.freepik.com/vectors/car">
            Car vector created by freepik - www.freepik.com
        </a>
    Computer Player Car Image:
        https://pixabay.com/vectors/car-racing-speed-auto-green-312571/

"""

import math
import pygame
import random
import time

# Game Configuration
SCREEN_SIZE = (600, 800)
SCREEN_DISPLAY_CAPTION = 'FormulaPy'
SPLASH_SCREEN_TIME = 5
SPLASH_SCREEN_IMAGE_FILENAME = 'splash-screen.jpg'
HUMAN_PLAYER_IMAGE_FILENAME = 'human-player-racecar.png'
COMPUTER_PLAYER_IMAGE_FILENAME = 'computer-player-racecar.png'
HUMAN_PLAYER_IMAGE_SIZE = (72, 168)
COMPUTER_PLAYER_IMAGE_SIZE = (72, 168)
COMPUTER_PLAYER_COUNT = 3
ROAD_STRIPE_COUNT = 15
ROAD_STRIPE_WIDTH = 15
ROAD_STRIPE_HEIGHT = 75
ROAD_STRIPE_SPACING = 25
ROAD_STRIPE_Y_DELTA_CONSTANT = 5
MESSAGE_FONT = 'freesansbold.ttf'
MESSAGE_FONT_SIZE = 25
MESSAGE_GAME_OVER = 'You Crashed! Your score was: '
CLOCK_FPS = 60
DELTA_X_LEFT_CONSTANT = -5
DELTA_X_RIGHT_CONSTANT = 5
OVERTAKE_COMPUTER_SCORE_INCREMENT = 10

# Colors
BLACK = (0, 0, 0)
GREY = (211, 211, 211)
WHITE = (255, 255, 255)


class Car:

    def __init__(self, pos_x=0, pos_y=0, delta_x=DELTA_X_RIGHT_CONSTANT,
                 delta_y=0, human=False):
        """Initialise a car object.

        Args:
            pos_x (int): The position of the car on the x-plane.
            pos_y (int): The position of the car on the y-plane.
            delta_x (int): The amount by which to move the car on the x-plane.
            delta_y (int): The amount by which to move the car on the y-plane.
            human (bool): Whether the car is a human player or not.

        """

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.delta_x = delta_x
        self.delta_y = delta_y
        self.human = human
        self.image = None

    def load_transform_image(self):
        """Load the car image from the filesystem."""

        self.image = pygame.image.load(
            HUMAN_PLAYER_IMAGE_FILENAME).convert() if self.human else \
            pygame.image.load(COMPUTER_PLAYER_IMAGE_FILENAME).convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(
            self.image, HUMAN_PLAYER_IMAGE_SIZE) if self.human else \
            pygame.transform.scale(self.image, COMPUTER_PLAYER_IMAGE_SIZE)

    def render_image(self):
        """Render the car image on the display."""

        screen.blit(self.image, [self.pos_x, self.pos_y])

    def turn_left_right(self):
        """Move the car on the x-plane by delta x."""

        self.pos_x += self.delta_x

    def move_up_down(self):
        """Move the car on the y-plane by delta y."""

        self.pos_y += self.delta_y


def initialize_screen():
    """Return the display with an initial splash screen."""

    # Set the display caption
    pygame.display.set_caption(SCREEN_DISPLAY_CAPTION)

    # Instantiate a new display with the given screen size
    display = pygame.display.set_mode(SCREEN_SIZE)

    # Load and transform the splash screen image
    splash_screen_image = pygame.image.load(
        SPLASH_SCREEN_IMAGE_FILENAME).convert()
    splash_screen_image.set_colorkey(BLACK)
    splash_screen_image = pygame.transform.scale(
        splash_screen_image, SCREEN_SIZE)

    # Display the splash screen for a defined period of time
    display.blit(splash_screen_image, [0, 0])
    pygame.display.flip()
    time.sleep(SPLASH_SCREEN_TIME)

    return display


def create_human_player():
    """Create a car object that is controlled by the human player."""

    # Create the human player car object
    human_player_car = Car(
        pos_x=int(round((SCREEN_SIZE[0]/2) - (HUMAN_PLAYER_IMAGE_SIZE[0]/2))),
        pos_y=SCREEN_SIZE[1] - HUMAN_PLAYER_IMAGE_SIZE[1] - 50,
        delta_x=0,
        delta_y=0,
        human=True)

    # Transform and scale the size of the player car image to fit the screen
    human_player_car.load_transform_image()

    return human_player_car


def create_computer_players():
    """Create a list of car objects that act as obstacles."""

    # Create computer car object obstacles
    for n in range(COMPUTER_PLAYER_COUNT):

        # Randomly initialise the initial (x, y) co-ordinate for this computer
        init_x = random.randrange(
            0, SCREEN_SIZE[0] - COMPUTER_PLAYER_IMAGE_SIZE[0])
        init_y = random.randrange(-125, -25)

        # Randomise the rate of change in the y-plane, starting with slow speeds
        init_delta_y = random.randint(2, 3)

        # Create a new computer player
        global computer_players
        computer_player_car = Car(
            pos_x=init_x,
            pos_y=init_y,
            delta_x=0,
            delta_y=init_delta_y,
            human=False)

        # Transform and scale the size of the computer player car image
        computer_player_car.load_transform_image()

        # Add the new computer player to the list of computer players
        computer_players.append(computer_player_car)


def create_road_stripe_marks():
    """Create a list of road stripe marking co-ordinates."""

    # Initialise a list to store the road strip markings
    road_stripe_marks = []

    # Create the road stripe markings and add them to the list
    road_stripe_pos_x = int(round((SCREEN_SIZE[0]/2) - (ROAD_STRIPE_WIDTH/2)))
    road_stripe_pos_y = -10
    for n in range(ROAD_STRIPE_COUNT):
        road_stripe_marks.append([road_stripe_pos_x, road_stripe_pos_y])
        road_stripe_pos_y += ROAD_STRIPE_HEIGHT + ROAD_STRIPE_SPACING

    return road_stripe_marks


def render_road_stripe_marks():
    """Render the list of road stripe markings as rectangles."""

    # Render the road stripe marks
    global road_stripe_markings
    for n in range(ROAD_STRIPE_COUNT):
        pygame.draw.rect(screen, WHITE, [
            road_stripe_markings[n][0], road_stripe_markings[n][1],
            ROAD_STRIPE_WIDTH, ROAD_STRIPE_HEIGHT])


def move_road_stripe_marks():
    """Move the road stripe marking rectangles on the y-plane."""

    # Move the road stripe marks
    global road_stripe_markings
    for n in range(ROAD_STRIPE_COUNT):
        road_stripe_markings[n][1] += ROAD_STRIPE_Y_DELTA_CONSTANT
        if road_stripe_markings[n][1] > SCREEN_SIZE[1]:
            road_stripe_markings[n][1] = -30 - ROAD_STRIPE_HEIGHT


def computers_overtaken():
    """Check whether a computer car object has moved out of visibility on
    the y-plane. If so, increment the player score and recycle the computer car
    object, gradually increasing its delta-y speed along the y-plane in
    proportion with the increasing player score."""

    # Check whether computer players have moved out of the visible y-plane
    global score, speed_increment
    for n in range(COMPUTER_PLAYER_COUNT):

        # Render the current computer player and increment its y-plane position
        computer_players[n].render_image()
        computer_players[n].pos_y += computer_players[n].delta_y

        # Test whether the current computer player has moved out of visibility
        if computer_players[n].pos_y > SCREEN_SIZE[1]:

            # Increment the score
            score += OVERTAKE_COMPUTER_SCORE_INCREMENT

            # Reset the computer player
            computer_players[n].pos_x = random.randrange(
                0, SCREEN_SIZE[0] - COMPUTER_PLAYER_IMAGE_SIZE[0])
            computer_players[n].pos_y = random.randrange(-125, -25)

            # Incrementally increase the speed of the computer vertical movement
            # Increase the speed every time the score increments by another 100
            speed_increment = max(2, math.floor(score / 100) + 1)
            computer_players[n].delta_y = random.randint(
                speed_increment, speed_increment + 1)


def collision_with_screen_boundaries():
    """Check whether the human car object has exceeded the screen boundaries
    along the x-plane."""

    # Check whether the position of the player exceeds the screen boundaries
    if human_player.pos_x > SCREEN_SIZE[0] - HUMAN_PLAYER_IMAGE_SIZE[0] or \
            human_player.pos_x < 0:
        return True
    return False


def collision_with_computer():
    """Check whether the human car object has collided with one of the
    computer car objects."""

    # Check whether the player has collided with a computer player
    for n in range(COMPUTER_PLAYER_COUNT):

        # Get the current (x, y) position of the current computer player
        computer_pos_x = computer_players[n].pos_x
        computer_pos_y = computer_players[n].pos_y

        if (human_player.pos_x + HUMAN_PLAYER_IMAGE_SIZE[0] > computer_pos_x) \
                and (human_player.pos_x < computer_pos_x +
                     COMPUTER_PLAYER_IMAGE_SIZE[0]) \
                and (human_player.pos_y < computer_pos_y +
                     COMPUTER_PLAYER_IMAGE_SIZE[1]) \
                and (human_player.pos_y +
                     HUMAN_PLAYER_IMAGE_SIZE[1] > computer_pos_y):

            return True

    return False


def game_over():
    """If a collision event has occurred, render a game over message, then reset
    the game parameters before starting a new indefinite game loop after
    a brief pause."""

    # Display the game over message along with the score
    global score, speed_increment
    font = pygame.font.Font(MESSAGE_FONT, MESSAGE_FONT_SIZE)
    text = font.render(MESSAGE_GAME_OVER + str(score), True, BLACK)
    text_rectangle = text.get_rect()
    text_rectangle.center = ((SCREEN_SIZE[0] / 2), (SCREEN_SIZE[1] / 2))
    screen.blit(text, text_rectangle)
    pygame.display.update()

    # Pause the application before continuing with a new game loop
    time.sleep(2)

    # Reset the game parameters
    global clock, human_player, computer_players, collision_event_detected
    clock = pygame.time.Clock()
    human_player = create_human_player()
    computer_players = []
    create_computer_players()
    collision_event_detected = False
    score = 0
    speed_increment = 2

    # Start a new game via the indefinite game loop
    indefinite_game_loop()


def indefinite_game_loop():
    """FormulaPy game events and subsequent display rendering actions."""

    # ----- FORMULAPY GAME LOOP -----
    while not request_window_close:

        # ----- EVENT DETECTION LOOP -----
        for event in pygame.event.get():

            # Close Window Event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Keyboard Key Down Event
            if event.type == pygame.KEYDOWN:

                # Left Key
                if event.key == pygame.K_LEFT:
                    human_player.delta_x = DELTA_X_LEFT_CONSTANT

                # Right Key
                if event.key == pygame.K_RIGHT:
                    human_player.delta_x = DELTA_X_RIGHT_CONSTANT

            # Keyboard Key Up Event
            if event.type == pygame.KEYUP:

                # Left or Right Key
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    human_player.delta_x = 0

        # ----- UPDATE DISPLAY -----

        # Fill the display with a white background
        screen.fill(GREY)

        # Whilst there is no collision event
        global collision_event_detected
        if not collision_event_detected:

            # Render the road stripe markings
            render_road_stripe_marks()

            # Move the road stripe markings
            move_road_stripe_marks()

            # Render the player car object
            human_player.render_image()

            # Move the human player car object as a result of key down events
            # See event detection loop - keyboard key down events
            human_player.turn_left_right()

            # Check whether computer players have been overtaken i.e. whether
            # a computer has moved out of the visible y-plane. If so,
            # increment the score and reset the computer player
            computers_overtaken()

            # Check for a collision event with the screen boundaries
            if collision_with_screen_boundaries():
                collision_event_detected = True

            # Check for a collision event with a computer player
            if collision_with_computer():
                collision_event_detected = True

        # Collision event detected
        else:

            # Display the game over message and wait before starting a new game
            game_over()

        # Update the contents of the entire display
        pygame.display.update()
        clock.tick(60)


# Initialise the imported PyGame modules
pygame.init()

# Start the screen
screen = initialize_screen()

# Maintain the screen until the user closes the window
request_window_close = False

# Initialise a clock to track time
clock = pygame.time.Clock()

# Create the human player
human_player = create_human_player()

# Initialise a list to store the computer players
computer_players = []
create_computer_players()

# Create road stripe marks
road_stripe_markings = create_road_stripe_marks()

# Maintain the game loop until a collision event
collision_event_detected = False

# Keep score
score = 0

# Maintain a game speed incrementer
speed_increment = 2

# Start the indefinite game loop
indefinite_game_loop()
