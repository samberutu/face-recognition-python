import face_recognition
from PIL import Image, ImageDraw

#data encoding dari setiap wajah EX: ll dan nm
ll = face_recognition.load_image_file( './gambar/wajahDiketahui/hotman-paris-hutapea.jpg')
ll_encoding = face_recognition.face_encodings(ll)[0]

nm = face_recognition.load_image_file( './gambar/wajahDiketahui/nikita-mirjani.jpg')
nm_encoding = face_recognition.face_encodings(nm)[0]

encoding_terdeteksi = [ll_encoding,nm_encoding]

nama_wajah = ['hotman-paris-hutapea', 'nikita mirjani']

#membuat data dari test gambar
gambar_test = face_recognition.load_image_file('./gambar/tidakDiketahui/hotman dan nikita.jpg')

#deteksi wajah dalam gambar
test_lokasi = face_recognition.face_locations(gambar_test)
test_encoding = face_recognition.face_encodings(gambar_test,test_lokasi)

# buat kotak pada wajah jika terdeteksi
gambar_pil = Image.fromarray(gambar_test)

# buat gambar sederhana
draw = ImageDraw.Draw(gambar_pil)

# perulangan untuk melihat semua wajah pada gambar 
for(top, right, bottom, left), face_encoding in zip(test_lokasi, test_encoding):
  matches = face_recognition.compare_faces(encoding_terdeteksi, face_encoding)
  name = "tidak dikenal"
  # kemiripan terlihat
  if True in matches:
    first_match_index = matches.index(True)
    name = nama_wajah[first_match_index]
  # gambar box pada wajah
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))
  # nama pada wajah
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))
del draw
# tampilkan hasil
#gambar_pil.show()
# simpan hasil
gambar_pil.save('hasil.jpg')


