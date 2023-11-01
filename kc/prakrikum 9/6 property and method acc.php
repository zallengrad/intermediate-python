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
echo $televisi -> sku;
echo "<br>";
echo $televisi -> merk;
echo "<br>";
echo $televisi -> harga;
echo "<br>";
echo $televisi -> pesanProduk();
echo "<br>"


?>