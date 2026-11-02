# Word Counter - No file needed
text = input("Enter your sentence: ")
words = text.lower().split()

freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

print("\nWord Count:", len(words))
print("Character Count:", len(text))
for word, count in freq.items():
    print(f"{word}: {count}")