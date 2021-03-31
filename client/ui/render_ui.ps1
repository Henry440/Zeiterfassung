$Pfad = ".\template\"
$Files = Get-ChildItem $Pfad
Write-Host $Files

#python -m PyQt5.uic.pyuic -x mainframe.ui -o mainframe.py