def combine_cf(cf1, cf2):
    return cf1 + cf2 * (1 - cf1)

def hitung_cf(rule_cf, user_cf):
    return rule_cf * user_cf