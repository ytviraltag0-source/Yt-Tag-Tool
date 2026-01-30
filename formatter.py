def clean_tags(raw):
    unique = list(set(raw))
    final = []
    total = 0

    for tag in unique:
        tag = tag.strip().lower()
        if total + len(tag) < 480:
            final.append(tag)
            total += len(tag) + 2

    return final
