import pygame
import sys
import os
import random
import time

from pygame.locals import *


def play_again():
    pygame.init()

    font = pygame.font.SysFont("Arial", 36)

    screen = pygame.display.set_mode([500, 500])

    pygame.display.set_caption('Blackjack')

    suits = ["clubs", "hearts", "diamonds", "spades"]

    red = (255, 0, 0)
    blue = (0, 0, 255)
    orange = (255, 165, 0)

    hit = pygame.Rect(20, 20, 40, 50)
    stand = pygame.Rect(380, 20, 40, 50)

    player_total = 0
    dealer_total = 0

    count = 0

    draws = []

    running = True
    while running:

        if (count < 1):
            dealer_total += random.randint(1, 10)

            player_total += random.randint(1, 10)
            player_total += random.randint(1, 10)

            count += 1

        if player_total > 21:
            running = False
            print('Bust!')
            time.sleep(2)
            play_again()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if (hit.collidepoint(x, y)):
                    mouse_presses = pygame.mouse.get_pressed()
                    suit_number = random.randint(0, 3)
                    card_number = random.randint(1, 10)
                    if mouse_presses[0]:
                        player_total += card_number

                        print('The card drawn was a: ' + str(card_number) + " of " + suits[suit_number])
                        print('Your total is: ' + str(player_total))
                if (stand.collidepoint(x, y)):
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        while (dealer_total < 16):
                            dealer_total += random.randint(1, 10)
                        if (dealer_total > 21 or player_total > dealer_total):
                            print("You win!")
                            running = False
                            time.sleep(2)
                            play_again()
                        else:
                            print("Dealer wins!")
                            lose = font.render("You lose!", True, red)
                            screen.blit(lose, (250 - lose.get_width() // 2, 100 - lose.get_height() // 2))
                            running = False
                            time.sleep(2)
                            play_again()



        screen.fill((255, 255, 255))

        player_text = font.render("Your total: " + str(player_total), True, red)
        screen.blit(player_text,(200 - player_text.get_width() // 2, 150 - player_text.get_height() // 2))

        dealer_text = font.render("Dealer's total: " + str(dealer_total), True, blue)
        screen.blit(dealer_text,(200 - dealer_text.get_width() // 2, 75 - dealer_text.get_height() // 2))

        pygame.draw.rect(screen, blue, hit)
        pygame.draw.rect(screen, orange, stand)

        pygame.display.flip()

    pygame.quit()

play_again()