$Files = Get-ChildItem
Write-Host $Files

for($i = 0; $i -lt $Files.Length; $i++){
    $fi = $Files[$i]
    $f = $fi.Name.Split(".")
    $out = $f[0] + ".py"
    if($f[1] -eq "ui"){
        python -m PyQt5.uic.pyuic -x $fi -o $out
    }
}

#python -m PyQt5.uic.pyuic -x mainframe.ui -o mainframe.py