import re
def detect_word_pattern(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        print("Word patterns detected:")
    for match in matches:
        print(match)
    else:
        print("No word patterns detected.")

sample_inputs = [
(r"\bcat\b", "The cat sat on the mat"),
(r"\b\d{4}\b", "The year is 2025 and last year was 2024"),
(r"\b[a-zA-Z]{5}\b", "Hello world from Python"),
(r"\bing\b", "Running and walking are good exercises")
]
for pattern, text in sample_inputs:
    print("Pattern:", pattern)
    print("Text:", text)
    detect_word_pattern(pattern, text)
    print("-" * 40)
