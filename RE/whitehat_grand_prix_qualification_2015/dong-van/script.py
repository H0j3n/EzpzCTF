import base64

custom_enc = "ms4otszPhcr7tMmzGMkHyFn="
ori = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789/="
custom = "ELF8n0BKxOCbj/WU9mwle4cG6hytqD+P3kZ7AzYsag2NufopRSIVQHMXJri51Tdv"
fix_enc = ""

# Fixing 
for i in range(len(custom_enc)):
	try:
		fix_enc += ori[custom.index(custom_enc[i])]
	except:
		fix_enc += custom_enc[i]
# Decode
print(base64.b64decode(fix_enc))
