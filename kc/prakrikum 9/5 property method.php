<?php 

class Produk {
    public $sku = "001";
    public $merk = "samsung";
    public $harga = 400000;

    public function pesanProduk(){
        return "Produk dipesan...";
    }
}

$televisi = new Produk();
?>