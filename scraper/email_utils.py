def generate_email_formats(name, domain):
    """
    Generate possible email formats based on a person's name and domain.
    Handles names with 1, 2, or many parts.
    """
    parts = name.lower().split()

    if len(parts) == 1:
        first = parts[0]
        last = ""
    else:
        first = parts[0]
        last = parts[-1]

    formats = [
        f"{first}.{last}@{domain}" if last else f"{first}1@{domain}",
        f"{first}{last}@{domain}" if last else f"{first}2@{domain}",
        f"{first[0]}{last}@{domain}" if last else f"{first}3@{domain}",
        f"{first}@{domain}"
    ]

    return list({email for email in formats if "@" in email})