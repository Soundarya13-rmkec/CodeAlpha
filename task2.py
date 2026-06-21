print("=" * 60)
print("      CYBER SECURITY - PHISHING AWARENESS")
print("=" * 60)

name = input("Enter your name: ")

print("\nWelcome,", name)
print("\nPhishing is a cybercrime where attackers attempt")
print("to steal sensitive information such as passwords,")
print("credit card numbers, and personal data.")

print("\nTypes of Phishing Attacks")
print("1. Email Phishing")
print("2. Spear Phishing")
print("3. Smishing (SMS Phishing)")
print("4. Vishing (Voice Phishing)")
print("5. Clone Phishing")

print("\nExample Scenario")
print("-" * 40)
print("You receive an email from 'support-bank@gmail.com'")
print("asking you to verify your account immediately.")
print("The email contains a suspicious link.")
print("-" * 40)

choice = input("\nWould you click the link? (yes/no): ")

if choice.lower() == "yes":
    print("\nWarning! This could be a phishing attack.")
else:
    print("\nCorrect! Avoid clicking suspicious links.")

print("\nTips to Stay Safe")
print("- Verify sender email addresses")
print("- Do not share passwords or OTPs")
print("- Use strong passwords")
print("- Enable two-factor authentication")
print("- Check website URLs carefully")

print("\n" + "=" * 60)
print("                 AWARENESS QUIZ")
print("=" * 60)

score = 0

questions = [
    ("Phishing attacks are used to steal personal information. (true/false): ", "true"),
    ("It is safe to share OTPs with anyone. (true/false): ", "false"),
    ("HTTPS websites are generally more secure than HTTP websites. (true/false): ", "true"),
    ("You should verify suspicious emails before responding. (true/false): ", "true"),
    ("Urgent prize-winning emails are always genuine. (true/false): ", "false")
]

for q, ans in questions:
    user = input(q)
    if user.lower() == ans:
        score += 1

print("\nQuiz Completed")
print("Your Score:", score, "/ 5")

percentage = (score / 5) * 100
print("Percentage:", percentage, "%")

if percentage >= 80:
    print("Security Awareness Level: Excellent")
elif percentage >= 60:
    print("Security Awareness Level: Good")
else:
    print("Security Awareness Level: Needs Improvement")

print("\nThank you for participating in the")
print("Phishing Awareness Training Program.")
