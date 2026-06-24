import streamlit as st

from knowledge_base import (
    load_gejala,
    load_diagnosa,
    load_rules
)

from inference_engine import (
    forward_chaining
)

st.set_page_config(
    page_title="Sistem Pakar Diagnosa Kerusakan Komputer/Laptop",
    layout="wide"
)

st.title("💻 Sistem Pakar Diagnosa Kerusakan Komputer/Laptop")
st.subheader("Kelompok 4 - Sistem Pakar")

gejala = load_gejala()
diagnosa = load_diagnosa()
rules = load_rules()

st.markdown("### Pilih Gejala Yang Dialami")

pilihan = {}

opsi_cf = {
    "Tidak":0.0,
    "Sedikit Yakin":0.2,
    "Cukup Yakin":0.4,
    "Yakin":0.6,
    "Sangat Yakin":0.8,
    "Pasti":1.0
}

for item in gejala:

    jawaban = st.selectbox(
        f"{item['kode']} - {item['nama']}",
        opsi_cf.keys(),
        key=item["kode"]
    )

    if opsi_cf[jawaban] > 0:
        pilihan[item["kode"]] = opsi_cf[jawaban]

if st.button("Diagnosa"):

    hasil = forward_chaining(
        pilihan,
        rules
    )

    if not hasil:
        st.warning(
            "Tidak ditemukan diagnosa yang sesuai."
        )

    else:

        terbaik = sorted(
            hasil.items(),
            key=lambda x: x[1],
            reverse=True
        )

        st.success("Diagnosa Berhasil")

        for kode, cf in terbaik:

            data = next(
                d for d in diagnosa
                if d["kode"] == kode
            )

            st.markdown("---")

            st.subheader(data["nama"])

            st.write(
                f"Tingkat Keyakinan: {cf*100:.2f}%"
            )

            st.write(
                f"Deskripsi: {data['deskripsi']}"
            )

            st.write(
                f"Solusi: {data['solusi']}"
            )