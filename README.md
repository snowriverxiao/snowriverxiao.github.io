<p align="center">
  <h1 align="center">Monty Hall Problem</h1>
  <h3 align="center">Xue Xiao</h3>
  <div align="center">
        <img src="./diagram.png", width="500">
  </div>
  
## The problem
In the classic Monty Hall game, there are three doors—only one of which hides a prize, while the other two are empty. You choose a door at random, say Door #1. Then, a bystander (often imagined as the host) opens one of the remaining two doors—say Door #2—revealing it to be empty. Now you're faced with a choice: should you stick with your original selection, or switch to the remaining unopened door (Door #3)?

Many argue that switching improves your odds, based on the classic reasoning: your initial choice has a 1/3 chance of being correct, while the two unchosen doors collectively carry a 2/3 chance. Once the host reveals one of those unchosen doors to be empty, the full 2/3 probability is said to "transfer" to the other unopened door, making switching the optimal strategy.

This conclusion, however, relies on a key assumption: that the host knows where the prize is and always opens an empty door on purpose. That knowledge—and the deliberate behavior based on it—directly affects the probability distribution.

Now, let’s reconsider the question more precisely: When you are presented with the option to switch, should you? In other words, we should only evaluate the subset of cases where a valid switching scenario actually occurs—that is, the host opens an empty door, and one unopened alternative remains. To compute accurate probabilities, we must condition only on such situations. The denominator of your probability becomes the total number of valid switching scenarios; then you compare how often sticking vs. switching leads to a win within this conditional space.

#### Revisiting the 3-door case:

Case 1 (you initially pick the prize) has a 1/3 chance.
Cases 2 and 3 (you initially pick an empty door) together have a 2/3 chance.
However, these do not equally lead to switching situations.

In Case 1, no matter which of the two remaining doors the bystander opens, you're always offered a switching opportunity—100% of the time.
In Cases 2 and 3, if the bystander chooses randomly between the remaining doors (without knowledge of the prize location), there's only a 50% chance they reveal an empty door that leaves exactly one unopened alternative—meaning only a 50% chance of a valid switching scenario.
But if the bystander knows where the prize is and intentionally avoids revealing it, then Cases 2 and 3 also always lead to switching situations. In that case, the original 2/3 probability on the unchosen side holds, and switching remains the superior strategy. The bystander’s knowledge effectively fixes the background distribution and eliminates randomness from the setup.

In short, if the bystander acts randomly—as you do when choosing your door—the background distribution changes. You’re no longer sampling uniformly from all three cases but are conditioning only on those where a switching opportunity arises. Within that conditional set, the probability of winning by switching becomes equal to that of staying. This happens because Case 1 (choosing the prize initially) has a lower chance of being sampled, but always results in a switching opportunity. Meanwhile, Cases 2 and 3 each have only a 50% chance of qualifying as switching situations.

Again, if the bystander uses knowledge to always avoid revealing the prize, then Cases 2 and 3 each have a 100% chance of leading to a switching situation. As a result, the original 2-to-1 bias toward the unchosen side is preserved. No surprise: switching remains the better strategy, just as commonly taught.

#### Extension to More Than Three Doors
The same logic generalizes to scenarios with more than three doors. Suppose you begin with n doors. You choose one, and the bystander then opens all but one of the remaining doors. A switching scenario is valid only if none of the opened doors reveals the prize.

In Case 1 (you initially choose the prize), the bystander can always open n−2 empty doors, so a switching scenario occurs 100% of the time. In any of the other n-1 cases (you initially choose an empty door), there’s only a 1/(n-1) chance that the bystander opens all other empty doors and avoids the prize—assuming they choose randomly without knowledge.

But if you require the bystander to avoid revealing the prize—ensuring that a switching scenario always occurs when possible—then the distribution no longer shifts randomly. Instead, it becomes fixed in favor of the unchosen side, which retains a higher probability of hiding the prize. In this setup, all of the other n−1 cases (where you initially chose incorrectly) now each have a 100% chance of resulting in a switching scenario. As a result, switching once again becomes the advantageous strategy.

To illustrate this, here is a Python simulation. You can run it with --times to specify how many simulations to perform, --n to set the number of doors, and --randomHost to control the host's behavior—use 1 for a random (uninformed) host, or 0 for an informed host who always avoids revealing the prize.

## Run the code
```bash
python 3doors.py --n 3 --times 100000  --randomHost 0
```
</p>


## Requirements
To run the code you have to install python and its numpy library.

## License
The code is licensed under [LICENSE](LICENSE). 
