import face_recognition

data = face_recognition.load_image_file( './gambar/wajahDiketahui/kekeyi.jpg')
data_encoding = face_recognition.face_encodings(data)[0]

inputn = face_recognition.load_image_file( './gambar/tidakDiketahui/kekeyi2.jpg')
input_encoding = face_recognition.face_encodings(inputn)[0]

result = face_recognition.compare_faces(
    [data_encoding], input_encoding)

if result[0]:
    print("benar")
else:
    print("salah")