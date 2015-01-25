# -*- coding: utf8 -*-

# Copyright (C) 2015  Ben Ockmore

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import pygame

GAME_SIZE = (640, 600)


def init():
    pygame.init()

    # Load the icon into a surface
    icon_surface = pygame.image.load('./assets/graphics/icon.png')
    pygame.display.set_icon(icon_surface)

    pygame.display.set_mode(GAME_SIZE)


def run():
    while 1:
        pass
