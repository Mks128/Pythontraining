# Substituting a character set with a specific character The task is to replace a character set with a given character. A character set means a range of characters. In the re.sub() method a character set is written inside [ ](square brackets). In this example, the lower case character set i.e., [a-z] will be replaced by the digit 0. Below is the implementation.
import re
def substitutor():
    sentence = "22 April is celebrated as Earth Day."
    print(re.sub(r"[a-z]", "0", sentence))
substitutor()