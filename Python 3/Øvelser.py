biler = 100 #sætter variablen biler til 100
plads_i_en_bil = 4.0 #sætter variablen til 4.0
førere = 30 #sætter variablen til 30
passagerer = 90 #sætter variablen til 90
biler_ude_af_drift = biler - førere #laver en ny variable ud fra udregningen
biler_i_kørsel = førere #laver en ny variabel som er lig med en anden variabel
samlet_bil_kapacitet = biler_i_kørsel * plads_i_en_bil #laver en ny variable ud fra udregningen
gennemsnit_af_passagere_per_bil = passagerer / biler_i_kørsel #laver en ny variable ud fra udregningen

print("Der er", biler, "biler til rådighed.")
print("Der er kun", førere, "førere til rådighed.")
print("Der vil være", biler_ude_af_drift, "tomme biler i dag.")
print("Vi kan transportere", samlet_bil_kapacitet, "personer i dag.")
print("Vi har", passagerer, "passagere i dag.")
print("vi skal cirka putte", gennemsnit_af_passagere_per_bil, "i hver bil.")
