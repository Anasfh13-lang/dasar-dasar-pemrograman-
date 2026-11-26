import streamlit as st


# Kasir Sederhana dengan Diskon
# Tugas ddp Anas_0110126043

DAFTAR_PRODUK = {
    "Nasi Goreng": 16000,
    "Mie Goreng": 15000,
    "Roti Bakar": 8000,
    "Kopi Susu": 7000,
    "Teh Manis": 5000,
    "Air Mineral": 3000,
}


def hitung_diskon(subtotal, status_member):
    if status_member == "Gold":
        persen = 15
    elif status_member == "Silver":
        persen = 10
    else:
        persen = 0

    # IF: bonus diskon untuk belanja besar
    if subtotal >= 50000:
        persen = persen + 5

    nominal = subtotal * persen / 100
    return persen, nominal

def format_rupiah(angka):
    return "Rp " + f"{angka:,.0f}".replace(",", ".")



st.set_page_config(page_title="Kasir Sederhana", page_icon="🧾")
st.title(" Kasir Sederhana beli banyak pasti diskon")
st.caption(" Pilih produk, tambahkan ke keranjang, lalu lihat total diskon yang kamu dapat! ")

if "keranjang" not in st.session_state:
    st.session_state.keranjang = []


nama_pelanggan = st.text_input("Nama pelanggan", placeholder="Contoh: Budi")      # widget 1
produk = st.selectbox("Pilih produk yang kamu mau", list(DAFTAR_PRODUK.keys()))   # widget 2
jumlah = st.number_input("Jumlah beli", min_value=1, max_value=100, value=1)      # widget 3
status_member = st.radio(                                                         # widget 4
    "Status member", ["Non-member", "Silver", "Gold"], horizontal=True
)

kolom_tambah, kolom_reset = st.columns(2)

if kolom_tambah.button("➕ Tambah ke keranjang", use_container_width=True):
    harga = DAFTAR_PRODUK[produk]

    item = {
        "Produk": produk,
        "Harga": harga,
        "Jumlah": jumlah,
        "Total": harga * jumlah,
    }
    st.session_state.keranjang.append(item)

if kolom_reset.button("🗑️ Kosongkan keranjang", use_container_width=True):
    st.session_state.keranjang = []


# Proses dan output keranjang :

st.divider()
st.subheader("Keranjang belanja")

keranjang = st.session_state.keranjang

if len(keranjang) == 0:
    st.info("Keranjang masih kosong. Tambahkan produk dulu.")
else:
    # LOOP: buat menghitung subtotal & menyiapkan tabel tampilan
    subtotal = 0
    baris_tabel = []
    for item in keranjang:
        subtotal = subtotal + item["Total"]
        baris_tabel.append(
            {
                "Produk": item["Produk"],
                "Harga": format_rupiah(item["Harga"]),
                "Jumlah": item["Jumlah"],
                "Total": format_rupiah(item["Total"]),
            }
        )

    st.table(baris_tabel)

    persen_diskon, nominal_diskon = hitung_diskon(subtotal, status_member)
    total_bayar = subtotal - nominal_diskon

    # IF / ELSE: sapaan pelanggan
    if nama_pelanggan.strip() != "":
        st.write(f"Pelanggan: **{nama_pelanggan}** ({status_member})")
    else:
        st.write(f"Pelanggan: **Umum** ({status_member})")

    # OUTPUT: st.metric
    m1, m2, m3 = st.columns(3)
    m1.metric("Subtotal", format_rupiah(subtotal))
    m2.metric("Diskon", format_rupiah(nominal_diskon), f"{persen_diskon}%")
    m3.metric("Total Bayar", format_rupiah(total_bayar))

    # IF / ELSE: pesan promo
    if persen_diskon > 0:
        st.success(f" Selamat! Kamu hemat {format_rupiah(nominal_diskon)}")
    else:
        st.warning(" Belum dapat diskon nih. Ayu jadi member atau belanja minimal Rp 50.000 untuk dapat diskon:) ")

