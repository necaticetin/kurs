print("inglizce olan ama türkçede de kullanılan sözcükler")


meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Sesli gülmek",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO":  "agresifleşmek/sinirlenmek",
            }
            
            
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Sözlükte bu kelime yok")
