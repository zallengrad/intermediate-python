<?php 

class Produk {
    public $sku = "001";
    public $merk = "samsung";
    public $harga = 400000;

    public function pesanProduk(){
        return "Produk dipesan...";
    }
}

$mesinCuci = new Produk();
$mesinCuci -> sku = "002";
$mesinCuci -> sku = "LG";
$mesinCuci -> sku = "1500000";


$mesinCuci = new Produk();
echo $mesinCuci -> sku;
echo "<br>";
echo $mesinCuci -> merk;
echo "<br>";
echo $mesinCuci -> harga;
echo "<br>";
echo $mesinCuci -> pesanProduk();
echo "<br>"


?>