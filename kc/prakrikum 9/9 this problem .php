<?php 

class Produk {
    public $jenis = "";
    public $merek = "";
    
    public function pesanProdukTelevisi(){
        return "Televisi dipesan......";
    }
    public function pesanProdukMesinCuci(){
        return "Mesin Cuci dipesan......";
    }
}

$produk01 = new Produk();
$produk01 -> jenis = "Televisi";
$produk01 -> merek = "Xiaomi";

$produk02 = new Produk();
$produk02 -> jenis = "Mesin Cuci";
$produk02 -> merek = "Honda";

echo $produk01 -> pesanProdukTelevisi();
echo "<br>";
echo $produk02 -> pesanProdukMesinCuci();

?>