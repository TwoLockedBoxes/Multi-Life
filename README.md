This project started when I asked myself the question: What if the rules for a cellular automaton changed depending on their location on the grid?
The thought is related to an idea in physics that suggests that physical constants, such as the speed of light, may vary throughout the universe.
These constants are fundamental to the specific structure of reality, and similarly, the rules of a cellular automaton are fundamental to the structures that it forms.

***This program is simply a standard GOL-style cellular automaton, with the added capability of being able to designate specific regions of the grid with custom rules.***

The rules are defined in the standard GOL format of bM/sN: 
  1) An inactive cell with exactly M neighbors will become active.
  2) An active cell with N neighbors will remain active.
  3) All other active cells beocome inactive.

--- Controls ---
- Left click to activate cells
- Right click to deactivate cells
- Spacebar to play and pause
- Escape to exit

--- Setting a Rule---

For Conway's GOL, the rule is b3/s23. In this program, M and N are lists containing the allowed values. So in this case, M = [3], N = [2, 3].
If we wish to add this rule to, say, all even-numbered columns, we would do the following:
  1) In the marked section, create an empty list to hold the range of cells, i.e., cells = [].
  2) Using any type of function, designate combination any coordinates between 0 and the grid size.
  3) Use grid.add_rule([3], [2, 3], cells], passing it the empty list as its third argument.
  4) For further rules, clear the list, use this as the list for step 1 and repeat.

Note that if a grid space does not have a rule applied to it, it will not interact with the simulation at all, so make sure to cover all spaces!

Here are a few interesting and fun things to try:

- A fun way to divide up the grid is like a chess board. This causes many interesting behaviors and structures to arise.
- Setting the bM rule to include 0 will cause cells to spontaneously pop into existence in empty spaces! ***Epilepsy warning on this one, seriously.***
- Pay attention to how the structures change upon adding or removing a number from sN. Certain structures are only possible with or without certain numbers!
- One feature of Conway's GOL rule that is surpsisingly uncommon is its relative stability. Most rules lead to one of two main results:
    1) The cells all die out relatively quickly
    2) The cells fill up the whole grid quickly
  The b3/s23 rule is somewhat rare in that its active cell count can remain relatively constant for prolonged periods, although most configurations do still
  wind up in the first state. It is an interesting challange to try and find other "quasi-stable" solutions, especially with changing rules!
- Don't be afraid to add more than two rules, just make sure you cover all the grid spaces!
