from main import *

passwd = Password(n_numb=4, n_alpha=10, n_char=2, alpha_type="upper")
print(passwd.generate())