# PassForge Documentation
First, download the modules listed in the [requirements.txt](requirements.txt) file using the command `pip install -r requirements.txt`.

## Using the CLI:
Open the [main.py](main.py) file.

### - Navigation:

- ⬆️ Navigate down
- ⬇️ Navigate up
- ⬅️ Decrement by 1, switch to the left
- ➡️ Increment by 1, switch to the right

---

## Usage via Python console:

### Generation with default parameters
Open a Python terminal where you downloaded the program and import [core.py](core.py).
Create an instance of the Password class with the desired password length in a variable like this:
```python
import core

password = core.Password(10)
```
The password is constructed prioritizing letters, then numbers, and finally special characters.
Passwords generated, with more than 3 characters, will contain an average of 60% letters, 20% numbers, and 20% special characters.

Now, use the `generate()` method to generate your password. You can use the `print()` function to display it.

```python
import core

password = core.Password(10)
print(password.generate())
```
You have generated your 10-character password!

### Generation with custom parameters:
You can generate your password as you wish using the following parameters:

**n_numb** (int): the number of digits

**n_alpha** (int): the number of letters

**n_char** (int): the number of characters

**not_numb** (list[int]): a list containing the digits that will not be present in the generated password

**not_alpha** (list[str]): a list containing the letters that will not be present in the generated password

**not_char** (list[str]): a list containing the characters that will not be present in the generated password

**alpha_type** (str): the type of letters (uppercase, lowercase, or both)

#### ⚠️ The variable types must be respected!

You can then generate your password like this:
```python
import core

password = core.Password(n_numb=5, n_alpha=8, n_char=2, alpha_type="uppercase", not_numb=[6])
print(password.generate())
```
In this case, the password will have 5 digits without the digit 6, 8 uppercase letters, and 2 characters.
