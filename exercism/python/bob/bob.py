def response(hey_bob):
    is_yelling = hey_bob.upper() == hey_bob and any(c.isalpha() for c in hey_bob)
    is_question = hey_bob.strip().endswith("?")

    if hey_bob.strip() == '':
        return "Fine. Be that way!"
    elif is_yelling and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_yelling:
        return "Whoa, chill out!"
    elif is_question:
        return "Sure."
    else:
        return "Whatever."
