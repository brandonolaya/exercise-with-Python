# Remove the characters to the left of our main text:

# ,

# :

# %

# _

# #


txt = ",:_#,,,,,,:::____##Python_ _Total,,,,,,::#"
x = txt.lstrip(',:%_#')
print(x)