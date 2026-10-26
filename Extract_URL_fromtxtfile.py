import re

# Read the contents of the input file
with open("websites.txt", "r") as file:
  text = file.read()

# Regular expression pattern to match URLs
url_pattern = r"https?://[^\s]+"

# Find all occurrences of the pattern
urls = re.findall(url_pattern, text)

# Save the extracted URLs into the output file
with open("urls.txt", "w") as file:
  for url in urls:
    file.write(url + "\n")

print(f"Extracted {len(urls)} URLs successfully and saved to 'urls.txt'.")
print("Extracted URLs:")
for url in urls:
  print(url)
