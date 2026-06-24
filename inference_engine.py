from certainty_factor import hitung_cf, combine_cf

def forward_chaining(gejala_user, rules):

    hasil = {}

    for rule in rules:

        cocok = True
        nilai_min = 1

        for g in rule["kondisi"]:
            if g not in gejala_user:
                cocok = False
                break

            nilai_min = min(nilai_min, gejala_user[g])

        if cocok:

            cf_rule = hitung_cf(
                rule["cf_pakar"],
                nilai_min
            )

            kode = rule["hasil"]

            if kode in hasil:
                hasil[kode] = combine_cf(
                    hasil[kode],
                    cf_rule
                )
            else:
                hasil[kode] = cf_rule

    return hasil