
### Yeni bir depo oluşturmak

Yeni bir depo oluşturmak için, bir klasör oluşturup içerisinde

```git init```

komutunu çalıştırın.

### Bir depoyu kopyalamak

Yerel deponuzun çalışan bir kopyasını oluşturmak için

```git clone /yol/depo```

uzak sunucu kullandığımız durumda

```git clone kullaniciadi@sunucu:/yol/depo```

### Ekleme & teslim

Değişiklikleri belirtmek (Index'e eklemek) için

```
git add <dosyaadı>
git add *
```

temel git iş akışında bu ilk adımdır. Değişiklikleri depoya eklemek için

```git commit -m "Teslim mesajı"```

şimdi dosyalar HEAD'e eklendi, fakat henüz uzak deponuza değil.

### Değişiklikleri göndermek

Şimdi değişiklikleriniz yerel deponuzun HEAD'i içerisinde.

Bu değişiklikleri uzak deponuza göndermek için,

```git push origin master```

değişiklikleri uzak deponuzdaki göndermek istediğiniz dal'ı master ile değiştirin. 

Henüz uzak bir deponuz yoksa ve uzak depo eklemek istiyorsanız,

```git remote add origin <sunucu>```

şimdi değişikliklerinizi uzak sunucuya gönderebilirsiniz.

###Dallar ile çalışmak

Dallar farklı özellikleri ayrı ayrı geliştirmek için kullanılır. Yeni bir depo oluşturduğunuzda master "varsayılan" daldır. Diğer dallar geliştirildikten sonra master'a birleştirilir.

"feature_x" adıyla yeni bir dal oluşturup o dala geçmek için 

```git checkout -b feature_x```

master'a geri geçmek için

```git checkout master```

ve oluşturduğumuz dalı silmek için

```git branch -d feature_x```

bir dalı uzak deponuza göndermedikçe başkaları tarafından kullanılabilir olmaz

```git push origin <dal>```
