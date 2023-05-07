# simple-text-menu
Implementation of idea of simple in setup / use text menu. Is for using via text prompt: (Terminal, Sockets, Chat clients, etc..)

The idea of recursive engine to draw dialog menus with different contexts that are
simple to organize was born, when i was implementing text-like menu wuth multiple
choices for the user interface on the microcontroller.

So, the similar idea might be used to provide user interface in IOT devices,
or the menu itself can also be rendered on server machine, and then might be
sent trough text sending protocols, like TCP, and then just wait for user input
to process further actions.

The idea lays in the tree-like structure of menus hierarchy. Like:
Menu
  |
  +---Sound
  |     |
  |     +--- On / Off  (Callable handler that handles user input)
  |     |
  |     +--- Volume  (Callable handler that handles user input)
  |
  +---Display
  |     |
  |     +--- On / Off  (Callable handler that handles user input)
  |     |
  |     +--- Brightness  (Callable handler that handles user input)
  |
  +---Etc...
