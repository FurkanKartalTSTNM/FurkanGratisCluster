Specification Heading
=====================
Created by testinium on 25.08.2023

This is an executable specification file which follows markdown syntax.
Every heading in this file denotes a scenario. Every bulleted point denotes a step.
     
IOS Scenario Purchasing Below Shipping Cost
-------------------------------------------
tags:Gratis_IOS_KargoIndirimsiz
* Uygulama baslatilir
* Ana sayfa sepet ikonuna tiklanir
* Sepet ikonu ile login olunur
* Sepet kontrol edilerek temizlenir
* Ana sayfa tab'ına tıklanır
* Ana sayfadan bir urun sepete eklenir
//* Sepet kasa arkasi popup'i kapatilir
* Tek ürünün ve toplam fiyatın kontrolü yapılır
* Adrese Teslim butonuna tıklanır
* Adrese Teslim teslimat Bilgileri alanı kontrol edilir
* Adrese Teslim seçeneğine tıklanır ve devam edilir
* Teslimat alanı kontrol edilir
* Sipariş Özeti alanı kontrol edilir
* Iyzico alanı fiyat kontrol edilir

IOS Scenario Purchasing Above Shipping Cost
-------------------------------------------
tags:Gratis_IOS_KargoIndirimli
* Uygulama baslatilir
* Ana sayfa sepet ikonuna tiklanir
* Sepet ikonu ile login olunur
* Sepet kontrol edilerek temizlenir
* Kategoriler sayfasina gecilir
* "Elektrikli Ürünler" isimli kategori seçilir
* Alt kategorilerden biri "Küçük Ev Aletleri", "Elektrikli Süpürge" seçilir
* Urun detay sayfasına geçilir
* Ürün detay sayfasinda urun sepete eklenir
* Sepete git'e tıklanır
//* Sepet kasa arkasi popup'i kapatilir
* Tek ürünün ve toplam fiyatın kontrolü yapılır
* Adrese Teslim butonuna tıklanır
* Adrese Teslim teslimat Bilgileri alanı kontrol edilir
* Adrese Teslim seçeneğine tıklanır ve devam edilir
* Teslimat alanı kontrol edilir
* Sipariş Özeti alanı kontrol edilir
* Iyzico alanı fiyat kontrol edilir