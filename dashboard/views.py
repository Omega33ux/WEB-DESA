from django.shortcuts import render


def index(request):

    context = {

        "penduduk": "8.796",
        "luas": "369,00 Ha",
        "rt": 23,
        "rw": 6,
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
            "jabatan": "Kasi Pemerintahan",
            "foto": "image/kasi_pemerintahan.jpeg"
        },
        {
            "nama": "M. Irfa farhan",
            "jabatan": "Kasi Kesra",
            "foto": "image/kasi_kesra.jpeg"
        },
        {
            "nama": "Toyib",
            "jabatan": "Kasi Pelayanan",
            "foto": "image/kasi_pelayanan.jpeg"
        },
        {
            "nama": "Nurliah",
            "jabatan": "Kaur Keuangan",
            "foto": "image/kaur_keuangan.jpeg"
        },
        {
            "nama": "Rukman",
            "jabatan": "Kaur Perencanaan",
            "foto": "image/kaur_perencanaan.jpeg"
        },
        {
            "nama": "Zaenal ridwan nurhakim",
            "jabatan": "Kepala Dusun 1",
            "foto": "image/kadus_1.jpeg"
        },
        {
            "nama": "Nurjaman",
            "jabatan": "Kepala Dusun 2",
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
                "gambar": "image/pertanian2.jpeg",
                "deskripsi": "Desa Sumur Bandung memiliki lahan pertanian yang menjadi sumber mata pencaharian masyarakat."
            },
            {
                "slug": "umkm",
                "judul": "UMKM",
                "gambar": "image/umkm2.png",
                "deskripsi": "Berbagai usaha mikro berkembang mulai dari kuliner, kerajinan hingga perdagangan."
            },
            {
                "slug": "industri",
                "judul": "Industri",
                "gambar": "image/industri2.jpeg",
                "deskripsi": "Didukung kawasan industri di sekitar Desa Sumur Bandung sehingga membuka banyak lapangan pekerjaan."
            },
        ],

        # =========================
        # BERITA DESA
        # =========================
        "berita": [
    {
        "slug": "perlombaan-badminton",
        "judul": "Perlombaan Badminton",
        "tanggal": "07 Agustus 2026",
        "gambar": "image/berita4.jpeg",
        "isi": "Desa Sumurbandung – Suasana penuh semangat dan antusiasme terlihat dalam kegiatan perlombaan badminton."
    },
    {
        "slug": "perlombaan-catur",
        "judul": "Perlombaan Catur",
        "tanggal": "08 Agustus 2026",
        "gambar": "image/berita5.jpeg",
        "isi": "Desa Sumurbandung – Perlombaan catur menjadi salah satu kegiatan yang turut memeriahkan rangkaian perlombaan masyarakat."
    },
    {
        "slug": "posyandu",
        "judul": "Posyandu dan Pelayanan Imunisasi Anak",
        "tanggal": "04 Agustus 2026",
        "gambar": "image/berita6.jpeg",
        "isi": "Desa Sumurbandung – Kegiatan pelayanan kesehatan masyarakat kembali dilaksanakan melalui Posyandu."
    },
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
# PELAYANAN DESA
# =========================
"pelayanan": [
    {
        "icon": "📄",
        "nama": "Surat Keterangan Domisili",
        "deskripsi": "Pelayanan pembuatan surat keterangan domisili bagi masyarakat Desa Sumur Bandung."
    },
    {
        "icon": "📋",
        "nama": "Pengaduan Masyarakat",
        "deskripsi": "Pelayanan penerimaan dan penanganan pengaduan masyarakat terkait berbagai permasalahan di Desa Sumur Bandung."
    },
    {
        "icon": "👨‍👩‍👧",
        "nama": "Surat Keterangan Keluarga",
        "deskripsi": "Pelayanan administrasi terkait data dan keterangan keluarga masyarakat desa."
    },
    {
        "icon": "🏠",
        "nama": "Surat Pengantar",
        "deskripsi": "Pelayanan surat pengantar untuk berbagai keperluan administrasi masyarakat."
    },
    {
        "icon": "📝",
        "nama": "Surat Keterangan Tidak Mampu",
        "deskripsi": "Pelayanan surat keterangan tidak mampu bagi masyarakat yang memenuhi persyaratan."
    },
    {
        "icon": "📑",
        "nama": "Pelayanan Administrasi Desa",
        "deskripsi": "Berbagai pelayanan administrasi untuk membantu kebutuhan masyarakat Desa Sumur Bandung."
    },
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

        "perlombaan-badminton": {
            "judul": "Perlombaan Badminton",
            "gambar": "image/berita4.jpeg",
            "tanggal": "07 Agustus 2026",
            "isi": """
Desa Sumurbandung – Suasana penuh semangat dan antusiasme terlihat dalam kegiatan perlombaan badminton yang diselenggarakan di Desa Sumurbandung, Kecamatan Jayanti, Kabupaten Tangerang. Kegiatan ini menjadi salah satu ajang olahraga yang mempertemukan masyarakat sekaligus menjadi sarana untuk mempererat tali silaturahmi antarwarga.

Sejak pertandingan dimulai, para peserta tampak menunjukkan semangat dan kemampuan terbaiknya di lapangan. Setiap pertandingan berlangsung dengan cukup sengit, namun tetap mengedepankan nilai-nilai sportivitas, disiplin, dan sikap saling menghargai antar peserta.

Tidak hanya peserta yang turut meramaikan kegiatan, masyarakat juga terlihat antusias memberikan dukungan kepada para pemain. Suasana semakin meriah ketika pertandingan berlangsung, dengan sorakan dan dukungan dari warga yang menyaksikan jalannya perlombaan.

Perlombaan badminton ini tidak hanya bertujuan untuk mencari pemenang, tetapi juga menjadi wadah bagi masyarakat untuk menyalurkan minat dan bakat di bidang olahraga. Melalui kegiatan tersebut, warga dapat berinteraksi dan berkumpul dalam suasana yang positif dan penuh kekeluargaan.

Selain meningkatkan aktivitas fisik, kegiatan olahraga seperti ini juga dapat menjadi media untuk membangun kebersamaan di tengah masyarakat. Pertandingan yang berlangsung secara sportif diharapkan mampu menumbuhkan rasa percaya diri, kedisiplinan, serta semangat kompetitif yang sehat di antara para peserta.

Bagi mahasiswa KKM Universitas Bina Bangsa Kelompok 94, keterlibatan dalam kegiatan perlombaan badminton menjadi salah satu bentuk partisipasi dalam mendukung kegiatan positif masyarakat Desa Sumurbandung. Kehadiran mahasiswa diharapkan dapat membantu menciptakan kegiatan yang aktif, meriah, serta memberikan manfaat bagi masyarakat.

Melalui perlombaan badminton ini, diharapkan semangat berolahraga dan kebersamaan masyarakat Desa Sumurbandung dapat terus berkembang. Menang atau kalah bukan menjadi tujuan utama, melainkan bagaimana setiap peserta mampu menjunjung tinggi sportivitas, menjaga persaudaraan, dan menikmati setiap proses pertandingan.

Kegiatan ini sekaligus menjadi bukti bahwa olahraga dapat menjadi sarana sederhana untuk mempererat hubungan sosial masyarakat. Dengan semangat kebersamaan dan sportivitas, diharapkan kegiatan serupa dapat terus dilaksanakan dan menjadi bagian dari aktivitas positif masyarakat Desa Sumurbandung.
"""
        },

        "perlombaan-catur": {
            "judul": "Perlombaan Catur",
            "gambar": "image/berita5.jpeg",
            "tanggal": "08 Agustus 2026",
            "isi": """
Desa Sumurbandung – Perlombaan catur menjadi salah satu kegiatan yang turut memeriahkan rangkaian perlombaan masyarakat di Desa Sumurbandung, Kecamatan Jayanti, Kabupaten Tangerang. Kegiatan ini berlangsung dengan penuh antusiasme dan diikuti oleh peserta dari berbagai kalangan masyarakat.

Sejak pertandingan dimulai, para peserta terlihat serius dan fokus dalam menyusun strategi untuk menghadapi lawan masing-masing. Setiap langkah pada papan catur menjadi bagian penting dalam menentukan jalannya pertandingan. Suasana pertandingan berlangsung tenang, namun tetap dipenuhi dengan semangat kompetisi dan antusiasme para peserta maupun masyarakat yang menyaksikan.

Perlombaan catur tidak hanya mengandalkan kemampuan bermain, tetapi juga membutuhkan konsentrasi, ketelitian, kesabaran, serta kemampuan dalam menentukan strategi. Para peserta dituntut untuk mampu berpikir beberapa langkah ke depan dan mengambil keputusan secara tepat dalam menghadapi berbagai situasi selama pertandingan.

Selain menjadi ajang kompetisi, kegiatan ini juga menjadi sarana untuk mempererat silaturahmi dan kebersamaan antarwarga Desa Sumurbandung. Masyarakat dapat berkumpul, berinteraksi, serta memberikan dukungan kepada para peserta dalam suasana yang penuh kekeluargaan.

Mahasiswa KKM Universitas Bina Bangsa Kelompok 94 turut berpartisipasi dalam mendukung pelaksanaan kegiatan tersebut. Keterlibatan mahasiswa menjadi salah satu bentuk kontribusi dalam menyukseskan kegiatan masyarakat sekaligus membangun hubungan yang lebih dekat dengan warga Desa Sumurbandung.

Melalui perlombaan catur ini, diharapkan masyarakat dapat semakin mengenal dan mengembangkan potensi olahraga yang membutuhkan kecerdasan, konsentrasi, dan strategi. Kegiatan tersebut juga diharapkan dapat menumbuhkan semangat sportivitas serta menciptakan ruang interaksi positif bagi masyarakat.

Perlombaan catur menjadi bukti bahwa kegiatan olahraga tidak selalu membutuhkan aktivitas fisik yang berat. Permainan strategi seperti catur juga mampu memberikan manfaat dalam melatih kemampuan berpikir sekaligus menjadi sarana hiburan dan mempererat kebersamaan.

Dengan terlaksananya kegiatan ini, diharapkan semangat masyarakat untuk berpartisipasi dalam berbagai kegiatan positif dapat terus meningkat. Perlombaan catur bukan hanya tentang siapa yang menjadi pemenang, tetapi juga tentang membangun sportivitas, kebersamaan, dan semangat persaudaraan di tengah masyarakat Desa Sumurbandung.
"""
        },

        "posyandu": {
            "judul": "Posyandu dan Pelayanan Imunisasi Anak",
            "gambar": "image/berita6.jpeg",
            "tanggal": "04 Agustus 2026",
            "isi": """
Desa Sumurbandung – Kegiatan pelayanan kesehatan masyarakat kembali dilaksanakan melalui Posyandu di Desa Sumurbandung, Kecamatan Jayanti, Kabupaten Tangerang. Salah satu pelayanan yang diberikan dalam kegiatan tersebut adalah imunisasi bagi anak sebagai bagian dari upaya menjaga kesehatan dan mendukung tumbuh kembang anak sejak usia dini.

Kegiatan imunisasi berlangsung dengan dukungan kader Posyandu dan tenaga kesehatan. Para orang tua turut membawa anak mereka untuk mendapatkan pelayanan kesehatan sesuai dengan kebutuhan dan jadwal imunisasi yang telah ditentukan. Kegiatan ini juga menjadi kesempatan bagi masyarakat untuk memperoleh informasi mengenai pentingnya menjaga kesehatan anak.

Imunisasi merupakan salah satu langkah penting dalam upaya memberikan perlindungan kepada anak dari berbagai penyakit yang dapat dicegah melalui imunisasi. Dengan mengikuti jadwal imunisasi yang dianjurkan oleh tenaga kesehatan, orang tua turut berperan dalam menjaga kesehatan dan meningkatkan perlindungan anak.

Selain pelayanan imunisasi, kegiatan Posyandu juga menjadi tempat untuk memantau pertumbuhan dan perkembangan anak. Kader bersama tenaga kesehatan melakukan pelayanan seperti penimbangan berat badan, pengukuran tinggi badan, serta pemantauan kondisi kesehatan anak. Hasil pemantauan tersebut dapat menjadi bahan perhatian bagi orang tua dalam mendukung pertumbuhan anak secara optimal.

Antusiasme masyarakat terlihat dari kehadiran para orang tua yang membawa anaknya ke Posyandu. Kehadiran masyarakat dalam kegiatan tersebut menunjukkan adanya kesadaran akan pentingnya pemeriksaan kesehatan secara rutin, khususnya bagi bayi dan balita.

Mahasiswa KKM Universitas Bina Bangsa Kelompok 94 turut berpartisipasi dalam mendukung kegiatan Posyandu di Desa Sumurbandung. Keterlibatan mahasiswa menjadi salah satu bentuk kepedulian terhadap kesehatan masyarakat sekaligus mendukung kelancaran kegiatan pelayanan kesehatan yang dilaksanakan bersama kader dan tenaga kesehatan.

Melalui kegiatan Posyandu dan imunisasi, diharapkan kesadaran masyarakat terhadap pentingnya kesehatan ibu dan anak semakin meningkat. Peran aktif orang tua, kader Posyandu, tenaga kesehatan, serta masyarakat menjadi bagian penting dalam menciptakan lingkungan yang mendukung tumbuh kembang anak.

Kegiatan ini diharapkan dapat terus dilaksanakan secara rutin dan mendapat dukungan dari seluruh masyarakat. Dengan memanfaatkan pelayanan Posyandu secara aktif, masyarakat Desa Sumurbandung dapat bersama-sama membangun kesadaran akan pentingnya menjaga kesehatan sejak usia dini demi menciptakan generasi yang sehat, aktif, dan memiliki tumbuh kembang yang optimal.
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