from django.shortcuts import render


def index(request):

    context = {

        "penduduk": "8.796",
        "luas": "369,00 Ha",
        "rt": 18,
        "rw": 4,
        "umkm": 96,

                "judul_profil": "Mengenal Desa Sumur Bandung",
        "profil": "Desa Sumur Bandung merupakan salah satu desa yang berada di Kecamatan Jayanti, Kabupaten Tangerang, Provinsi Banten. Desa ini memiliki potensi yang cukup besar dalam berbagai sektor pembangunan, terutama pada bidang pertanian, usaha mikro, kecil, dan menengah (UMKM), pendidikan, serta pelestarian budaya masyarakat. Sebagian besar masyarakat menggantungkan mata pencahariannya pada sektor pertanian, sehingga sektor ini menjadi salah satu penopang utama perekonomian desa. Di samping itu, keberadaan berbagai pelaku UMKM turut memberikan kontribusi dalam meningkatkan kesejahteraan masyarakat melalui pengembangan produk lokal dan kegiatan ekonomi kreatif. Pada bidang pendidikan, Desa Sumur Bandung memiliki berbagai lembaga pendidikan yang berperan dalam meningkatkan kualitas sumber daya manusia. Sementara itu, nilai-nilai budaya, tradisi, serta semangat gotong royong yang masih terjaga menjadi modal sosial yang penting dalam mendukung pembangunan desa yang berkelanjutan. Dengan potensi yang dimiliki tersebut, Desa Sumur Bandung memiliki peluang besar untuk terus berkembang melalui kolaborasi antara pemerintah desa, masyarakat, serta berbagai pihak, termasuk perguruan tinggi, dalam mewujudkan desa yang mandiri, maju, dan sejahtera.",

        # =========================
        # VISI & MISI
        # =========================
        "visi": "Menjadikan Sumurbandung Sebagai Desa yang Mandiri berbasis pertanian, untuk mencapai masyarakat yang sehat,cerdas dan lebih sejahtera serta mewujudkan masyarakat yang maju di bidang ekonomi dan industri.",

        "misi": [
            "Meningkatkan Pembangunan infrastrukrur yang mendukung perekonomian desa, seperti jalan ,jembatan serta infrastruktur strategis lainnya.",
            "Meningkatkan pembangunan di bidang kesehatan untuk mendorong derajat kesehatan masyarakat agar dapat bekerja lebih optimal dan memiliki harapan hidup yang lebih panjang.",
            "Meningkatkan pembangunan di bidang pendidikan untuk mendorong peningkatan kualitas sumber daya manusia agar memiliki kecerdasan dan daya saing yang lebih baik.",
            "Meningkatkan pembangunan ekonomi dengan mendorong semakin tumbuh dan berkembangnya pembangunan di bidang pertanian,industri dan perdagangan.",
            "Menciptakan tatakelola pemerintah yang baik berdasarkan demokratisasi,transfaransi,berkeadilan dan mengutamakan pelayanan kepada masyarakat. .",
            "Terbangunnya balai latihan kerja (BLK).",
            "Bekerja sama dengan lembaga-lembaga terkait dalam rangka membangun desa sumurbandung.",
        ],

        # =========================
        # PERANGKAT DESA
        # =========================
        "perangkat": [
            {
                "nama": "H.Ahmad Jajuli,S.E",
                "jabatan": "Kepala Desa",
                "foto": "image/kades.jpeg"
            },
            {
                "nama": "Ahmad masyhudi",
                "jabatan": "Sekretaris Desa",
                "foto": "image/sekdes.jpeg"
            },
            {
                "nama": "Aceng fahrudin",
                "jabatan": "Kasi_Pemerintahan",
                "foto": "image/kasi_pemerintahan.jpeg"
            },
            {
                "nama": "M. Irfa farhan",
                "jabatan": "Kasi_Kesra",
                "foto": "image/kasi_kesra.jpeg"
            },
            {
                 "nama": "Toyib",
                 "jabatan": "Kasi_Pelayanan",
                 "foto": "image/kasi_pelayanan.jpeg"
            },
            {
                 "nama": "Nurliah",
                 "jabatan": "Kaur_Keuangan",
                 "foto": "image/kaur_keuangan.jpeg"
            },
            {
                 "nama": "Rukman",
                 "jabatan": "Kaur_Perencanaan",
                 "foto": "image/kaur_perencanaan.jpeg"
            },
            {
                 "nama": "Zaenal ridwan nurhakim",
                 "jabatan": "kadus_1",
                 "foto": "image/kadus_1.jpeg"
            },
            {
                 "nama": "Nurjaman",
                 "jabatan": "kadus_2",
                 "foto": "image/kadus_2.jpeg"
            },
        ],

       
        # =========================
        # POTENSI DESA
        # =========================
        "potensi": [
            {
                "slug": "pertanian",
                "judul": "Pertanian",
                "gambar": "image/pertanian.jpeg",
                "deskripsi": "Desa Sumur Bandung memiliki lahan pertanian yang menjadi sumber mata pencaharian masyarakat."
            },
            {
                "slug": "umkm",
                "judul": "UMKM",
                "gambar": "image/umkm.png",
                "deskripsi": "Berbagai usaha mikro berkembang mulai dari kuliner, kerajinan hingga perdagangan."
            },
            {
                "slug": "industri",
                "judul": "Industri",
                "gambar": "image/industri.jpeg",
                "deskripsi": "Didukung kawasan industri di sekitar Desa Sumur Bandung sehingga membuka banyak lapangan pekerjaan."
            },
        ],

        # =========================
        # BERITA DESA
        # =========================
        "berita": [
    {
        "slug": "gotong-royong",
        "judul": "Kegiatan Gotong Royong Warga",
        "tanggal": "10 Agustus 2026",
        "gambar": "image/berita1.jpeg",
        "isi": "Masyarakat Desa Sumur Bandung melaksanakan kegiatan gotong royong membersihkan lingkungan."
    },
    {
        "slug": "posyandu",
        "judul": "Pelayanan Posyandu",
        "tanggal": "08 Agustus 2026",
        "gambar": "image/berita2.jpeg",
        "isi": "Pelayanan kesehatan balita dan ibu hamil berjalan dengan baik di Posyandu Desa."
    },
    {
        "slug": "kkm-uniba",
        "judul": "Mahasiswa KKM UNIBA",
        "tanggal": "05 Agustus 2026",
        "gambar": "image/berita3.jpeg",
        "isi": "Mahasiswa KKM Universitas Bina Bangsa melaksanakan berbagai program pemberdayaan masyarakat."
    }
],

        # =========================
        # PELAYANAN DESA
        # =========================
        "pelayanan": [
            {
                "nama": "Surat Keterangan Domisili",
                "icon": "📄",
                "deskripsi": "Pelayanan pembuatan surat keterangan domisili bagi warga Desa Sumur Bandung."
            },
            {
                "nama": "Surat Pengantar KTP",
                "icon": "🪪",
                "deskripsi": "Pelayanan pengantar pembuatan KTP baru maupun perubahan data."
            },
            {
                "nama": "Surat Pengantar KK",
                "icon": "👨‍👩‍👧‍👦",
                "deskripsi": "Pelayanan pembuatan maupun perubahan Kartu Keluarga."
            },
            {
                "nama": "Surat Keterangan Usaha",
                "icon": "🏪",
                "deskripsi": "Pelayanan surat keterangan usaha untuk pelaku UMKM."
            },
            {
                "nama": "Surat Keterangan Tidak Mampu",
                "icon": "🤝",
                "deskripsi": "Pelayanan administrasi untuk keperluan bantuan sosial dan pendidikan."
            },
            {
                "nama": "Pelayanan Pengaduan",
                "icon": "📢",
                "deskripsi": "Masyarakat dapat menyampaikan saran, kritik, dan pengaduan kepada pemerintah desa."
            }
        ],

        # =========================
        # FASILITAS UMUM
        # =========================
        "fasilitas": [
            {
                "nama": "Kantor Desa",
                "gambar": "image/kantordesa.jpg",
                "deskripsi": "Pusat pelayanan administrasi dan pemerintahan Desa Sumur Bandung."
            },
            {
                "nama": "Masjid",
                "gambar": "image/masjid.webp",
                "deskripsi": "Sarana ibadah masyarakat yang digunakan untuk kegiatan keagamaan."
            },
            {
                "nama": "Sekolah",
                "gambar": "image/sekolah.avif",
                "deskripsi": "Tersedia PAUD, SD, dan lembaga pendidikan lainnya untuk menunjang pendidikan masyarakat."
            },
            {
                "nama": "Posyandu",
                "gambar": "image/posyandu.jpeg",
                "deskripsi": "Fasilitas pelayanan kesehatan bagi balita, ibu hamil, dan lansia."
            },
            {
                "nama": "Lapangan",
                "gambar": "image/lapangan.webp",
                "deskripsi": "Digunakan untuk kegiatan olahraga, upacara, dan kegiatan masyarakat."
            },
            {
                "nama": "Jalan Desa",
                "gambar": "image/jalan.jpg",
                "deskripsi": "Akses jalan yang menghubungkan antar wilayah di Desa Sumur Bandung."
            }
        ],

        # =========================
        # KONTAK DESA
        # =========================

        "kontak": {

            "alamat": "Jl. Raya Sumur Bandung, Kecamatan Jayanti, Kabupaten Tangerang",

            "telepon": "(021) 12345678",

            "email": "desasumurbandung@gmail.com",

            "jam": "Senin - Jumat : 08.00 - 15.00 WIB"

        },

        

    }

    return render(request, "dashboard/index.html", context)

# =========================
# DETAIL POTENSI
# =========================
def potensi_detail(request, slug):

    data_potensi = {

        "pertanian": {
            "judul": "Potensi Pertanian Desa Sumur Bandung",
            "gambar": "image/pertanian.jpeg",
            "isi": """
Desa Sumur Bandung memiliki lahan pertanian yang cukup luas dan menjadi salah satu sumber mata pencaharian utama masyarakat.

Berbagai komoditas seperti padi, sayuran dan tanaman hortikultura dibudidayakan oleh para petani dengan memanfaatkan lahan yang subur.

Selain menjadi sumber ekonomi masyarakat, sektor pertanian juga menjadi potensi unggulan desa yang terus dikembangkan melalui berbagai program pemerintah desa.
"""
        },

        "umkm": {
            "judul": "Potensi UMKM Desa Sumur Bandung",
            "gambar": "image/umkm.png",
            "isi": """
Desa Sumur Bandung memiliki berbagai pelaku UMKM yang bergerak di bidang kuliner, perdagangan, kerajinan serta usaha rumahan.

UMKM menjadi salah satu penggerak ekonomi masyarakat dan membuka lapangan pekerjaan bagi warga sekitar.
"""
        },

        "industri": {
            "judul": "Potensi Industri Desa Sumur Bandung",
            "gambar": "image/industri.jpeg",
            "isi": """
Keberadaan kawasan industri di sekitar Desa Sumur Bandung memberikan peluang kerja bagi masyarakat serta mendorong pertumbuhan ekonomi desa.

Keberadaan industri juga meningkatkan aktivitas perdagangan dan jasa di wilayah desa.
"""
        }

    }

    potensi = data_potensi.get(slug)

    if potensi is None:
        return render(request, "404.html")

    return render(
        request,
        "dashboard/potensi_detail.html",
        {"potensi": potensi}
    )

def berita_detail(request, slug):

    data = {

        "gotong-royong": {
            "judul": "Kegiatan Gotong Royong Warga",
            "gambar": "image/berita1.jpeg",
            "tanggal": "10 Agustus 2026",
            "isi": """
Masyarakat Desa Sumur Bandung melaksanakan kegiatan gotong royong membersihkan lingkungan desa.

Kegiatan ini bertujuan meningkatkan kebersihan lingkungan sekaligus mempererat rasa kebersamaan antarwarga.

Melalui kegiatan tersebut diharapkan masyarakat semakin peduli terhadap kebersihan dan kelestarian lingkungan.
"""
        },

        "posyandu": {
            "judul": "Pelayanan Posyandu",
            "gambar": "image/berita2.jpeg",
            "tanggal": "08 Agustus 2026",
            "isi": """
Pelayanan Posyandu rutin dilaksanakan untuk balita, ibu hamil, dan lansia.

Kegiatan meliputi penimbangan balita, pemeriksaan kesehatan serta pemberian vitamin.
"""
        },

        "kkm-uniba": {
            "judul": "Mahasiswa KKM Universitas Bina Bangsa",
            "gambar": "image/berita3.jpeg",
            "tanggal": "05 Agustus 2026",
            "isi": """
Mahasiswa KKM Universitas Bina Bangsa melaksanakan berbagai program pemberdayaan masyarakat.

Program meliputi pendidikan, kesehatan, ekonomi, lingkungan serta digitalisasi desa.
"""
        }

    }

    berita = data.get(slug)

    if berita is None:
        return render(request, "404.html")

    return render(
        request,
        "dashboard/berita_detail.html",
        {"berita": berita}
    )