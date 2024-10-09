# HexagonsInTKinter  
Messing with hexagons and tkinter  

## Who

I am a self-taught hobbyist that lacks focus and discipline. I do not make spaghetti code, I make spaghetti soup. My code is a mess of comments and mixed conventions and at least three different ways to express 2D vectors (mixed haphazardly and inconsistently).
## What  

Basically just the color puzzle mini-game from Disgaea, but with hexagons.  

Using:  
- Python  
- tkinter  
- RedBlobGames hexagon functions  

## Where

Currently just on github at https://github.com/zelbo/HexagonsInTKinter.  
Once I have a functional prototype, I might make a discord and subreddit.

## Why  

### Hexagons?

Something I've been interested in messing with for a while. There are a few different ideas I'd like to tinker with that deal with hexagons, this mini-game is just the first one I happened to settle on.

The main reason for doing a mini-game is to give me something fun to work on while learning, to keep me interested in the project and stay motivated to work on it and continue learning.

### Python?

While there are other languages I'm more interested in, a project came up that required using python. I wasn't very familiar with the language before that, and this is an attempt to dive into it a little more fully.

### tkInter?

After playing around with a few simple console applications, I wanted to dig into a GUI. After looking at several options, I decided to use tkInter. The choice was somewhat arbitrary, but some of the reasons for picking it over some of the other options include:

- Simplicity: function over form for this project
- Standard library only: an artificial constraint that should help me learn just what the standard library can and can't do, and keep a tighter focus

## How

The idea is that you have a grid of different colored tiles. Currently this grid is very simply randomly created, eventually I would like to use a mix of various procedural generation techniques to make fun and interesting boards.

For each color used, there is one orb of that color. After placing each orb, you choose the first one to activate. This starts a flood-fill algorithm that replaces the color of the tile with the color of the orb, spreading to neighboring tiles. Activated orbs are destroyed.

As the color spreads, any orbs that are on affected tiles get added to a list. After the current flood-fill is finished, the next orb in the list is activated.

The goal of the game is to arrange the orbs and activate them in an order that causes the process to clear as many tiles as possible.