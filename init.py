import secrets,sys

with open(".env","w") as f:
    f.write("SECRET_KEY="+secrets.token_hex(32)+"\n")
    f.write("DEBUG="+sys.argv[1])