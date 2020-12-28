cat file.txt | grep -E "^\([[:digit:]]{3}\) [[:digit:]]{3}-[[:digit:]]{4}$|^[[:digit:]]{3}-[[:digit:]]{3}-[[:digit:]]{4}$"
