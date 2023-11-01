<?php 

class Produk {
    public $sku = "000";
    public $merk = "";
    public $harga = 0;

    public function pesanProduk(){
        return "Produk dipesan...";
    }
}

$televisi = new Produk();
$televisi -> sku = "001";
$televisi -> sku = "4000000000";
$televisi -> sku = "1500000";

$mesinCuci = new Produk();
$mesinCuci -> sku = "002";
$mesinCuci -> sku = "LG";
$mesinCuci -> sku = "1500000";

$speaker = new Produk();
$speaker -> sku = "003";
$speaker -> sku = "JBL";
$speaker -> sku = "9500000";

print_r($televisi);
echo "<br>";
print_r($mesinCuci);
echo "<br>";
print_r($speaker);
echo "<br>";
?>