# Case I : Video Streaming Service
* Repository ini berisi file python yang membuat simple program 
untuk masalah Case I, yaitu Video Streaming Service di pembelajaran
Python Software Engineering di platform PacMann.
* Beberapa tujuan dari program tersebut adalah:
  1. Setiap _user_ bisa mengecek _plan_ apa saja yang ada di PacFlix.
  2. Setiap _current user_ bisa mengecek _durasi plan_ dan _current plan_
     yang dipakai saat ini.
  3. Setiap _current user_ bisa upgrade _current plan_ dan dapat diskon
     jika sudah berlangganan lebih dari dua belas bulan.
  4. Setiap _new user_ dapat diskon jika memiliki _referral code_.
* Program menggunakan OOP dan dalam hal ini yang menjadi objek adalah
  User sebagai _current user_ dan NewUser sebagai user baru yang
  mau berlangganan.
* class User:
  - Atribut-atributnya:
    1. username (nama pengguna).
    2. current_plan (plan yang sedang digunakan jika ada).
    3. duration_plan (durasi plan yang sedang digunakan).
  - Method-methodnya:
    1. check_benefit (mengecek semua plan yang ada di PacFlix).
    2. check_plan (mengecek plan yang sedang digunakan beserta durasinya
       dengan cara menginput username pengguna).
    3. upgrade_plan (menampilkan harga yang harus dibayar jika ingin
       upgrade plan dari current plan dan mendapat bonus jika durasi
       plan lebih dari dua belas bulan.
* class NewUser:
  - Atribut-atributnya:
    1. username (nama pengguna).
  - Method-methodnya:
    1. check_benefit (mengecek semua plan yang ada di PacFlix).
    2. pick_plan (menampilkan harga yang harus dibayar jika ingin
       membeli plan dan mendapat bonus jika memiliki referral code.
  
