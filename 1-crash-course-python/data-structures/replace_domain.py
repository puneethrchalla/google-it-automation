# Good Example for IT application of string indexing, slicing & substring check 

def replace_domain(email, old_domain, new_domain):
    if '@' + old_domain in email:
        return email[:email.index('@')] + '@' + new_domain
    return email

print(replace_domain('puneethreddy@me.com', 'me.com', 'icloud.com'))
print(replace_domain('puneethreddy@icloud.com', 'me.com', 'icloud.com'))