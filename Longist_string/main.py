def longest_common_prefix(strings):
    if not strings:
        return ""

    # Sort the strings to ensure that the shortest string comes first
    strings.sort()

    # Take the first and last strings after sorting
    first_str, last_str = strings[0], strings[-1]

    common_prefix = []

    # Iterate through characters of the first and last strings
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break

    return "".join(common_prefix)


# Example usage
data = ["flower", "flow", "flight"]
result = longest_common_prefix(data)
print(f"The longest common prefix is: {result}")
