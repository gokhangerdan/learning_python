
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

```git remote add origin <sunucu>``

şimdi değişikliklerinizi uzak sunucuya gönderebilirsiniz.
