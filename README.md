## Refactoring Practice

Copy this template repository to your own Github account. Then clone it to your computer and do the refactorings.  Push your work to Github.

Each subdirectory contains some code that needs refactoring.

1. In this README, write one line describing each refactoring you apply and why.
2. Perform the refactoring in the subdirectory code.


## `time/timestamp.py`

1. Refactor name of create_time_from_times_tamp function because the function name should be lowercase and separate by underscore.
2. Refactor name of Args because the variable should have meaning.
3. Delete unnecessary else because we already check the len of timestamp.
4. Extract is_valid_time because It hard to understand.

## `game_framework/gamelib.py`

Look for refactorings in the class `GameApp`.

* Avoid side-effects: replace side effect with return value (the caller must use the return value)

* Encapsulate a collection - provide behavior that subclasses of GameApp need instead of requiring them to manipulate a collection that belongs to the GameApp class.
  - Hint: `elements`  

Refactoring 
1. Refactor the create_canvas function to return the canvas because the old version doesn't init the self.canvas.
2. Refactor the string literal with constant because It can change to be constant.
3. Passing the argument width and high to create_canvas because It will be easier to understand.
4. Refactor the constant of canvas width height and delay because It has to be a constant for init the canvas.

## `recipe/recipe.py` and `recipe/main.py`

This uses a `dataclass`, which requires Python 3.7.

The Recipe class defines a recipe for a hot beverage with attributes:
* name - name of the recipe
* coffee - units of coffee
* chocolate - units of chocolate
* milk - units of milk
* sugar - units of sugar
* price - (float) price in Baht

Refactor `main.py`.  What can you do to eliminate the long, boring code?






## Resources

* <https://refactoringguru.com/refactoring> 
* *Refactoring - Improving the Design of Existing Code* by Martin Fowler.  The bible on refactoring.  The first 4 chapters explain the fundamentals.
* <https://refactoring.com> Online version of Fowler's book, but lacks explanation of the refactorings.
