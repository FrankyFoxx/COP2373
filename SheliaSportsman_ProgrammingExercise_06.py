import re

# -----------------------------
# Validation Functions
# -----------------------------

def validate_phone(phone):
    """
    Valid formats:
    - 123-456-7890
    - (123) 456-7890
    - 1234567890
    - 123.456.7890
    - 123 456 7890
    """
    pattern = r'^(\(\d{3}\)\s?|\d{3}[-.\s]?)\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))


def validate_ssn(ssn):
    """
    Valid format:
    - 123-45-6789
    """
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, ssn))


def validate_zip(zip_code):
    """
    Valid formats:
    - 12345
    - 12345-6789
    """
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, zip_code))


# -----------------------------
# Main Function
# -----------------------------

def main():
    print("Enter the following information:")

    phone = input("Phone Number: ")
    ssn = input("Social Security Number: ")
    zip_code = input("ZIP Code: ")

    print("\nValidation Results:")
    print(f"Phone Number Valid: {validate_phone(phone)}")
    print(f"SSN Valid: {validate_ssn(ssn)}")
    print(f"ZIP Code Valid: {validate_zip(zip_code)}")


# -----------------------------
# Test Cases
# -----------------------------

def run_tests():
    print("\nRunning Tests...\n")

    phone_tests = [
        "123-456-7890", "(123) 456-7890", "1234567890",
        "123.456.7890", "123 456 7890", "12-3456-7890"
    ]

    ssn_tests = [
        "123-45-6789", "000-12-3456", "123456789", "12-345-6789"
    ]

    zip_tests = [
        "12345", "12345-6789", "1234", "123456", "12345-678"
    ]

    print("Phone Number Tests:")
    for t in phone_tests:
        print(f"{t}: {validate_phone(t)}")

    print("\nSSN Tests:")
    for t in ssn_tests:
        print(f"{t}: {validate_ssn(t)}")

    print("\nZIP Code Tests:")
    for t in zip_tests:
        print(f"{t}: {validate_zip(t)}")


# -----------------------------
# Run Program
# -----------------------------

if __name__ == "__main__":
    run_tests()
    main()